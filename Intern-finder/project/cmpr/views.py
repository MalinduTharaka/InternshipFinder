from django.shortcuts import render, redirect, get_object_or_404
from dash.models import company
from .forms import CompanyForm

def company_list(request):
    companies = company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})

def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_login')
    else:
        form = CompanyForm()
    return render(request, 'company_form.html', {'form': form})

def company_update(request, company_id):
    # Rename the model variable to avoid conflict
    comp = get_object_or_404(company, company_id=company_id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=comp)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=comp)
    return render(request, 'company_form.html', {'form': form})


def company_delete(request, company_id):
    # Rename the model variable to avoid conflict
    comp = get_object_or_404(company, company_id=company_id)
    if request.method == 'POST':
        comp.delete()
        return redirect('company_list')
    return render(request, 'company_delete.html', {'company': comp})
