from django.db import models

# Create your models here.

class DataMaster(models.Model):
    url_string = models.CharField(max_length=30)
    md5_hash = models.CharField(max_length=16)

    def __unicode__(self):
        return "{0}-{1}".format(self.url_string, self.md5_hash)