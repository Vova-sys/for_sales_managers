# Generated by Django 3.0.9 on 2020-08-05 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='FUCK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('COOL', models.CharField(max_length=30, verbose_name='Наименование')),
            ],
        ),
        migrations.DeleteModel(
            name='GOODS',
        ),
    ]
