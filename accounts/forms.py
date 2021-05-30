from django import forms
from .models import Student, User, Hotel
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    mobile_number = forms.CharField(required=True)
    branch = forms.CharField(required=True)
    email = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.first_name = self.cleaned_data.get('first_name')
        student.last_name = self.cleaned_data.get('last_name')
        student.mobile_number = self.cleaned_data.get('mobile_number')
        student.branch = self.cleaned_data.get('branch')
        student.email = self.cleaned_data.get('email')
        student.save()

        return user


class HotelForm(forms.ModelForm):

    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']
