# Generated by Django 4.2.1 on 2023-12-06 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0003_alter_client_killed_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='killed_by',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='agents.agent'),
        ),
    ]
