# Generated by Django 4.1.7 on 2023-04-02 11:15

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='doc_content',
            field=wagtail.fields.RichTextField(blank=True, null=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='subtitle',
            field=models.CharField(blank=True, help_text='Введите подстроку', max_length=100, null=True, verbose_name='Подстрока'),
        ),
    ]
