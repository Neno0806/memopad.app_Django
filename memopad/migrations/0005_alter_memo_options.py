# Generated by Django 4.1.3 on 2023-03-15 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memopad', '0004_alter_memo_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memo',
            options={'verbose_name': 'メモのデータ'},
        ),
    ]