from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home , name="home"),
    # path('join',views.join , name="join"),
    path('trending',views.trending, name="trending"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('join',views.log,name="join"),
    path("upload",views.upload,name="upload"),
    path("remove/<int:id>",views.remove,name="hey"),
     path("category/<int:id>",views.category),
    
    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
