# Generated by Django 4.0.3 on 2022-03-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_alter_news_urltoimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='urlToImage',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]