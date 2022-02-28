from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse

from .forms import *


# Create your views here.

def landing_page(request):
    if request.method == 'POST':
        var = request.POST
        tracking_id = var['query']
        file = files.objects.get(tracking_id=tracking_id)
        history = transaction.objects.filter(file=file).order_by('created_at')
    else:
        return render(request, 'core/landing-page.html')

    return render(request, 'core/landing-page.html', {'history': history})


@login_required
def file_view(request):
    userquery = transaction.objects.filter(assigned_to=request.user, is_active=True).values('file')
    filequery = files.objects.filter(id__in=userquery)

    return render(request, 'core/file_view.html', {'files': filequery})


@login_required
def file_detail(request, pk):
    file = files.objects.get(id=pk)
    if request.method == 'POST':
        form = CreateTransactionForm(request.POST, initial={'file': file})
        if not form.is_valid():
            pass
        else:
            tranins = form.save(commit=False)
            usrchk = transaction.objects.filter(file=file, assigned_to=tranins.assigned_to, is_active=True)
            if usrchk.exists():
                return HttpResponse('Cant assign to this user')
            else:
                ins = transaction.objects.get(file=file, assigned_to=request.user, is_active=True)
                print(ins.is_active)
                ins.is_active = False
                ins.save()
                form.save()
                return redirect('core:file_view')
    else:
        form = CreateTransactionForm(initial={'file': file})

    return render(request, 'core/file_detail.html', {'file': file, 'form': form})


@login_required
def file_add(request):
    if request.method == 'POST':
        form = CreateFile(request.POST)
        if form.is_valid():
            create_file = form.save()
            create_trans = transaction.objects.create(file=create_file, assigned_to=request.user)
            return redirect('core:file_view')
    else:
        form = CreateFile
    return render(request, 'core/file_add.html', {'form': form})


@login_required
def file_delete(request, pk):
    files.objects.get(id=pk).delete()
    return redirect('core:file_view')
