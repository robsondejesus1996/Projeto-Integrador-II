# Generated by Django 3.0.4 on 2020-03-30 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0005_auto_20200324_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('cover', models.ImageField(upload_to='images/')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacao.Funcionario')),
            ],
        ),
    ]
