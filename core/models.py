from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import shortuuid


# Create your models here.

class files(models.Model):
    tracking_id = models.CharField(default=shortuuid.ShortUUID().random(length=7), editable=False, max_length=8)
    file_name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '{} {}'.format(self.tracking_id, self.file_name)

    def get_absolute_url(self):
        return reverse('core:file_detail', args=[str(self.id)])

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"


class transaction(models.Model):
    file = models.ForeignKey(files, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=True)
