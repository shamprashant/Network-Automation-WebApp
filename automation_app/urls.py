from django.conf.urls import url
from automation_app import views

app_name = 'automation_app'
urlpatterns = [
    url(r'^$',views.running_config, name = "running_config"),
    url(r'index/',views.index, name = "index"),
    url(r'^get_result/',views.get_result, name = "get_result"),
]
