from django.db import models


# Create your models here.


'''class User(AbstractUser):
    pass
    name = models.CharField(max_length=50,blank=True)
    second_name=models.CharField(max_length=50,blank=True)
    birth_date = models.DateField(null=True,blank=True)
    bio = models.TextField(max_length=500,blank=True)
    userpic = models.ImageField(upload_to='userpic/',blank=True)
    location = models.CharField(max_length=60,blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        abstract = True'''


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




