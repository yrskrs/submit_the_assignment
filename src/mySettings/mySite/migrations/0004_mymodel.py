# Generated by Django 5.1 on 2024-08-23 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0003_delete_folderconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
    ]
