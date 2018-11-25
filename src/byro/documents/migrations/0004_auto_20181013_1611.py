# Generated by Django 2.1.1 on 2018-10-13 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20181009_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='direction',
            field=models.CharField(choices=[('incoming', 'incoming'), ('outgoing', 'outgoing'), ('other', 'other')], default='outgoing', max_length=8),
        ),
    ]