# Generated by Django 2.2.6 on 2019-10-11 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adicional',
            fields=[
                ('idAdicional', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(default='texto')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=4)),
                ('quantidade', models.DecimalField(decimal_places=4, max_digits=4)),
                ('unidade', models.CharField(max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Adicional',
                'verbose_name_plural': 'Adicionais',
                'ordering': ['nome'],
            },
        ),
    ]
