# Generated by Django 4.0.5 on 2022-07-06 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_rename_email_booking_email_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='message',
            field=models.TextField(max_length=500, null=True),
        ),
    ]