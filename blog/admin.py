from django.contrib import admin
from blog.models import Article

# Register your models here.

# admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "get_content"]
    
    @admin.display(description="내용")
    def get_content(self, obj):
        return  obj.content[:30]