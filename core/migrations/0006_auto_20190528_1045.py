# Generated by Django 2.2 on 2019-05-28 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190528_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juridico',
            name='enviar_arquivo',
        ),
        migrations.RemoveField(
            model_name='juridico',
            name='forum',
        ),
    ]
