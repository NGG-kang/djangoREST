# Generated by Django 3.1.6 on 2021-02-17 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_post_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ip',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
