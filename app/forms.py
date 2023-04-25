
from django import forms
from django.forms import ModelForm
from .models import ChatMessage


class ChatMessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
                           "class": "forms", "rows": 3, "placeholder": "Type message here .."}), max_length=200, required=False)

    class Meta:
        model = ChatMessage
        fields = ["body"]
