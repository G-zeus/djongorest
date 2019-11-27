from djongo import models

# Create your models here.

class Categoria(models.Model):
    description = models.CharField( max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return '{}' . format(self.description)

    class Meta:
        verbose_name_plural = "Categorias"
     