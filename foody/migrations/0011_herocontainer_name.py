# Generated by Django 3.2.18 on 2023-04-22 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foody', '0010_alter_herocontainer_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='herocontainer',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]