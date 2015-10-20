from importlib import import_module
from django.contrib.auth.models import Group
from jet.dashboard import settings

clients_group = Group.objects.get(name='Clientes')
managers_group = Group.objects.get(name='Managers')

def get_current_dashboard(location, user):

    if location == 'index':
        if user.is_superuser:
            print(user)
            path = settings.JET_INDEX_DASHBOARD
        elif clients_group in user.groups.all():
            path = settings.JET_INDEX_CLIENT_DASHBOARD
        elif managers_group in user.groups.all():
            path = settings.JET_INDEX_MANAGER_DASHBOARD

    elif location == 'app_index':
        if user.is_superuser:
            path = settings.JET_APP_INDEX_DASHBOARD
        elif clients_group in user.groups.all():
            path = settings.JET_APP_INDEX_CLIENT_DASHBOARD
        elif managers_group in user.groups.all():
            path = settings.JET_APP_INDEX_MANAGER_DASHBOARD
    else:
        raise ValueError('Unknown dashboard location: %s' % location)
    print(path)
    module, cls = path.rsplit('.', 1)
    module = import_module(module)
    index_dashboard_cls = getattr(module, cls)
    print(index_dashboard_cls)

    return index_dashboard_cls
