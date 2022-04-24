from django.shortcuts import render, redirect
from cardenas.models import *
from cardenas.forms import *
from django.contrib.auth.decorators import login_required
import uuid
from azure.storage.blob import BlockBlobService

# Create your views here.

def cfs_dashboard(request):
    return render(request, 'dashboard.html', {})

@login_required
def view_infFotografico(request):
    reports = PhotographicReport.objects.all()
    return render(request, 'fotografico/view.html', {'reports' : reports})

@login_required
def create_infFotografico(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PhotographicReportForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('photographic_view')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = PhotographicReportForm()
    return render(request, 'fotografico/create.html', {'form': form})

@login_required
def photographic_view_one(request, pk=None):
    report = PhotographicReport.objects.all().filter(id = pk).first()
    if report:
        photos = PhotographicItem.objects.all().filter(fk_informe = report.id)
        context = {
            'report' : report,
            'photos' : photos,
        }
        return render(request, 'fotografico/view_one.html', context)
    return redirect('cfs_dashboard')

def upload_picture(file):
    BASE_URL = 'https://azurestoragedjango.blob.core.windows.net/blobstoragedjango/'
    try:
        file_upload_name = str(uuid.uuid4()) + file.name
        blob_service_client = BlockBlobService(account_name = 'azurestoragedjango', 
                                                    account_key='pcl7A+5jw+Hru8JNcJKOdhnxKfQBHTkPvz13wflaukb42v9o7nLLcRELwAsJRM/Y8xEy/AyNfRd/+AStvDu7fA==')
        blob_service_client.create_blob_from_bytes( container_name = 'blobstoragedjango', blob_name = file_upload_name, blob = file.read())
        return BASE_URL + file_upload_name
    except:
        return None

def delete_file(file):
    if file != 'https://winaero.com/blog/wp-content/uploads/2019/11/Photos-new-icon.png':
        try:
            blob_service_client = BlockBlobService(account_name = 'azurestoragedjango', 
                                                    account_key='pcl7A+5jw+Hru8JNcJKOdhnxKfQBHTkPvz13wflaukb42v9o7nLLcRELwAsJRM/Y8xEy/AyNfRd/+AStvDu7fA==')
            file_name = file[file.rfind('/') + 1:]
            blob_service_client.delete_blob(container_name = 'blobstoragedjango', blob_name = file_name)
            return True
        except:
            return False
    return True

@login_required
def photographic_create_row(request, pk=None):
    if request.method == 'POST':
        report = PhotographicReport.objects.all().filter(id = pk).first()
        if 'file1' in request.FILES:
            file1 = upload_picture(request.FILES['file1'])
        else:
            file1 = "https://winaero.com/blog/wp-content/uploads/2019/11/Photos-new-icon.png"
        if 'file2' in request.FILES:
            file2 = upload_picture(request.FILES['file2'])
        else:
            file2 = "https://winaero.com/blog/wp-content/uploads/2019/11/Photos-new-icon.png"
        PhotographicItem.objects.create(
            description = request.POST['description'],
            pictureOne = file1,
            pictureTwo = file2,
            fk_informe = report
        )
        return redirect('photographic_view_one', pk = report.id)
        # form = EvidenciaFotograficaForm(request.POST)
        # if form.is_valid():
        #     report = form.save()
        #     report.fk_informe = pk
        #     return redirect('photographic_view_one', pk = report.id)
        # else:
        #     return redirect('dashboard_home')
    return render(request, 'fotografico/create_item.html', {})

@login_required
def photographic_generate(request, pk=None):
    report = PhotographicReport.objects.all().filter(id = pk).first()
    if report:
        photos = PhotographicItem.objects.all().filter(fk_informe = report.id)
        context = {
            'report' : report,
            'photos' : photos,
        }
        return render(request, 'fotografico/document.html', context)
    return redirect('cfs_dashboard')

@login_required
def photographic_delete(request, pk=None):
    report = PhotographicReport.objects.all().filter(id = pk).first()
    if report:
        items = PhotographicItem.objects.all().filter(fk_informe = report)
        for item in items:
            if delete_file(item.pictureOne) and delete_file(item.pictureTwo):
                item.delete()
        report.delete()
    return redirect('photographic_view')

@login_required
def photographic_delete_item(request, pk=None):
    item = PhotographicItem.objects.all().filter(id = pk).first()
    report = item.fk_informe
    if item:
        if delete_file(item.pictureOne) and delete_file(item.pictureTwo):
            item.delete()
    return redirect('photographic_view_one', pk=report.id)
    