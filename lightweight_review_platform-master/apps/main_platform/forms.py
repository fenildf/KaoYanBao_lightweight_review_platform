#!/usr/bin/env python
# encoding: utf-8

from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['title', 'category', 'answer', 'note',]


