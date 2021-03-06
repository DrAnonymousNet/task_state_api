# Generated by Django 4.0.5 on 2022-06-08 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('draft', 'draft'), ('active', 'active'), ('done', 'done'), ('achieved', 'achieved')], default='draft', max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
