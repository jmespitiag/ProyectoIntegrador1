# Generated by Django 4.2.4 on 2023-09-13 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PruebaVocacional', '0005_remove_test_respuesta_test_respuesta1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='test',
            name='id_estudiante',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='PruebaVocacional.student', verbose_name='ID de estudiante'),
        ),
    ]
