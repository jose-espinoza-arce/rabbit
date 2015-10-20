from django.conf import settings

# Dashboard
JET_INDEX_DASHBOARD = getattr(settings, 'JET_INDEX_DASHBOARD',
                              'jet.dashboard.dashboard.DefaultIndexDashboard')
JET_APP_INDEX_DASHBOARD = getattr(settings, 'JET_APP_INDEX_DASHBOARD',
                                  'jet.dashboard.dashboard.DefaultAppIndexDashboard')

JET_INDEX_CLIENT_DASHBOARD = getattr(settings, 'JET_INDEX_CLIENT_DASHBOARD',
                                     'jet.dashboard.dashboard.ClientIndexDashboard')
JET_APP_INDEX_CLIENT_DASHBOARD = getattr(settings, 'JET_APP_INDEX_CLIENT_DASHBOARD',
                                         'jet.dashboard.dashboard.ClientAppIndexDashboard')

JET_INDEX_MANAGER_DASHBOARD = getattr(settings, 'JET_INDEX_MANAGER_DASHBOARD',
                                     'jet.dashboard.dashboard.ManagerIndexDashboard')
JET_APP_INDEX_MANAGER_DASHBOARD = getattr(settings, 'JET_APP_INDEX_MANAGER_DASHBOARD',
                                         'jet.dashboard.dashboard.ManagerAppIndexDashboard')