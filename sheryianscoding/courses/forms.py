from django import forms
from .models import *

class PaymentForm(forms.Form):
    model = Payments
    fields = ['card_holder_name', 'card_last4', 'card_type']

    labels = {
        'card_holder_name': 'Card Holder Name',
        'card_last4': 'Card Last 4 Digits',
        'card_type': 'Card Type'
    }