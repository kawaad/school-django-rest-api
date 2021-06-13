# Generated by Django 3.2.3 on 2021-05-24 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_alter_curso_nivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('B', 'Básico'), ('I', 'Intermediário'), ('A', 'Avançado')], max_length=1),
        ),
    ]
