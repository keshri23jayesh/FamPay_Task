import datetime
from threading import Timer
import requests
from youtube_server_calls.models import video_details

import json

# interval to call thread API
interval = 10


def check_existing_entry(video_id:str):
    """
    helper method for checking existing entry in DB
    :param video_id:
    :return:
    """
    try:
        video_details.objects.get(video_id=video_id)
        return True
    except Exception as e:
        print(e)
    return False


def destructure_video_details(video_obj:dict):
    """
    helper method to create video details.
    :param video_obj:
    :return:
    """
    video_detail_dict = {}
    video_id = video_obj['id']['videoId']
    if not check_existing_entry(video_id):
        video_detail_dict['video_id'] = video_id
        video_detail_dict['publishedAt'] = video_obj['snippet']['publishedAt']
        video_detail_dict['video_title'] = video_obj['snippet']['title']
        video_detail_dict['video_desc'] = video_obj['snippet']['description']
        video_detail_dict['thumbnail_url'] = video_obj['snippet']['thumbnails']['default']['url']
    print(video_detail_dict)
    return video_detail_dict


def insert_new_video_data(respoanse_array):
    """
    helper method to insert non repeating data into database.
    :param respoanse_array:
    :return:
    """
    try:
        for each_video_detail in respoanse_array:
            video_detail_dict = destructure_video_details(each_video_detail)
            if len(video_detail_dict):
                video_id = video_detail_dict['video_id']
                publishedAt = video_detail_dict['publishedAt']
                video_title = video_detail_dict['video_title'].encode('unicode_escape')
                video_desc = video_detail_dict['video_desc'].encode('unicode_escape')
                thumbnail_url = video_detail_dict['thumbnail_url']

                video_obj = video_details(video_id=video_id,
                                           publishedAt=publishedAt,
                                           video_title=video_title,
                                           video_desc=video_desc,
                                           thumbnail_url=thumbnail_url)
                video_obj.save()
    except Exception as e:
        print(e)


class youtube_search_api_config():
    def __init__(self):
        pass

    def youtube_search_api(self):
        """
        recursive function, called in every 10 sec
        :return: None
        """
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        KEY = 'AIzaSyCLDdK3sLahpBnc1lxNOhGFKuUmM_5E3Ac'
        d = datetime.datetime.today() - datetime.timedelta(days=1)
        RFC_formatted = d.isoformat("T") + "Z"
        params = {
            'part': 'snippet',
            'q': 'python',
            'key': KEY,
            'type': 'video',
            'order': 'date',
            'publishedAfter': RFC_formatted,
            'maxResults': 50
        }
        r = requests.get(search_url, params=params)
        if r.status_code == 200:
            r = json.loads(r.text)
            insert_new_video_data(r['items'])
        Timer(interval, self.youtube_search_api).start()
