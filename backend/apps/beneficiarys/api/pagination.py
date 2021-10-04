from rest_framework.response import Response
from rest_framework import pagination
 
class BeneficiarioPagination(pagination.PageNumberPagination):
    page_size = 100

    def get_paginated_response(self, data):
        response = super(BeneficiarioPagination, self).get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages
        return response
