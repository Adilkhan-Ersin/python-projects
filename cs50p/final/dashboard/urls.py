from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name='index'),
  path('login', views.login_view, name='login'),
  path('logout', views.logout_view, name='logout'),
  path('forgot', views.forgot_view, name='forgot'),
  path('register', views.register_view, name='register'),
  path('404', views.not_found, name='404'),
  path('403', views.error, name='403'),
  path('charts/transactions/', views.charts_data, name='charts_data'),
  path('charts', views.charts, name='charts'),
  path('tables', views.tables, name='tables'),
  path('submit_transaction', views.submit_transaction, name='submit_transaction'),
  path('submit_goal', views.submit_goal, name='submit_goal'),
  path('delete_goal/<int:post_id>', views.delete_goal, name='delete_goal'),
  path('edit_goal/<int:post_id>', views.edit_goal, name='edit_goal'),
]