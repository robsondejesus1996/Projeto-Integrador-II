# Generated by Django 3.0.4 on 2020-03-30 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0006_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='funcionario',
        ),
    ]