# Generated by Django 2.1.5 on 2020-12-06 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='code',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
