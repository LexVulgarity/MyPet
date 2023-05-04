from django.db import models

class Recipe(models.Model):
    title = models.CharField('Название', max_length=50)
    describe = models.TextField('Описание')
    image = models.ImageField(upload_to='img/',blank=True)
    rec_time=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipies'




