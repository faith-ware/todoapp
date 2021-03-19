from django.urls import path
from todo.views import home_page, update_task, delete_task

app_name = "todo"

urlpatterns = [
    path("", home_page, name="home"),
    path("update/<int:id>/", update_task, name="updatetask"),
    path("delete/<int:id>/", delete_task, name="deletetask"),

]
