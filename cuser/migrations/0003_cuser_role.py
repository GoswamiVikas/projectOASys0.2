# Generated by Django 2.1.3 on 2018-11-16 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuser', '0002_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuser',
            name='role',
            field=models.CharField(choices=[('Student', 'Student'), ('Instructor', 'Instructor')], default='Student', max_length=7),
        ),
    ]
