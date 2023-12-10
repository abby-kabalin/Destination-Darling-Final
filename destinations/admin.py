from django.contrib import admin
from .models import Destination, Destination_Comment

class DestCommentInline(admin.TabularInline):
    model = Destination_Comment
    extra = 0


# Register your models here.
class DestinationAdmin(admin.ModelAdmin):
    inlines = [
        DestCommentInline,
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
admin.site.register(Destination_Comment)
