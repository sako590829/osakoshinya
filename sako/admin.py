from django.contrib import admin
from .models import Blog
from django.utils.safestring import mark_safe


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','createday','coment','image')
    search_fields = ('createday',)

    def image(self, obj):
         return mark_safe('<image src="{}" style="width:50px; height:50px;">'.format(obj.image.url))

admin.site.register(Blog,BlogAdmin)

