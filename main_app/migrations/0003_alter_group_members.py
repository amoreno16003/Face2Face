# Generated by Django 4.1.3 on 2022-12-13 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "main_app",
            "0002_delete_room_remove_message_date_remove_message_room_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="members",
            field=models.ManyToManyField(blank=True, to="main_app.participant"),
        ),
    ]
