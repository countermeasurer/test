from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Robot

class RobotView(View):
    def get(self, request):
        serial = request.GET.get('serial')
        model = request.GET.get('model')
        version = request.GET.get('version')

        robots = Robot.objects.filter(
            serial=serial,
            model=model,
            version=version
        )

        response = []

        for robot in robots:
            response.append(({
                'id': robot.id,
                'serial': robot.serial,
                'model': robot.model,
                'version': robot.version,
                'created': robot.created.strftime('%Y-%m-%d %H:%M:%S')
            }))

        return JsonResponse(response, safe=False)

    def post(self, request):

        robot = Robot(
            serial=request.POST.get('serial'),
            model=request.POST.get('model'),
            version=request.POST.get('version'),
        )

        robot.save()


        response = {
            'id': robot.id,
            'serial': robot.serial,
            'model': robot.model,
            'version': robot.version,
            'created': robot.created.strftime('%Y-%m-%d %H:%M:%S')
        }

        return JsonResponse(response)

    def put(self, request):
        serial = request.PUT.get('serial'),
        model = request.PUT.get('model'),
        version = request.PUT.get('version'),

        robot = Robot.objects.get(
            serial=serial,
            model=model,
            version=version
        )

        robot.serial = request.PUT.get('new_serial'),
        robot.model = request.PUT.get('new_model'),
        robot.version = request.PUT.get('new_version')

        robot.save()

        response = {
            'id': robot.id,
            'serial': robot.serial,
            'model': robot.model,
            'version': robot.version,
            'created': robot.created.strftime('%Y-%m-%d %H:%M:%S')
        }

        return JsonResponse(response)

    def delete(self, request):
        serial = request.DELETE.get('serial'),
        model = request.DELETE.get('model'),
        version = request.DELETE.get('version')

        robot = Robot.objects.get(
            serial=serial,
            model=model,
            version=version
        )

        robot.delete()

        response = {
            'message': 'Robot deleted successfully.'
        }

        return JsonResponse(response)
