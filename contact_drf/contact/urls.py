from django.urls import path,include
from rest_framework.routers import DefaultRouter
from contact.views import *

router=DefaultRouter()
router.register(r'contacts',ContactViewSet,basename='contact')
urlpatterns=[
    path('',include(router.urls)),
]