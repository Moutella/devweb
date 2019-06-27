# Generated by Django 2.2.1 on 2019-06-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=200)),
                ('nascimento', models.DateField(null=True)),
                ('cpf', models.CharField(max_length=11)),
                ('slug', models.SlugField(max_length=200)),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
    ]
