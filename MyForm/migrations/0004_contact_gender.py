# Generated by Django 3.0.1 on 2020-05-30 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyForm', '0003_auto_20200530_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female')], default=0),
            preserve_default=False,
        ),
    ]
