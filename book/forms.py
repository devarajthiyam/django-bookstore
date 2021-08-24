from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    required_css_class = 'required-field'
    publish_date = forms.DateField(widget=forms.TextInput(
        attrs={'type' : 'date'}
        ))

    class Meta:
        
        model = Book

        exclude = []

        labels = {}



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self:
            field.field.widget.attrs.update({'class': 'form-control'})

        self.fields['publish_date'].widget.attrs.update({'class': 'form-control'})