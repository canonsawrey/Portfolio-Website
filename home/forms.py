from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea())

    def __init__(self):
        super(ContactForm, self).__init__()
        self.fields['content'].label = "Message"
