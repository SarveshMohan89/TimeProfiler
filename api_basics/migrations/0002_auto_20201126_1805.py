# Generated by Django 3.1.3 on 2020-11-26 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
