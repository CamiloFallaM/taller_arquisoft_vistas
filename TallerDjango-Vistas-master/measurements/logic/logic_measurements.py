from .. models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement_db(n):
    measurement = Measurement.objects.get(pk=n)
    return measurement

def delete_measurement_db(n):
    info = Measurement.objects.filter(pk=n).delete()
        
    if info[0] > 0:
        message = "Measurement con el id " + str(n) + " fue borrado exitosamente!"
    else:
        message = "Measurement con el id " + str(n) + " no se ha podido borrar porque no existe."
        
    return message

def update_measurement_db(n, new_value):
    measurement = Measurement.objects.get(pk=n)
    measurement.value = new_value
    measurement.save()
    return measurement
