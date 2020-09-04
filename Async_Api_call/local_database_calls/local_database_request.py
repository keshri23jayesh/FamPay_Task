from django.template import loader
from django.http import HttpResponse
from rest_framework.views import APIView


from local_database_calls.local_database_config import LocalDatabaseApiConfig

local_database_api_config_instance = LocalDatabaseApiConfig()


class GetNextPaginationVideosList(APIView):
    def get(self, request):
        """
        :param request: request contains page_no for pagination.
        :return: list of videos in each page.
        """
        page_no = request.GET.get('page_no')
        response = local_database_api_config_instance.get_next_pagination_response(page_no)
        return response


class SearchVideosByParam(APIView):
    def get(self, request):
        """
        :param request: request contain Query String.
        :return: list of videos falling in this search criteria.
        """
        params = request.GET.get('params')
        response = local_database_api_config_instance.get_serach_results_for_param(params)
        return response


"""
The below code is commented intensely 
"""
# def search_videos(request):
#     text = request.GET.get('text')
#     query_params = set(text.split(' '))
#     print(query_params)
#     response = local_database_api_config_instance.get_serach_results(query_params)
#     return JsonResponse(response, status=500, safe=False)


def load_pagination_page(request):
    """
    :param request:
    :return: render a html template for pagination
    """
    try:
        template = loader.get_template('local_database_calls/pagination.html')
        context = {}
        return HttpResponse(template.render(context, request))
    except Exception as e:
        pass


def load_search_template(request):
    """
    :param request:
    :return: render a html template for search
    """
    try:
        template = loader.get_template('local_database_calls/searchVideos.html')
        context = {}
        return HttpResponse(template.render(context, request))
    except Exception as e:
        pass