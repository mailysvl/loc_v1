from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'required': True}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm'}))
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm adult', 'required': True}))
    details = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control md-textarea', 'required': True})
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['details'].label = "Your message"


class MyForm(forms.Form):
    checkIn = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y'),
                                                     attrs={'class': 'form-control form-control-sm', 'require': True}))
    checkOut = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y'),
                                                      attrs={'class': 'form-control form-control-sm', 'require': True}))
    adult = forms.ChoiceField(choices=((None, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)),
                              widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
