from django.contrib import admin  # Импортируем модуль админки Django
from django.urls import include, path  # Импортируем функции для работы с URL-маршрутами
from django.views.generic import TemplateView  # Импортируем класс для отображения статических страниц


urlpatterns = [
    path('api/', include('api.urls')),
    #Доступ к интерфейсу администратора.
    path('admin/', admin.site.urls),
]

urlpatterns.append(
    # Маршрут для документации API (Redoc).
    # При переходе на `/redoc/` будет отображаться статическая HTML-страница с документацией.
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'  
    ),
)
