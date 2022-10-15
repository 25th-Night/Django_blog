from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name = "카테고리")
    description = models.TextField(max_length=255, verbose_name="카테고리 안내")
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "카테고리"
        verbose_name_plural = "카테고리 목록"
    

class Article(models.Model):
    category = models.ManyToManyField(Category, blank=True, verbose_name="카테고리")
    title = models.CharField(max_length=100, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="갱신일")
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "게시글"
        verbose_name_plural = "게시글 목록"


class Comment(models.Model):
    content = models.CharField(max_length=100, verbose_name= "댓글")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name="게시글")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="갱신일")

    def __str__(self):
        return f"{self.content[:10]}"
    
    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글 목록"