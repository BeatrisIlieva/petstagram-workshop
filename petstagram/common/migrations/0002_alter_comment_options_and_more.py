# Generated by Django 5.2 on 2025-04-18 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('photos', '0002_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_time_of_publication']},
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['date_time_of_publication'], name='common_comm_date_ti_d3f02d_idx'),
        ),
    ]
