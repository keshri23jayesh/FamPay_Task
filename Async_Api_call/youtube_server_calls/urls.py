from django.conf.urls import url
from youtube_server_calls import youtube_server_call_request

urlpatterns = [
    url(r'^thread_function$', youtube_server_call_request.youtube_search_api, name="thread_function")
]