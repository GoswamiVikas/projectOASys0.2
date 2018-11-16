# Generated by Django 2.1.3 on 2018-11-16 00:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20181112_0430'),
        ('students', '0005_auto_20181113_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_datetime', models.DateTimeField()),
                ('asmt_solution_file', models.FileField(upload_to='asmt_submission/')),
            ],
        ),
        migrations.RenameField(
            model_name='assignment',
            old_name='due_date',
            new_name='due_datetime',
        ),
        migrations.AddField(
            model_name='assignment',
            name='asmt_file',
            field=models.FileField(default=django.utils.timezone.now, upload_to='asmt/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='asmt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Assignment'),
        ),
        migrations.AddField(
            model_name='submission',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.StudentProfile'),
        ),
        migrations.AddField(
            model_name='mark',
            name='asmt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Assignment'),
        ),
        migrations.AddField(
            model_name='mark',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.StudentProfile'),
        ),
    ]