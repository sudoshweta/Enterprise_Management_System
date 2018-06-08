# Generated by Django 2.0.6 on 2018-06-08 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IT_Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30)),
                ('project_description', models.CharField(max_length=30)),
                ('project_manager_id', models.IntegerField()),
                ('project_price', models.IntegerField()),
                ('project_start_date_time', models.DateTimeField()),
                ('project_end_date_time', models.DateTimeField()),
                ('project_total_working_hr', models.IntegerField()),
                ('project_total_time_taken', models.IntegerField()),
            ],
        ),
    ]
