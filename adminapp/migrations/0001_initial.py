# Generated by Django 4.1.4 on 2023-01-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(default='', upload_to='adminapp/')),
                ('image_2', models.ImageField(default='', upload_to='adminapp/')),
                ('image_3', models.ImageField(default='', upload_to='adminapp/')),
            ],
        ),
    ]
