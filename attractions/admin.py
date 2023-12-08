from django.contrib import admin
from .models import Attraction, AttractionComment

class CommentInline(admin.TabularInline):
    model = AttractionComment
    extra = 0

class AttractionAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = [
        "name",
        "author",
        "location",
        "description",
        "rating",
        "address",
        "tags",
    ]

admin.site.register(Attraction, AttractionAdmin)
admin.site.register(AttractionComment)
