# Generated by Django 5.1 on 2024-09-04 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='update_add',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
