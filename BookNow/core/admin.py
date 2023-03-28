from django.contrib import admin
from .models import *


@admin.register(MeetingRoom1)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("title", "name", "start", "end")




