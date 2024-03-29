from django.db import models


class Blog(models.Model):
    """ Модель Блога """
    poster = models.ImageField(
        upload_to="blogs/",
        verbose_name="Постер",
    )
    title = models.CharField(
        max_length=120,
        verbose_name="Название",
    )
    description = models.TextField(
        max_length=2000,
        verbose_name="Описание",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
