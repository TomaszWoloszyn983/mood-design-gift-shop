# Generated by Django 3.2 on 2023-02-27 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_post_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.ManyToManyField(blank=True, to='home.NewsletterUser'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(max_length=150),
        ),
    ]