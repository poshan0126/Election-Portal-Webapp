# Generated by Django 2.0.7 on 2018-07-21 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.TextField(default='Write the executive summary ...'),
        ),
    ]
