import json
# import class we're going to extend
from django.views.generic import View
# import our jsonresponse object
from django.http.response import JsonResponse

from .models import PlantStatus
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class History(View):
    # to add a historical element to db
    def post(self, request):
        received_json = json.loads(request.body.decode('utf-8'))

        # create platstatus object by parsing json
        plant_status = PlantStatus.objects.create()

        if 'humidity' in received_json:
            plant_status.humidity = received_json['humidity']
        if 'temperature' in received_json:
            plant_status.temperature = received_json['temperature']
        if 'light_exposure' in received_json:
            plant_status.light_exposure = received_json['light_exposure']
        if 'uv_level' in received_json:
            plant_status.uv_level = received_json['uv_level']
        if 'soil_moisture' in received_json:
            plant_status.soil_moisture = received_json['soil_moisture']

        plant_status.save()
        return JsonResponse({"response": plant_status.status_time})

    def get(self, request):

        stati = PlantStatus.objects.all()
        current_index = len(stati)

        response = {'count': len(stati), 'stati': []}

        for k in stati:
            # ps = PlantStatus.objects.get(pk=current_index - k)
            status_dictionary = {'time': k.status_time,
                                 'humidity': k.humidity,
                                 'temperature': k.temperature,
                                 'light_exposure': k.light_exposure,
                                 'uv_level': k.uv_level,
                                 'soil_moisture': k.soil_moisture}
            response['stati'].append(status_dictionary)

        return JsonResponse(response, status=200)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(History, self).dispatch(request, *args, **kwargs)


class LatestStatus(View):
    def get(self, request):
        current_index = len(PlantStatus.objects.all())
        plant_status = PlantStatus.objects.get(pk=current_index)

        status_dictionary = {'time': plant_status.status_time,
                             'humidity': plant_status.humidity,
                             'temperature': plant_status.temperature,
                             'light_exposure': plant_status.light_exposure,
                             'uv_level': plant_status.uv_level,
                             'soil_moisture': plant_status.soil_moisture}

        return JsonResponse(status_dictionary, status=200)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LatestStatus, self).dispatch(request, *args, **kwargs)
