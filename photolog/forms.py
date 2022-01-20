from .models import Comment, Account, Post
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm      

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

class Meta:
    model = Account
    fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image')
