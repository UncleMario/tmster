from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select

from tmster.engine.models import Student, Opinion, Comment

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ('calification','points','total_surveys')
        widgets = {
        'name' : TextInput(attrs={'placeholder':'Nombre'}),
        'school' : Select(attrs={'class':''}),
        'carrer' : TextInput(attrs={'placeholder':'Carrera'}),
        'facebook' : TextInput(attrs={'placeholder':'Facebook'}),
        'twitter' : TextInput(attrs={'placeholder':'Twitter'}),
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

class SurveyForm(forms.Form):
    opinion1 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
        )
    opinion2 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
        )
    opinion3 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
        )
    opinion4 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
        )
    opinion5 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
        )
    comment = forms.CharField(
        required=False,
        widget = forms.Textarea()
        )
