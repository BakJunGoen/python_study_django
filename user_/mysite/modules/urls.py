from django.urls import path

from . import views 


app_name = 'modules'

urlpatterns = [
    path('', views.index, name='modules_views index'),
    path('signUp/', views.signUp, name="sign Up"),
    path('signUp2/', views.singup2.as_view(), name="signUp Test")
    # path('user/', user_views.index, name='user_views index')
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('test1', views.test.as_view(), name='test'),
    # path('api/test', views.API.as_view(), name='API'),
]