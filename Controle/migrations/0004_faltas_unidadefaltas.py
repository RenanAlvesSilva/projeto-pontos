# Generated by Django 5.0.7 on 2024-08-08 01:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adm', '0004_alter_funcionarios_unidade'),
        ('Controle', '0003_alter_faltas_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='faltas',
            name='UnidadeFaltas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UnidadeFaltas', to='Adm.unidades'),
        ),
    ]
