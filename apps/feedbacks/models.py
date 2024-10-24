import uuid
from django.db import models


class Feedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_positive = models.BooleanField(default=True)
    text = models.CharField(max_length=255)
    rating = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating}"
