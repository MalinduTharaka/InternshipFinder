from django.shortcuts import render,redirect
from dash.models import job

# Create your views here.
def index(request):
    return render(request,"posting.html")

def insertData(request):
    data=job.objects.all()
    print(data)
    context={"data":data}
    
    if  request.method == "POST":
        companyid=request.POST.get('companyid')
        jobid=request.POST.get('jobid')
        jobrole=request.POST.get('jobrole')
        flyer=request.POST.get('flyer')
        print(companyid,jobid,jobrole,flyer)
        query=job(companyid=companyid , jobid=jobid ,jobrole=jobrole , flyer=flyer )   
        query.save()

        return redirect('/')

    return render(request,"posting.html",context)