from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet, UserViewSet, RoleViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('register', RegisterViewSet, basename='register')
router.register('users', UserViewSet, basename='users')
router.register('roles', RoleViewSet, basename='roles')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
