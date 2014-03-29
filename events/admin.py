from django.contrib import admin
from events.models import PressCutting, Location, Person, Event

admin.site.register(PressCutting)
admin.site.register(Location)
admin.site.register(Person)
admin.site.register(Event)
