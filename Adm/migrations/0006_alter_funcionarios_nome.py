# Generated by Django 5.0.7 on 2024-08-20 23:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adm', '0005_unidades_latitude_unidades_longitude'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionarios',
            name='nome',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nome', to=settings.AUTH_USER_MODEL),
        ),
    ]
