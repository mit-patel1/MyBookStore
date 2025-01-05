from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class EmailOrMobileLoginForm(AuthenticationForm):
    username = forms.CharField(label="Email or Mobile Number")


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    mobile_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'mobile_number', 'password1', 'password2']

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        if User.objects.filter(mobile_number=mobile_number).exists():
            raise forms.ValidationError("This mobile number is already registered.")
        return mobile_number

