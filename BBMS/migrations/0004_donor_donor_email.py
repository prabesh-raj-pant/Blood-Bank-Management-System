# Generated by Django 5.0.1 on 2024-01-24 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBMS', '0003_donor_user_bloodbank_receipent'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='Donor_Email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
