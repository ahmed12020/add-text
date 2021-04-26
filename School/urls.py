from django.urls import path, include
from . import views
from django.contrib.auth import views as view
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required



app_name = 'School'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('update/', views.update, name='update'),
    path('login/', view.LoginView.as_view(template_name='School/login.html'),name='login'),
    path('logout/', view.LogoutView.as_view(template_name='School/logout.html'), name='logout'),
    path('changepass/', view.PasswordChangeView.as_view(template_name='School/change.html'), name='change'),
    # path('api_1/', views.StudentListApiView.as_view(), name='api_1'),
    # path('api/<int:id>/', views.StudentDetailAPIView.as_view(), name='apidetail'),
    # path('update/<int:id>/', views.StudentUpdateAPIView.as_view(), name='apiupdate'),
    # path('del/<int:id>/', views.StudentDeleteAPIView.as_view(), name='del'),
    # path('create/', views.StudentCreatAPIView.as_view(),name='create'),
    path('index/', views.TemplateProfView.as_view(), name='index'),
    path('inside/', views.inside, name='inside'),
    path('page/', views.studentview, name='page'),
    path('set/', views.setsession, name='set'),
    path('get/', views.getsession, name='get'),
    path('del/', views.delsession, name='del'),
]
