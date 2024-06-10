from django.db import models
from django.urls import reverse


# Create your models here.

class GrupoMusical(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation", blank=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Grupo musical"
        verbose_name_plural = "Grupos musicales"


class Author(models.Model):
    """
    Modelo que representa un autor
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s, %s' % (self.last_name, self.first_name)
