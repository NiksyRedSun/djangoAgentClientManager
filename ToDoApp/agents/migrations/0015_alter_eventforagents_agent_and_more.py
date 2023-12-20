# Generated by Django 4.2.1 on 2023-12-20 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0014_alter_eventforclients_agent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventforagents',
            name='agent',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='agents.agent'),
        ),
        migrations.AlterField(
            model_name='eventforagents',
            name='target',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='agents.agent'),
        ),
        migrations.AlterField(
            model_name='eventforclients',
            name='agent',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='agents.agent'),
        ),
        migrations.AlterField(
            model_name='eventforclients',
            name='client',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='agents.client'),
        ),
    ]