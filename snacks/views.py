# instructor wants to use template view instead of default import
from django.views.generic import TemplateView

# in order to use TemplateView, need to add a sub-class and extend TemplateView
# for a given templete, this view will be responsible for making the markup available so that it can be rendered in teh browser
class HomePageView(TemplateView):
    # TemplateView needs one thing from the sub-class
    template_name = "home.html"
