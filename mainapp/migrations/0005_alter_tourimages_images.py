# Generated by Django 4.1.7 on 2023-04-02 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_remove_tour_images_tourimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourimages',
            name='images',
            field=models.FileField(null=True, upload_to='images'),
        ),
    ]