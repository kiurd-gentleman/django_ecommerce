# Generated by Django 3.1.2 on 2022-03-24 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20220325_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='team/'),
        ),
    ]