# Generated by Django 2.1 on 2020-09-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200904_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics'),
        ),
    ]
