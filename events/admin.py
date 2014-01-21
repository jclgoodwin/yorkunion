from django.contrib import admin
from events.models import Location, Person, Event

admin.site.register(Location)
admin.site.register(Person)
admin.site.register(Event)
