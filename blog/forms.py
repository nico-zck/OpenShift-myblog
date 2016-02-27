from django.forms import *

from blog.models import Message, Comment


class CommentForm(ModelForm):
    comment = CharField(label='Your Comment', max_length=300, min_length=10, required=True,
                        widget=Textarea({'placeholder': 'Comment(Required)', 'required': 'required'}))

    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'name': TextInput({'placeholder': 'Name(Required)', 'required': 'required'}),
            'email': EmailInput({'placeholder': 'Email'}),
            'blog_url': URLInput({'placeholder': 'Website'}),
            'article': HiddenInput(),
        }


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'name': TextInput({'placeholder': 'Name', 'required': 'required'}),
            'email': TextInput({'placeholder': 'Email', 'required': 'required'}),
            'phone_number': TextInput({'placeholder': 'Phone'}),
            'qq_number': TextInput({'placeholder': 'QQ'}),
            'message': Textarea({'placeholder': 'Message', 'required': 'required'}),
        }
