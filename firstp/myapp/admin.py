from django.contrib import admin
from .models import Articles, Category
from django.utils.html import format_html

@admin.action(description='انتشار مقالات انتخاب شده')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
@admin.action(description='پیش نویس مقالات انتخاب شده')
def make_drafted(modeladmin, request, queryset):
    queryset.update(status='d')
@admin.action(description='انتشار دسته بندی انتخاب شده')
def make_published_cat(modeladmin, request, queryset):
    queryset.update(status=False)
@admin.action(description='پیش نویس دسته بندی انتخاب شده')
def make_drafted_cat(modeladmin, request, queryset):
    queryset.update(status=True)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'position', 'parent')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    actions = [make_published_cat, make_drafted_cat]

admin.site.register(Category, CategoryAdmin)
admin.site.site_header = "وبلاگ جنگوی من"

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', Articles.images_tags, 'slug', 'status', 'category_to_str')
    list_filter = ('published', 'status')
    search_fields = ('title', 'discription')
    actions = [make_published, make_drafted]

    Articles.jpublish.short_description = "زمان انتشار"
    def category_to_str(self, obj):
        return ", ".join([categori.title for categori in obj.category_publish()]) 

    category_to_str.short_description = " دسته بندی"
    
admin.site.register(Articles, ArticlesAdmin)
    

