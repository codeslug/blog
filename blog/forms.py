from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class FeedbackForm(forms.Form):
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)

class SurveyForm(forms.Form):
    MEALS = [("b", "Breakfast"), ("l", "Lunch"), ("d", "Dinner")]
    favorite_meal = forms.ChoiceField(choices=MEALS)