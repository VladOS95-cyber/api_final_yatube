# Generated by Django 3.1.7 on 2021-03-09 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_group_description'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set(),
        ),
    ]
