# Generated by Django 2.2.2 on 2019-06-05 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0010_copy_data_to_response_status_int'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificatieresponse',
            name='response_status',
        ),
    ]