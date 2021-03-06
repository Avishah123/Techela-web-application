# Generated by Django 3.1.7 on 2021-04-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_amongus_registration_callofduty_registration_clash_registration_csgo_registration_treasurehunt_regis'),
    ]

    operations = [
        migrations.CreateModel(
            name='bolly_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('mobile_number', models.CharField(max_length=254)),
                ('branch', models.CharField(max_length=254)),
                ('email', models.CharField(max_length=254)),
                ('college_name', models.CharField(max_length=254)),
                ('dicord_id', models.CharField(max_length=254)),
                ('student_id', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='chess_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('mobile_number', models.CharField(max_length=254)),
                ('branch', models.CharField(max_length=254)),
                ('email', models.CharField(max_length=254)),
                ('college_name', models.CharField(max_length=254)),
                ('dicord_id', models.CharField(max_length=254)),
                ('student_id', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='meme_registration',
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
            name='openmic_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('mobile_number', models.CharField(max_length=254)),
                ('branch', models.CharField(max_length=254)),
                ('email', models.CharField(max_length=254)),
                ('college_name', models.CharField(max_length=254)),
                ('dicord_id', models.CharField(max_length=254)),
                ('student_id', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='scrib_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('mobile_number', models.CharField(max_length=254)),
                ('branch', models.CharField(max_length=254)),
                ('email', models.CharField(max_length=254)),
                ('college_name', models.CharField(max_length=254)),
                ('dicord_id', models.CharField(max_length=254)),
                ('student_id', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
