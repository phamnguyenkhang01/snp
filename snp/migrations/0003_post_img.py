# Generated by Django 5.1.4 on 2025-02-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snp', '0002_post_author_post_date_time_alter_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
