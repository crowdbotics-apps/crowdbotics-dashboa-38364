# Generated by Django 2.2.28 on 2023-01-20 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_remove_subscription_application'),
        ('apps', '0003_auto_20230120_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='subscription',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='subscriptions.Subscription'),
        ),
    ]
