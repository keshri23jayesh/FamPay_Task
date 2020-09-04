#!/bin/sh
# Wait for database to get available

python manage.py shell <<EOF
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("""CREATE INDEX publish_date ON VIDEO_DETAILS (publishedAt)""")
    cursor.execute("""ALTER TABLE VIDEO_DETAILS  ADD FULLTEXT(video_desc)""")
    cursor.execute("""ALTER TABLE VIDEO_DETAILS  ADD FULLTEXT(video_title)""")
EOF