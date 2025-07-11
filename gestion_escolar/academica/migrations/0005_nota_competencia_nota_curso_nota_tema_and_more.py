# Generated by Django 5.2.3 on 2025-06-29 23:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0004_alter_nota_nota'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota',
            name='competencia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academica.competencia'),
        ),
        migrations.AddField(
            model_name='nota',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academica.curso'),
        ),
        migrations.AddField(
            model_name='nota',
            name='tema',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academica.tema'),
        ),
        migrations.AlterField(
            model_name='nota',
            name='nota',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
