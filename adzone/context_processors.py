from adzone.models import AdCategory

def get_source_ip(request):

    if 'REMOTE_ADDR' in request.META:

        return {'from_ip': request.META.get('REMOTE_ADDR')}
    else:
        return {}

def get_category_nodes(request):

    return {'nodes':AdCategory.objects.all()}

