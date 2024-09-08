# Generated by Django 5.0.7 on 2024-09-01 21:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adm', '0009_funcionarios_usuario_alter_funcionarios_nome'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionarios',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unidades', to='Adm.unidades'),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='usuario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='funcionario', to=settings.AUTH_USER_MODEL),
        ),
    ]
