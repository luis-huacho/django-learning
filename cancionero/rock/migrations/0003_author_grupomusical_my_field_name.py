# Generated by Django 5.0.6 on 2024-06-10 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rock', '0002_alter_grupomusical_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
            ],
        ),
        migrations.AddField(
            model_name='grupomusical',
            name='my_field_name',
            field=models.CharField(blank=True, help_text='Enter field documentation', max_length=20),
        ),
    ]
