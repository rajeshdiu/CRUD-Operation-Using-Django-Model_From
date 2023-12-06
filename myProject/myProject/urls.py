from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myProject import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('myStudent/',views.myStudent,name="myStudent"),
    path('deleteStudent/<str:myid>',views.deleteStudent,name="deleteStudent"),
    path('editStudent/<str:myid>',views.editStudent,name="editStudent"),
    path('myTeacher/',views.myTeacher,name="myTeacher"),
    path('deleteTeacher/<str:myid>',views.deleteTeacher,name="deleteTeacher"),
    path('editTeacher/<str:myid>',views.editTeacher,name="editTeacher"),
    path('myEmployee/',views.myEmployee,name="myEmployee"),
    path('deleteEmployee/<str:myid>',views.deleteEmployee,name="deleteEmployee"),
    path('editEmployee/<str:myid>',views.editEmployee,name="editEmployee"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
