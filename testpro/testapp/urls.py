from django.conf.urls import url,include
from.views import testAPIView,viewsetCRUD
from rest_framework import routers
rauting=routers.DefaultRouter()
rauting.register("testviewset",viewsetCRUD)
urlpatterns=[
    url(r"^testAPIView/$",testAPIView.as_view()),
    #url(r"^for retrive/(?p<pk>\d+)/$",retrive.as_view())
    url(r'',include(rauting.urls))
]