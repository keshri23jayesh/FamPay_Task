from django.db import models


# Create your models here.


class Search(models.Lookup):
    lookup_name = 'search'

    def as_mysql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return 'MATCH (%s) AGAINST (%s IN NATURAL LANGUAGE MODE)' % (lhs, rhs), params


models.CharField.register_lookup(Search)
models.TextField.register_lookup(Search)


class video_details(models.Model):
    video_id = models.CharField(max_length=50, unique=True)
    publishedAt = models.DateTimeField(max_length=50)
    video_title = models.TextField(blank=True)
    video_desc = models.TextField(blank=True)
    thumbnail_url = models.TextField(blank=True)

    class Meta:
        db_table = 'VIDEO_DETAILS'


class api_keys(models.Model):
    api_key = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'API_KEYS'