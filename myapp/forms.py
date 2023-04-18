from django import forms
from .models import resume

class resumeForm(forms.ModelForm):
    class Meta:
        model = resume
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
             'email': forms.TextInput(attrs={'class': 'form-control'}),
              'phone': forms.TextInput(attrs={'class': 'form-control'}),
               'aboutyou': forms.TextInput(attrs={'class': 'form-control'}), 
             'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'school': forms.TextInput(attrs={'class': 'form-control'}),
            'university': forms.TextInput(attrs={'class': 'form-control'}),
               'experience': forms.TextInput(attrs={'class': 'form-control'}),
                'skills': forms.TextInput(attrs={'class': 'form-control'}),

        }