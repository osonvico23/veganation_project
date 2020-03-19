from django.contrib.auth.models import User
from veganation.models import UserProfile
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
<<<<<<< HEAD
        fields = ('username','firstName','lastName','email',
        'password')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False);

=======
        fields = ('username', 'email', 'password',)
>>>>>>> 743661b8ccee8b567c81f294db1fe5a0dff6d157

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('firstName', 'lastName', 'veganSince',
        'isVegan', 'profilePic', 'quote', 'occupation', 'city',)
