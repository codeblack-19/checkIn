# Generated by Django 4.1.1 on 2022-09-20 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_group', '0006_chatgroup_createdat_chatgroup_updatedat'),
        ('chat_members', '0002_alter_chatgroupmembers_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroupmembers',
            name='group',
            field=models.ForeignKey(db_column='pk', default=1, on_delete=django.db.models.deletion.CASCADE, to='chat_group.chatgroup'),
        ),
    ]
