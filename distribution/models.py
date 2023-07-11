from datetime import timezone
from django.db import models
from django.utils import timezone


class Distribution(models.Model):
    students = models.TextField()
    subjects = models.TextField()
    result = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def save_form_data(self, form):
        self.students = form.cleaned_data['students']
        self.subjects = form.cleaned_data['subjects']
        self.result = form.cleaned_data['result']
      
        self.save()
