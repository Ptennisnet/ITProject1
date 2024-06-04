# Generated by Django 5.0.3 on 2024-06-04 03:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_medicalrecord_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalrecord',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]