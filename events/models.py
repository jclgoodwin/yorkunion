from django.db import models
from geoposition.fields import GeopositionField


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
    slug = models.SlugField(db_index=False)
    when = models.DateTimeField()
    location = models.ForeignKey(Location, null=True, blank=True)
    facebook_event_id = models.BigIntegerField(null=True, blank=True)
    eventbrite_event_id = models.BigIntegerField(null=True, blank=True)
    blurb = models.TextField(null=True, blank=True)
    speakers = models.OneToOneField(Person, null=True, blank=True)
    blurb_secondary = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name
