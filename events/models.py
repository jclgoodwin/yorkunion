from django.db import models
from geoposition.fields import GeopositionField
import datetime


class Link(models.Model):
    """
    A link to an web page, such as a SoundCloud or YouTube recording.

    """
    title = models.CharField(max_length=300)
    url = models.URLField()

    def __unicode__(self):
        return self.title + ' [' + self.publication + ']'


class PressCutting(Link):
    """
    A link to an web page, usually a review or preview of a York Union event, displayed on the "Press" page.

    """
    author = models.CharField(max_length=200, blank=True)
    publication = models.CharField(max_length=200)
    when = models.DateField(null=True, blank=True)


class Location(models.Model):
    """
    A location (usually a room at the University of York) where events are held.

    """
    name = models.CharField(max_length=200)
    position = GeopositionField()

    def __unicode__(self):
        return self.name


class Person(models.Model):
    """
    A person speaking at an event. Typically only used for events with
    speakers "for the motion" and "against the motion".

    """
    name = models.CharField(max_length=200)
    biography = models.TextField()

    def __unicode__(self):
        return self.name


class Event(models.Model):
    """
    A single event, in the past or in the future.

    """
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
        from django.core.urlresolvers import reverse
        return reverse('event', args=(str(self.slug),))

    def __unicode__(self):
        return self.name
