# Generated by Django 5.0.7 on 2024-07-22 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('published_date', models.DateField()),
                ('isbn', models.CharField(max_length=13)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='covers/')),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
