from django.contrib import admin

from .models import Project
from .services import extract_project_images


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "slug",
        "created_at",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    def save_model(
        self,
        request,
        obj,
        form,
        change,
    ):
        super().save_model(
            request,
            obj,
            form,
            change,
        )

        extract_project_images(obj)