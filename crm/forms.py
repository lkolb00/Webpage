from django import forms
from .models import Student, Event, Club, Meal


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('username', 'password', 'student_name', 'email', 'phone', 'city', 'state','nu_id','role')


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ( 'event_name', 'event_category', 'description', 'location', 'event_date')

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ( 'club_name', 'club_category', 'club_description', 'created_date')

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    class Meta:
        model = Student
        fields = ('username', 'student_name', 'email', 'nu_id', 'city', 'state', 'phone', 'role', 'password' )
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']: raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ('meal_name', 'meal_description', 'meal_drink', 'price')




