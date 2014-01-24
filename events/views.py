from django.shortcuts import render
import datetime

# from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.views import generic

from events.models import Event

def index(request):
    event_expiry_time = datetime.date.now() + datetime.timedelta(minutes=10) # events become "past events" 30 minutes after the start time

    events_for_slider = Event.objects.all().filter(when__gte=event_expiry_time, image__isnull=False)
    forthcoming_events_list = Event.objects.all().filter(when__gte=event_expiry_time).order_by('when')
    past_events_list = Event.objects.all().filter(when__lt=datetime.date.today()).order_by('-when')
    context = {
            'events_for_slider': events_for_slider,
    		'future_events_list': forthcoming_events_list,
    		'past_events_list': past_events_list
    	}
    return render(request, 'index.html', context)

# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_poll_list'

#     def get_queryset(self):
#         """Return the last five published polls."""
#         return Poll.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Event
    template_name = 'event.html'

def about(request):
	return render(request, 'about.html')
