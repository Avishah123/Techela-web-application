# Generated by Django 3.1.7 on 2021-04-04 15:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_bolly_registration_chess_registration_meme_registration_openmic_registration_scrib_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='chess_registration',
            name='chess_id',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meme_registration',
            name='meme_upload',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
