# Generated by Django 2.2.1 on 2019-06-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_id',
            field=models.IntegerField(default=123456789, verbose_name='GroupId'),
        ),
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]