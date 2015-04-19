import json
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from models import Measurements, VesnaReading
from login.models import ApiAuth

@login_required
def index(request):
    measurements = request.user.measurements_set.all().order_by('-name')
    last_update = {m: m.vesnareading_set.all().order_by('-time')[0].time.strftime('%d-%m-%Y %H:%m') for m in measurements}
    context = {'measurementss': measurements,
               'last_update': last_update}
    print measurements, last_update
    return render(request, 'measurements.html', context)

@login_required
def measurements(request, name):
    readings = request.user.measurements_set.get(name=name).vesnareading_set.all()
    for reading in readings:
        try:
            reading.time = timezone.localtime(reading.time).strftime('%d/%m/%Y %H:%M')
        except:
            reading.delete()
            print 'deleting false reading'
    context = {'readings': readings}
    return render(request, 'readings.html', context)

def put_value(request, token, measurements, reading):
    reading = json.loads(reading)
    try:
        user = ApiAuth.objects.get(token=token).user
    except:
        return HttpResponse(json.dumps(False))
    try:
        collection = user.measurements_set.get(name=measurements)
    except:
        print 'made new collection'
        collection = Measurements()
        collection.name = measurements
        collection.owner = user
        collection.save()
    vesna_reading = VesnaReading()
    vesna_reading.measurements = collection
    vesna_reading.CO = reading['CO']
    vesna_reading.NO2 = reading['NO2']
    vesna_reading.O3 = reading['O3']
    vesna_reading.temp = reading['temp']
    vesna_reading.humidity = reading['humidity']
    vesna_reading.movement = reading['movement']
    vesna_reading.time = timezone.localtime(timezone.now())
    vesna_reading.save()
    return HttpResponse(json.dumps(True))