
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Inclui as rotas do app core
]

# path("events/", include("events.urls", namespace="events")),
# path("donations/", include("donations.urls", namespace="donations")),
# path("core/", include("core.urls", namespace="core")),
# path("needs/", include("needs.urls", namespace="needs")),
# # Users app URLs - all auth and user management handled here
# path("users/", include("users.urls", namespace="users")),