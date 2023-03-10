# Generated by Django 4.1.5 on 2023-01-09 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name_plural': 'Habilidades',
                'ordering': ['habilidad'],
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['first_name'], 'verbose_name_plural': 'Departamentos'},
        ),
    ]
