from django.shortcuts import render
import datetime

from django.contrib.sitemaps import Sitemap

# from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from events.models import Event, PressCutting

def index(request):
    event_expiry_time = datetime.datetime.now() + datetime.timedelta(minutes=30) # events become "past events" 30 minutes after the start time

    events_for_slider = Event.objects.all().filter(when__gte=event_expiry_time).exclude(image='').order_by('when')
    forthcoming_events_list = Event.objects.all().filter(when__gte=event_expiry_time).order_by('when')
    past_events_list = Event.objects.all().filter(when__lt=event_expiry_time).order_by('-when')

    context = {
        'events_for_slider':    events_for_slider,
        'future_events_list':   forthcoming_events_list, 
        'past_events_list':     past_events_list
    }

    return render(request, 'index.html', context)

class DetailView(generic.DetailView):
    model = Event
    template_name = 'event.html'

def about(request):
    return render(request, 'about.html')

def press(request):
    context = {
        'press_cuttings': PressCutting.objects.all().order_by('-when')
    }
    return render(request, 'press.html', context)

class EventsSitemap(Sitemap):
    def changefreq(self, item):
        if item.when + datetime.timedelta(days=5) > datetime.datetime.now():
            return 'daily'
        else:
            return 'monthly'

    priority = 0.5

    def items(self):
        return Event.objects.all()

    def lastmod(self, item):
        return item.last_modified

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index', 'about', 'press']

    def location(self, item):
        return reverse(item)
