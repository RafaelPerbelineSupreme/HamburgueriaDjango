# Generated by Django 2.2.6 on 2019-10-24 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pais', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('idEstado', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(default='texto')),
                ('uf', models.CharField(max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('estadoPais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pais.Pais')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'ordering': ['nome'],
            },
        ),
    ]
