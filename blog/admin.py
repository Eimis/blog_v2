from django.contrib import admin

from blog.models import StaticFiles
from blog.models import Thought


class StaticFilesAdmin(admin.ModelAdmin):
    pass


class ThoughtAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(StaticFiles, StaticFilesAdmin)
admin.site.register(Thought, ThoughtAdmin)
