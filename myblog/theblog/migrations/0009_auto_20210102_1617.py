# Generated by Django 3.1.2 on 2021-01-02 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0008_auto_20210102_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link Above to Read Blog Post', max_length=255),
        ),
    ]
