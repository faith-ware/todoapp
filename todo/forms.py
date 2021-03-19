from django import forms
from .models import Task

class TaskForm(forms.Form):
    name = forms.CharField(max_length=255, label="", widget=forms.TextInput(
        attrs={
            "name" : "name",
            "id" : "text",
            "type" : "text",
            "value" : "",
            "required" : "required",
        }))

class UpdateForm(forms.Form):
    name = forms.CharField(max_length=255, label="Edit", widget=forms.TextInput(
        attrs={
            "name" : "update",
            "id" : "updateText",
            "type" : "text",
            "value" : "",
            "required" : "required",
        }
    ))
