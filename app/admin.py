from django.contrib.admin import register, ModelAdmin
from .models import Item


@register(Item)
class ItemAdmin(ModelAdmin):
    list_display = 'id', 'title', 'amount', 'price', 'added_time'
    list_display_links = 'id', 'title'
    ordering = 'id',

