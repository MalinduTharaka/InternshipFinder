from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from dash.models import cv

def about(request):
    return render(request, "about.html")

def index(request):
    return render(request, "index.html")

def mycv(request):
    data = cv.objects.all()
    context = {"data": data}
    return render(request, 'mycv.html', context)

def insertData(request):
    data = cv.objects.all()
    context = {"data": data}
    if request.method == "POST":
        cv_id = request.POST.get('cv_id')
        full_name = request.POST.get('full_name')
        nic = request.POST.get('nic')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        institute = request.POST.get('institute')
        degree = request.POST.get('degree')
        work_exp = request.POST.get('work_exp')
        work_company = request.POST.get('work_company')
        skills = request.POST.get('skills')
        projects = request.POST.get('projects')
        optional_details = request.POST.get('optional_details')

        query = cv(
            cv_id=cv_id,
            full_name=full_name,
            nic=nic,
            age=age,
            gender=gender,
            email=email,
            telephone=telephone,
            institute=institute,
            degree=degree,
            work_exp=work_exp,
            work_company=work_company,
            skills=skills,
            projects=projects,
            optional_details=optional_details,
        )
        query.save()
        return redirect("index")  # Redirect to the 'index' view upon successful form submission

    return render(request, "mycv.html", context)

def updateData(request, cv_id):
    instance = get_object_or_404(cv, cv_id=cv_id)
    context = {"instance": instance}

    if request.method == "POST":
        # Get the updated data from the form
        full_name = request.POST.get('full_name')
        nic = request.POST.get('nic')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        institute = request.POST.get('institute')
        degree = request.POST.get('degree')
        work_exp = request.POST.get('work_exp')
        work_company = request.POST.get('work_company')
        skills = request.POST.get('skills')
        projects = request.POST.get('projects')
        optional_details = request.POST.get('optional_details')

        # Update the fields of the existing instance
        instance.full_name = full_name
        instance.nic = nic
        instance.age = age
        instance.gender = gender
        instance.email = email
        instance.telephone = telephone
        instance.institute = institute
        instance.degree = degree
        instance.work_exp = work_exp
        instance.work_company = work_company
        instance.skills = skills
        instance.projects = projects
        instance.optional_details = optional_details

        # Save the updated instance
        instance.save()

        # Redirect to the 'mycv' view upon successful update
        return HttpResponseRedirect(reverse('mycv'))

    return render(request, 'edit.html', context)

def deleteData(request, cv_id):
    # Get the instance of the CV model with the specified id
    instance = get_object_or_404(cv, cv_id=cv_id)

    # Delete the instance
    instance.delete()

    # Redirect to the 'mycv' view after deletion
    return HttpResponseRedirect(reverse('mycv'))
