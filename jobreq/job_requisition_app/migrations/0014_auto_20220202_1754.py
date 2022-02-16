# Generated by Django 3.2.9 on 2022-02-02 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_requisition_app', '0013_jobrequisition_tickets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=200)),
                ('emp_name', models.CharField(max_length=200)),
                ('emp_desi', models.CharField(max_length=200)),
                ('emp_rm1', models.CharField(max_length=200)),
                ('emp_rm1_id', models.CharField(max_length=200)),
                ('emp_rm2', models.CharField(max_length=200)),
                ('emp_rm2_id', models.CharField(max_length=200)),
                ('emp_rm3', models.CharField(max_length=200)),
                ('emp_rm3_id', models.CharField(max_length=200)),
                ('emp_process', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='agent_status',
            field=models.CharField(default='Active', max_length=30),
        ),
    ]