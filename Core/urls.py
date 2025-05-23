
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('products.urls')),
    path('api/', include('orders.urls')),

        # JWT token authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),      # Giriş yapar
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),     # Token yenile
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
