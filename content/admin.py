from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from content.models import  Content, Menu

class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'status', 'create_at']
    list_filter = ['status', 'type']
    prepopulated_fields = {'slug': ('title',)}

class MenuAdmin(DraggableMPTTAdmin):
    mptt_indent_field = 'title'
    list_display = ['tree_actions', 'indented_title', 'status']


admin.site.register(Content, ContentAdmin)
admin.site.register(Menu, MenuAdmin)

