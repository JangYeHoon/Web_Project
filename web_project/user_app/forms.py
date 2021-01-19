from django.forms import ModelForm
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = {'id', 'email', 'password', 'name_ko', 'name_eng', 'call', 'passport', 'country', 'birthday', 'sex'}