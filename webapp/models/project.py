from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    start_date = models.DateField(
        verbose_name="Дата начала",
        null=False,
        blank=False,
    )
    end_date = models.DateField(
        verbose_name="Дата окончания",
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Название'
    )
    description = models.TextField(
        max_length=2000,
        null=True,
        blank=True,
        verbose_name='Описание'
    )
    users = models.ManyToManyField(
        through='webapp.ProjectUser',
        to=User,
        related_name='users_projects'
    )

    def __str__(self):
        return f"{self.start_date} - {self.end_date} - {self.title} - {self.description[:25]} "

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ["-start_date"]
