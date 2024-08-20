from django.contrib.auth.forms import UserCreationForm
from .models import User, Travel
from django.forms import ModelForm
class MyUserCreationForm(UserCreationForm):
        class Meta:
            model = User
            fields = ['username', 'password1', 'password2']


class TravelForm(ModelForm):
    class Meta:
        model = Travel
        fields = '__all__'



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','username','email','bio','travels']