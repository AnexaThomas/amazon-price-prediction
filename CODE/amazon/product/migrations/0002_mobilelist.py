# Generated by Django 3.2.13 on 2022-08-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mobilelist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobimg', models.ImageField(upload_to='mobiles')),
                ('mobname', models.CharField(max_length=255)),
                ('mobprice', models.CharField(max_length=50)),
            ],
        ),
    ]
