from django.db import models

# Create your models here.
class Blog(models.Model): #Model?
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField() #이게 입력받는 것인가?

    def __str__(self):
        return self.title 

    def summary(self):
        return self.body[:100]

