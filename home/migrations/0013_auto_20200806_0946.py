# Generated by Django 2.2.15 on 2020-08-06 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0012_auto_20200806_0942"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customtext",
            old_name="nameChanged",
            new_name="nameChangedAgain",
        ),
        migrations.RenameField(
            model_name="customtext", old_name="test444", new_name="test12",
        ),
        migrations.RenameField(
            model_name="customtext", old_name="test5", new_name="test54",
        ),
        migrations.RenameField(
            model_name="customtext", old_name="title1234ds", new_name="title",
        ),
    ]
