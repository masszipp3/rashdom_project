# Generated by Django 4.1.4 on 2023-01-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmeuser', '0003_alter_projectdetails_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Msgs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Email', models.CharField(max_length=1000)),
                ('Phone', models.BigIntegerField()),
                ('Message', models.CharField(max_length=5000)),
            ],
        ),
    ]
