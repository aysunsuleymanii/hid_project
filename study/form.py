from django import forms
from study.models import flashcardSet

class FlashcardSetForm(forms.ModelForm):
    class Meta:
        model = flashcardSet
        fields = ['name']