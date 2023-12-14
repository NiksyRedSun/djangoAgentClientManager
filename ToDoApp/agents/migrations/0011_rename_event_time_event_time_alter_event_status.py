# Generated by Django 4.2.1 on 2023-12-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0010_alter_event_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_time',
            new_name='time',
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.IntegerField(choices=[(1, 'успех'), (2, 'осечка'), (3, 'раскрытие'), (4, 'смерть агента')], default=1),
        ),
    ]
