# Generated by Django 4.2.3 on 2023-07-19 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sako', '0003_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='IMG_6149.jpeg', upload_to=''),
        ),
    ]
