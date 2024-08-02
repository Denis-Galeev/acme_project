from django.contrib import admin  # type: ignore

# Из модуля models импортируем модель Birthday...
from .models import Birthday

# ...и регистрируем её в админке:
admin.site.register(Birthday)
