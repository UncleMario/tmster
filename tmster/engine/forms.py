from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select

from howmuch.article.models import Student, Opinion, Comment

class StudentForm(ModelForm):
    class Meta:
        model = Student
        widgets = {
        'name' : TextInput(),
        'school' : Select(),
        'twitter' : TextInput(),
        'facebook' : TextInput(),
        }

class OpinionForm(forms.Form):
    variant = forms.ChoiceField(
        widget = forms.Select(),)
    value = forms.IntegerField(
        widget = forms.TextInput())

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        widgets = {
        'text' : TextInput(),
        }