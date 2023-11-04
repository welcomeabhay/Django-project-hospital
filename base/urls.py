from django.urls import path
from .import views


urlpatterns=[
    path('',views.Home,name='home'),
    path('dept',views.Departments,name='departments'),
    path('doc',views.Our_doctors,name='doctors'),
    path('edit_doc',views.Edit_Doc,name='edit_doc'),
    path('reg',views.Register,name='register'),
    path('p_reg',views.Patient_reg,name='patient_reg'),
    path('in',views.Login,name='login'),
    path('out',views.Logout,name='logout'),
    path('p_data',views.Patient_data,name='patient_data'),
    path('pat_pro',views.Edit_pat,name='pat_pro'),
    path('pat_record/<int:p_id>/',views.Patient_record,name='pat_record')

]