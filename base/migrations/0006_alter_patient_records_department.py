# Generated by Django 4.2.7 on 2023-11-04 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_doctor_specialization_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_records',
            name='department',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.department'),
        ),
    ]
