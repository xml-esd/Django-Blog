# Generated by Django 3.0.4 on 2020-03-26 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makale', '0002_auto_20200322_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='makale',
            old_name='baslik',
            new_name='Başlık',
        ),
        migrations.RenameField(
            model_name='makale',
            old_name='olusturma_Tarihi',
            new_name='Olusturma_Tarihi',
        ),
        migrations.RenameField(
            model_name='makale',
            old_name='yazar',
            new_name='Yazar',
        ),
        migrations.RenameField(
            model_name='makale',
            old_name='icerik',
            new_name='İçerik',
        ),
    ]
