from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from .views import SubjectViewSet, UserViewSet

router = DefaultRouter()
router.register(prefix='subjects', viewset=SubjectViewSet, basename='subjects')
router.register(prefix='users', viewset=UserViewSet, basename='users')

urlpatterns = router.urls

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
