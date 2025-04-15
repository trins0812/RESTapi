from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
from rest_framework.authtoken.views import ObtainAuthToken
from .views import SecureHelloView

urlpatterns = [
    path("", include(router.urls)),
    path('api-token-auth/', ObtainAuthToken.as_view()),
    path('secure-hello/', SecureHelloView.as_view()),
]