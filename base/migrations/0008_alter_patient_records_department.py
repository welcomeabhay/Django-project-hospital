# Generated by Django 4.2.7 on 2023-11-04 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_patient_records_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_records',
            name='department',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='base.department'),
        ),
    ]
