from django import forms
from .models import Bug, Comment

class AddBugForm(forms.ModelForm):
    class Meta: 
        model = Bug
        fields = ('title', 'description')
        
class AddBugCommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('contents', 'user', 'bug')
        