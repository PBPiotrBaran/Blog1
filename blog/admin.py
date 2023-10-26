from django.contrib import admin
from django.utils.html import format_html
from .models import Post

#admin.site.register(Post)

class Voteinline(admin.TabularInline):
   # model = Post # muszę zefiniować nowy model który załaduje dane w tabeli liniowo dane do modelu post
    pass


#dekorowanie, nadpisywanie zdefiniowanych klas systemu
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author','title','show_url']
    list_filter = ['author']
    #list_display_links = ['text']
    search_fields = ['title']
   # inlines = Voteinline


    def show_url(self,obj):
        if len(obj.text) is not None:
            return format_html(f'<a href="{obj.text}" target = blanc > {obj.text}</a>')
        else:
            return ''

    show_url.short_description = 'URL'


#@admin.register(Vote)
#class VoteAdmin(admin.ModelAdmin):
 #   pass


