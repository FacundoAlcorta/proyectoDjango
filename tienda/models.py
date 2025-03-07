from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    precio = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='tienda',null=True,blank=True)
    disponibilidad = models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self) -> str:
        return self.nombre
