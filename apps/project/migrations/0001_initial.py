# Generated by Django 2.0.6 on 2018-06-21 17:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IT_Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=30, null=True)),
                ('project_description', models.CharField(blank=True, max_length=10000, null=True)),
                ('project_price', models.IntegerField(blank=True, null=True)),
                ('project_start_date_time', models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 21, 17, 33, 11, 660207), null=True)),
                ('project_end_date_time', models.DateTimeField(blank=True, default=None, null=True)),
                ('project_total_working_hr', models.IntegerField(blank=True, null=True)),
                ('project_total_time_taken', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'ACTIVE'), ('inactive', 'INACTIVE'), ('completed', 'completed'), ('cancelled', 'cancelled')], default='active', max_length=30)),
                ('client_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.CLIENT')),
            ],
        ),
    ]
