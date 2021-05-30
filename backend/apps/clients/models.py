from django.db import models


class Natural(models.Model):
    dni = models.CharField(max_length=8, unique=True, 
            blank=False, null=False,
            error_messages={'unique':"Este DNI ya se encuentra registrado. :c"}
    )
    names = models.CharField(max_length=100)
    last_name_p = models.CharField(max_length=100)
    last_name_m = models.CharField(max_length=100)

    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    image = models.ImageField(max_length=250, upload_to="clients/", null=True, blank=True)


    def __str__(self):
        return  f"{self.names} {self.last_name_p} {self.last_name_m} - {self.dni}"

    class Meta:
        verbose_name = 'Natural'
        verbose_name_plural = 'Naturals'


class Juridica(models.Model):
    ruc = models.CharField(max_length=11, unique=True, blank=False, null=False)
    name = models.CharField(max_length=100)

    direccion = models.CharField(max_length=100, blank=False, null=False)
    telefono = models.CharField(max_length=100, blank=False, null=False)
    # direccion = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return  f"{self.name}"

    class Meta:
        verbose_name = 'Juridica'
        verbose_name_plural = 'Juridicas'
