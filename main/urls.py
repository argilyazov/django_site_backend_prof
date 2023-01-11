from django.urls import path
from . import views
urlpatterns = [

    path('',views.index ),
    path('demand',views.demand ),
    path('geography',views.geography ),
    path('skills',views.skills ),
    path('last_vac',views.last_vac )
]