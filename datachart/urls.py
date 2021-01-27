from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^result$', views.result, name='result'),
    url(r'^live_data$', views.live_data, name='live_data'),
    url(r'^get_live_data$', views.get_live_data, name='get_live_data'),
    url(r'^get_live_line_chart$', views.get_live_line_chart, name='get_live_line_chart'),
    url(r'^show_data$', views.show_data, name='show_data'),

    
]
