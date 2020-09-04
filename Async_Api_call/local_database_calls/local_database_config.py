from rest_framework.response import Response
from rest_framework import serializers

from django.core.paginator import Paginator
from django.db.models import Q

from youtube_server_calls.models import video_details


class video_detailsSerializer(serializers.ModelSerializer):
    """
    class for serializing the data
    """
    class Meta:
        model = video_details
        fields = '__all__'

"""
The below code is commented intensely 
"""

# def unpacking_data_for_serach(queryset, res):
#     """
#     helper method for unpacking of data
#     :param queryset:
#     :param res:
#     :return: dict
#     """
#     for row in queryset:
#         if not row.id in res:
#             video_obj = {}
#             video_obj['id'] = row.id
#             video_obj['video_id'] = row.video_id
#             video_obj['publishedAt'] = row.publishedAt
#             video_obj['video_title'] = row.video_title
#             video_obj['video_desc'] = row.video_desc
#             video_obj['thumbnail_url'] = row.thumbnail_url
#             res[row.id] = video_obj
#     return res


class LocalDatabaseApiConfig():
    def __init__(self):
        pass

    def get_next_pagination_response(self, page_no):
        response = video_details.objects.all().order_by('id')
        pagineted_response = Paginator(response, 10)
        page = pagineted_response.page(page_no)
        serializer = video_detailsSerializer(page, many=True)
        return Response(serializer.data)

    def get_serach_results_for_param(self, params:str):
        response = video_details.objects.filter(Q(video_title__search=params)|Q(video_desc__search=params))
        serializer = video_detailsSerializer(response, many=True)
        return Response(serializer.data)

    """
    The below code is commented intensely 
    """
    # def get_serach_results(self, query_params:set):
    #     res = {}
    #     for elem in query_params:
    #         response = video_details.objects.filter(Q(video_title__contains=elem)|Q(video_desc__contains=elem))
    #         if response is not None:
    #             res = unpacking_data_for_serach(response, res)
    #     return res


