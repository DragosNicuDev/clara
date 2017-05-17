from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import PhotoUpload
from django.utils.html import mark_safe


class ImageInline(GenericTabularInline):
    model = PhotoUpload


# Register your models here.
class PhotoUploadAdmin(admin.ModelAdmin):
    fields = ('image_tag', 'image', 'status', 'date_upload', 'date_approved')
    list_display = ('image_tag', 'status', 'date_upload', 'date_approved')
    readonly_fields = ('image_tag', 'date_upload', 'date_approved')
    list_filter = ('status',)
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(status='ap')
    make_published.short_description = "Mark selected photos as Approved"

    def image_tag(self, obj):
        return mark_safe('<img src="%s" width="150"/>' % (obj.image.url))

    image_tag.short_description = 'On site photo'


admin.site.register(PhotoUpload, PhotoUploadAdmin)
# admin.site.register()
