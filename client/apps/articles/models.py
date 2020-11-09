from django.db import models
from .choices import *



class ClientErip(models.Model):
    region = models.CharField('Регион', max_length = 30, choices = REGION_CHOICE)
    date_add_card = models.DateTimeField('Дата заведения карточки')
    name = models.CharField('Наименование', max_length = 30)
    enter_point = models.CharField('Точка входа', max_length = 30)
    unp = models.CharField('УНП', max_length = 20)
    kind_of_activity = models.CharField('Вид деятельности', max_length = 30)
    leader = models.CharField('Руководитель (ЛПР)', max_length = 30)
    contact_face = models.CharField('Контактное лицо', max_length = 30)
    number = models.CharField('Телефон', max_length = 20, help_text = "Введите телефон в международном формате +375*********")
    email = models.CharField('E-mail', max_length = 20)
    site = models.CharField('Сайт', max_length = 30)
    service = models.CharField('Сервис', max_length = 30)
    type_of_appeal = models.CharField('Текущее мероприятие', max_length = 30)
    contact_event = models.CharField('Вид контакта', max_length = 200)
    event_date = models.DateTimeField('Дата контакта')
    result = models.CharField('Результат', max_length = 300)
    more_info = models.CharField('Примечание', max_length = 300)
    status = models.CharField('Статус', max_length =20, choices = STATUS_CHOICE)
    additional_information = models.CharField('Номер договора', max_length = 30)
    date_sending_application = models.DateTimeField('Дата договора')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиента'
        verbose_name_plural = 'Клиенты'

class Registration(models.Model):
    name_registration = models.CharField('Наименование', max_length = 30)
    aggregator = models.CharField('Агрегатор', max_length = 30)
    date_move_request = models.DateTimeField('Дата направления заявки')
    date_move_documentPU = models.DateTimeField('Дата направления документов ПУ')
    date_red_time = models.DateTimeField('Ожидание документов (контрольный срок)')

    def __str__(self):
        return self.name_registration

    class Meta:
        verbose_name = 'Оформление'
        verbose_name_plural = 'Оформления'

