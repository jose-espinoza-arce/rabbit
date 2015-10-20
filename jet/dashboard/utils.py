from importlib import import_module
from django.contrib.auth.models import Group
from jet.dashboard import settings
try:
    clients_group = Group.objects.get(name='Clientes')
except:
    clients_group = None
try:
    managers_group = Group.objects.get(name='Managers')
except:
    managers_group = None

def get_current_dashboard(location, user):
    path = None
    if location == 'index':
        if user.is_superuser:
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
    module, cls = path.rsplit('.', 1)
    module = import_module(module)
    index_dashboard_cls = getattr(module, cls)

    return index_dashboard_cls
