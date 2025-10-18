from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'pdf', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'mt-1 focus:ring-blue-500 border px-3 py-2 h-10 focus:ring-1 focus:outline-none focus:border-blue-100 block w-full shadow-sm sm:text-sm'
                         ' border-gray-300 rounded-md'
            })
