# Generated by Django 2.0.3 on 2018-03-11 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='First book from saga'),
            preserve_default=False,
        ),
    ]
