# Generated by Django 4.1.2 on 2023-03-31 02:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("autho", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EncryptedMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("encrypted_text", models.TextField()),
                ("encrypted_message", models.BinaryField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tweet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("twitter_user_fullname", models.CharField(max_length=150)),
                ("username", models.CharField(max_length=255)),
                ("link", models.CharField(max_length=255)),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("twitter_userid", models.CharField(default="", max_length=100)),
                ("key", models.TextField(null=True)),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="BypassDM_V1.encryptedmessage",
                    ),
                ),
                (
                    "twitter_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="autho.twitteruser",
                    ),
                ),
            ],
        ),
    ]
