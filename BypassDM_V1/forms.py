from tinymce.widgets import TinyMCE

class TweetForm(forms.Form):
    username = forms.CharField(max_length=255)
    message = forms.CharField(widget=TinyMCE())



# from django import forms

# class TweetForm(forms.Form):
#     username = forms.CharField(max_length=255)
#     message = forms.CharField(widget=forms.Textarea)


