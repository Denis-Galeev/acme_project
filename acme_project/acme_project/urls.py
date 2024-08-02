# Импортируем настройки проекта.
from django.conf import settings  # type: ignore
# Импортируем функцию, позволяющую серверу разработки отдавать файлы.
from django.conf.urls.static import static  # type: ignore
from django.contrib import admin  # type: ignore
from django.urls import include, path  # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
    path('', include('pages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
