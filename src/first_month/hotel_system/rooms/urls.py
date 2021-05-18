from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns =[
    path('', views.home, name='home'),
    path('reserve/<int:pk>', views.reserve, name ="reserve"),
    path('checkout/<int:pk>', views.checkout, name='checkout'),
    path('rate/<int:pk>', views.rate, name='rate'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
