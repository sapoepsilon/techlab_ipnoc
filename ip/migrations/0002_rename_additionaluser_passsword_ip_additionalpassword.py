# Generated by Django 3.2.8 on 2021-10-26 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ip',
            old_name='additionalUser_passsword',
            new_name='additionalPassword',
        ),
    ]
