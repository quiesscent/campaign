from django.contrib import admin
from .models import Event, Blog, Candidate, Issue, Volunteer, Ward, County, Policies
# Register your models here.

admin.site.register(Event)
admin.site.register(Blog)
admin.site.register(Volunteer)
admin.site.register(Ward)
admin.site.register(County)
admin.site.register(Policies)
admin.site.register(Issue)

