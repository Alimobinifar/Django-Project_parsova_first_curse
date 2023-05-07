# Generated by Django 3.2.18 on 2023-05-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Author',
        ),
        migrations.AddField(
            model_name='book',
            name='Author',
            field=models.ManyToManyField(to='books.Author'),
        ),
    ]
