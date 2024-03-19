from django.shortcuts import render,get_object_or_404,redirect
from dash.models import Interview,job,pending,student,company,cv

from django.contrib import messages
from django.db.models import Q

# Create your views here.
def index(request,username):
    cmp = company.objects.filter(cmp_username=username).first()
    interviews = Interview.objects.all()
    students_data = student.objects.all()
    pending_data=pending.objects.all()
    interview_count = Interview.objects.count()
    pending_count = pending.objects.count()
    job_count = job.objects.count()
    color = None
    query = ""
    
    if request.method == "POST":
        if "add" in request.POST:
            date = request.POST.get("date")
            time = request.POST.get("time")
            student_nic = request.POST.get("student")
            position = request.POST.get("position")

            student_obj = get_object_or_404(student, stu_nic=student_nic)

            Interview.objects.create(
            date=date,
            time=time,
            stu_nic=student_obj,
            position=position,
            )
            color = 'success'
            messages.success(request, "Interview Schedule added successfully...")
            return redirect('indexapp',username=username)
        

        elif "update" in request.POST:
            id = request.POST.get("id")
            date = request.POST.get("date")
            time = request.POST.get("time")
            student_nic = request.POST.get("student")  # Assuming this is the NIC of the student
            position = request.POST.get("position")

            updateInterview = get_object_or_404(Interview, id=id)
            updateInterview.date = date
            updateInterview.time = time
            updateInterview.stu_nic = student_nic  # Assign NIC value instead of student object
            updateInterview.position = position
            updateInterview.save()

            color = "info"
            messages.success(request, "Interview Schedule Updated successfully...")

        
        elif "delete" in request.POST:
            id = request.POST.get("id")
            Interview.objects.get(id=id).delete()
            color = "danger"

            messages.success(request,"Student Deleted Successfully")

        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            interviews = Interview.objects.filter(Q(stu_nic__stu_nic__icontains=query) | Q(position__icontains=query))
    
    
    
    context={"interviews":interviews,"pending_data":pending_data, 'interview_count': interview_count, "pending_count": pending_count, "job_count": job_count, "students_data":students_data,"cmp": cmp}
    return render(request,"companyd.html",context)

def view_cv(request, nic):
    cv_data = cv.objects.filter(nic=nic)  # Filter cv objects based on nic field
    return render(request, 'viewcv.html', {'cv_data': cv_data})
