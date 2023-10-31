from django import forms
from .models import JobApply
from django.core.validators import FileExtensionValidator

class JobApplyForm(forms.ModelForm):
    cv = forms.FileField(
        label='cv',
        widget=forms.ClearableFileInput(attrs={"accept": ".pdf"}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf'], message='Only pdf file are allowed')],
    )

    class Meta:
        model = JobApply
        fields = ['email', 'linkedIn', 'github', 'cv', 'cover_litter']

