from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Tag(models.Model):
    title = models.CharField("Название", max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self) -> str:
        return f"{self.title}"


class News(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    text = models.TextField("Содержание")
    image = models.ImageField(upload_to="news/%Y/%m/%d")
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self) -> str:
        return f"Новость: {self.title}"


class View(models.Model):
    quantity = models.PositiveIntegerField("Количество просмотров", default=0)
    news = models.OneToOneField(to=News, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Просмотр"
        verbose_name_plural = "Просмотры"

    def __str__(self) -> str:
        return f"Просмотры новости: {self.news}"


@receiver(post_save, sender=News)
def create_profile(sender, **kwargs) -> None:  # noqa
    if kwargs.get("created"):
        View.objects.create(news=kwargs.get("instance"))
