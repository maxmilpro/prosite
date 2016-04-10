from django.contrib import admin

from .models import Project, Proposal, Section

admin.site.register(Project)
admin.site.register(Proposal)
admin.site.register(Section)