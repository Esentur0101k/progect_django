from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f"{self.title} {self.pk}"


class Area(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()

    def __str__(self):
        return f"{self.name}-{self.pk}"


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    text = models.TextField()


    def __str__(self):
        return self.author