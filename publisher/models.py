from django.db import models
from users.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='books/pdfs/')
    approved = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title
