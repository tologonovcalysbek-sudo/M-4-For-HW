from django.db import models


class Tag(models.Model):
    name = models.CharField()

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)  
    description = models.TextField(null=True, blank=True)  
    is_active = models.BooleanField(default=True)  

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    title = models.CharField()
    content = models.TextField()
    rate = models.IntegerField()
    user = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        name = self.category.name if self.category else "-"
        return f"{self.title} -- {name}"

















































# class Category(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     is_active = models.BooleanField()

#     def __str__(self):
#         return self.title
    

