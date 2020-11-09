# Generated by Django 3.0.9 on 2020-08-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('Минск', 'Минск'), ('Брест', 'Брест'), ('Витебск', 'Витебск'), ('Гомель', 'Гомель'), ('Гродно', 'Гродно'), ('Могилев', 'Могилев')], max_length=30, verbose_name='Регион')),
                ('date_add_card', models.DateTimeField(verbose_name='Дата заведения карточки')),
            ],
        ),
        migrations.AlterModelOptions(
            name='clienterip',
            options={'verbose_name': 'Клиента', 'verbose_name_plural': 'Клиенты'},
        ),
    ]