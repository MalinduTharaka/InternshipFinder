# Generated by Django 5.0.2 on 2024-03-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0005_remove_internregistration_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intern',
            name='companyid',
            field=models.IntegerField(max_length=5),
        ),
        migrations.AlterField(
            model_name='intern',
            name='jobid',
            field=models.IntegerField(max_length=5),
        ),
        migrations.AlterField(
            model_name='intern',
            name='postid',
            field=models.IntegerField(max_length=5, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='internregistration',
            name='intern_id',
            field=models.IntegerField(max_length=6, unique=True),
        ),
    ]
