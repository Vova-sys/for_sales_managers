# Generated by Django 3.0.9 on 2020-08-05 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20200805_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('COOL', models.CharField(max_length=30, verbose_name='Наименование')),
                ('kind_of_activity', models.CharField(max_length=30, verbose_name='Вид деятельности')),
            ],
            options={
                'verbose_name': 'Оформление',
                'verbose_name_plural': 'Оформления',
            },
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Мероприятие', 'verbose_name_plural': 'Мероприятия'},
        ),
        migrations.AlterField(
            model_name='clienterip',
            name='status',
            field=models.CharField(choices=[('Интерес', 'Интерес'), ('Намерение', 'Намерение'), ('Предпочтение', 'Предпочтение'), ('Отказ', 'Отказ'), ('Покупка', 'Покупка'), ('Нет контакта', 'Нет контакта'), ('СЗ', 'СЗ')], max_length=20, verbose_name='Статус'),
        ),
    ]