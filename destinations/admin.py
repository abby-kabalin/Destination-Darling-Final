from django.contrib import admin
from .models import Destination, Attraction, Destination_Comment

class DestCommentInline(admin.TabularInline):
    model = Destination_Comment
    extra = 0


class AttractionInline(admin.TabularInline):
    model = Attraction
    extra = 0

# Register your models here.
class DestinationAdmin(admin.ModelAdmin):
    inlines = [
        DestCommentInline,
        AttractionInline,
    ]
    list_display = [
        "location",
        "details",
        "country",
        "date",
        "author",
    ]

admin.site.register(Destination, DestinationAdmin)
admin.site.register(Attraction)
admin.site.register(Destination_Comment)
