import datetime
from threading import Timer
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse

import os

# import google_auth_oauthlib.flow
# import googleapiclient.discovery
# import googleapiclient.errors

interval = 10


class youtube_search_api_config():
    def __init__(self):
        pass

    def youtube_search_api(self):
        print("Hi")
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        KEY = 'AIzaSyA9TMP0vpJ4Z9hN5PIFTqgfGcAqX_di470'
        # d = datetime.datetime.utcnow() # <-- get time in UTC
        d = datetime.datetime.today() - datetime.timedelta(days=1)
        RFC_formatted = d.isoformat("T") + "Z"
        params = {
            'part': 'snippet',
            'q': 'python',
            'key': KEY,
            'type': 'video',
            'order': 'date',
            'publishedAfter': RFC_formatted
        }
        r = requests.get(search_url, params=params)
        print(r.text)
        Timer(interval, self.youtube_search_api).start()
