from django.conf.urls import url,include
from.views import testAPIView,viewsetCRUD
from rest_framework import routers
from rest_framework.authtoken import views
rauting=routers.DefaultRouter()
rauting.register("testviewset",viewsetCRUD)
urlpatterns=[
    url(r"^testAPIView/$",testAPIView.as_view()),
    #url(r"^for retrive/(?p<pk>\d+)/$",retrive.as_view())
    url(r'',include(rauting.urls)),
    url(r"^obtain_token/",views.obtain_auth_token)
]