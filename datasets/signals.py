from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from dramatiq import pipeline

from .models import File


@receiver(post_save, sender=File)
def backup_and_extract_content(sender, instance, **kwargs):
    from .tasks import backup_file, content_from_file

    if instance.s3_url is None or instance.content is None:
        if settings.ASYNC_FILE_PROCESSING:
            pipeline(
                [
                    backup_file.message(instance.pk),
                    content_from_file.message_with_options(
                        pipe_ignore=True, args=(instance.pk,)
                    ),
                ]
            ).run()
        else:
            backup_file_url = backup_file(instance.pk)
            if backup_file_url:
                content_from_file(instance.pk)
