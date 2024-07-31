# Generated by Django 5.0.7 on 2024-07-31 01:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adm', '0003_alter_funcionarios_unidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionarios',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Unidades', to='Adm.unidades'),
        ),
    ]
