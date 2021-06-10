from django.db import models
from django.core import validators
# Managers
from apps.beneficiarys.managers import BeneficiarioManager, OriginManager


class Origin(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(
        auto_now_add=True
    )   

    objects = models.Manager()
    plus_objects = OriginManager()

    def __str__(self):
        return f"{self.name}"


class Beneficiario(models.Model):
    dni = models.CharField(
        max_length=8,
        unique=True,
        error_messages={
            'unique': f"DNI ya registrado "
        },
        validators=[
            validators.MinLengthValidator(8)
        ]
    )
    names = models.CharField(
        max_length=255
    )
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)

    created_at = models.DateTimeField(
        auto_now_add=True
    )        

    objects = models.Manager()
    plus_objects = BeneficiarioManager()

    def __str__(self):
        return self.names