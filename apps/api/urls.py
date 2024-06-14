from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


docs = [
    path('', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(), name='swagger'),
    path('redoc/', SpectacularRedocView.as_view(), name='redoc'),
]

v1 = [
]

urlpatterns = [
    path("schema/", include(docs)),
    path("v1/", include(v1))
]
