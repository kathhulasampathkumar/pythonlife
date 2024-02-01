from django.urls import path, include
from user_master import views

urlpatterns = [
    path('', views.index, name='index'),            #default index page url
    # path('<slug:empcode>/<str:url>/', views.home, name='home'),     #default home page to get session from  page url
    # path('<slug:url>/<slug:url2>/<slug:url3>/',views.testview,name='testview'),
    # path('apply_certificate', views.apply_certificate, name='apply_certificate'),  #render apply certificate page      
    # path('get_skill_field_master_fields', views.get_skill_field_master_fields, name='get_skill_field_master_fields'), #load skill fields in apply certificate 
    # path('get_skill_field_master_fieldsV1', views.get_skill_field_master_fieldsV1, name='get_skill_field_master_fieldsV1'), #load skill fields in apply certificate 
    # path('save_certificate', views.save_certificate, name='save_certificate'),#to  save_certificate 
    # # path('getDesignationRandom', views.getDesignationRandom, name='getDesignationRandom'), #json responce by empcode json 
    # path('employee_json_responce', views.employee_json_responce, name='employee_json_responce'), #json responce by empcode json 
    # path('employee_json_responce2', views.employee_json_responce2, name='employee_json_responce2'), #json responce by empcode json 
     
    # path('certificate_approvals', views.certificate_approvals, name='certificate_approvals'),  #approve page for reporting persons 
    # path('certificate/certificate_approvals/<int:main_id>/', views.update_cert, name='update_cert'), #approve page for reporting persons 
    # path('get_certificate', views.get_certificate, name='get_certificate'),  #get certificate  page which approved by hod /head 
    # path('search_certificate', views.search_certificate, name='search_certificate'),  #search certificate by empcode or certificate name   
    # path('logout', views.logout, name='logout'),   #logout from django to rewamp
    # path('homepage', views.homepage, name='homepage'),   #logout from django to rewamp homepage
    # path('convert_pdf', views.convert_pdf, name='convert_pdf'), #to convert pdf or show view  
    # path('download_pdf', views.download_pdf, name='download_pdf'), #to download pdf   
    # path('apply_certificate/db', views.dbtable_backup, name='dbtable_backup'), #to dbtable_backup
    # path('database_json', views.database_json, name='database_json'), #json responce by database_json json    
    # path('getTcodelist', views.getTcodelist, name='getTcodelist'), #json responce by getTcodelist json    
    # path('update_multiple', views.update_multiple, name='update_multiple'), #json responce by getTcodelist json    
    # path('delete_certificate', views.delete_certificate, name='delete_certificate'),     
    # path('remove_certificate', views.remove_certificate, name='remove_certificate'),  
]
handler404 ='user_master.views.error_404'
