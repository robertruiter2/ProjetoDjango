from django.db import models

# Create your models here.
class CustomManager(models.Model):
    def search(self, query):
        return self.get_queryset().filter(models.Q(name__icontains = query) | models.Q(description__icontains = query))

class Course(models.Model):
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Sobre o curso', blank=True)
    start_date = models.DateField('Data de Início', blank=True, null=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', blank=True, null=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = CustomManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.slug