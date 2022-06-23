from os import name
import uuid
from django.db import models


class Industry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.IntegerField()
    # creator = models.ForeignKey()
    # updater = models.ForeignKey()
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    name = models.CharField(max_length=128)
    image = models.FileField(upload_to='industry/')

    class Meta:
        verbose_name_plural = 'Industries'

    def __str__(self):
        return self.name
