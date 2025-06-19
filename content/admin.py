from django.contrib import admin
from .models import ContentItem, ContentItemVersion


class ContentItemVersionInline(admin.TabularInline):
    model = ContentItemVersion
    readonly_fields = ("version_number", "created_at")
    can_delete = False
    extra = 0


@admin.register(ContentItem)
class ContentItemAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "created_at", "updated_at")
    inlines = [ContentItemVersionInline]


admin.site.register(ContentItemVersion)
