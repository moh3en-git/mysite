from django.contrib import admin
from blog.models import Post,Contact
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author','counted_views','status','published_date','created_date',)
    search_fields = ('title','content',)
    #ordering = ['-published_date']
    list_filter = ('status','author')

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','created_date')
    list_filter = ('email',)
    search_fields = ('name','message')

admin.site.register(Contact,ContactAdmin)
admin.site.register(Post,PostAdmin)