from django.db import models
# Create your models here.

class Recipe(models.Model):
    title = models.CharField('Название', max_length=50)
    describe = models.TextField('Описание')
    image = models.ImageField(upload_to='img/',blank=True)
    objects = models.Manager()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipies'