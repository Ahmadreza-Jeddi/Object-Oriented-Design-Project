import json

from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View

from auth.mixins import UserPassesTestMixin
from auth.models import UserCatalog
from management.models.jobs import EmployeeCatalog
from management.status import ManagerRequired


class EmployeeCreateView(UserPassesTestMixin):

    def __init__(self, *args, **kwargs):
        test_object = ManagerRequired()
        super().__init__(test_object, *args, **kwargs)

    def get(self, request):
        return render(request, 'management/addEmployee.html')

    def post(self, request):
        json_data = json.loads(request.body)
        username = json_data['username']
        password = json_data['password']
        name = json_data['name']
        unit = json_data['unit']
        user = UserCatalog.get_instance().create(username, password, name)
        if user == 'unique':
            return HttpResponse(status=455)
        elif user == 'invalid':
            return HttpResponse(status=456)
        EmployeeCatalog.get_instance().create(user, unit)
        return HttpResponseRedirect('/management/listEmployees/')
