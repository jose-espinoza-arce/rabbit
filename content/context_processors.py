from __future__ import unicode_literals

from content.models import AdCategory
from content.forms import AdSearchForm

def get_source_ip(request):

    if 'REMOTE_ADDR' in request.META:

        return {'from_ip': request.META.get('REMOTE_ADDR')}
    else:
        return {}


def get_category_nodes(request):

    return {'nodes': AdCategory.objects.all()}


def search_form(request):
    """
    Ensure that the search form is available site wide
    """
    return {'search_form': AdSearchForm(request.GET)}

