# Generated by Django 4.1.1 on 2022-10-05 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0008_remove_center_optionname'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='bonusesPercent',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='center',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='center',
            name='hideBuyBtn',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='center',
            name='optionName',
            field=models.CharField(blank=True, max_length=355, null=True),
        ),
        migrations.AddField(
            model_name='center',
            name='prepaymentPercent',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='center',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='center',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
