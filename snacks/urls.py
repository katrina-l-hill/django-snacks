from django.urls import path

# go in the views.py file and import HomePageView
from .views import HomePageView

# associate some url with a view
# for a given url, who's the view that's responsible for doing the work
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
