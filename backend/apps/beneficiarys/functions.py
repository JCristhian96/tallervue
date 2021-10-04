from rest_framework.response import Response
from rest_framework import status


def response_with_paginator(viewset, queryset):
    page = viewset.paginate_queryset(queryset)
    if page is not None:
        serializer = viewset.get_serializer(page, many=True)
        return viewset.get_paginated_response(serializer.data)

    return Response(viewset.get_serializer(queryset, many=True).data)