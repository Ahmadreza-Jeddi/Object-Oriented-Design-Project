from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from django.views.generic import ListView

from management.models import Employee
from management.mixins import ManagerRequiredMixin


class EmployeeListView(ManagerRequiredMixin, View):

    def get(self, request):
        employees = Employee.dump_all()
        t = get_template('management/viewEmployees.html')
        # print(em)
        html = t.render({'employees': employees}, request)
        return HttpResponse(html)
