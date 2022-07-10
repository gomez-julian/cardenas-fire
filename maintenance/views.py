from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from maintenance.models import *
from maintenance.forms import FirebaseReportForm

# Create your views here.

@login_required
def view_mensual(request):
    reports = FirebaseReport.objects.all()
    return render(request, 'view.html', {'reports' : reports,
                                        'type' : 'Mensual'})

def create_maintenance(request):
    if request.method == 'POST':
        pass
        form = FirebaseReportForm(request.POST)
        if form.is_valid():
            report = form.save()
            return render(request, 'generate.html', {'report' : report})
    return render(request, 'create.html', {})

def delete_maintenance(request, pk=None):
    report = FirebaseReport.objects.all().filter(id = pk).first()
    if report:
        report.delete()
    return redirect('view_mensual')

def form_maintenance(request, pk=None):
    report = FirebaseReport.objects.all().filter(id = pk).first()
    if report:
        return render(request, 'form.html', {'report' : report})
    return redirect('view_mensual')