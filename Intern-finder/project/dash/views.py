from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import job, company, Interview, pending, student

@login_required
def indexx(request, username):
    # Fetching student data filtered by username
    stu = student.objects.filter(user_name=username).first()
    
    # Fetching other data
    data = job.objects.all()
    datac = company.objects.all()
    datai = Interview.objects.all()
    datap = pending.objects.all()
    
    context = {
        "data": data,
        "datac": datac,
        "datai": datai,
        "datap": datap,
        "stu": stu,  # Passing student data to the template
        "username": username
    }
    return render(request, 'student.html', context)

def apply(request):
    companyid = request.GET.get('companyid')
    companyname = request.GET.get('companyname')
    jobrole = request.GET.get('jobrole')
    
    intern_data = job.objects.filter(pk=1).first()
    flyer = None
    if intern_data:
        flyer = intern_data.flyer
    
    context = {
        'flyer_text': flyer,
        'companyid': companyid,
        'companyname': companyname,
        'jobrole' : jobrole,
    }
    
    return render(request, 'apply.html', context)

@login_required
def apply_job(request):
    if request.method == 'GET':
        companyid = request.GET.get('companyid')
        jobrole = request.GET.get('jobrole')
        
        # Assuming you want to get the username of the logged-in user
        username = request.user.username
        
        stu_nic = 20
        pending.objects.create(company_id=companyid, jobrole=jobrole, stu_nic=stu_nic)
        
        # Redirect to indexx with the username parameter
        return redirect('indexx', username=username)
