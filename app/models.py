from django.db import models

# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=250, blank=False, null=False)
    country = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='authors', max_length=255, blank=False, null=False, default='-')
    biography = models.TextField(blank=False, null=False)

    def __str__(self):
        return f'{self.name} {self.last_name}'

    class Meta:
        db_table = 'authors'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['id']

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250, blank=False, null=False)
    date_published = models.DateField(blank=False, null=False)
    image = models.ImageField(upload_to='books', max_length=255, blank=False, null=False, default='-')
    author_id = models.ManyToManyField(Author)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'books'
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['id']
    