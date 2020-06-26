# Generated by Django 3.0.4 on 2020-05-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makale', '0007_yorum'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='makale',
            options={'ordering': ['-Olusturma_Tarihi', 'Yazar']},
        ),
        migrations.AlterModelOptions(
            name='yorum',
            options={'ordering': ['-yorum_tarih', 'yorum_yapan']},
        ),
        migrations.AlterField(
            model_name='yorum',
            name='yorum_içerik',
            field=models.CharField(max_length=200, verbose_name='Yorum İçeriği'),
        ),
        migrations.AlterField(
            model_name='yorum',
            name='yorum_yapan',
            field=models.CharField(max_length=50, verbose_name='İsim'),
        ),
    ]
