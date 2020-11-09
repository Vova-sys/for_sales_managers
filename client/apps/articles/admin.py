from django.contrib import admin
from .models import ClientErip, Registration
import csv
from django.http import HttpResponse


class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_add_card','region','unp','contact_face','leader','number','email','type_of_appeal','contact_event','event_date','result','more_info','status','additional_information')
    search_fields = ['unp','name','additional_information']
    list_filter = ('date_add_card','event_date','date_sending_application','region','status')
    date_hierarchy = ('date_add_card')
    ordering = ('-date_add_card',)
    actions = ['make_on', 'make_off', 'make_not_on', 'export_as_csv']
    #list_editable = ('contact_face', 'number')
    save_as = True

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = "Экспорт в CSV (ОТЧЕТ)"

    def make_on(self, request, queryset):
        queryset.update(status='Интерес')
    make_on.short_description = "Перевод в статус Интерес"

    def make_off(self, request, queryset):
        queryset.update(status='Намерение')
    make_off.short_description = "Перевод в статус Намерение"

    def make_not_on(self, request, queryset):
        queryset.update(status='Предпочтение')
    make_not_on.short_description = "Перевод в статус Предпочтение"

    def make_not_on(self, request, queryset):
        queryset.update(status='Отказ')
    make_not_on.short_description = "Перевод в статус Отказ"

    def make_not_on(self, request, queryset):
        queryset.update(status='Покупка')
    make_not_on.short_description = "Перевод в статус Покупка"

    def make_not_on(self, request, queryset):
        queryset.update(status='Нет контакта')
    make_not_on.short_description = "Перевод в статус Нет контакта"

    def make_not_on(self, request, queryset):
        queryset.update(status='СЗ')
    make_not_on.short_description = "Перевод в статус СЗ"

class BlogAdmin2(admin.ModelAdmin):
    list_display = ('name_registration', 'aggregator','date_move_request','date_move_documentPU','date_red_time')
    search_fields = ['name_registration','aggregator','date_red_time']
    list_filter = ('name_registration', 'aggregator','date_move_request','date_move_documentPU','date_red_time')
    date_hierarchy = ('date_red_time')
    ordering = ('-name_registration',)
    actions = ['make_on', 'make_off', 'make_not_on', 'export_as_csv']
    #list_editable = ('aggregator', 'date_move_request')
    save_as = True

    def export_as_csv2(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv2.short_description = "Экспорт в CSV (ОТЧЕТ)"



admin.site.register(ClientErip, BlogAdmin)
admin.site.register(Registration, BlogAdmin2)