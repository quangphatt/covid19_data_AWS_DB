from django import forms

class DateInput(forms.DateInput):
	input_type = 'date'

class DateForm(forms.Form):
	date_picked = forms.DateField(widget=DateInput)