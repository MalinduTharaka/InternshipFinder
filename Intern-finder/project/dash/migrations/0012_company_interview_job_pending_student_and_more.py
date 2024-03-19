# Generated by Django 5.0.2 on 2024-03-08 16:06

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0011_alter_intern_flyer'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.IntegerField(unique=True)),
                ('cmp_name', models.CharField(max_length=20)),
                ('cmp_username', models.CharField(max_length=20, unique=True)),
                ('cmp_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('stu_nic', models.CharField(max_length=15)),
                ('position', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyid', models.IntegerField()),
                ('jobid', models.IntegerField()),
                ('jobrole', models.CharField(max_length=20)),
                ('flyer', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='pending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.IntegerField()),
                ('stu_nic', models.IntegerField()),
                ('jobrole', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('stu_nic', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('telephone', models.CharField(max_length=20)),
                ('job_role', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=50)),
                ('stu_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='CompanyRegistration',
        ),
        migrations.DeleteModel(
            name='Intern',
        ),
        migrations.DeleteModel(
            name='InternRegistration',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='age',
            new_name='cv_id',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='full_name',
            new_name='degree',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='stu_id',
            new_name='work_exp',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='nic',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='qualification',
        ),
        migrations.AddField(
            model_name='cv',
            name='institute',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='optional_detail',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='projects',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='work_company',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cv',
            name='skills',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='cv',
            name='stu_nic',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='dash.student'),
            preserve_default=False,
        ),
    ]