# Generated by Django 5.0.7 on 2024-09-24 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Controle', '0020_atrasos'),
    ]

    operations = [
        migrations.AddField(
            model_name='atrasos',
            name='atraso',
            field=models.IntegerField(null=True),
        ),
    ]
