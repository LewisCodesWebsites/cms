from django.db import models
from django.conf import settings


class ContentItem(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="content_items",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        creating = self.pk is None
        super().save(*args, **kwargs)
        if creating:
            version_number = 1
        else:
            version_number = self.versions.count() + 1
        ContentItemVersion.objects.create(
            item=self,
            title=self.title,
            body=self.body,
            version_number=version_number,
        )

    def __str__(self) -> str:
        return f"{self.title}"


class ContentItemVersion(models.Model):
    item = models.ForeignKey(ContentItem, related_name="versions", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    version_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-version_number"]

    def __str__(self) -> str:
        return f"{self.item.title} v{self.version_number}"
