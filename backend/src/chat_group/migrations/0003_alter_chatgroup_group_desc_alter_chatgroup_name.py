# Generated by Django 4.1.1 on 2022-09-19 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_group', '0002_rename_desciption_chatgroup_group_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroup',
            name='group_desc',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='chatgroup',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
