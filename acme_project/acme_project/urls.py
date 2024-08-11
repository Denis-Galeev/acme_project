# Импортируем настройки проекта.
from django.conf import settings  # type: ignore
# Импортируем функцию, позволяющую серверу разработки отдавать файлы.
from django.conf.urls.static import static  # type: ignore
from django.contrib import admin  # type: ignore
# Добавьте новые строчки с импортами классов.
from users.forms import CustomUserCreationForm  # type: ignore
from django.views.generic.edit import CreateView  # type: ignore
from django.urls import include, path, reverse_lazy   # type: ignore

handler404 = 'core.views.page_not_found'
# handler403 = 'core.views.csrf_failure'

urlpatterns = [
    path('admin/', admin.site.urls),
    # Подключаем urls.py приложения для работы с пользователями.
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=CustomUserCreationForm,
            success_url=reverse_lazy('pages:homepage'),
        ),
        name='registration',
    ),
    path('birthday/', include('birthday.urls')),
    path('', include('pages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Если проект запущен в режиме разработки...
if settings.DEBUG:
    import debug_toolbar  # type: ignore
    # Добавить к списку urlpatterns список адресов из приложения debug_toolbar:
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
