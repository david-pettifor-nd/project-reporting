from django.contrib import admin
from time_management.models import RedmineUser, TeamMember, Team

# Register your models here.
admin.site.register(RedmineUser)
admin.site.register(TeamMember)
admin.site.register(Team)