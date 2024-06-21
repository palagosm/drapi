from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono_contacto = models.CharField(max_length=15, null=True, blank=True)
    nombre_cliente = models.CharField(max_length=100, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        db_table = 'custom_user'
