# Generated by Django 2.2.4 on 2019-08-03 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter tag title', max_length=100, unique=True, verbose_name='Titre')),
                ('description', models.TextField(help_text='Enter tag description', max_length=255, verbose_name='Description')),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
