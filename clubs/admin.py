from django.contrib import admin
from clubs.models import Location, College, Major, Advisor, Organization, Question

admin.site.register(Location)
admin.site.register(College)
admin.site.register(Major)
admin.site.register(Advisor)
admin.site.register(Question)
admin.site.register(Organization)
admin.autodiscover()
