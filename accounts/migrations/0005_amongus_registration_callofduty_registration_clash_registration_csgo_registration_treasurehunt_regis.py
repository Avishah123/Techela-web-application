# Generated by Django 3.1.7 on 2021-03-30 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='amongus_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('mobile_number', models.CharField(max_length=254)),
                ('branch', models.CharField(max_length=254)),
                ('email', models.CharField(max_length=254)),
                ('college_name', models.CharField(max_length=254)),
                ('dicord_id', models.CharField(max_length=254)),
                ('player_id', models.CharField(max_length=254)),
                ('student_id', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='callofduty_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('mobile_number', models.CharField(max_length=254)),
                ('branch', models.CharField(max_length=254)),
                ('email', models.CharField(max_length=254)),
                ('college_name', models.CharField(max_length=254)),
                ('dicord_id', models.CharField(max_length=254)),
                ('player_id', models.CharField(max_length=254)),
                ('student_id', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='clash_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('mobile_number', models.CharField(max_length=254)),
                ('branch', models.CharField(max_length=254)),
                ('email', models.CharField(max_length=254)),
                ('college_name', models.CharField(max_length=254)),
                ('dicord_id', models.CharField(max_length=254)),
                ('player_id', models.CharField(max_length=254)),
                ('student_id', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='csgo_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('mobile_number', models.CharField(max_length=254)),
                ('branch', models.CharField(max_length=254)),
                ('email', models.CharField(max_length=254)),
                ('college_name', models.CharField(max_length=254)),
                ('dicord_id', models.CharField(max_length=254)),
                ('csgo_id', models.CharField(max_length=254)),
                ('student_id', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='treasurehunt_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('mobile_number', models.CharField(max_length=254)),
                ('branch', models.CharField(max_length=254)),
                ('email', models.CharField(max_length=254)),
                ('college_name', models.CharField(max_length=254)),
                ('dicord_id', models.CharField(max_length=254)),
                ('insta_id', models.CharField(max_length=254)),
                ('student_id', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='valorant_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('mobile_number', models.CharField(max_length=254)),
                ('branch', models.CharField(max_length=254)),
                ('email', models.CharField(max_length=254)),
                ('college_name', models.CharField(max_length=254)),
                ('dicord_id', models.CharField(max_length=254)),
                ('valorant_id', models.CharField(max_length=254)),
                ('student_id', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
