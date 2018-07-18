from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View

from auth.mixins import LoginRequiredMixin
from management.models.criterion import CriterionCatalog


class ViewCriterionDetailedView(LoginRequiredMixin):
    def get(self, request):
        criteria = CriterionCatalog.get_instance().dump_all()
        print('###########', criteria)
        t = get_template('management/viewCriteriaDetailed.html')
        html = t.render({'criteria': criteria}, request)
        return HttpResponse(html)
