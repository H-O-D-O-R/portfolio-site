import os
import zipfile

from django.conf import settings
from django.db import models

from django.conf import settings
from django.db import models


class Project(models.Model):
    title = models.CharField(
        max_length=100
    )

    slug = models.SlugField(
        unique=True
    )

    short_description = models.TextField()

    description = models.TextField()

    stack = models.CharField(
        max_length=300
    )

    github_url = models.URLField(
        blank=True
    )

    image = models.ImageField(
        upload_to='projects/',
        blank=True
    )

    images_archive = models.FileField(
        upload_to='projects/archives/',
        blank=True
    )

    sections = models.JSONField(
        default=list,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    @property
    def images_url(self):
        return (
            f'{settings.MEDIA_URL}'
            f'projects/{self.slug}/images/'
        )

    def __str__(self):
        return self.title