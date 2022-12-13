# Generated by Django 4.1.3 on 2022-12-13 02:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Room",
        ),
        migrations.RemoveField(
            model_name="message",
            name="date",
        ),
        migrations.RemoveField(
            model_name="message",
            name="room",
        ),
        migrations.RemoveField(
            model_name="message",
            name="user",
        ),
        migrations.RemoveField(
            model_name="message",
            name="value",
        ),
        migrations.AddField(
            model_name="message",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="message",
            name="group",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="main_app.group",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="message",
            name="sender",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="message",
            name="text",
            field=models.CharField(default="enter message", max_length=300),
            preserve_default=False,
        ),
    ]
