# Generated by Django 3.2 on 2023-04-05 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('web_code', models.CharField(max_length=128)),
                ('country_code', models.CharField(blank=True, max_length=128, null=True)),
                ('flag', models.ImageField(blank=True, null=True, upload_to='countries/flags/')),
                ('phone_code', models.CharField(blank=True, max_length=128, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('phone_number_length', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
                'db_table': 'main_country',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('readonly', models.BooleanField(default=False)),
                ('maintenance', models.BooleanField(default=False)),
                ('down', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'mode',
                'verbose_name_plural': 'mode',
                'db_table': 'mode',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.country')),
            ],
            options={
                'verbose_name': 'state',
                'verbose_name_plural': 'states',
                'db_table': 'main_state',
                'ordering': ('name',),
            },
        ),
    ]
