from django.shortcuts import render, redirect, get_object_or_404
from dash.models import student
from .forms import StudentForm

def student_list(request):
    students = student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_login')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_update(request, stu_nic):
    # Use a different variable name, e.g., 'student_instance'
    student_instance = get_object_or_404(student, stu_nic=stu_nic)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student_instance)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student_instance)
    return render(request, 'student_form.html', {'form': form})

def student_delete(request, stu_nic):
    # Use a different variable name, e.g., 'student_instance'
    student_instance = get_object_or_404(student, stu_nic=stu_nic)
    if request.method == 'POST':
        student_instance.delete()
        return redirect('student_list')
    return render(request, 'student_delete.html', {'student': student_instance})
