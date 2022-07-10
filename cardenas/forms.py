from django.forms import ModelForm
from cardenas.models import PhotographicReport, PhotographicItem

class PhotographicReportForm(ModelForm):
    class Meta:
        model = PhotographicReport
        fields = ['title', 'app_title', 'date']

class PhotographicItemForm(ModelForm):
    class Meta:
        model = PhotographicItem
        fields = ['description', 'pictureOne', 'pictureTwo']