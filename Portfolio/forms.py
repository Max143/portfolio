from django import forms


class SendMsgForm(forms.Form):
    name = forms.CharField(max_length=99, required=True)
    email = forms.EmailField(required=True)
    CHOOSE =[("Company Owner", "Company Owner"), ("HR", "HR"), ("Freelancer", "Freelancer"), ("Other", "Other")]
    person = forms.ChoiceField(choices=CHOOSE, label="Select")
    subject = forms.CharField(max_length=100, required=True)
    msg = forms.CharField(required=True, max_length=1000, widget=forms.Textarea)


