
from django import forms
from .models import Blog,Area,Comment

class Formblog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'




class FormArea(forms.ModelForm):
    class Meta:
        model = Area
        fields = '__all__'


class UpdateAreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = '__all__'



class CreateCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['author','text']


