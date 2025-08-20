from django.db import models

# Create your models here.
class flashcard(models.Model):
    question=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    file=models.FileField(upload_to='flashcardSource/',blank=True,null=True)
    text=models.TextField(blank=True,null=True)
    favourite=models.BooleanField(default=False)

class flashcardSet(models.Model):
    name=models.CharField(max_length=100)
    cards=models.ForeignKey(flashcard,on_delete=models.CASCADE,blank=True,null=True,related_name='flashcards');

class summary(models.Model):
    summaryFile=models.FileField(blank=True,null=True);
    inputFile=models.FileField(upload_to='summarySource/',blank=True,null=True);

class graded_assignment(models.Model):
    assigmentName=models.TextField(max_length=100,null=True,blank=True);

class assignments(models.Model):
    assignmentFile=models.FileField(upload_to='assignments/',blank=True,null=True);
    name=models.CharField(max_length=100,null=True,blank=True);
    result=models.TextField(max_length=2,blank=True,null=True);

    assignments=models.ForeignKey(graded_assignment,on_delete=models.CASCADE,blank=True,null=True,related_name='graded_assignments');