# Generated by Django 4.2.1 on 2023-12-15 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0012_alter_event_agent_alter_event_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventForAgents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'успех'), (2, 'осечка'), (3, 'раскрытие'), (4, 'смерть агента')], default=1)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='agents.agent')),
                ('target', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='agents.agent')),
            ],
        ),
        migrations.CreateModel(
            name='EventForClients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'успех'), (2, 'осечка'), (3, 'раскрытие'), (4, 'смерть агента')], default=1)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='agents.agent')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='agents.client')),
            ],
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
