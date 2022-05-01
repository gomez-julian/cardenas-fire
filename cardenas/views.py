from django.contrib.auth.decorators import login_required
from azure.storage.blob import BlockBlobService
from django.shortcuts import render, redirect
from cardenas.models import *
from cardenas.forms import *
import uuid
import os


DEFAULT_IMAGE_URL = 'https://winaero.com/blog/wp-content/uploads/2019/11/Photos-new-icon.png'


def cfs_dashboard(request):
    return render(request, 'dashboard.html', {})


def get_azure_service():
    azure_account_name = os.environ['AZURE_ACCOUNT_NAME']
    azure_account_key = os.environ['AZURE_ACCOUNT_KEY'] 
    return BlockBlobService(account_name = azure_account_name, 
                            account_key= azure_account_key)


@login_required
def view_infFotografico(request):
    reports = PhotographicReport.objects.all()
    return render(request, 'fotografico/view.html', {'reports' : reports})


@login_required
def create_infFotografico(request):
    if request.method == 'POST':
        form = PhotographicReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('photographic_view')
    return render(request, 'fotografico/create.html', {})


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
    BASE_URL = os.environ['AZURE_STORAGE_URL']
    try:
        file_upload_name = str(uuid.uuid4()) + file.name
        blob_service_client = get_azure_service()
        blob_service_client.create_blob_from_bytes( container_name = os.environ['AZURE_CONTAINER_NAME'], 
                                                    blob_name = file_upload_name, 
                                                    blob = file.read())
        return BASE_URL + file_upload_name
    except:
        return None


def delete_file(file):
    if file != DEFAULT_IMAGE_URL:
        try:
            blob_service_client = get_azure_service()
            file_name = file[file.rfind('/') + 1:]
            blob_service_client.delete_blob(container_name = os.environ['AZURE_CONTAINER_NAME'], 
                                            blob_name = file_name)
            return True
        except:
            return False
    return True


@login_required
def photographic_create_row(request, pk=None):
    if request.method == 'POST':
        report = PhotographicReport.objects.all().filter(id = pk).first()
        file1 = upload_picture(request.FILES['file1']) if 'file1' in request.FILES else DEFAULT_IMAGE_URL
        file2 = upload_picture(request.FILES['file2']) if 'file2' in request.FILES else DEFAULT_IMAGE_URL
        PhotographicItem.objects.create(pictureOne = file1,
                                        pictureTwo = file2,
                                        description = request.POST['description'],
                                        fk_informe = report)
        return redirect('photographic_view_one', pk = report.id)
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

