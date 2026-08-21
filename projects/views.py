from django.shortcuts import get_object_or_404, render

from .models import Project


def home(request):
    projects = Project.objects.all()

    return render(
        request,
        "home.html",
        {
            "projects": projects,
            "is_home": True,
        },
    )


def project_detail(request, slug):
    project = get_object_or_404(
        Project,
        slug=slug,
    )

    stack = [
        item.strip()
        for item in project.stack.split(",")
        if item.strip()
    ]

    return render(
        request,
        "project_detail.html",
        {
            "project": project,
            "stack": stack,
            "is_home": False,
        },
    )