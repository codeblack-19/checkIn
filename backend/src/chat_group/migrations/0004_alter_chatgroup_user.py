# Generated by Django 4.1.1 on 2022-09-19 22:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat_group', '0003_alter_chatgroup_group_desc_alter_chatgroup_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroup',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
