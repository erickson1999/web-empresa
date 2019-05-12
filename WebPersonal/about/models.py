from django.db import models

# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    image=models.ImageField(upload_to='projects')
    link=models.URLField(null=True,blank=True)
    create=models.TimeField(auto_now_add=True,verbose_name="date create")
    update=models.TimeField(auto_now=True,verbose_name="date update")

    def __str__(self):
        return self.name

