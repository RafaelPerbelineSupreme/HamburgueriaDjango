# Generated by Django 2.2.6 on 2019-10-11 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tipoFuncionario',
            fields=[
                ('idTipoFuncionario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(default='texto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'tipoFuncionario',
                'verbose_name_plural': 'tiposFuncionarios',
                'ordering': ['nome'],
            },
        ),
    ]
