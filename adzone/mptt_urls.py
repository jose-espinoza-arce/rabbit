# coding: utf-8
from django.utils.module_loading import import_string


def _load(module):
    return import_string(module) if isinstance(module, str) else module


class view():
    def __init__(self, model, model_object, view, view_object, slug_field):
        self.model = _load(model)
        self.model_object = _load(model_object)
        self.view = _load(view)
        self.view_object = _load(view_object)
        self.slug_field = slug_field

        # define 'get_path' method for model
        self.model.get_path = lambda instance: '/'.join([getattr(item, slug_field) for item in instance.get_ancestors(include_self=True)])

    def __call__(self, *args, **kwargs):
        if 'path' not in kwargs:
            raise ValueError('Path was not captured! Please capture it in your urlconf. Example: url(r\'^gallery/(?P<path>.*)\', mptt_urls.view(...), ...)')

        instance = None  # actual instance the path is pointing to (None by default)
        path = kwargs['path']
        instance_slug = path.split('/')[-1]  # slug of the instance
        is_object_instance = False
        view = self.view

        try:
            is_object_instance = path.split('/')[-2] == 'ad'
        except:
            pass

        if instance_slug:
            if is_object_instance:
                candidates = self.model_object.objects.filter(**{self.slug_field: instance_slug})
                view = self.view_object
            else:
                candidates = self.model.objects.filter(**{self.slug_field: instance_slug})  # candidates to be the instance
                #view = self.view
            for candidate in candidates:
                # here we compare each candidate's path to the path passed to this view
                if candidate.get_path() == path:

                    instance = candidate
                    break

        kwargs['instance'] = instance

        if instance:
            kwargs['pk'] = instance.pk

        return view.as_view()(*args, **kwargs)

