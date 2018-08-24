from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):
    tittle = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    objects = models.Manager() #The default manager

    # To avoid saving every entry as Blogs object and use the title as default name
    def __str__(self):
        return self.tittle
    #saving as Blogs not Blogss
    class Meta:
        verbose_name_plural = "Posts"
