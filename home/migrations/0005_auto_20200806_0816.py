# Generated by Django 2.2.15 on 2020-08-06 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200806_0814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customtext',
            old_name='test55',
            new_name='test5',
        ),
        migrations.AddField(
            model_name='customtext',
            name='title22',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
