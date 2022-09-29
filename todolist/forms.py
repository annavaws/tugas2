from django import forms
from django.contrib.auth.models import User

from todolist.models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    is_finished = forms.ChoiceField(choices=(
        ("Selesai", "Selesai"),
        ("Belum Selesai", "Belum selesai")
    ), initial="Belum Selesai")

    class Meta():
        model = Task
        exclude = ('user', 'date', 'is_finished')
