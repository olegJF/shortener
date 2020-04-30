from django.db import models
from short_urls.utils import create_short_url, validate_url


class URL(models.Model):
    url = models.CharField(max_length=250,  validators=[validate_url])
    short = models.CharField(max_length=7, unique=True,  blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    cnt = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.short :
            self.short = create_short_url(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
