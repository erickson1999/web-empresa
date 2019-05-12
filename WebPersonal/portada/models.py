from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    image=models.ImageField(upload_to='projects')
    create=models.DateTimeField(auto_now_add=True,verbose_name="date create")
    update=models.DateTimeField(auto_now=True,verbose_name="date update")

    def __str__(self):
        return self.title


