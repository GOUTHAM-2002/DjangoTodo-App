from django.db import models

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.title + " " + self.color

class Todos(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
