from django.conf.urls import url
from . import views

app_name = "music"

urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name="index"),
    url(r'^contact/$', views.ContactView.as_view(), name="contact"),
    url(r'^thanks/$', views.thankyou, name="thanks"),
    url(r'^signin/$', views.Signin.as_view(), name="signin"),
    url(r'^login/$', views.login_user, name="login"),
    url(r'^logout/$', views.logout_user, name="logout"),
    url(r'^addalbum/$', views.add_album.as_view(), name="addalbum"),
    url(r'^songs/$', views.songs, name="songs"),

]


