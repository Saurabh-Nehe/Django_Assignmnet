# Generated by Django 3.2.14 on 2022-07-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0007_rename_id_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
