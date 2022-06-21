from django.urls import path
from courses.views import List_View, Detail_View, Create_View, Update_View, Delete_View

app_name='courses'
urlpatterns = [
    path('', List_View.as_view(template_name = 'courses/courses_list.html') , name='course_list'),
    # course end descript
    path('<int:pk>/detail/', Detail_View.as_view(), name='course_detail'),
    path('create/', Create_View.as_view(), name='course_create'),
    path('<int:pk>/update/', Update_View.as_view(), name='course_update'),
    path('<int:pk>/delete/', Delete_View.as_view(), name='course_delete'),
]
