# Generated by Django 5.0.7 on 2024-08-25 01:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adm', '0009_funcionarios_usuario_alter_funcionarios_nome'),
        ('Controle', '0010_alter_pontoentrada_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoentrada',
            name='unidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Adm.unidades'),
        ),
    ]
