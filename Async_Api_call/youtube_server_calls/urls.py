from django.conf.urls import url
from youtube_server_calls import youtube_server_call_request

urlpatterns = [
    url(r'^$', youtube_server_call_request.TriggerYouTubeSearch.as_view(), name="start_data_pulling")
]