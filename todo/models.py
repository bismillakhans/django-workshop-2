from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=256)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'todos'
        verbose_name = 'Todo Item'
        verbose_name_plural = 'Todo Items'