from django import forms

from . models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    # patient_name = forms.CharField(widget=forms.TextInput(attrs={
    #     "placeholder":"Patient Name"
    # }))
    # patient_phone = forms.CharField(widget=forms.TextInput(attrs={
    #     "placeholder":"Patient Phone"
    # }))
    # patient_email = forms.CharField(widget=forms.TextInput(attrs={
    #     "placeholder":"Patient Email"
    # }))

    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date' : DateInput(),
        }

        labels = {
            'patient_name': "Patient Name",
            'patient_phone': "Patient Phone :",
            'patient_email': "Patient Email :",
            'doc_name': "Doctor Name :",
            'booking_date': "Booking Date :",
        }
