from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

#oaoaoaoaooaoaoa
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "start_time", "max_users", "min_users")


class LessonAdmin(admin.ModelAdmin):
    list_display = ("name", "video_link", "product_id")

    # def video_link(self, obj):
    #     return mark_safe(f'<a href="{obj.video_link}" target="_blank">{obj.video_link}</a>')
    # video_link.short_description = 'Link'


admin.site.register(Product, ProductAdmin)
admin.site.register(Lesson, LessonAdmin)