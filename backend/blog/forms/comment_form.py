__all__ = ['CommentForm']


from django import forms


class CommentForm(forms.Form):
    comment_content = forms.CharField()
