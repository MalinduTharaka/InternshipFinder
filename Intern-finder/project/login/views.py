from django.shortcuts import render, redirect
from django.contrib import messages
from dash.models import student, company

def main_page(request):
    return render(request, 'mainpage.html')

def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            student_obj = student.objects.get(user_name=username, stu_password=password)
            # Perform any additional actions after successful login
            return redirect('indexx', username=username)  # Redirect to student dashboard
        except student.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'stulogin.html')

def company_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            company_obj = company.objects.get(cmp_username=username, cmp_password=password)
            # Perform any additional actions after successful login
            return redirect('indexapp', username=username)  # Redirect to company dashboard
        except company.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'cmplogin.html')
