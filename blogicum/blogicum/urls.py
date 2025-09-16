"""Головные маршруты проекта.

Подключает приложения `pages`, `users`, `blog`, а также Django auth.
"""

from typing import List

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import URLPattern, include, path

handler403 = 'pages.views.permission_denied'
handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'

urlpatterns: List[URLPattern] = [
    path('pages/', include('pages.urls', namespace='pages')),
    path('', include('users.urls', namespace='users')),
    path('', include('blog.urls', namespace='blog')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    try:
        import debug_toolbar  # noqa: F401
    except Exception:
        debug_toolbar = None  # type: ignore
    else:
        urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
