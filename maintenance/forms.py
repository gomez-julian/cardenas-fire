from django.forms import ModelForm
from maintenance.models import FirebaseReport

class FirebaseReportForm(ModelForm):
    class Meta:
        model = FirebaseReport
        exclude = []