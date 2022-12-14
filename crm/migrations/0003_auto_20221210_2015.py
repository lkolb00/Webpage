# Generated by Django 3.2.3 on 2022-12-11 02:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20221210_2006'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EventCreateDate',
        ),
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
