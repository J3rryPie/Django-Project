# Generated by Django 2.1.5 on 2020-12-06 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20201207_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='code',
            field=models.TextField(blank=True, null=True),
        ),
    ]
