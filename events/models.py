from django.db import models
from geoposition.fields import GeopositionField
import datetime


class PressCutting(models.Model):
    name = models.CharField(max_length=300)
    author = models.CharField(max_length=200, blank=True)
    url = models.URLField()
    publication = models.CharField(max_length=200)
    when = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.name, '[' + self.publication + ']'

class Location(models.Model):
    name = models.CharField(max_length=200)
    position = GeopositionField()

    def __unicode__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=200)
    biography = models.TextField()

    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(db_index=False)
    when = models.DateTimeField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to='%Y')
    location = models.ForeignKey(Location, null=True, blank=True)
    facebook_event_id = models.BigIntegerField(null=True, blank=True)
    eventbrite_event_id = models.BigIntegerField(null=True, blank=True)
    blurb = models.TextField(blank=True)
    for_the_motion = models.ManyToManyField(Person, null=True, blank=True, related_name='for')
    against_the_motion = models.ManyToManyField(Person, null=True, blank=True, related_name='against')
    blurb_secondary = models.TextField(blank=True)

    def has_multiple_speakers(self):
        return self.for_the_motion.count() > 0 and self.against_the_motion.count() > 0

    def is_finished(self):
        return self.when + datetime.timedelta(minutes=30) <= datetime.datetime.now()

    def get_absolute_url(self):
        return "/%s" % self.slug

    def __unicode__(self):
        return self.name
