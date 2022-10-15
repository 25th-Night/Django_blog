from django.contrib import admin
from blog.models import Article, Category, Comment

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "get_description"]
    
    @admin.display(description="카테고리 안내")
    def get_description(self, obj):
        return obj.description[:30]

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "get_content"]
    
    @admin.display(description="내용")
    def get_content(self, obj):
        return  obj.content[:30]
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [ "get_article", "get_content"]
    
    @admin.display(description="댓글")
    def get_content(self, obj):
        return  obj.content[:30]
    
    @admin.display(description="게시글 제목")
    def get_article(self, obj):
        return  obj.article.title