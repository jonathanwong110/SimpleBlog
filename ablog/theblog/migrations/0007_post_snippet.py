# Generated by Django 4.2 on 2023-05-10 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("theblog", "0006_alter_post_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="snippet",
            field=models.CharField(
                default="Click Link Above to Read Blog Post", max_length=255
            ),
        ),
    ]