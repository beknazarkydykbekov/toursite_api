# Generated by Django 4.1.7 on 2023-04-02 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Бронь', 'verbose_name_plural': 'Брони'},
        ),
        migrations.AddField(
            model_name='order',
            name='tour',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.tour', verbose_name='тур'),
            preserve_default=False,
        ),
    ]