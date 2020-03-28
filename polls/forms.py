from django import forms
from django.forms import ModelForm
from .models import *

class QuestionCreationForm(forms.ModelForm):
	class Meta:
		model = Question 
		fields = ['question_text']

class ChoiceCreationForm(forms.ModelForm):
	class Meta:
		model = Choice 
		fields = ['option']