from django import forms
from models import UserProfile
from django.contrib.auth.forms import UserCreationForm
class IamaForm(forms.Form):
    weapon = forms.TypedChoiceField(
        choices = UserProfile.WEAPON_CHOICES,
        coerce = lambda x: str(x),
        widget = forms.Select,
        initial = UserProfile.WEAPON_CHOICES[0][0],
        required = True
    )
    gender = forms.TypedChoiceField(
        choices = UserProfile.GENDER_CHOICES,
        coerce = lambda x: str(x),
        widget = forms.Select,
        initial = UserProfile.GENDER_CHOICES[0][0],
        required = True,
    )

class UserRegistrationForm(UserCreationForm):
    weapon = forms.TypedChoiceField(
        choices = UserProfile.WEAPON_CHOICES,
        coerce = lambda x: str(x),
        widget = forms.Select,
        initial = UserProfile.WEAPON_CHOICES[0][0],
        required = True
    )
    gender = forms.TypedChoiceField(
        choices = UserProfile.GENDER_CHOICES,
        coerce = lambda x: str(x),
        widget = forms.Select,
        initial = UserProfile.GENDER_CHOICES[0][0],
        required = True,
    )
    
    email = forms.EmailField(required=True)
    
    def save(self, commit=True):
        newUser = super(UserCreationForm, self).save(commit=commit)
        newProfile = UserProfile()
        newProfile.user = newUser
        newProfile.is_active = False
        newProfile.gender = self.cleaned_data['gender']
        newProfile.weapon = self.cleaned_data['weapon']
        newProfile.email = self.cleaned_data['email']
        return newProfile
