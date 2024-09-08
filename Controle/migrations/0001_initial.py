# Generated by Django 5.0.7 on 2024-08-07 01:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Adm', '0004_alter_funcionarios_unidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faltas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('falta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faltas', to='Adm.funcionarios')),
            ],
        ),
    ]
