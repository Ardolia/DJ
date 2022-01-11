from django.urls import path

from bboard.views import index, by_rubric
from .views import BbCteateView

urlpatterns = [
    path('add/', BbCteateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),

]