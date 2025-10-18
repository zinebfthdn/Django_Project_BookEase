from django import forms
from users.models import User


class PublisherEditForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'mt-1 px-3 py-2 h-10  border border-gray-300 focus:ring-1 focus:outline-none focus:ring-blue-500 focus:border-blue-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md',
            'placeholder': 'Username'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'mt-1 px-3 py-2 h-10  border border-gray-300 focus:ring-1 focus:outline-none focus:ring-blue-500 focus:border-blue-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md',
            'placeholder': 'Email'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email']