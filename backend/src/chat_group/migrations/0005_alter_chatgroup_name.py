# Generated by Django 4.1.1 on 2022-09-19 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_group', '0004_alter_chatgroup_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroup',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
