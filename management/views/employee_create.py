import json

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from auth.models import UserCatalog
from management.mixins import ManagerRequiredMixin
from management.models.jobs import EmployeeCatalog


class EmployeeCreateView(ManagerRequiredMixin):

    def get(self, request):
        return render(request, 'management/addEmployee.html')

    def post(self, request):
        json_data = json.loads(request.body)
        username = json_data['username']
        password = json_data['password']
        name = json_data['name']
        unit = json_data['unit']
        user = UserCatalog.get_instance().create(username, password, name)
        EmployeeCatalog.get_instance().create(user, unit)
        return HttpResponseRedirect('/')
