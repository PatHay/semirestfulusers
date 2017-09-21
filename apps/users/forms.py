from django import forms
import re, md5

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# # PASSWORD_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d') #searches for a upper case followed by a number and the |(or operator) looks for a number then a upper case
NAME_REGEX = re.compile(r'\W.*[A-Za-z]|[A-Za-z]\.*\W|\d.*[A-Za-z]|[A-Za-z].*\d')

class Register(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=255)
    last_name = forms.CharField(label='Last Name', max_length=255)
    email = forms.CharField(label='Email', max_length=255)
    def clean(self):
        cleaned_data = super(Register, self).clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        email = cleaned_data.get("email")
        if NAME_REGEX.search(first_name):
            msg = "Invalid first name!"
            self.add_error('first_name', msg)
        if NAME_REGEX.search(last_name):
            msg = "Invalid last name!"
            self.add_error('last_name', msg)
        if not EMAIL_REGEX.match(email):
            msg = "Invalid Email Address"
            self.add_error('email', msg)