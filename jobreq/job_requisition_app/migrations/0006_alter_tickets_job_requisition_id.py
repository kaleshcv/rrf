# Generated by Django 4.0.1 on 2022-01-26 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_requisition_app', '0005_jobrequisition_tickets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='job_requisition_id',
            field=models.CharField(max_length=10),
        ),
    ]