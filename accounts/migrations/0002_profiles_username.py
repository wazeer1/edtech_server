# Generated by Django 3.2 on 2023-04-07 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
