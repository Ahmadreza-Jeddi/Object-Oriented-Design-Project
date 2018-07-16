from django.shortcuts import render
from django.views.generic.base import View

from management.models.jobs import EmployeeCatalog
from management.mixins import ManagerRequiredMixin


class EmployeeListView(ManagerRequiredMixin, View):

    http_method_names = ('get',)
    
    def get(self, request):
        context = {
            'employees': EmployeeCatalog.get_instance().dump_all()
        }
        return render(request, 'management/viewEmployees.html', context)
