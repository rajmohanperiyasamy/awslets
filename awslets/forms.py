from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.fields['message'].widget.attrs['class'] = 'message-box'
    #     self.fields['message'].widget.attrs['placeholder'] = 'Write details here'


    class Meta:
        model = Contact
        fields = '__all__'