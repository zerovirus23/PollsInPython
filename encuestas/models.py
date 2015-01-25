import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField('date published')
    
    #
    def was_published_recently(self):
        return self.publication_date >= timezone.now() - datetime.timedelta(days=1)
    
    was_published_recently.admin_order_field = 'publication_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
    #Representación como cadena del objeto
    def __str__(self):
        return self.question_text
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    #Representación como cadena del objeto
    def __str__(self):
        return self.choice_text
    