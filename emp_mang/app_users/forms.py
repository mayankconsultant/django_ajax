from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import  appuser

class UserCreationForm(UserCreationForm):
    class Meta:
        model = appuser
        fields = ('email',)

class UserChangeForm (UserChangeForm):
    class Meta:
        model = appuser
        fields = ('email','password',)
