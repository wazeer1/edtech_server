from django.db import models
from main.models import *
from versatileimagefield.fields import VersatileImageField

# Create your models here.
class Question(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.TextField()
    user = models.ForeignKey('accounts.Profiles', on_delete=models.CASCADE)
    images = VersatileImageField(upload_to="static/questions/",blank=True,null=True)
    topic = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        db_table = 'discussions_question'
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ('-date_added',)

    def  __str__(self):
        return self.question
    

class Answer(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey('discussions.Question', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.Profiles', on_delete=models.CASCADE)
    answer = models.TextField()
    is_correct = models.BooleanField(default=False)
    class Meta:
        db_table = 'discussions_answers'
        verbose_name = 'Answers'
        verbose_name_plural = 'Answers'
        ordering = ('-date_added',)

    def  __str__(self):
        return self.question
