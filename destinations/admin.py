from django.contrib import admin
from .models import Destination, DestinationComment

class DestinationCommentInline(admin.TabularInline):
    model = DestinationComment
    extra = 0


# Register your models here.
class DestinationAdmin(admin.ModelAdmin):
    inlines = [
        DestinationCommentInline,
    ]
    list_display = [
        "location",
        "details",
        "country",
        "rating",
        "date",
        "author",
    ]

admin.site.register(Destination, DestinationAdmin)
admin.site.register(DestinationComment)
