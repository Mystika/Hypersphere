from django.forms import Form,CharField,EmailField,TextInput,PasswordInput,EmailInput
from account.models import User

class SignUpForm(Form):
    username = CharField(label="username",required=True, widget=TextInput(attrs={'placeholder': 'Pick a username','required':'','class':'flat-input flat-warn'}), max_length=20)
    email = EmailField(label="email", required=True, widget=EmailInput(attrs={'placeholder': 'Enter a email','required':'','class':'flat-input flat-warn'}))
    password = CharField(label='password',required=True,widget=PasswordInput(attrs={'placeholder': 'Password','required':'','class':'flat-input flat-warn'}))
    passwordConfirm = CharField(label='password_confirm',required=True,widget=PasswordInput(attrs={'placeholder': 'Password Confirm','required':'','class':'flat-input flat-warn'}))

class LoginForm(Form):
    username = CharField(label="username",required=True, widget=TextInput(attrs={'placeholder': 'Username','required':'','class':'flat-input flat-warn'}), max_length=20)
    password = CharField(label='password',required=True, widget=PasswordInput(attrs={'placeholder': 'Password','required':'','class':'flat-input flat-warn'}))

