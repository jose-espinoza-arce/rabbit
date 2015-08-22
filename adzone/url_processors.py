# coding: utf-8
from __future__ import unicode_literals

from django.utils.module_loading import import_string
from django.shortcuts import redirect
from django.template.defaultfilters import slugify
from django.contrib import messages

from taggit.utils import parse_tags

from taggit.models import Tag, TaggedItem
try:
    from unidecode import unidecode
except ImportError:
    unidecode = lambda tag: tag

from adzone.views import AdListView


class tagview():
    def __init__(self, tagmodel, view, slug_field):
        self.tagmodel = tagmodel
        self.view = view
        self.slug_field = slug_field

    def __call__(self, request, *args, **kwargs):
        if 'path' not in kwargs:
            raise ValueError('Path was not captured! Please capture it in your urlconf. Example: url(r\'^tags/(?P<path>.*)\', mptt_urls.view(...), ...)')

        print 'tagview'
        path = kwargs['path']
        path_slugs = path.split('/')
        tag_slugs = [tag.slug for tag in self.tagmodel.objects.all()]
        path_tag_slugs = list(set(path_slugs).intersection(tag_slugs))

        if not path_tag_slugs:
            messages.add_message(request, messages.INFO, 'No se encontaron resultados')
            return redirect('adzone:ad_list')
        elif set(path_tag_slugs) != set(path_slugs):
            return redirect('adzone:tagged_ads', path=('/').join(path_tag_slugs))
        elif 'from_search' in kwargs:
            return redirect('adzone:tagged_ads', path=path)

        kwargs['slugs'] = path_tag_slugs
        return self.view.as_view()(request, *args, **kwargs)


class searchview():
    def __call__(self, request, *args, **kwargs):
        if request.GET:
            q = request.GET['q']
            path = ('/').join([slugify(unidecode(tag)) for tag in parse_tags(q)])
            kwargs['path'] = path
            kwargs['from_search'] = True
            return tagview(Tag, AdListView, 'slug')(request, *args, **kwargs)

        return redirect('adzone:ad_list')


def _load(module):
    return import_string(module) if isinstance(module, str) else module


class view():
    """
    Taken (and modified) from mptt_urls. Manage category/ad urls and calls view=AdLisView or AdDetailView depending on
    last url slot of the path.
    """
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
            raise ValueError('Path was not captured! Please capture it in your urlconf. Example: url(r\'^categories/(?P<path>.*)\', mptt_urls.view(...), ...)')

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

