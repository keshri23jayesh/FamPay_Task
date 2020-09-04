from threading import Timer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse

from youtube_server_calls.youtube_search_api_config import youtube_search_api_config

youtube_search_api_config_instance = youtube_search_api_config()


class TriggerYouTubeSearch(APIView):
    def get(self, request):
        """
        Triggering thread function for continuously pulling data
        :param request:
        :return: True
        """
        youtube_search_api_config_instance.youtube_search_api()
        return JsonResponse({'status': 'SuccessFully Triggered Youtube API call.'})
