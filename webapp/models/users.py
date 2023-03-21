from django.contrib.auth.models import User
from django.db import models

from webapp.models import Project


class ProjectUser(models.Model):
    user = models.ForeignKey(
        to=User,
        related_name='user_projects',
        verbose_name='Пользователь',
        null=False,
        on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        to=Project,
        related_name='project_users',
        verbose_name='Пользователь',
        null=False,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name='Пользователь проекта'
        verbose_name_plural='Пользователи проекта'

