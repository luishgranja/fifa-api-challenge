from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from apps.players import urls as players_urls
from apps.teams import urls as teams_urls

urlpatterns = [
    path('api/players/', include(players_urls)),
    path('api/teams/', include(teams_urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
