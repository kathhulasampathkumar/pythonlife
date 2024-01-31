from django.db import models
from datetime import date, datetime, time
from django.utils import timezone

# Create your models here.
class user_master(models.Model):                
    empcode=models.IntegerField(serialize=True,auto_created=True)
    empname=models.CharField(max_length=50)
    designation=models.IntegerField(null=True,blank=True)
    department=models.IntegerField(null=True,blank=True)
    password=models.CharField(max_length=50)    
    rolename=models.CharField(max_length=50)
    createdby =models.CharField(max_length=50)
    jn_date=models.DateField(default='0000-00-00',null=True,blank=True)
    lv_date=models.DateField(default='0000-00-00',null=True,blank=True)
    dob=models.DateField(default='0000-00-00',null=True,blank=True)
    mail_id=models.CharField(max_length=50,null=True,blank=True)
    external_mail=models.CharField(max_length=50,null=True,blank=True)
    personal_mail=models.CharField(max_length=50,null=True,blank=True)
    mail_indi=models.CharField(max_length=50,null=True,blank=True)
    gndr=models.IntegerField(default=1)
    QMS=models.IntegerField(default=1)
    SAP=models.IntegerField(default=1)
    crnt_sts=models.IntegerField(default=1)
    mgr=models.IntegerField(null=True,blank=True)
    blood_group=models.CharField(max_length=10,null=True,blank=True)
    phno=models.IntegerField(null=True,blank=True)
    loc=models.CharField(max_length=50,null=True,blank=True)
    empgroup=models.CharField(max_length=20,null=True,blank=True)
    empsubgroup=models.CharField(max_length=20,null=True,blank=True)
    payscale_grade=models.CharField(max_length=20,null=True,blank=True)
    payscale_level=models.CharField(max_length=20,null=True,blank=True)
    payscale_sub_level=models.CharField(max_length=20,null=True,blank=True)
    pay_range=models.CharField(max_length=20,null=True,blank=True)
    adapt=models.CharField(max_length=20,null=True,blank=True)
    empType=models.CharField(max_length=50,null=True,blank=True)
    extn=models.CharField(max_length=50,null=True,blank=True)
    shrt=models.CharField(max_length=50,null=True,blank=True)
    active_name=models.CharField(max_length=10,null=True,blank=True)
    photo_sts=models.IntegerField(default=0,null=True,blank=True)
    build_no=models.CharField(max_length=10,null=True,blank=True)
    room_no	=models.CharField(max_length=10,null=True,blank=True) 
    local_std_code=models.CharField(max_length=10,null=True,blank=True)
    sys_no=models.CharField(max_length=15,null=True,blank=True)
    loc_outstn=models.CharField(max_length=50,null=True,blank=True)
    gl=models.CharField(max_length=60,null=True,blank=True)
    tl=models.IntegerField(null=True,blank=True)
    level_1=models.IntegerField(null=True,blank=True)
    level_2=models.IntegerField(null=True,blank=True)
    company_id=models.IntegerField(null=True,blank=True)
    tprog=models.CharField(max_length=20,null=True,blank=True)   
    timestamp=models.DateTimeField(default=datetime.now)
    delete1=models.IntegerField(default=0)
    marital_status=models.IntegerField(default=0)
    tms_status=models.IntegerField(default=0)
    ass_role=models.CharField(max_length=10,null=True,blank=True)
    qualification=models.CharField(max_length=20,default='SSC',null=True,blank=True)
    empcode_md5=models.CharField(max_length=50,null=True,blank=True)
    tr_facility=models.CharField(max_length=10,null=True,blank=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    marriage_date=models.DateField(default='0000-00-00',null=True,blank=True)
    phone_permission=models.CharField(default=0,max_length=20)
    bus_route=models.CharField(max_length=10,null=True,blank=True,default=0)
    ext_status=models.CharField(max_length=10,null=True,blank=True)
    work_loc=models.CharField(max_length=50,null=True,blank=True)
    audit_emp_sts=models.CharField(max_length=50,null=True,blank=True)
    auditor_qua_date=models.DateField(default='0000-00-00',null=True,blank=True)
    auditor_disqua_date=models.DateField(default='0000-00-00',null=True,blank=True)
    uan=models.CharField(max_length=20,null=True,blank=True)
    pan=models.CharField(max_length=20,null=True,blank=True)
    bank_indi=models.CharField(max_length=500,null=True,blank=True)
    bank_acc=models.CharField(max_length=500,null=True,blank=True)
    attendance_status=models.CharField(max_length=10,null=True,blank=True)
    ess=models.CharField(max_length=10,null=True,blank=True)
    alt_contact=models.CharField(max_length=20,null=True,blank=True)
    ot_flag=models.CharField(max_length=20,null=True,blank=True)
    rsc=models.CharField(max_length=2,null=True,blank=True)

    def __str__(self):
        return  self.empname
        # return str(self.empcode)+"  - "+ str(self.empname)+"  - "+ str(self.department)
    class Meta:
        db_table="user_master"

