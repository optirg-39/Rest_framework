from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    """Default limit we override it by mylimit"""

    limit_query_param = 'mylimit'

    """Default offset we override it by myoffset"""
    offset_query_param = 'myoffset'

    """To abote user we defin max_limit"""
    max_limit = 6


