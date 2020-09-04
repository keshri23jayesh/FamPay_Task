from django.conf.urls import url
from local_database_calls import local_database_request
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
     # URLs for rendering template rendering
     url(r'^pagination$', local_database_request.load_pagination_page, name="pagination"),
     url(r'^search$', local_database_request.load_search_template, name="search"),

     # URLs for APIs
     url(r'^get_pagination_video_response$', local_database_request.GetNextPaginationVideosList.as_view(), name="get_videos_query"),
     url(r'^get_search_response$', local_database_request.SearchVideosByParam.as_view(), name="search_videos_with_index")
]