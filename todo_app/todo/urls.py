
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('add_todo/',views.add_todo, name = 'add_todo'),
    path('edit_todo/<todo_id>/',views.edit_todo, name = 'edit_todo'),
    path('delete/<todo_id>/',views.delete_todo, name = 'delete_todo'),
    path('search/',views.search_results, name = 'search_results'),
    path('account/',views.account, name = 'account'),
    path('register/',views.register_page, name = 'register'),
    path('login/',views.login_page, name = 'login'),
    path('logout/',views.logout_page, name = 'logout'),
]
