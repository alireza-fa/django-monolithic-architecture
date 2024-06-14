from collections import OrderedDict

from rest_framework.pagination import LimitOffsetPagination as _LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination as _PageNumberPagination
from rest_framework.response import Response
from rest_framework import serializers


class LimitOffsetPagination(_LimitOffsetPagination):
    default_limit = 10
    max_limit = 50

    def get_paginated_data(self, data):
        return OrderedDict([
            ('limit', self.limit),
            ('offset', self.offset),
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('result', data)
        ])

    def get_paginated_response(self, data):
        """
        We redefine this method in order to return `limit` and `offset`.
        This is used by the frontend to construct the pagination itself.
        """
        return Response(OrderedDict([
            ('limit', self.limit),
            ('offset', self.offset),
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


class PageNumberPagination(_PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_number'
    max_page_size = 1000

    def __init__(self, page_size: int = 12, page_size_query_params: str = "page_size", max_page_size: int = 1000):
        self.page_size = page_size
        self.page_query_param = page_size_query_params
        self.max_page_size = max_page_size


class ListResponse(serializers.Serializer):
    count = serializers.IntegerField()
    next = serializers.CharField(default="next page link")
    previous = serializers.CharField(default="previous page link")
