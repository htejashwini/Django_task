from django import forms


class SubjectStudentForm(forms.Form):
    students = forms.CharField(label='Students (comma-separated)', max_length=100)
    subjects = forms.CharField(label='Subjects (comma-separated)', max_length=100)

    def clean(self):
        cleaned_data = super().clean()
        students = cleaned_data.get('students', '').split(',')
        subjects = cleaned_data.get('subjects', '').split(',')

        if len(students) == 0 or len(subjects) == 0:
            raise forms.ValidationError('Both students and subjects are required.')
        return cleaned_data
