from django.shortcuts import render
from .logic.logic_measurements import get_all_measurements
from .logic.logic_measurements import get_measurement_db
from .logic.logic_measurements import delete_measurement_db
from .logic.logic_measurements import update_measurement_db
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def get_measurements(request):
    measurements = get_all_measurements()
    measurement_list = serializers.serialize('json', measurements)
    return HttpResponse(measurement_list, content_type='application/json')

def get_measurement(request, pk=1):
    measurement = get_measurement_db(pk)
    measurement_seria = serializers.serialize('json', [measurement])
    return HttpResponse(measurement_seria, content_type='application/json')

def delete_measurement(request, pk=1):
    message = delete_measurement_db(pk)
    return HttpResponse(message)

def update_measurement(request, pk=1, new_value=100):
    measurement = update_measurement_db(pk, new_value)
    measurement_seria = serializers.serialize('json', [measurement])
    return HttpResponse(measurement_seria, content_type='application/json')