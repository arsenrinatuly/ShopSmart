from django.db import models

# Create your models here.
import uuid
from django.db import models

class ShoppingList(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.uuid)

class Item(models.Model):
    list = models.ForeignKey(ShoppingList, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_bought = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({'✓' if self.is_bought else '✗'})"
