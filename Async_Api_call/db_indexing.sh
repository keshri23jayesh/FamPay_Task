#!/bin/sh
# Wait for database to get available

python manage.py shell <<EOF
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("""CREATE INDEX publish_date ON VIDEO_DETAILS (publishedAt)""")
    cursor.execute("""ALTER TABLE VIDEO_DETAILS  ADD FULLTEXT(video_desc)""")
    cursor.execute("""ALTER TABLE VIDEO_DETAILS  ADD FULLTEXT(video_title)""")
    cursor.execute("""INSERT INTO API_KEYS(api_key, status) VALUES ('AIzaSyD4Ywf-gemyGOd5aWcR7YQusWXi1h3yUao', 1)""")
    cursor.execute("""INSERT INTO API_KEYS(api_key, status) VALUES ('AIzaSyCLDdK3sLahpBnc1lxNOhGFKuUmM_5E3Ac', 1)""")
    cursor.execute("""INSERT INTO API_KEYS(api_key, status) VALUES ('AIzaSyBl0kc3YKA_INvxrP6bRVt3sNuyWaucJaA', 1)""")
    cursor.execute("""INSERT INTO API_KEYS(api_key, status) VALUES ('AIzaSyDqNdG256yq6byh2OpwEkB4wO_qmrOFDfc', 1)""")
EOF