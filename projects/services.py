import os
import zipfile

from django.conf import settings


def extract_project_images(project):
    if not project.images_archive:
        return

    archive_path = project.images_archive.path

    output_dir = os.path.join(
        settings.MEDIA_ROOT,
        "projects",
        project.slug,
        "images",
    )

    os.makedirs(
        output_dir,
        exist_ok=True,
    )

    with zipfile.ZipFile(
        archive_path,
        "r",
    ) as archive:

        for member in archive.infolist():

            if member.is_dir():
                continue

            filename = os.path.basename(
                member.filename
            )

            if not filename:
                continue

            extension = os.path.splitext(
                filename
            )[1].lower()

            if extension not in {
                ".png",
                ".jpg",
                ".jpeg",
                ".webp",
                ".gif",
            }:
                continue

            target_path = os.path.join(
                output_dir,
                filename,
            )

            with archive.open(member) as source:
                with open(
                    target_path,
                    "wb",
                ) as target:
                    target.write(
                        source.read()
                    )