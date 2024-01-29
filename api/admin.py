from django.contrib import admin

from api.models import Package


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("cam_id", "video_color", "time_section", "channel_no", "config_no")
