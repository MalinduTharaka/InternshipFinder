from django.db import models

class cv(models.Model):
    # CV form
    cv_id = models.IntegerField(null=False,  primary_key=True)
    full_name = models.CharField(max_length=100, blank=False, null=False,default='full name')
    nic = models.TextField(max_length=12)
    age = models.IntegerField(blank=False,default=18)
    gender = models.TextField(max_length=10,default='male')
    email = models.EmailField(max_length=255, unique=True,default='123@mail.com')
    telephone = models.IntegerField(blank=False)
    institute = models.CharField(max_length=20) 
    degree = models.TextField(max_length=100)
    work_exp = models.TextField(blank=False, null=False)
    work_company = models.TextField(max_length=100, blank=False)
    skills = models.CharField(max_length=50)
    projects = models.CharField(max_length=500)
    optional_details = models.TextField(max_length=500)

    def __str__(self):
        return str(self.cv_id)

class company(models.Model):
    company_id = models.IntegerField(unique=True, null=False)
    cmp_name = models.CharField(max_length=20)
    type = models.CharField(max_length=20,default='default')
    cmp_username = models.CharField(max_length=20, unique=True)
    cmp_password = models.CharField(max_length=20)

    def _str_(self):
        return str(self.company_id)

class job(models.Model):
    companyid = models.IntegerField(blank=False, null=False)
    jobid = models.IntegerField(blank=False, null=False)
    jobrole = models.CharField(max_length=20, blank=False, null=False)
    flyer = models.CharField(max_length=1000, blank=False, null=False)

    def _str_(self):
        return str(self.jobid)

class student(models.Model):
    stu_nic = models.CharField(max_length=15, primary_key=True, null=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    telephone = models.CharField(max_length=20)
    job_role = models.CharField(max_length=100)
    user_name = models.CharField(max_length=50)
    stu_password = models.CharField(max_length=50)
    

    def _str_(self):
        return self.stu_nic 
    
class Interview(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    date = models.DateField()
    time = models.TimeField()
    stu_nic = models.CharField(max_length=15)
    position = models.CharField(max_length=75)

    def _str_(self):
        return str(self.id)
    
class pending(models.Model):
    company_id = models.IntegerField()
    stu_nic = models.IntegerField()
    jobrole = models.CharField(max_length=20)

    def _str_(self):
        return self.jobrole
