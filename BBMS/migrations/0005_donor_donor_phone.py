# Generated by Django 5.0.1 on 2024-01-24 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBMS', '0004_donor_donor_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='Donor_Phone',
            field=models.IntegerField(default=10),
        ),
    ]