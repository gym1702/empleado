# Generated by Django 4.1.5 on 2023-01-09 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['name'], 'verbose_name_plural': 'Departamentos'},
        ),
    ]
