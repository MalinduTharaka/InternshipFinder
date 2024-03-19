# Generated by Django 5.0.2 on 2024-03-05 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.TextField(max_length=10)),
                ('full_name', models.CharField(max_length=100)),
                ('birthday', models.TextField(max_length=20)),
                ('age', models.IntegerField()),
                ('nic', models.TextField(max_length=12)),
                ('gender', models.TextField(max_length=10)),
                ('qualification', models.TextField(max_length=500)),
                ('skills', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('postid', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('companyid', models.CharField(max_length=5)),
                ('jobid', models.CharField(max_length=5)),
                ('jobrole', models.CharField(max_length=5)),
                ('flyer', models.FileField(upload_to='')),
            ],
        ),
    ]