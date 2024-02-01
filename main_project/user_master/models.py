from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


class UserMaster(models.Model):
    empcode = models.IntegerField()
    empname = models.CharField(max_length=90, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=500, blank=True, null=True)
    rolename = models.CharField(max_length=40, blank=True, null=True)
    createdby = models.CharField(max_length=50, blank=True, null=True)
    jn_date = models.DateField(blank=True, null=True)
    lv_date = models.DateField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    mail_id = models.CharField(max_length=100)
    external_mail = models.CharField(max_length=100, blank=True, null=True)
    personal_mail = models.CharField(max_length=100, blank=True, null=True)
    mail_indi = models.CharField(max_length=3, blank=True, null=True)
    gndr = models.IntegerField()
    qms = models.IntegerField(db_column='QMS')  # Field name made lowercase.
    sap = models.IntegerField(db_column='SAP')  # Field name made lowercase.
    crnt_sts = models.IntegerField()
    mgr = models.IntegerField()
    blood_group = models.CharField(max_length=10, blank=True, null=True)
    phno = models.CharField(max_length=30)
    loc = models.CharField(max_length=20, blank=True, null=True)
    empgroup = models.CharField(max_length=10, blank=True, null=True)
    empsubgroup = models.CharField(max_length=10, blank=True, null=True)
    payscale_grade = models.CharField(max_length=20, blank=True, null=True)
    payscale_level = models.CharField(max_length=20, blank=True, null=True)
    payscale_sub_level = models.CharField(max_length=3, blank=True, null=True)
    pay_range = models.CharField(max_length=10, blank=True, null=True)
    adapt = models.CharField(max_length=20, blank=True, null=True)
    emptype = models.CharField(db_column='empType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extn = models.CharField(max_length=50, blank=True, null=True)
    shrt = models.CharField(max_length=50, blank=True, null=True)
    active_name = models.CharField(max_length=1, blank=True, null=True)
    photo_sts = models.IntegerField()
    build_no = models.CharField(max_length=4, blank=True, null=True)
    room_no = models.CharField(max_length=3, blank=True, null=True)
    local_std_code = models.CharField(max_length=8, blank=True, null=True)
    sys_no = models.CharField(max_length=15, blank=True, null=True)
    loc_outstn = models.CharField(max_length=50, blank=True, null=True)
    gl = models.CharField(max_length=60, blank=True, null=True)
    tl = models.IntegerField()
    level_1 = models.IntegerField()
    level_2 = models.IntegerField()
    company_id = models.IntegerField()
    tprog = models.CharField(max_length=15, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    marital_status = models.IntegerField()
    tms_status = models.IntegerField()
    ass_role = models.CharField(max_length=10, blank=True, null=True)
    qualification = models.CharField(max_length=90, blank=True, null=True)
    empcode_md5 = models.CharField(max_length=100, blank=True, null=True)
    tr_facility = models.CharField(max_length=1, blank=True, null=True)
    first_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    marriage_date = models.DateField(blank=True, null=True)
    phone_permission = models.CharField(max_length=1)
    bus_route = models.CharField(max_length=10, blank=True, null=True)
    ext_status = models.CharField(max_length=20)
    work_loc = models.CharField(max_length=50, blank=True, null=True)
    audit_emp_sts = models.IntegerField()
    auditor_qua_date = models.DateField()
    auditor_disqua_date = models.DateField()
    uan = models.CharField(max_length=20, blank=True, null=True)
    pan = models.CharField(max_length=30, blank=True, null=True)
    bank_indi = models.CharField(max_length=500, blank=True, null=True)
    bank_acc = models.CharField(max_length=500, blank=True, null=True)
    attendance_status = models.CharField(max_length=10, blank=True, null=True)
    ess = models.CharField(max_length=10, blank=True, null=True)
    alt_contact = models.CharField(max_length=15, blank=True, null=True)
    ot_flag = models.CharField(max_length=2, blank=True, null=True)
    shrt_name = models.CharField(max_length=10, blank=True, null=True)
    fl_elg = models.IntegerField()
    rsc = models.IntegerField()
    emp_cat = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_master'


class MrsMaterialCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    mrs_no = models.CharField(max_length=50)
    material_code = models.CharField(max_length=50)
    batch_number = models.CharField(max_length=50)
    system_ip = models.CharField(max_length=50)
    emp_code = models.IntegerField()
    entry_date = models.CharField(max_length=50)
    entry_time = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Mrs_material_code'


class OilChangeOilchangedata(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_code = models.IntegerField()
    employee_name = models.CharField(max_length=100)
    project = models.CharField(max_length=50)
    rake_id = models.CharField(max_length=100)
    commissioning_date = models.DateField()
    railway_shed = models.CharField(max_length=100)
    railway_zone = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    regreasing_date = models.DateField()
    oil_change_date = models.DateField()
    km_cover_oil = models.IntegerField()
    km_cover_regr = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Oil_change_oilchangedata'


class Sheet1(models.Model):
    slno = models.IntegerField(blank=True, null=True)
    project = models.CharField(max_length=11, blank=True, null=True)
    createdon = models.CharField(max_length=8, blank=True, null=True)
    orderno = models.IntegerField(blank=True, null=True)
    matcode = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=40, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    batch = models.CharField(max_length=10, blank=True, null=True)
    remarks = models.CharField(max_length=12, blank=True, null=True)
    timestamp = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sheet1'


class Abc(models.Model):
    slno = models.IntegerField()
    catid = models.IntegerField()
    change_cat = models.CharField(max_length=500)
    reasonofchange = models.CharField(max_length=100)
    typeofchange = models.CharField(max_length=100)
    conclusionbyme = models.CharField(max_length=500)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'abc'


class AccTrackCategoryMaster(models.Model):
    cat_id = models.SmallAutoField(primary_key=True)
    cat_name = models.CharField(max_length=30)
    type = models.CharField(max_length=15)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField(blank=True, null=True)
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'acc_track_category_master'


class AccTrackHistory(models.Model):
    slno = models.IntegerField()
    comments = models.TextField()
    date = models.DateField()
    status = models.IntegerField()
    updated = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_reason = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'acc_track_history'


class AccTrackNtry(models.Model):
    slno = models.SmallAutoField(primary_key=True)
    description = models.TextField()
    date = models.DateField()
    req = models.IntegerField()
    dept = models.IntegerField()
    loc = models.CharField(max_length=4)
    cat_id = models.SmallIntegerField()
    sub_cat_id = models.SmallIntegerField()
    status = models.SmallIntegerField()
    responsibility = models.CharField(max_length=150)
    other_emp = models.IntegerField()
    timestamp = models.DateTimeField(blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'acc_track_ntry'


class AccTrackStatusMaster(models.Model):
    status = models.SmallAutoField(primary_key=True)
    status_name = models.CharField(max_length=30)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField(blank=True, null=True)
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'acc_track_status_master'


class AccTrackSubCategoryMaster(models.Model):
    cat_id = models.SmallIntegerField()
    sub_cat_id = models.SmallAutoField(primary_key=True)
    sub_cat_name = models.CharField(max_length=150)
    responsibility = models.CharField(max_length=150)
    type = models.CharField(max_length=15)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField(blank=True, null=True)
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'acc_track_sub_category_master'


class AcceptanceCriteria(models.Model):
    docno = models.PositiveBigIntegerField(primary_key=True)
    sfcode = models.CharField(max_length=20, blank=True, null=True)
    slno = models.CharField(max_length=4, blank=True, null=True)
    ac1 = models.CharField(max_length=20, blank=True, null=True)
    ac2 = models.CharField(max_length=20, blank=True, null=True)
    ac3 = models.CharField(max_length=20, blank=True, null=True)
    ac4 = models.CharField(max_length=20, blank=True, null=True)
    ac5 = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.CharField(max_length=50, blank=True, null=True)
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField(blank=True, null=True)
    delete_by = models.IntegerField(blank=True, null=True)
    dalete_date = models.CharField(max_length=20, blank=True, null=True)
    delete_reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acceptance_criteria'


class AeGallery(models.Model):
    ext = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    data = models.CharField(max_length=150)
    image_time = models.DateTimeField()
    html_enty_text = models.CharField(max_length=500)
    html_spl_chars = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ae_gallery'


class AlternateMaster(models.Model):
    reqid = models.IntegerField()
    unit_no = models.IntegerField()
    code = models.CharField(max_length=30, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alternate_master'


class AlternateMaster1(models.Model):
    reqid = models.IntegerField()
    unit_no = models.IntegerField()
    code = models.CharField(max_length=30)
    remarks = models.TextField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alternate_master1'


class AlternateMaterialCodeNew(models.Model):
    m_code = models.CharField(max_length=15)
    m_category = models.CharField(max_length=50)
    e_code = models.CharField(max_length=50)
    delete1 = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'alternate_material_code_new'


class AmcDetails(models.Model):
    sno = models.IntegerField(blank=True, null=True)
    coach_no = models.IntegerField(blank=True, null=True)
    coach_type = models.CharField(max_length=10, blank=True, null=True)
    inv_type = models.CharField(max_length=10, blank=True, null=True)
    zone = models.CharField(max_length=40, blank=True, null=True)
    shed = models.CharField(max_length=40, blank=True, null=True)
    us_no = models.IntegerField(blank=True, null=True)
    cu_no = models.IntegerField(blank=True, null=True)
    createdby = models.SmallIntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'amc_details'


class ApplSwDg(models.Model):
    dgid = models.IntegerField()
    empcode = models.IntegerField()
    project = models.IntegerField()
    takentime = models.FloatField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'appl_sw_dg'


class ApplSwProj(models.Model):
    projid = models.AutoField(primary_key=True)
    project = models.CharField(max_length=100, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'appl_sw_proj'


class AprslHeaderMaster(models.Model):
    form_name = models.CharField(max_length=1)
    header_no = models.IntegerField()
    header_name = models.CharField(max_length=50)
    p = models.IntegerField()
    a = models.IntegerField()
    g = models.IntegerField()
    e = models.IntegerField()
    max_marks = models.IntegerField()
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'aprsl_header_master'


class AprslItemMaster(models.Model):
    form_name = models.CharField(max_length=1)
    header_no = models.IntegerField()
    item_no = models.IntegerField()
    item_name = models.CharField(max_length=50)
    p = models.IntegerField()
    a = models.IntegerField()
    g = models.IntegerField()
    e = models.IntegerField()
    max_marks = models.IntegerField()
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'aprsl_item_master'


class Arose(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'arose'


class AssemblyTypeMstr(models.Model):
    slno = models.AutoField(primary_key=True)
    assembly_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'assembly_type_mstr'


class AssocFamily(models.Model):
    fid = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    sap_no = models.CharField(max_length=5)
    fname = models.CharField(max_length=50, blank=True, null=True)
    frel = models.CharField(max_length=15, blank=True, null=True)
    fgender = models.IntegerField(blank=True, null=True)
    fdob = models.DateField()
    fage = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    act_sts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'assoc_family'


class Atest(models.Model):
    sno = models.AutoField(primary_key=True)
    gr = models.CharField(max_length=150)
    display = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'atest'


class AttendedAt(models.Model):
    at_no = models.AutoField(primary_key=True)
    at_name = models.CharField(max_length=50)
    createdby = models.SmallIntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attended_at'


class AuditAuditorAction(models.Model):
    uniq_slno = models.IntegerField()
    nc_no = models.IntegerField(primary_key=True)
    audi_date = models.DateField()
    category = models.IntegerField()
    agtstd = models.CharField(max_length=500, blank=True, null=True)
    nc_detils = models.CharField(max_length=50, blank=True, null=True)
    cls_audit = models.CharField(max_length=50, blank=True, null=True)
    docs = models.CharField(max_length=50, blank=True, null=True)
    ofi_sts = models.IntegerField()
    ofi_details = models.CharField(max_length=5000, blank=True, null=True)
    act_taken = models.CharField(max_length=50, blank=True, null=True)
    nc_ref = models.IntegerField()
    verified = models.CharField(max_length=50, blank=True, null=True)
    complied = models.CharField(max_length=50, blank=True, null=True)
    not_complied = models.CharField(max_length=50, blank=True, null=True)
    veri_corr_act = models.CharField(max_length=1000, blank=True, null=True)
    veri_siml_act = models.CharField(max_length=1000, blank=True, null=True)
    eff_ver_audit = models.CharField(max_length=1000, blank=True, null=True)
    nc_sts = models.IntegerField()
    nc_sts_commnet = models.CharField(max_length=2000, blank=True, null=True)
    nc_close_date = models.DateField()
    pd_stg = models.CharField(max_length=150, blank=True, null=True)
    grade = models.CharField(max_length=25, blank=True, null=True)
    rating = models.CharField(max_length=25, blank=True, null=True)
    requirement = models.CharField(max_length=1000, blank=True, null=True)
    failure = models.CharField(max_length=1000, blank=True, null=True)
    evidence = models.CharField(max_length=1000, blank=True, null=True)
    cancell_nc = models.CharField(max_length=1000, blank=True, null=True)
    cancel_by = models.IntegerField()
    cancel_time = models.DateTimeField()
    repeat_nc = models.IntegerField()
    auditee_acc = models.IntegerField()
    nc_not_reason = models.TextField(blank=True, null=True)
    followup_auditor = models.IntegerField()
    followup_date = models.CharField(max_length=200, blank=True, null=True)
    first_mail_count = models.IntegerField()
    attachment = models.CharField(max_length=500, blank=True, null=True)
    pro_ext = models.CharField(max_length=100, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audit_auditor_action'


class AuditAuditorAction22092022(models.Model):
    uniq_slno = models.IntegerField()
    nc_no = models.IntegerField(primary_key=True)
    audi_date = models.DateField()
    category = models.IntegerField()
    agtstd = models.CharField(max_length=500, blank=True, null=True)
    nc_detils = models.CharField(max_length=50, blank=True, null=True)
    cls_audit = models.CharField(max_length=50, blank=True, null=True)
    docs = models.CharField(max_length=50, blank=True, null=True)
    ofi_sts = models.IntegerField()
    ofi_details = models.CharField(max_length=5000, blank=True, null=True)
    act_taken = models.CharField(max_length=50, blank=True, null=True)
    nc_ref = models.IntegerField()
    verified = models.CharField(max_length=50, blank=True, null=True)
    complied = models.CharField(max_length=50, blank=True, null=True)
    not_complied = models.CharField(max_length=50, blank=True, null=True)
    veri_corr_act = models.CharField(max_length=1000, blank=True, null=True)
    veri_siml_act = models.CharField(max_length=1000, blank=True, null=True)
    eff_ver_audit = models.CharField(max_length=1000, blank=True, null=True)
    nc_sts = models.IntegerField()
    nc_sts_commnet = models.CharField(max_length=2000, blank=True, null=True)
    nc_close_date = models.DateField()
    pd_stg = models.CharField(max_length=150, blank=True, null=True)
    grade = models.CharField(max_length=25, blank=True, null=True)
    rating = models.CharField(max_length=25, blank=True, null=True)
    requirement = models.CharField(max_length=1000, blank=True, null=True)
    failure = models.CharField(max_length=1000, blank=True, null=True)
    evidence = models.CharField(max_length=1000, blank=True, null=True)
    cancell_nc = models.CharField(max_length=1000, blank=True, null=True)
    cancel_by = models.IntegerField()
    cancel_time = models.DateTimeField()
    repeat_nc = models.IntegerField()
    auditee_acc = models.IntegerField()
    nc_not_reason = models.TextField(blank=True, null=True)
    followup_auditor = models.IntegerField()
    followup_date = models.CharField(max_length=200, blank=True, null=True)
    first_mail_count = models.IntegerField()
    attachment = models.CharField(max_length=500, blank=True, null=True)
    pro_ext = models.CharField(max_length=100, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audit_auditor_action_22-09-2022'


class AuditAuditorList(models.Model):
    empcode = models.IntegerField()
    department = models.IntegerField()
    loc = models.CharField(max_length=50, blank=True, null=True)
    audit_emp_sts = models.IntegerField()
    auditor_qua_date = models.DateField()
    auditor_disqua_date = models.DateField()
    crnt_sts = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    audit_scope = models.TextField(blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'audit_auditor_list'


class AuditAuditorList22092022(models.Model):
    empcode = models.IntegerField()
    department = models.IntegerField()
    loc = models.CharField(max_length=50, blank=True, null=True)
    audit_emp_sts = models.IntegerField()
    auditor_qua_date = models.DateField()
    auditor_disqua_date = models.DateField()
    crnt_sts = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    audit_scope = models.TextField(blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'audit_auditor_list_22-09-2022'


class AuditBmpsMaster(models.Model):
    name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=25)
    loc = models.CharField(max_length=20)
    rev_no = models.IntegerField()
    type = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'audit_bmps_master'


class AuditBmpsMaster22092022(models.Model):
    name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=25)
    loc = models.CharField(max_length=20)
    rev_no = models.IntegerField()
    type = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'audit_bmps_master_22-09-2022'


class AuditDeligateAction(models.Model):
    slno = models.IntegerField()
    uniq_slno = models.IntegerField()
    nc_no = models.IntegerField()
    category = models.IntegerField()
    audit_id = models.CharField(max_length=50, blank=True, null=True)
    pro_date_comp = models.DateField()
    root_cause = models.CharField(max_length=1000, blank=True, null=True)
    corr_detail = models.CharField(max_length=1000, blank=True, null=True)
    pro_corr_act = models.CharField(max_length=1000, blank=True, null=True)
    detl_corr_act = models.CharField(max_length=1000, blank=True, null=True)
    act_com_date = models.DateField()
    veri_corr_act = models.CharField(max_length=1000, blank=True, null=True)
    veri_siml_act = models.CharField(max_length=100, blank=True, null=True)
    eff_ver_audit = models.CharField(max_length=1000, blank=True, null=True)
    ofi_action = models.CharField(max_length=2000, blank=True, null=True)
    attachment = models.CharField(max_length=250, blank=True, null=True)
    ofi_attachment = models.CharField(max_length=250, blank=True, null=True)
    submit_val = models.CharField(max_length=250, blank=True, null=True)
    auditee_acc = models.IntegerField()
    nc_not_reason = models.TextField(blank=True, null=True)
    cancel_by = models.IntegerField()
    cancel_time = models.DateTimeField()
    doc_id = models.CharField(max_length=100, blank=True, null=True)
    delete1 = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audit_deligate_action'


class AuditDeligateAction22092022(models.Model):
    slno = models.IntegerField()
    uniq_slno = models.IntegerField()
    nc_no = models.IntegerField()
    category = models.IntegerField()
    audit_id = models.CharField(max_length=50, blank=True, null=True)
    pro_date_comp = models.DateField()
    root_cause = models.CharField(max_length=1000, blank=True, null=True)
    corr_detail = models.CharField(max_length=1000, blank=True, null=True)
    pro_corr_act = models.CharField(max_length=1000, blank=True, null=True)
    detl_corr_act = models.CharField(max_length=1000, blank=True, null=True)
    act_com_date = models.DateField()
    veri_corr_act = models.CharField(max_length=1000, blank=True, null=True)
    veri_siml_act = models.CharField(max_length=100, blank=True, null=True)
    eff_ver_audit = models.CharField(max_length=1000, blank=True, null=True)
    ofi_action = models.CharField(max_length=2000, blank=True, null=True)
    attachment = models.CharField(max_length=250, blank=True, null=True)
    ofi_attachment = models.CharField(max_length=250, blank=True, null=True)
    submit_val = models.CharField(max_length=250, blank=True, null=True)
    auditee_acc = models.IntegerField()
    nc_not_reason = models.TextField(blank=True, null=True)
    cancel_by = models.IntegerField()
    cancel_time = models.DateTimeField()
    delete1 = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audit_deligate_action_22-09-2022'


class AuditFeedback(models.Model):
    fb_id = models.AutoField(primary_key=True)
    uniq_slno = models.CharField(max_length=11, blank=True, null=True)
    audit_masterid = models.CharField(max_length=11, blank=True, null=True)
    rating = models.CharField(max_length=100, blank=True, null=True)
    auditor_empcode = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'audit_feedback'


class AuditPlan(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    audit_id = models.CharField(max_length=250, blank=True, null=True)
    audit_loccode = models.CharField(max_length=25, blank=True, null=True)
    audit_dept = models.IntegerField()
    auditor_empcode = models.IntegerField()
    bmps_id = models.CharField(max_length=100, blank=True, null=True)
    plan_date = models.DateField()
    plan_ftime_hh = models.CharField(max_length=25)
    plan_ftime_mm = models.CharField(max_length=25)
    plan_totime_hh = models.CharField(max_length=25)
    plan_totime_mm = models.CharField(max_length=25)
    plan_to_date = models.DateField()
    audit_type_id = models.IntegerField()
    type_seq_no = models.IntegerField()
    approve_type = models.IntegerField()
    approval_sts = models.IntegerField()
    approved_by = models.IntegerField()
    approved_date = models.DateField()
    release_sts = models.IntegerField()
    auditee_by = models.IntegerField()
    auditee_sts = models.IntegerField(blank=True, null=True)
    auditee_approved_date = models.DateField()
    deligate = models.IntegerField()
    audit_act_date = models.DateField()
    audit_act_time = models.CharField(max_length=25, blank=True, null=True)
    ncs = models.IntegerField()
    audit_sts = models.IntegerField()
    secondary = models.IntegerField()
    remarks = models.CharField(max_length=2000, blank=True, null=True)
    fncs = models.IntegerField()
    audit_obs = models.TextField(blank=True, null=True)
    multi_slno = models.IntegerField()
    first_mail_count = models.IntegerField()
    release_to = models.CharField(max_length=10, blank=True, null=True)
    cross_dept = models.IntegerField()
    cmm_mail = models.CharField(max_length=500, blank=True, null=True)
    fileddate = models.DateField()
    dept_hod_code = models.IntegerField()
    active_ids = models.IntegerField()
    final_submit = models.IntegerField()
    delete1 = models.IntegerField()
    delete_by = models.CharField(max_length=7)
    deleted_timestamp = models.CharField(max_length=20)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audit_plan'


class AuditPlan22092022(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    audit_id = models.CharField(max_length=250, blank=True, null=True)
    audit_loccode = models.CharField(max_length=25, blank=True, null=True)
    audit_dept = models.IntegerField()
    auditor_empcode = models.IntegerField()
    bmps_id = models.CharField(max_length=100, blank=True, null=True)
    plan_date = models.DateField()
    plan_ftime_hh = models.CharField(max_length=25)
    plan_ftime_mm = models.CharField(max_length=25)
    plan_totime_hh = models.CharField(max_length=25)
    plan_totime_mm = models.CharField(max_length=25)
    plan_to_date = models.DateField()
    audit_type_id = models.IntegerField()
    type_seq_no = models.IntegerField()
    approve_type = models.IntegerField()
    approval_sts = models.IntegerField()
    approved_by = models.IntegerField()
    approved_date = models.DateField()
    release_sts = models.IntegerField()
    auditee_by = models.IntegerField()
    auditee_sts = models.IntegerField(blank=True, null=True)
    auditee_approved_date = models.DateField()
    deligate = models.IntegerField()
    audit_act_date = models.DateField()
    audit_act_time = models.CharField(max_length=25, blank=True, null=True)
    ncs = models.IntegerField()
    audit_sts = models.IntegerField()
    secondary = models.IntegerField()
    remarks = models.CharField(max_length=2000, blank=True, null=True)
    fncs = models.IntegerField()
    audit_obs = models.TextField(blank=True, null=True)
    multi_slno = models.IntegerField()
    first_mail_count = models.IntegerField()
    release_to = models.CharField(max_length=10, blank=True, null=True)
    cross_dept = models.IntegerField()
    cmm_mail = models.CharField(max_length=500, blank=True, null=True)
    fileddate = models.DateField()
    dept_hod_code = models.IntegerField()
    active_ids = models.IntegerField()
    delete1 = models.IntegerField()
    delete_by = models.CharField(max_length=7)
    deleted_timestamp = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    final_submit = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'audit_plan_22-09-2022'


class AuditRatingmaster(models.Model):
    desc = models.CharField(max_length=100, blank=True, null=True)
    input_type = models.CharField(max_length=20, blank=True, null=True)
    rat_id = models.CharField(max_length=20, blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'audit_ratingmaster'


class AuditTypeMaster(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=250)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'audit_type_master'


class AuditTypeMaster22092022(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=250)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'audit_type_master_22-09-2022'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AutoLogout(models.Model):
    slno = models.AutoField(primary_key=True)
    time = models.IntegerField()
    msg = models.CharField(max_length=10)
    createdby = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auto_logout'


class BankMaster(models.Model):
    bank_slno = models.AutoField(primary_key=True)
    companycode = models.IntegerField(db_column='Companycode', blank=True, null=True)  # Field name made lowercase.
    bank_key = models.CharField(db_column='Bank_Key', max_length=5, blank=True, null=True)  # Field name made lowercase.
    acc_no = models.CharField(db_column='Acc_no', max_length=15, blank=True, null=True)  # Field name made lowercase.
    acc_name = models.CharField(max_length=23, blank=True, null=True)
    bank_limit = models.BigIntegerField(blank=True, null=True)
    cc_limit = models.IntegerField(blank=True, null=True)
    lc_limit = models.IntegerField(blank=True, null=True)
    street = models.CharField(max_length=29, blank=True, null=True)
    city = models.CharField(max_length=16, blank=True, null=True)
    branch_name = models.CharField(db_column='Branch_name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ifsc_code = models.CharField(max_length=10, blank=True, null=True)
    from_date = models.CharField(max_length=10, blank=True, null=True)
    to_date = models.CharField(max_length=10, blank=True, null=True)
    tax_no = models.CharField(max_length=15, blank=True, null=True)
    delete1 = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_master'


class BankMasterOld(models.Model):
    bank_slno = models.AutoField(primary_key=True)
    company_code = models.IntegerField(db_column='Company code')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bank_key = models.CharField(db_column='Bank Key', max_length=5)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    acc_no = models.CharField(db_column='Acc_no', max_length=18, blank=True, null=True)  # Field name made lowercase.
    acc_name = models.CharField(max_length=50, blank=True, null=True)
    bank_limit = models.IntegerField()
    cc_limit = models.CharField(max_length=16)
    lc_limit = models.CharField(max_length=16)
    street = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=25)
    branch_name = models.CharField(db_column='Branch_name', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ifsc_code = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()
    tax_no = models.CharField(max_length=16, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bank_master_old'


class Barcode(models.Model):
    barcode_name = models.CharField(max_length=50)
    ip = models.CharField(max_length=20)
    sys_name = models.CharField(max_length=50)
    matnr = models.CharField(max_length=11)
    batch = models.CharField(max_length=11)
    start = models.IntegerField()
    end = models.IntegerField()
    matnr_status = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    uniq_slno = models.AutoField(primary_key=True)
    refresh = models.IntegerField()
    refresh_by = models.IntegerField()
    refresh_reason = models.CharField(max_length=300)
    refresh_timestamp = models.CharField(max_length=20)
    pcb_slno = models.IntegerField()
    order_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'barcode'


class BarcodeBayMaster(models.Model):
    bay_no = models.AutoField(primary_key=True)
    bay_name = models.CharField(max_length=50)
    bay_resp_code = models.IntegerField()
    ip = models.CharField(max_length=25)
    sys_name = models.CharField(max_length=25)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'barcode_bay_master'


class BarcodeDeptMaster(models.Model):
    deptcode = models.IntegerField()
    deptname = models.CharField(max_length=25)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    loc = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'barcode_dept_master'


class BarcodeSlno(models.Model):
    seq_slno = models.AutoField(primary_key=True)
    barcode_name = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    sys_name = models.CharField(max_length=50)
    slno = models.CharField(max_length=10)
    status = models.IntegerField()
    status_update_timestamp = models.CharField(max_length=20)
    createdby = models.IntegerField()
    refresh = models.IntegerField()
    refresh_by = models.IntegerField()
    refresh_reason = models.CharField(max_length=300)
    refresh_timestamp = models.CharField(max_length=20)
    order_no = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'barcode_slno'


class BgFdMain(models.Model):
    fd_slno = models.AutoField(primary_key=True)
    fd_no = models.CharField(max_length=20)
    bank_slno = models.IntegerField()
    bank_key = models.CharField(db_column='Bank_Key', max_length=10, blank=True, null=True)  # Field name made lowercase.
    amount = models.BigIntegerField()
    roi = models.FloatField()
    fd_open_date = models.DateField()
    maturity_date = models.DateField()
    status = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bg_fd_main'


class BgFdSub(models.Model):
    fd_bg_slno = models.AutoField(primary_key=True)
    fd_slno = models.IntegerField()
    bg_no = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bg_fd_sub'


class BgIomApproval(models.Model):
    app_id = models.AutoField(primary_key=True)
    iom_no = models.IntegerField()
    empcode = models.CharField(max_length=6)
    status = models.IntegerField()
    comments = models.CharField(max_length=250, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bg_iom_approval'


class BgIomAttachments(models.Model):
    slno = models.AutoField(primary_key=True)
    iom_no = models.IntegerField()
    type = models.IntegerField()
    attach_name = models.TextField(blank=True, null=True)
    empcode = models.CharField(max_length=8, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bg_iom_attachments'


class BgIomEntry(models.Model):
    empcode = models.CharField(max_length=7, blank=True, null=True)
    iom_no = models.AutoField(primary_key=True)
    company_code = models.IntegerField()
    iom_type = models.IntegerField()
    bg_type = models.IntegerField()
    railways = models.TextField(db_column='Railways', blank=True, null=True)  # Field name made lowercase.
    contract_through = models.CharField(max_length=2, blank=True, null=True)
    contract_no = models.CharField(max_length=300, blank=True, null=True)
    contract_date = models.DateField()
    contract_todate = models.DateField()
    contract_value = models.BigIntegerField()
    customer_id = models.IntegerField()
    contract_desc = models.TextField(blank=True, null=True)
    bg_favour = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.IntegerField()
    bgno = models.CharField(max_length=18, blank=True, null=True)
    bgdate = models.DateField()
    ext_bg_no = models.CharField(max_length=18, blank=True, null=True)
    bg_benficiary = models.TextField(blank=True, null=True)
    bg_amt = models.BigIntegerField()
    bg_vailddate = models.DateField()
    bg_exirydate = models.DateField(db_column='Bg_exirydate')  # Field name made lowercase.
    bg_closedate = models.DateField()
    amc_extend_upto = models.IntegerField()
    amc_extend_value = models.IntegerField()
    completed_value = models.IntegerField()
    bank_slno = models.IntegerField()
    bank_key = models.CharField(db_column='Bank_Key', max_length=6, blank=True, null=True)  # Field name made lowercase.
    extn_reason = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    bg_active = models.IntegerField()
    stamp = models.TextField(blank=True, null=True)
    hod_code = models.CharField(max_length=6, blank=True, null=True)
    hod_sts = models.IntegerField()
    hod_app_time = models.DateTimeField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bg_iom_entry'


class BgIomHistory(models.Model):
    slno = models.AutoField(primary_key=True)
    iom_no = models.IntegerField()
    status = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    empcode = models.CharField(max_length=7, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bg_iom_history'


class BgIomStatusMaster(models.Model):
    slno = models.AutoField(primary_key=True)
    status = models.IntegerField()
    sts_des = models.CharField(max_length=50, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bg_iom_status_master'


class BgIomType(models.Model):
    iom_no = models.AutoField(primary_key=True)
    iom_name = models.CharField(max_length=30, blank=True, null=True)
    delete1 = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bg_iom_type'


class BgMain(models.Model):
    bg_slno = models.AutoField(primary_key=True)
    iom_no = models.IntegerField()
    company_code = models.IntegerField()
    empcode = models.CharField(max_length=7, blank=True, null=True)
    bg_type = models.IntegerField()
    iom_type = models.IntegerField()
    contract_no = models.CharField(max_length=300, blank=True, null=True)
    contract_date = models.DateField()
    contract_todate = models.DateField()
    contract_value = models.BigIntegerField()
    customer_id = models.IntegerField()
    contract_desc = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.IntegerField()
    bg_favour = models.TextField(blank=True, null=True)
    bgno = models.CharField(max_length=18, blank=True, null=True)
    bgdate = models.DateField()
    ext_bg_no = models.CharField(max_length=18, blank=True, null=True)
    bg_benficiary = models.TextField(blank=True, null=True)
    bg_amt = models.BigIntegerField()
    bg_vailddate = models.DateField()
    bg_amt_old = models.BigIntegerField()
    bg_vailddate_old = models.DateField()
    status = models.IntegerField()
    bank_slno = models.IntegerField()
    delete1 = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bg_main'


class BgType(models.Model):
    type_slno = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100, blank=True, null=True)
    type_extn = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bg_type'


class Bookreimburse(models.Model):
    id = models.BigAutoField(primary_key=True)
    empcode = models.IntegerField()
    category = models.IntegerField()
    totalamount = models.IntegerField()
    requestdate = models.DateField()
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bookreimburse'


class Bookreimbursesubdata(models.Model):
    id = models.BigAutoField(primary_key=True)
    ref_no = models.IntegerField()
    bill_no = models.IntegerField()
    bill_date = models.DateField()
    bill_amount = models.IntegerField()
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bookreimbursesubdata'


class BusDetails(models.Model):
    slno = models.AutoField(primary_key=True)
    vec_type = models.CharField(max_length=10)
    vanname = models.CharField(max_length=200)
    endtime = models.CharField(max_length=6)
    extn = models.IntegerField(blank=True, null=True)
    loccode = models.CharField(max_length=20)
    source = models.CharField(max_length=200)
    destination = models.CharField(max_length=100)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bus_details'


class BusMembers(models.Model):
    empcode = models.IntegerField()
    empname = models.CharField(max_length=100)
    route = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    group = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bus_members'


class BusRoutes(models.Model):
    slno = models.IntegerField()
    place = models.CharField(max_length=200)
    timings = models.CharField(max_length=6)
    delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bus_routes'


class Cal5(models.Model):
    cal_for = models.CharField(max_length=20)
    order_no = models.CharField(max_length=20)
    mat_code = models.CharField(max_length=20)
    sl_no = models.CharField(max_length=20)
    unit_sl = models.CharField(max_length=10)
    mvstb = models.CharField(max_length=10)
    mip_voltage = models.CharField(max_length=10)
    cal_op_curr = models.CharField(max_length=10)
    mop_current = models.CharField(max_length=10)
    error = models.CharField(max_length=10)
    ins_id = models.CharField(max_length=100)
    results = models.CharField(max_length=10)
    createdby = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    no = models.IntegerField()
    enter_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'cal_5'


class Cal6(models.Model):
    cal_for = models.CharField(max_length=20)
    order_no = models.CharField(max_length=20)
    mat_code = models.CharField(max_length=20)
    sl_no = models.IntegerField()
    unit_sl = models.CharField(max_length=10)
    mvstb = models.CharField(max_length=10)
    mip_voltage = models.CharField(max_length=10)
    cal_op_curr = models.CharField(max_length=10)
    mop_current = models.CharField(max_length=10)
    cop_current = models.CharField(max_length=20)
    error = models.CharField(max_length=10)
    ins_id = models.CharField(max_length=100)
    results = models.CharField(max_length=10)
    createdby = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    no = models.IntegerField()
    enter_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'cal_6'


class CalerderMstr(models.Model):
    date = models.DateField()
    week = models.CharField(max_length=20)
    rmrks = models.CharField(max_length=50)
    type = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'calerder_mstr'


class CalibAttachements(models.Model):
    rqst_no = models.IntegerField()
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=40)
    size = models.CharField(max_length=20)
    data = models.TextField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'calib_attachements'


class CalibData(models.Model):
    uniq_slno = models.IntegerField()
    response = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'calib_data'


class CalibDetails(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    medha_slno = models.CharField(max_length=50, blank=True, null=True)
    inst_type = models.IntegerField()
    make = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    rec_date = models.DateField()
    cal_type = models.CharField(max_length=20, blank=True, null=True)
    desc = models.TextField()
    asset_no = models.CharField(max_length=20, blank=True, null=True)
    manuf_slno = models.CharField(max_length=40, blank=True, null=True)
    specifications = models.CharField(max_length=100, blank=True, null=True)
    po = models.CharField(max_length=100, blank=True, null=True)
    warranty = models.CharField(max_length=11, blank=True, null=True)
    adj_pro = models.CharField(max_length=20, blank=True, null=True)
    certifi = models.CharField(max_length=20, blank=True, null=True)
    user_manul = models.CharField(max_length=20, blank=True, null=True)
    ser_manul = models.CharField(max_length=20, blank=True, null=True)
    accessor = models.CharField(max_length=20, blank=True, null=True)
    gauge_type = models.IntegerField()
    period = models.IntegerField()
    response = models.IntegerField()
    cal_date = models.DateField()
    phy_ava = models.CharField(max_length=20, blank=True, null=True)
    calib_date = models.DateField()
    cal_pr_no = models.CharField(max_length=30, blank=True, null=True)
    cal_pr_no_rev = models.IntegerField()
    sfno = models.CharField(max_length=15, blank=True, null=True)
    sfno_rev = models.IntegerField()
    created_by = models.CharField(max_length=6)
    ntry_date = models.DateField()
    cal_due_date = models.DateField()
    shuffle_not = models.IntegerField()
    response_date = models.DateField()
    usr_reason = models.CharField(max_length=100, blank=True, null=True)
    calib_reason = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField()
    received = models.IntegerField()
    scrap_comm = models.CharField(max_length=200, blank=True, null=True)
    delete1 = models.IntegerField()
    company = models.IntegerField()
    calib_attachment = models.CharField(max_length=5000, blank=True, null=True)
    maindate = models.DateField()
    assign_to = models.CharField(max_length=6, blank=True, null=True)
    stand_time = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    calib_attachment_pre = models.CharField(max_length=100, blank=True, null=True)
    external_status = models.IntegerField()
    ext2int_data_transfer = models.IntegerField()
    grno = models.CharField(max_length=30, blank=True, null=True)
    grn_date = models.CharField(max_length=15, blank=True, null=True)
    supplier = models.CharField(max_length=40, blank=True, null=True)
    range = models.CharField(max_length=70, blank=True, null=True)
    resolution = models.CharField(max_length=50, blank=True, null=True)
    accuracy = models.CharField(max_length=10, blank=True, null=True)
    attachments = models.CharField(max_length=30, blank=True, null=True)
    crimptool = models.CharField(max_length=500, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    loc = models.CharField(max_length=5, blank=True, null=True)
    yell_txt_sts = models.IntegerField()
    standard = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'calib_details'


class CalibDetailsExt(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    medha_slno = models.CharField(max_length=30)
    make = models.CharField(max_length=10)
    model = models.CharField(max_length=11)
    desc = models.TextField()
    cal_type = models.CharField(max_length=20)
    specifications = models.CharField(max_length=100)
    response = models.IntegerField()
    cal_date = models.DateField()
    phy_ava = models.CharField(max_length=20)
    cal_due_date = models.DateField()
    external_status = models.IntegerField()
    external_user = models.CharField(max_length=7)
    ext2int_data_transfer = models.IntegerField()
    dailymailstatus = models.IntegerField()
    childref = models.IntegerField()
    external_comment = models.TextField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'calib_details_ext'


class CalibDetailsHistory(models.Model):
    uniq_slno = models.IntegerField()
    cal_date = models.DateField()
    cal_due_date_old = models.DateField()
    cal_due_date_new = models.DateField()
    cer_no = models.CharField(max_length=100, blank=True, null=True)
    sts = models.CharField(max_length=20, blank=True, null=True)
    calib_reason = models.CharField(max_length=100, blank=True, null=True)
    ntry_by = models.CharField(max_length=6, blank=True, null=True)
    yell_txt = models.CharField(max_length=200, blank=True, null=True)
    calibby = models.CharField(max_length=50, blank=True, null=True)
    impact_sts = models.IntegerField()
    impact_assoc = models.IntegerField()
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    sf_308_sts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'calib_details_history'


class CalibDetailsOld(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    medha_slno = models.CharField(max_length=50, blank=True, null=True)
    inst_type = models.IntegerField()
    make = models.CharField(max_length=10, blank=True, null=True)
    model = models.CharField(max_length=11, blank=True, null=True)
    rec_date = models.DateField()
    cal_type = models.CharField(max_length=20, blank=True, null=True)
    desc = models.TextField()
    asset_no = models.CharField(max_length=20, blank=True, null=True)
    manuf_slno = models.CharField(max_length=15, blank=True, null=True)
    specifications = models.CharField(max_length=100, blank=True, null=True)
    po = models.CharField(max_length=100, blank=True, null=True)
    warranty = models.CharField(max_length=11, blank=True, null=True)
    adj_pro = models.CharField(max_length=20, blank=True, null=True)
    certifi = models.CharField(max_length=20, blank=True, null=True)
    user_manul = models.CharField(max_length=20, blank=True, null=True)
    ser_manul = models.CharField(max_length=20, blank=True, null=True)
    accessor = models.CharField(max_length=20, blank=True, null=True)
    gauge_type = models.IntegerField()
    period = models.IntegerField()
    response = models.IntegerField()
    cal_date = models.DateField()
    phy_ava = models.CharField(max_length=20, blank=True, null=True)
    calib_date = models.DateField()
    cal_pr_no = models.CharField(max_length=30, blank=True, null=True)
    cal_pr_no_rev = models.IntegerField()
    sfno = models.CharField(max_length=12, blank=True, null=True)
    sfno_rev = models.IntegerField()
    created_by = models.CharField(max_length=6)
    ntry_date = models.DateField()
    cal_due_date = models.DateField()
    shuffle_not = models.IntegerField()
    response_date = models.DateField()
    usr_reason = models.CharField(max_length=100, blank=True, null=True)
    calib_reason = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField()
    received = models.IntegerField()
    scrap_comm = models.CharField(max_length=200, blank=True, null=True)
    delete1 = models.IntegerField()
    company = models.IntegerField()
    calib_attachment = models.CharField(max_length=5000, blank=True, null=True)
    maindate = models.DateField()
    assign_to = models.CharField(max_length=6, blank=True, null=True)
    stand_time = models.IntegerField()
    calib_attachment_pre = models.CharField(max_length=100, blank=True, null=True)
    external_status = models.IntegerField()
    ext2int_data_transfer = models.IntegerField()
    grno = models.CharField(max_length=30, blank=True, null=True)
    grn_date = models.CharField(max_length=15, blank=True, null=True)
    supplier = models.CharField(max_length=40, blank=True, null=True)
    range = models.CharField(max_length=15, blank=True, null=True)
    resolution = models.CharField(max_length=20, blank=True, null=True)
    accuracy = models.CharField(max_length=10, blank=True, null=True)
    attachments = models.CharField(max_length=30, blank=True, null=True)
    crimptool = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calib_details_old'


class CalibGaugeMaster(models.Model):
    gua_id = models.AutoField(primary_key=True)
    guage = models.CharField(max_length=10)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'calib_gauge_master'


class CalibGuageDetails(models.Model):
    guid = models.AutoField(primary_key=True)
    uniq_slno = models.IntegerField()
    guage_type = models.CharField(max_length=30, blank=True, null=True)
    guage_desc = models.CharField(max_length=17, blank=True, null=True)
    createdby = models.CharField(max_length=6, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'calib_guage_details'


class CalibImpact(models.Model):
    uniq_slno = models.IntegerField()
    impact_stage = models.IntegerField()
    impa_comm = models.CharField(max_length=100, blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    correct = models.CharField(max_length=50, blank=True, null=True)
    respon = models.IntegerField()
    target_date = models.DateField()
    createdby = models.IntegerField()
    ntry_date = models.DateField()
    hod = models.IntegerField()
    hod_sts = models.IntegerField()
    hod_date = models.DateField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'calib_impact'


class CalibInstrMstr(models.Model):
    ins_id = models.AutoField(primary_key=True)
    instrument = models.CharField(max_length=100)
    company = models.IntegerField()
    loc = models.CharField(max_length=5, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'calib_instr_mstr'


class CalibMailRespMaster(models.Model):
    slno = models.AutoField(primary_key=True)
    dept = models.CharField(max_length=20)
    empcode = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'calib_mail_resp_master'


class CalibMedhaslnoMaster(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    medha_slno = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'calib_medhaslno_master'


class CalibPhyMaster(models.Model):
    pid = models.AutoField(primary_key=True)
    phy_ava = models.CharField(max_length=30)
    show = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'calib_phy_master'


class CalibPspmEntry(models.Model):
    pspmno = models.CharField(max_length=50, blank=True, null=True)
    manufacture = models.CharField(max_length=50, blank=True, null=True)
    rangeval = models.IntegerField(blank=True, null=True)
    make = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    response = models.IntegerField(blank=True, null=True)
    userloc = models.CharField(max_length=50, blank=True, null=True)
    verified_date = models.DateField()
    nxt_review_date = models.DateField()
    observations = models.TextField(blank=True, null=True)
    comments = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'calib_pspm_entry'


class CalibPspmHistory(models.Model):
    hid = models.AutoField(primary_key=True)
    id = models.IntegerField()
    response = models.IntegerField(blank=True, null=True)
    userloc = models.CharField(max_length=50, blank=True, null=True)
    verified_date = models.DateField()
    nxt_review_date = models.DateField()
    observations = models.TextField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'calib_pspm_history'


class CalibPspmMakesMstr(models.Model):
    make = models.CharField(max_length=50, blank=True, null=True)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'calib_pspm_makes_mstr'


class CalibPspmRangesMstr(models.Model):
    rangeval = models.CharField(max_length=50, blank=True, null=True)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'calib_pspm_ranges_mstr'


class CalibReasonForReturn(models.Model):
    rqst_no = models.IntegerField()
    desc_of_problem = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    slno = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'calib_reason_for_return'


class CalibRepairHis(models.Model):
    his_id = models.AutoField(primary_key=True)
    rep_id = models.IntegerField()
    uniq_slno = models.IntegerField()
    his_comm = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField()
    cate_r_s = models.CharField(max_length=6)
    app_hod = models.IntegerField()
    his_date = models.DateField()
    delete1 = models.IntegerField()
    scrap_comm = models.CharField(max_length=100, blank=True, null=True)
    scrap_date = models.DateField()
    scrap_by = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'calib_repair_his'


class CalibRepairNtry(models.Model):
    rep_id = models.AutoField(primary_key=True)
    uniq_slno = models.IntegerField()
    rep_rsn = models.CharField(max_length=500, blank=True, null=True)
    make = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    rep_type = models.IntegerField()
    ntry_date = models.DateField()
    ntry_by = models.IntegerField()
    rmks = models.CharField(max_length=300, blank=True, null=True)
    repair_cost = models.IntegerField()
    repair_time = models.IntegerField()
    status = models.IntegerField()
    repair_by = models.IntegerField()
    repair_date = models.DateField()
    int_ext = models.CharField(max_length=10, blank=True, null=True)
    cmpl_days = models.IntegerField()
    caldeptacc = models.CharField(max_length=30, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'calib_repair_ntry'


class CalibRepairNtry31102022(models.Model):
    rep_id = models.AutoField(primary_key=True)
    uniq_slno = models.IntegerField()
    rep_rsn = models.CharField(max_length=500, blank=True, null=True)
    make = models.CharField(max_length=10, blank=True, null=True)
    model = models.CharField(max_length=11, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    rep_type = models.IntegerField()
    ntry_date = models.DateField()
    ntry_by = models.IntegerField()
    rmks = models.CharField(max_length=300, blank=True, null=True)
    repair_cost = models.IntegerField()
    repair_time = models.IntegerField()
    status = models.IntegerField()
    repair_by = models.IntegerField()
    repair_date = models.DateField()
    int_ext = models.CharField(max_length=10, blank=True, null=True)
    cmpl_days = models.IntegerField()
    caldept_acceptance = models.CharField(db_column='Caldept_Acceptance', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'calib_repair_ntry_31_10_2022'


class CalibUsrNtry(models.Model):
    rqst_no = models.AutoField(primary_key=True)
    rqstd = models.IntegerField()
    rqstd_date = models.DateField()
    dept = models.IntegerField()
    uniq_slno_medha = models.IntegerField()
    any_accessories = models.CharField(max_length=1000)
    rqst_type = models.CharField(max_length=1)
    rqst_no_old = models.IntegerField()
    hod_sts = models.IntegerField()
    is_inst = models.CharField(max_length=1)
    hod_date = models.DateField()
    hod = models.IntegerField()
    hod_rej_rsn = models.CharField(max_length=500)
    service_charges = models.FloatField()
    parts_cost = models.FloatField()
    calib_cost = models.FloatField()
    remarks_by_calib = models.CharField(max_length=500)
    pay_rs = models.FloatField()
    pay_emp = models.IntegerField()
    calib_ntryby = models.IntegerField()
    calib_ntrydate = models.DateField()
    paid_sts = models.CharField(max_length=10)
    paid_by = models.IntegerField()
    paid_date = models.DateField()
    inst_sts = models.CharField(max_length=10)
    inst_hndover = models.IntegerField()
    inst_hndover_date = models.DateField()
    delete1 = models.IntegerField()
    attachment_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    comments = models.CharField(max_length=100)
    cal_type = models.IntegerField()
    cal_extranal = models.IntegerField()
    gl_tl = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'calib_usr_ntry'


class CanteenMembers(models.Model):
    empname = models.CharField(max_length=60)
    desg = models.CharField(max_length=60)
    dept = models.CharField(max_length=50)
    add = models.CharField(max_length=20)
    loc = models.IntegerField()
    delete1 = models.IntegerField()
    empcode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'canteen_members'


class CardLevelEntry(models.Model):
    from_field = models.CharField(db_column='from', max_length=10, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=11, blank=True, null=True)
    reference = models.CharField(max_length=11, blank=True, null=True)
    product_code = models.CharField(max_length=10, blank=True, null=True)
    subproject = models.CharField(max_length=150, blank=True, null=True)
    materialcode = models.CharField(max_length=15, blank=True, null=True)
    shorttext = models.CharField(max_length=150, blank=True, null=True)
    ecrdata = models.CharField(db_column='ecrData', max_length=50, blank=True, null=True)  # Field name made lowercase.
    refsubcategory = models.CharField(max_length=20, blank=True, null=True)
    modificationdetails = models.TextField(db_column='modificationDetails', blank=True, null=True)  # Field name made lowercase.
    stickerdetails = models.TextField(db_column='stickerDetails', blank=True, null=True)  # Field name made lowercase.
    details = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    date = models.DateField()
    scope = models.CharField(max_length=50, blank=True, null=True)
    software = models.CharField(max_length=100)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    mailids = models.CharField(max_length=150, blank=True, null=True)
    resonmodification = models.CharField(max_length=150, blank=True, null=True)
    campatability = models.CharField(max_length=150, blank=True, null=True)
    mutipleproducts = models.CharField(max_length=150, blank=True, null=True)
    unitlevel = models.CharField(max_length=150, blank=True, null=True)
    attachment = models.CharField(max_length=150, blank=True, null=True)
    revno = models.CharField(max_length=11, blank=True, null=True)
    moved_internet = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'card_level_entry'


class CatMaster(models.Model):
    cat_code = models.AutoField(primary_key=True)
    cat_desc = models.CharField(max_length=100)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cat_master'


class CcatMaster(models.Model):
    ccat_no = models.AutoField(primary_key=True)
    ccat_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ccat_master'


class CertCategoryMaster(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=50, blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cert_category_master'


class ChatMsgData(models.Model):
    sender = models.IntegerField()
    receiver = models.CharField(max_length=11)
    msg = models.TextField()
    date = models.DateField()
    sender_ip = models.CharField(max_length=15)
    reciever_ip = models.CharField(max_length=15)
    time = models.TimeField()
    type = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'chat_msg_data'


class ChatUserLogin(models.Model):
    empcode = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    cookie_id = models.CharField(max_length=50)
    ip = models.CharField(max_length=15)
    server_name = models.CharField(max_length=30)
    status = models.IntegerField()
    login_time = models.TimeField()
    logout_time = models.TimeField()
    xtra_field = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chat_user_login'


class CiSessions(models.Model):
    session_id = models.CharField(primary_key=True, max_length=40)
    ip_address = models.CharField(max_length=45)
    user_agent = models.CharField(max_length=120)
    last_activity = models.PositiveIntegerField()
    user_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'ci_sessions'


class CipRegistration(models.Model):
    regid = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    dept = models.IntegerField()
    loc = models.CharField(max_length=10)
    title = models.TextField(blank=True, null=True)
    improvement = models.TextField(blank=True, null=True)
    justification = models.TextField(blank=True, null=True)
    regdate = models.DateTimeField()
    startdate = models.DateField()
    targetdate = models.DateField()
    delete1 = models.IntegerField()
    improvement_category = models.CharField(max_length=50, blank=True, null=True)
    final_date = models.CharField(max_length=20, blank=True, null=True)
    hodapproved = models.IntegerField()
    hod = models.IntegerField()
    horizantal = models.CharField(max_length=1)
    cip_ppt = models.CharField(max_length=100, blank=True, null=True)
    cip_ppt_name = models.CharField(max_length=250, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cip_registration'


class CipTeamMom(models.Model):
    cip_id = models.AutoField(primary_key=True)
    regid = models.CharField(max_length=4)
    cip_empcode = models.CharField(max_length=10)
    cip_atta = models.CharField(max_length=100)
    cip_type = models.CharField(max_length=4)
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cip_team_mom'


class CncNtry(models.Model):
    slno = models.IntegerField()
    machine_name = models.IntegerField()
    pcb_name = models.CharField(max_length=500)
    material_number = models.CharField(max_length=12)
    project = models.CharField(max_length=50)
    program_name = models.CharField(max_length=500)
    revision_date = models.CharField(max_length=200)
    created = models.IntegerField()
    timestamp = models.DateTimeField(blank=True, null=True)
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cnc_ntry'


class ColorCodesMaster(models.Model):
    color_name = models.CharField(max_length=20)
    color_code = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'color_codes_master'


class CommonExtnMaster(models.Model):
    title = models.CharField(max_length=50)
    num = models.CharField(max_length=30)
    loc = models.CharField(max_length=4)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'common_extn_master'


class CompanycodeMaster(models.Model):
    code = models.IntegerField(primary_key=True)
    companyname = models.CharField(max_length=50, blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'companycode_master'


class CourierMaster(models.Model):
    cid = models.AutoField(primary_key=True)
    courier_name = models.CharField(max_length=100)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'courier_master'


class CronjobAuth(models.Model):
    slno = models.AutoField(primary_key=True)
    cid = models.IntegerField()
    empcode = models.IntegerField()
    date = models.DateField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cronjob_auth'


class CronjobMaster(models.Model):
    cid = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    deptcode = models.CharField(max_length=10, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cronjob_master'


class Customer(models.Model):
    cust_code = models.CharField(primary_key=True, max_length=10)
    cust_name = models.CharField(max_length=35)
    city = models.CharField(max_length=35)
    createdby = models.CharField(max_length=10)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerAttch(models.Model):
    customer_id = models.IntegerField()
    attachments = models.TextField(blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer_attch'


class CustomerOrders(models.Model):
    register_date = models.DateField()
    ship_to_party = models.CharField(max_length=100, blank=True, null=True)
    material_code = models.CharField(max_length=20, blank=True, null=True)
    shipping_center = models.CharField(max_length=4, blank=True, null=True)
    serial_num = models.IntegerField()
    inc_ncr = models.CharField(max_length=35, blank=True, null=True)
    warranty = models.IntegerField()
    inc_ncr_date = models.DateField()
    quantity = models.IntegerField()
    uom = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)
    sale_order_num = models.CharField(max_length=10, blank=True, null=True)
    sale_order_sts = models.CharField(max_length=1)
    raised_by = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    dob_test = models.DateField()

    class Meta:
        managed = False
        db_table = 'customer_orders'


class DeptForms(models.Model):
    formname = models.CharField(max_length=50)
    deptname = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'dept_forms'


class DeptHighpriorityMaster(models.Model):
    dept_code = models.CharField(max_length=10)
    quota_year = models.IntegerField()
    final_quota = models.IntegerField()
    dept_head_code = models.IntegerField()
    created_date = models.DateField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dept_highpriority_master'


class DeptMaster(models.Model):
    deptcode = models.IntegerField()
    deptname = models.CharField(max_length=50, blank=True, null=True)
    dept_mail = models.CharField(max_length=100, blank=True, null=True)
    sap_dept_code = models.IntegerField(blank=True, null=True)
    hod = models.IntegerField()
    dept_nickname = models.CharField(max_length=15, blank=True, null=True)
    production_type = models.CharField(max_length=1)
    loc = models.CharField(max_length=4, blank=True, null=True)
    company_id = models.IntegerField()
    identification_code = models.CharField(max_length=10, blank=True, null=True)
    createdby = models.CharField(max_length=40, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    max_priority_tags = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dept_master'


class DeptMaster27092022(models.Model):
    deptcode = models.IntegerField()
    deptname = models.CharField(max_length=50, blank=True, null=True)
    dept_mail = models.CharField(max_length=100, blank=True, null=True)
    sap_dept_code = models.IntegerField(blank=True, null=True)
    hod = models.IntegerField()
    dept_nickname = models.CharField(max_length=15, blank=True, null=True)
    production_type = models.CharField(max_length=1)
    loc = models.CharField(max_length=4, blank=True, null=True)
    company_id = models.IntegerField()
    identification_code = models.CharField(max_length=10, blank=True, null=True)
    createdby = models.CharField(max_length=40, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    max_priority_tags = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dept_master_27_09_2022'


class DeptMasterOld(models.Model):
    deptcode = models.IntegerField()
    deptname = models.CharField(max_length=50, blank=True, null=True)
    dept_mail = models.CharField(max_length=100)
    sap_dept_code = models.IntegerField()
    hod = models.IntegerField()
    dept_nickname = models.CharField(max_length=15)
    production_type = models.CharField(max_length=1)
    loc = models.CharField(max_length=4)
    company_id = models.IntegerField()
    identification_code = models.CharField(max_length=10)
    createdby = models.CharField(max_length=40, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    max_priority_tags = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dept_master_old'


class Designation(models.Model):
    designation_code = models.AutoField(primary_key=True)
    designation_name = models.CharField(max_length=50)
    createdby = models.CharField(max_length=40, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'designation'


class Designation23223(models.Model):
    designation_code = models.AutoField(primary_key=True)
    designation_name = models.CharField(max_length=50)
    createdby = models.CharField(max_length=40, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'designation_23_2_23'


class Designation27092022(models.Model):
    designation_code = models.AutoField(primary_key=True)
    designation_name = models.CharField(max_length=50)
    createdby = models.CharField(max_length=40, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'designation_27_09_2022'


class DesignationOld(models.Model):
    designation_code = models.AutoField(primary_key=True)
    designation_name = models.CharField(max_length=50)
    createdby = models.CharField(max_length=40, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'designation_old'


class DetailedInspection(models.Model):
    docno = models.CharField(max_length=20)
    postingdate = models.DateField(blank=True, null=True)
    qtyreceived = models.PositiveIntegerField(blank=True, null=True)
    vendor = models.CharField(max_length=8, blank=True, null=True)
    docbatchno = models.IntegerField(primary_key=True)
    materialcode = models.CharField(max_length=20)
    potext = models.CharField(max_length=500)
    upld_date = models.DateField()
    reqpackage = models.CharField(max_length=50, blank=True, null=True)
    receivedmpn = models.CharField(max_length=30, blank=True, null=True)
    rcdmfr = models.CharField(max_length=30, blank=True, null=True)
    rcdpackage = models.CharField(max_length=50, blank=True, null=True)
    appmfr = models.CharField(max_length=100, blank=True, null=True)
    receivedmfr = models.CharField(max_length=100, blank=True, null=True)
    batchno = models.CharField(max_length=50, blank=True, null=True)
    datecode = models.CharField(max_length=100)
    rpercentage = models.FloatField()
    make = models.CharField(max_length=50, blank=True, null=True)
    passiveburnin = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    sign = models.CharField(max_length=50, blank=True, null=True)
    refigi = models.CharField(max_length=30, blank=True, null=True)
    qualityofpart = models.CharField(max_length=50, blank=True, null=True)
    esdpacking = models.CharField(max_length=5, blank=True, null=True)
    instslno = models.CharField(max_length=150)
    qtyaccepted = models.CharField(max_length=8, blank=True, null=True)
    qtyrejected = models.CharField(max_length=8, blank=True, null=True)
    inspectedby = models.CharField(max_length=40, blank=True, null=True)
    approvedby = models.CharField(max_length=40, blank=True, null=True)
    inspecteddate = models.DateField(blank=True, null=True)
    approveddate = models.DateField(blank=True, null=True)
    finalsave = models.CharField(max_length=5)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=10)
    createdby = models.BigIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    note = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'detailed_inspection'
        unique_together = (('docbatchno', 'docno', 'materialcode'),)


class Detailedfcheck(models.Model):
    docno = models.CharField(max_length=20)
    sfcode = models.CharField(max_length=30, blank=True, null=True)
    specified = models.CharField(max_length=200, blank=True, null=True)
    observed = models.CharField(max_length=200, blank=True, null=True)
    qtyinspected = models.FloatField(blank=True, null=True)
    qtyaccepted = models.FloatField(blank=True, null=True)
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()
    qtyrejected = models.FloatField()
    materialcode = models.CharField(max_length=20)
    docbtch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detailedfcheck'


class Detailedpcheck(models.Model):
    docno = models.CharField(max_length=20, blank=True, null=True)
    sfcode = models.CharField(max_length=30, blank=True, null=True)
    specified = models.CharField(max_length=200, blank=True, null=True)
    observed = models.CharField(max_length=200, blank=True, null=True)
    qtyinspected = models.FloatField(blank=True, null=True)
    qtyaccepted = models.FloatField(blank=True, null=True)
    qtyrejected = models.FloatField(blank=True, null=True)
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()
    materialcode = models.CharField(max_length=20)
    docbtch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detailedpcheck'


class DigitalSignDocs(models.Model):
    slno = models.AutoField(primary_key=True)
    signed_empcode = models.IntegerField()
    signed_flname = models.CharField(max_length=500)
    signed_by = models.CharField(max_length=500)
    module_name = models.CharField(max_length=100)
    date = models.DateField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'digital_sign_docs'


class DisposalActionMaster(models.Model):
    dsp_no = models.AutoField(primary_key=True)
    dsp_name = models.CharField(max_length=50)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'disposal_action_master'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DocsDispatchGroupMaster(models.Model):
    loccode = models.CharField(max_length=20)
    empcode = models.IntegerField()
    active = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'docs_dispatch_group_master'


class DocsDispatchMailTimeMaster(models.Model):
    slno = models.AutoField(primary_key=True)
    time = models.CharField(max_length=10)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'docs_dispatch_mail_time_master'


class DocsDispatchModTransMaster(models.Model):
    trans_mod_no = models.AutoField(primary_key=True)
    trans_mod_name = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'docs_dispatch_mod_trans_master'


class DocsDispatchNtry(models.Model):
    slno = models.AutoField(primary_key=True)
    doc_slno = models.CharField(max_length=20)
    date = models.DateField()
    sender = models.IntegerField()
    desc = models.CharField(max_length=500)
    pack_no = models.IntegerField()
    trans_mod_no = models.IntegerField()
    mod_code_name = models.IntegerField()
    recipient_rcvd_timestamp = models.CharField(max_length=20)
    originate = models.CharField(max_length=15)
    destination = models.CharField(max_length=15)
    status = models.IntegerField()
    timestamp = models.CharField(max_length=25)
    van_sender = models.IntegerField()
    van_time = models.IntegerField()
    van_time_actu_send = models.CharField(max_length=20)
    trip_type = models.CharField(max_length=1)
    trip_slno = models.IntegerField()
    van_recip_sts = models.IntegerField()
    van_recipient = models.IntegerField()
    van_time_actu_recipient = models.CharField(max_length=20)
    van_send2_actu_recipient = models.CharField(max_length=20)
    van_docs_rcvd_sts = models.IntegerField()
    van_docs_rcvd_timestamp = models.CharField(max_length=20)
    van_docs_rcvd_by = models.IntegerField()
    van_docs_rcvd_sts2 = models.IntegerField()
    van_docs_rcvd_timestamp2 = models.CharField(max_length=20)
    van_docs_rcvd_by2 = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'docs_dispatch_ntry'


class DocsDispatchPackingMaster(models.Model):
    pack_no = models.AutoField(primary_key=True)
    pack_name = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'docs_dispatch_packing_master'


class DocsDispatchStatusMaster(models.Model):
    status = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'docs_dispatch_status_master'


class DrawingCategory(models.Model):
    category = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=150)
    code = models.CharField(max_length=10)
    type = models.IntegerField()
    userid = models.IntegerField()
    delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_category'


class DrawingComments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    drawingid = models.IntegerField()
    dwg_doc_id = models.IntegerField()
    dwg_received = models.IntegerField()
    creater = models.CharField(max_length=50)
    checker = models.CharField(max_length=10)
    approver = models.CharField(max_length=10)
    comment = models.CharField(max_length=100)
    date = models.DateTimeField()
    empcode = models.IntegerField()
    version_no = models.CharField(max_length=10)
    release_no = models.CharField(max_length=10)
    cmnts_extra_status = models.IntegerField()
    cmnts_extra_dnwldtime = models.DateTimeField()
    moved_toexternal = models.IntegerField()
    moved_to_datetime = models.DateTimeField()
    created_by = models.IntegerField()
    delete1 = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'drawing_comments'


class DrawingComments02122020(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    drawingid = models.IntegerField()
    dwg_doc_id = models.IntegerField()
    dwg_received = models.IntegerField()
    creater = models.CharField(max_length=50)
    checker = models.CharField(max_length=10)
    approver = models.CharField(max_length=10)
    comment = models.CharField(max_length=100)
    date = models.DateTimeField()
    empcode = models.IntegerField()
    version_no = models.CharField(max_length=10)
    release_no = models.CharField(max_length=10)
    cmnts_extra_status = models.IntegerField()
    cmnts_extra_dnwldtime = models.DateTimeField()
    moved_toexternal = models.IntegerField()
    moved_to_datetime = models.DateTimeField()
    created_by = models.IntegerField()
    delete1 = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'drawing_comments_02_12_2020'


class DrawingComments30122020(models.Model):
    comment_id = models.AutoField(primary_key=True)
    drawingid = models.IntegerField()
    dwg_doc_id = models.IntegerField()
    dwg_received = models.IntegerField()
    creater = models.CharField(max_length=50)
    checker = models.CharField(max_length=10)
    approver = models.CharField(max_length=10)
    comment = models.CharField(max_length=100)
    date = models.DateTimeField()
    empcode = models.IntegerField()
    version_no = models.CharField(max_length=10)
    release_no = models.CharField(max_length=10)
    cmnts_extra_status = models.IntegerField()
    cmnts_extra_dnwldtime = models.DateTimeField()
    moved_toexternal = models.IntegerField()
    moved_to_datetime = models.DateTimeField()
    created_by = models.IntegerField()
    delete1 = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'drawing_comments_30_12_2020'


class DrawingCommentsDuro(models.Model):
    comment_id = models.AutoField(primary_key=True)
    drawingid = models.IntegerField()
    dwg_doc_id = models.IntegerField()
    dwg_received = models.IntegerField()
    creater = models.CharField(max_length=50)
    checker = models.CharField(max_length=10)
    approver = models.CharField(max_length=10)
    comment = models.CharField(max_length=100)
    date = models.DateTimeField()
    empcode = models.IntegerField()
    version_no = models.CharField(max_length=10)
    release_no = models.CharField(max_length=10)
    cmnts_extra_status = models.IntegerField()
    cmnts_extra_dnwldtime = models.DateTimeField()
    moved_toexternal = models.IntegerField()
    moved_to_datetime = models.DateTimeField()
    created_by = models.IntegerField()
    delete1 = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'drawing_comments_duro'


class DrawingDcd(models.Model):
    dwg_dept = models.CharField(max_length=25)
    dwg_type = models.IntegerField()
    dwg_empcode = models.IntegerField()
    dwg_mailid = models.CharField(max_length=50)
    dwg_shortcut = models.CharField(max_length=5)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_dcd'


class DrawingDcdbulk(models.Model):
    empcode = models.CharField(max_length=7)
    drawingid = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'drawing_dcdbulk'


class DrawingDeletedCmnts(models.Model):
    ref_id = models.CharField(max_length=50, blank=True, null=True)
    cmnts = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drawing_deleted_cmnts'


class DrawingDoc(models.Model):
    dwg_doc = models.AutoField(primary_key=True)
    dwg_totid = models.IntegerField()
    drawingid = models.IntegerField()
    dwg_doc_id = models.IntegerField()
    doc_required = models.IntegerField()
    dwg_review = models.IntegerField()
    dwg_path = models.CharField(max_length=150)
    dwg_review_code = models.IntegerField()
    dwg_release = models.IntegerField()
    dwg_verifier = models.IntegerField()
    dwg_verifier_code = models.IntegerField()
    dwg_approval = models.IntegerField()
    dwg_approval_empcode = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    emp_come1 = models.CharField(max_length=10)
    deleted_by = models.IntegerField()
    softcopy_type = models.IntegerField()
    recevied_veri_date = models.DateField()
    download_sts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_doc'


class DrawingEntry(models.Model):
    drawingid = models.IntegerField(primary_key=True)
    unit_no = models.IntegerField()
    drawingname = models.CharField(max_length=40)
    projectid = models.IntegerField()
    projectname = models.CharField(max_length=100)
    sizetype = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    stdpart = models.CharField(max_length=10)
    sapcode = models.CharField(max_length=10)
    dept = models.IntegerField()
    empcode = models.IntegerField()
    sendto = models.IntegerField()
    checkercode = models.IntegerField()
    approvercode = models.IntegerField()
    date = models.DateTimeField()
    saveddate = models.CharField(max_length=20)
    createrstatus = models.IntegerField()
    checkerstatus = models.IntegerField()
    approverstatus = models.IntegerField()
    ecr_no = models.CharField(max_length=20)
    version_no = models.CharField(max_length=10)
    release_no = models.CharField(max_length=10)
    totstatus = models.IntegerField()
    finallinkone = models.CharField(max_length=100)
    finallinktwo = models.CharField(max_length=100)
    finallinkdd = models.CharField(max_length=100)
    finallinkthree = models.CharField(max_length=100)
    final = models.CharField(max_length=50)
    sapfinal = models.CharField(max_length=20)
    uploadeduser = models.IntegerField()
    category = models.IntegerField()
    comment = models.CharField(max_length=100)
    me_list = models.CharField(max_length=1)
    pre = models.CharField(max_length=3)
    pri = models.CharField(max_length=3)
    top = models.CharField(max_length=3)
    extra_status = models.IntegerField()
    extra_dnwldtime = models.DateTimeField()
    ip_type = models.IntegerField()
    moved_toexternal = models.IntegerField()
    moved_to_datetime = models.DateTimeField()
    attch_toexternal = models.IntegerField()
    attch_dttime_toexternal = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_entry'


class DrawingEntry07112020(models.Model):
    drawingid = models.AutoField(primary_key=True)
    unit_no = models.IntegerField()
    drawingname = models.CharField(max_length=40)
    projectid = models.IntegerField()
    projectname = models.CharField(max_length=100)
    sizetype = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    stdpart = models.CharField(max_length=10)
    sapcode = models.CharField(max_length=10)
    dept = models.IntegerField()
    empcode = models.IntegerField()
    sendto = models.IntegerField()
    checkercode = models.IntegerField()
    approvercode = models.IntegerField()
    date = models.DateTimeField()
    saveddate = models.CharField(max_length=20)
    createrstatus = models.IntegerField()
    checkerstatus = models.IntegerField()
    approverstatus = models.IntegerField()
    ecr_no = models.CharField(max_length=20)
    version_no = models.CharField(max_length=10)
    release_no = models.CharField(max_length=10)
    totstatus = models.IntegerField()
    finallinkone = models.CharField(max_length=100)
    finallinktwo = models.CharField(max_length=100)
    finallinkdd = models.CharField(max_length=100)
    finallinkthree = models.CharField(max_length=100)
    final = models.CharField(max_length=50)
    sapfinal = models.CharField(max_length=20)
    uploadeduser = models.IntegerField()
    category = models.IntegerField()
    comment = models.CharField(max_length=100)
    me_list = models.CharField(max_length=1)
    pre = models.CharField(max_length=3)
    pri = models.CharField(max_length=3)
    top = models.CharField(max_length=3)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_entry_07_11_2020'


class DrawingEntry13112020(models.Model):
    drawingid = models.AutoField(primary_key=True)
    unit_no = models.IntegerField()
    drawingname = models.CharField(max_length=40)
    projectid = models.IntegerField()
    projectname = models.CharField(max_length=100)
    sizetype = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    stdpart = models.CharField(max_length=10)
    sapcode = models.CharField(max_length=10)
    dept = models.IntegerField()
    empcode = models.IntegerField()
    sendto = models.IntegerField()
    checkercode = models.IntegerField()
    approvercode = models.IntegerField()
    date = models.DateTimeField()
    saveddate = models.CharField(max_length=20)
    createrstatus = models.IntegerField()
    checkerstatus = models.IntegerField()
    approverstatus = models.IntegerField()
    ecr_no = models.CharField(max_length=20)
    version_no = models.CharField(max_length=10)
    release_no = models.CharField(max_length=10)
    totstatus = models.IntegerField()
    finallinkone = models.CharField(max_length=100)
    finallinktwo = models.CharField(max_length=100)
    finallinkdd = models.CharField(max_length=100)
    finallinkthree = models.CharField(max_length=100)
    final = models.CharField(max_length=50)
    sapfinal = models.CharField(max_length=20)
    uploadeduser = models.IntegerField()
    category = models.IntegerField()
    comment = models.CharField(max_length=100)
    me_list = models.CharField(max_length=1)
    pre = models.CharField(max_length=3)
    pri = models.CharField(max_length=3)
    top = models.CharField(max_length=3)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_entry_13112020'


class DrawingEntryDuro(models.Model):
    drawingid = models.AutoField(primary_key=True)
    unit_no = models.IntegerField()
    drawingname = models.CharField(max_length=40)
    projectid = models.IntegerField()
    projectname = models.CharField(max_length=100)
    sizetype = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    stdpart = models.CharField(max_length=10)
    sapcode = models.CharField(max_length=10)
    dept = models.IntegerField()
    empcode = models.IntegerField()
    sendto = models.IntegerField()
    checkercode = models.IntegerField()
    approvercode = models.IntegerField()
    date = models.DateTimeField()
    saveddate = models.CharField(max_length=20)
    createrstatus = models.IntegerField()
    checkerstatus = models.IntegerField()
    approverstatus = models.IntegerField()
    ecr_no = models.CharField(max_length=20)
    version_no = models.CharField(max_length=10)
    release_no = models.CharField(max_length=10)
    totstatus = models.IntegerField()
    finallinkone = models.CharField(max_length=100)
    finallinktwo = models.CharField(max_length=100)
    finallinkdd = models.CharField(max_length=100)
    finallinkthree = models.CharField(max_length=100)
    final = models.CharField(max_length=50)
    sapfinal = models.CharField(max_length=20)
    uploadeduser = models.IntegerField()
    category = models.IntegerField()
    comment = models.CharField(max_length=100)
    me_list = models.CharField(max_length=1)
    pre = models.CharField(max_length=3)
    pri = models.CharField(max_length=3)
    top = models.CharField(max_length=3)
    extra_status = models.IntegerField()
    extra_dnwldtime = models.DateTimeField()
    ip_type = models.IntegerField()
    moved_toexternal = models.IntegerField()
    moved_to_datetime = models.DateTimeField()
    attch_toexternal = models.IntegerField()
    attch_dttime_toexternal = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_entry_duro'


class DrawingIndexCategorys(models.Model):
    dwg_category_id = models.AutoField(primary_key=True)
    dwg_mcode_id = models.IntegerField()
    active = models.CharField(max_length=1)
    dwg_category_sub = models.CharField(max_length=3)
    dwg_category_value = models.CharField(max_length=50)
    dwg_status = models.CharField(max_length=7)
    dwg_response = models.IntegerField()
    dwg_targetdate = models.DateField()
    dwg_remarks = models.TextField(blank=True, null=True)
    dwg_revno = models.IntegerField()
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'drawing_index_categorys'


class DrawingIndexCodes(models.Model):
    dwg_mcode_id = models.AutoField(primary_key=True)
    dwg_tot_id = models.IntegerField()
    dwg_mcode = models.CharField(max_length=50)
    dwg_category = models.CharField(max_length=50, blank=True, null=True)
    qty = models.IntegerField()
    mqty = models.IntegerField()
    dwg_mcode_ref = models.CharField(max_length=11)
    new_reuse = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_index_codes'


class DrawingReviewEntry(models.Model):
    dwg_review_id = models.AutoField(primary_key=True)
    dwg_tot_id = models.IntegerField()
    project_cft = models.IntegerField()
    cft_type = models.IntegerField()
    dwg_date = models.DateField()
    dwg_from = models.CharField(max_length=6)
    dwg_to = models.CharField(max_length=6)
    dwg_title = models.TextField(blank=True, null=True)
    dwg_agenda = models.TextField(blank=True, null=True)
    dwg_venu = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_review_entry'


class DrawingTot(models.Model):
    dwg_totid = models.AutoField(primary_key=True)
    drawingid = models.IntegerField()
    release_no = models.CharField(max_length=3)
    dwg_doc_id = models.IntegerField()
    dwg_approvded = models.IntegerField()
    dwg_verfication = models.IntegerField()
    dwg_scaned = models.IntegerField()
    dwg_issued = models.IntegerField()
    dwg_received = models.IntegerField()
    dwg_completed = models.IntegerField()
    dwg_timestamp = models.DateTimeField()
    drw_verificationtime = models.DateTimeField()
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'drawing_tot'


class DrawingTot0612(models.Model):
    dwg_totid = models.AutoField(primary_key=True)
    drawingid = models.IntegerField()
    release_no = models.CharField(max_length=3)
    dwg_doc_id = models.IntegerField()
    dwg_approvded = models.IntegerField()
    dwg_verfication = models.IntegerField()
    dwg_scaned = models.IntegerField()
    dwg_issued = models.IntegerField()
    dwg_received = models.IntegerField()
    dwg_completed = models.IntegerField()
    dwg_timestamp = models.DateTimeField()
    drw_verificationtime = models.DateTimeField()
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'drawing_tot_0612'


class DrawingTotAnew(models.Model):
    drawing_no = models.IntegerField()
    doc = models.IntegerField()
    old = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_anew'


class DrawingTotArchitecture(models.Model):
    dwg_acr_id = models.AutoField(primary_key=True)
    dwg_tot_id = models.IntegerField()
    dwg_acr_desc = models.TextField(blank=True, null=True)
    dwg_acr_model = models.IntegerField()
    dwg_engineer_e = models.CharField(max_length=7)
    dwg_engineer_m = models.CharField(max_length=7)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_architecture'


class DrawingTotAttendance(models.Model):
    dwg_tot_id = models.IntegerField()
    dwg_empcode = models.CharField(max_length=7)
    attendance = models.CharField(max_length=4)
    dwg_type = models.CharField(max_length=4)
    project_cft = models.IntegerField()
    cft_type = models.CharField(max_length=4)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_attendance'


class DrawingTotBom(models.Model):
    drawing_bom_id = models.AutoField(primary_key=True)
    drawing_bom_project = models.CharField(max_length=4)
    drawing_bom_main_code = models.CharField(max_length=15)
    assm_drawing = models.CharField(max_length=20)
    me_empcode = models.CharField(max_length=100)
    me_empcode_release = models.CharField(max_length=7)
    drawing_bom_creater = models.CharField(max_length=7)
    mev1 = models.CharField(max_length=7)
    mev2 = models.CharField(max_length=7)
    drawing_bom_date = models.DateTimeField()
    drawing_bom_status = models.CharField(max_length=3)
    drawing_bom_percentage = models.CharField(max_length=2)
    main_loc = models.CharField(max_length=2)
    drawing_tot_bom_latestattachment = models.CharField(max_length=100)
    bomreleaseattachment = models.CharField(max_length=50)
    bom_notes = models.TextField()
    bomtargetdate = models.DateField()
    iteration = models.IntegerField()
    delete1 = models.CharField(max_length=1)
    tvar = models.CharField(max_length=1)
    bom_ntry_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_bom'


class DrawingTotBomFinal(models.Model):
    drawing_bom_fid = models.AutoField(primary_key=True)
    ack_no = models.IntegerField()
    drawing_bom_id = models.CharField(max_length=100)
    drawing_bom_project = models.CharField(max_length=50)
    drawing_bom_project_dummy = models.CharField(max_length=50)
    type = models.IntegerField()
    drawing_bom_main_code = models.CharField(max_length=50)
    drawing_bom_main_desc = models.CharField(max_length=200)
    assm_drawing = models.CharField(max_length=20)
    drawing_bom_items = models.CharField(max_length=100)
    bom_items_draft = models.CharField(max_length=50)
    bom_testcopies = models.CharField(max_length=100)
    bom_items_attachment = models.CharField(max_length=100)
    drawing_bom_created = models.CharField(max_length=6)
    drawing_bom_verifier = models.CharField(max_length=7)
    drawing_bom_verifier1 = models.CharField(max_length=7)
    drawing_bom_approval = models.CharField(max_length=7)
    drawing_bom_status = models.CharField(max_length=2)
    drawing_bom_rev = models.CharField(max_length=50)
    drawing_bom_ecr = models.CharField(max_length=50)
    typeecr = models.IntegerField()
    drawing_bom_finalpdf = models.CharField(max_length=100)
    drawing_bom_timestamp = models.DateTimeField()
    bom_verificationtime = models.DateTimeField()
    timestampupdate = models.DateTimeField()
    delete1 = models.CharField(max_length=1)
    tvar = models.CharField(max_length=1)
    cnote = models.TextField(blank=True, null=True)
    rchange = models.TextField(blank=True, null=True)
    futuredate = models.DateField(db_column='futureDate')  # Field name made lowercase.
    datetype = models.CharField(db_column='dateType', max_length=50)  # Field name made lowercase.
    typesupp = models.CharField(max_length=100)
    bomtype = models.IntegerField()
    bomrefno = models.IntegerField()
    enabledoc = models.IntegerField()
    print_type = models.IntegerField()
    doc_no = models.CharField(max_length=100)
    masterdata = models.IntegerField()
    documentownership = models.CharField(max_length=50)
    doc_revert = models.IntegerField()
    backgrnd_data = models.IntegerField()
    backgrnd_data_datetime = models.DateTimeField()
    response = models.CharField(max_length=50)
    remarks = models.CharField(max_length=50)
    attachment = models.CharField(max_length=50)
    me_review = models.IntegerField()
    review_persons = models.CharField(max_length=500)
    intra_drawing_bom_fid = models.IntegerField()
    internet_move = models.IntegerField()
    internet_pdfmove = models.IntegerField()
    internet_softmove = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_bom_final'


class DrawingTotBomFinal041021(models.Model):
    drawing_bom_fid = models.AutoField(primary_key=True)
    ack_no = models.IntegerField()
    drawing_bom_id = models.CharField(max_length=100)
    drawing_bom_project = models.CharField(max_length=50)
    drawing_bom_project_dummy = models.CharField(max_length=50)
    type = models.IntegerField()
    drawing_bom_main_code = models.CharField(max_length=50)
    drawing_bom_main_desc = models.CharField(max_length=200)
    assm_drawing = models.CharField(max_length=20)
    drawing_bom_items = models.CharField(max_length=100)
    bom_items_draft = models.CharField(max_length=50)
    bom_testcopies = models.CharField(max_length=100)
    bom_items_attachment = models.CharField(max_length=100)
    drawing_bom_created = models.CharField(max_length=6)
    drawing_bom_verifier = models.CharField(max_length=7)
    drawing_bom_verifier1 = models.CharField(max_length=7)
    drawing_bom_approval = models.CharField(max_length=7)
    drawing_bom_status = models.CharField(max_length=2)
    drawing_bom_rev = models.CharField(max_length=10)
    drawing_bom_ecr = models.CharField(max_length=50)
    typeecr = models.IntegerField()
    drawing_bom_finalpdf = models.CharField(max_length=100)
    drawing_bom_timestamp = models.DateTimeField()
    bom_verificationtime = models.DateTimeField()
    timestampupdate = models.DateTimeField()
    delete1 = models.CharField(max_length=1)
    tvar = models.CharField(max_length=1)
    cnote = models.TextField(blank=True, null=True)
    rchange = models.TextField(blank=True, null=True)
    futuredate = models.DateField(db_column='futureDate')  # Field name made lowercase.
    datetype = models.CharField(db_column='dateType', max_length=50)  # Field name made lowercase.
    typesupp = models.CharField(max_length=100)
    bomtype = models.IntegerField()
    bomrefno = models.IntegerField()
    enabledoc = models.IntegerField()
    print_type = models.IntegerField()
    doc_no = models.CharField(max_length=100)
    masterdata = models.IntegerField()
    documentownership = models.CharField(max_length=50)
    doc_revert = models.IntegerField()
    backgrnd_data = models.IntegerField()
    backgrnd_data_datetime = models.DateTimeField()
    response = models.CharField(max_length=50)
    remarks = models.CharField(max_length=50)
    attachment = models.CharField(max_length=50)
    me_review = models.IntegerField()
    review_persons = models.CharField(max_length=500)
    intra_drawing_bom_fid = models.IntegerField()
    internet_move = models.IntegerField()
    internet_pdfmove = models.IntegerField()
    internet_softmove = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_bom_final_04_10_21'


class DrawingTotBomFinal0612(models.Model):
    drawing_bom_fid = models.AutoField(primary_key=True)
    ack_no = models.IntegerField()
    drawing_bom_id = models.CharField(max_length=100)
    drawing_bom_project = models.CharField(max_length=50)
    drawing_bom_project_dummy = models.CharField(max_length=50)
    type = models.IntegerField()
    drawing_bom_main_code = models.CharField(max_length=50)
    drawing_bom_main_desc = models.CharField(max_length=200)
    assm_drawing = models.CharField(max_length=20)
    drawing_bom_items = models.CharField(max_length=100)
    bom_items_draft = models.CharField(max_length=50)
    bom_testcopies = models.CharField(max_length=100)
    bom_items_attachment = models.CharField(max_length=100)
    drawing_bom_created = models.CharField(max_length=7)
    drawing_bom_verifier = models.CharField(max_length=7)
    drawing_bom_verifier1 = models.CharField(max_length=7)
    drawing_bom_approval = models.CharField(max_length=7)
    drawing_bom_status = models.CharField(max_length=2)
    drawing_bom_rev = models.CharField(max_length=10)
    drawing_bom_ecr = models.CharField(max_length=50)
    typeecr = models.IntegerField()
    drawing_bom_finalpdf = models.CharField(max_length=100)
    drawing_bom_timestamp = models.DateTimeField()
    bom_verificationtime = models.DateTimeField()
    timestampupdate = models.DateTimeField()
    delete1 = models.CharField(max_length=1)
    tvar = models.CharField(max_length=1)
    cnote = models.TextField()
    rchange = models.TextField()
    futuredate = models.DateField(db_column='futureDate')  # Field name made lowercase.
    datetype = models.CharField(db_column='dateType', max_length=50)  # Field name made lowercase.
    typesupp = models.CharField(max_length=100)
    bomtype = models.IntegerField()
    bomrefno = models.IntegerField()
    enabledoc = models.IntegerField()
    print_type = models.IntegerField()
    doc_no = models.CharField(max_length=100)
    masterdata = models.IntegerField()
    documentownership = models.CharField(max_length=50)
    doc_revert = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_bom_final_06_12'


class DrawingTotBomFinal2210(models.Model):
    drawing_bom_fid = models.AutoField(primary_key=True)
    ack_no = models.IntegerField()
    drawing_bom_id = models.CharField(max_length=100)
    drawing_bom_project = models.CharField(max_length=50)
    drawing_bom_project_dummy = models.CharField(max_length=50)
    type = models.IntegerField()
    drawing_bom_main_code = models.CharField(max_length=50)
    drawing_bom_main_desc = models.CharField(max_length=200)
    assm_drawing = models.CharField(max_length=20)
    drawing_bom_items = models.CharField(max_length=100)
    bom_items_draft = models.CharField(max_length=50)
    bom_testcopies = models.CharField(max_length=100)
    bom_items_attachment = models.CharField(max_length=100)
    drawing_bom_created = models.CharField(max_length=6)
    drawing_bom_verifier = models.CharField(max_length=7)
    drawing_bom_verifier1 = models.CharField(max_length=7)
    drawing_bom_approval = models.CharField(max_length=7)
    drawing_bom_status = models.CharField(max_length=2)
    drawing_bom_rev = models.CharField(max_length=50)
    drawing_bom_ecr = models.CharField(max_length=50)
    typeecr = models.IntegerField()
    drawing_bom_finalpdf = models.CharField(max_length=100)
    drawing_bom_timestamp = models.DateTimeField()
    bom_verificationtime = models.DateTimeField()
    timestampupdate = models.DateTimeField()
    delete1 = models.CharField(max_length=1)
    tvar = models.CharField(max_length=1)
    cnote = models.TextField(blank=True, null=True)
    rchange = models.TextField(blank=True, null=True)
    futuredate = models.DateField(db_column='futureDate')  # Field name made lowercase.
    datetype = models.CharField(db_column='dateType', max_length=50)  # Field name made lowercase.
    typesupp = models.CharField(max_length=100)
    bomtype = models.IntegerField()
    bomrefno = models.IntegerField()
    enabledoc = models.IntegerField()
    print_type = models.IntegerField()
    doc_no = models.CharField(max_length=100)
    masterdata = models.IntegerField()
    documentownership = models.CharField(max_length=50)
    doc_revert = models.IntegerField()
    backgrnd_data = models.IntegerField()
    backgrnd_data_datetime = models.DateTimeField()
    response = models.CharField(max_length=50)
    remarks = models.CharField(max_length=50)
    attachment = models.CharField(max_length=50)
    me_review = models.IntegerField()
    review_persons = models.CharField(max_length=500)
    intra_drawing_bom_fid = models.IntegerField()
    internet_move = models.IntegerField()
    internet_pdfmove = models.IntegerField()
    internet_softmove = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_bom_final_22_10'


class DrawingTotBomHistory(models.Model):
    bom_history_id = models.AutoField(primary_key=True)
    drawing_bom_id = models.IntegerField()
    bom_status = models.CharField(max_length=5)
    bom_type = models.CharField(max_length=5)
    bom_version = models.CharField(max_length=50)
    noofcopys = models.IntegerField()
    bom_associate = models.CharField(max_length=15)
    type_soft_hard = models.IntegerField()
    no_of_copies = models.IntegerField()
    soft_copy_req = models.IntegerField()
    bom_comment = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()
    doc_input_remarks = models.TextField(blank=True, null=True)
    masterdata = models.IntegerField()
    reqid = models.IntegerField()
    qap_attach = models.CharField(max_length=100)
    associate_init = models.IntegerField()
    accepsts = models.IntegerField()
    replied = models.IntegerField()
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'drawing_tot_bom_history'


class DrawingTotBomHistory041021(models.Model):
    bom_history_id = models.AutoField(primary_key=True)
    drawing_bom_id = models.IntegerField()
    bom_status = models.CharField(max_length=5)
    bom_type = models.CharField(max_length=5)
    bom_version = models.CharField(max_length=50)
    noofcopys = models.IntegerField()
    bom_associate = models.CharField(max_length=15)
    type_soft_hard = models.IntegerField()
    no_of_copies = models.IntegerField()
    soft_copy_req = models.IntegerField()
    bom_comment = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()
    doc_input_remarks = models.TextField(blank=True, null=True)
    masterdata = models.IntegerField()
    reqid = models.IntegerField()
    qap_attach = models.CharField(max_length=100)
    associate_init = models.IntegerField()
    accepsts = models.IntegerField()
    replied = models.IntegerField()
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'drawing_tot_bom_history_04_10_21'


class DrawingTotBomHistory0712(models.Model):
    bom_history_id = models.AutoField(primary_key=True)
    drawing_bom_id = models.IntegerField()
    bom_status = models.CharField(max_length=3)
    bom_type = models.CharField(max_length=1)
    bom_version = models.CharField(max_length=50)
    noofcopys = models.IntegerField()
    bom_associate = models.CharField(max_length=7)
    bom_comment = models.TextField()
    timestamp = models.DateTimeField()
    masterdata = models.IntegerField()
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'drawing_tot_bom_history_0712'


class DrawingTotBomHistory2210(models.Model):
    bom_history_id = models.AutoField(primary_key=True)
    drawing_bom_id = models.IntegerField()
    bom_status = models.CharField(max_length=5)
    bom_type = models.CharField(max_length=5)
    bom_version = models.CharField(max_length=50)
    noofcopys = models.IntegerField()
    bom_associate = models.CharField(max_length=15)
    type_soft_hard = models.IntegerField()
    no_of_copies = models.IntegerField()
    soft_copy_req = models.IntegerField()
    bom_comment = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()
    doc_input_remarks = models.TextField(blank=True, null=True)
    masterdata = models.IntegerField()
    reqid = models.IntegerField()
    qap_attach = models.CharField(max_length=100)
    associate_init = models.IntegerField()
    accepsts = models.IntegerField()
    replied = models.IntegerField()
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'drawing_tot_bom_history_22_10'


class DrawingTotBomItems(models.Model):
    drawing_tot_bom_itemid = models.AutoField(primary_key=True)
    drawing_bom_id = models.IntegerField()
    drawing_tot_bom_code = models.CharField(max_length=15)
    drawing_tot_bom_uom = models.CharField(max_length=10)
    drawing_tot_bom_qty = models.DecimalField(max_digits=10, decimal_places=3)
    drawing_tot_bom_qty_old = models.DecimalField(max_digits=10, decimal_places=3)
    drawing_tot_bom_category = models.CharField(max_length=3)
    drawing_tot_bom_nro = models.CharField(max_length=3)
    drawing_tot_bom_cmt = models.CharField(max_length=100)
    drawing_tot_bom_loc = models.TextField()
    timestamp = models.DateTimeField()
    iteration = models.CharField(max_length=3)
    newchanges = models.IntegerField()
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'drawing_tot_bom_items'


class DrawingTotBomMaterial(models.Model):
    productcode = models.CharField(max_length=15)
    empcode = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'drawing_tot_bom_material'


class DrawingTotCft(models.Model):
    historyid = models.AutoField(primary_key=True)
    dwg_mom_id = models.IntegerField()
    empcode = models.IntegerField()
    doc_details = models.TextField(blank=True, null=True)
    ecr = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'drawing_tot_cft'


class DrawingTotCftGroupmailid(models.Model):
    group_mailid = models.CharField(max_length=100)
    type = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_cft_groupmailid'


class DrawingTotCopyMaster(models.Model):
    docid = models.IntegerField(blank=True, null=True)
    deptid = models.IntegerField()
    type = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_copy_master'


class DrawingTotCpaChecklist(models.Model):
    param_id = models.AutoField(primary_key=True)
    parameter = models.TextField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_cpa_checklist'


class DrawingTotCpaChecksave(models.Model):
    drawing_bom_fid = models.IntegerField()
    param_id = models.IntegerField()
    check_val = models.IntegerField()
    remarks = models.CharField(max_length=500)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_cpa_checksave'


class DrawingTotDocInputs(models.Model):
    reqid = models.AutoField(primary_key=True)
    empcode = models.CharField(max_length=6)
    ntry_date = models.DateField()
    doc_type = models.IntegerField()
    doc_cate = models.IntegerField()
    responsibility = models.CharField(max_length=100)
    project = models.CharField(max_length=200)
    revno = models.IntegerField()
    documentownership = models.CharField(max_length=10)
    main_code = models.CharField(max_length=100)
    main_desc = models.CharField(max_length=200)
    remarks = models.TextField()
    req_attach = models.CharField(max_length=60)
    bom_history_id = models.IntegerField()
    stuatus = models.IntegerField()
    response = models.IntegerField()
    assign_date = models.DateField()
    released_through = models.IntegerField()
    revertto_user = models.IntegerField()
    me_code = models.IntegerField()
    me_remarks = models.TextField(blank=True, null=True)
    product_new_old = models.IntegerField()
    prod_specf = models.CharField(max_length=150)
    specfattach = models.CharField(max_length=100)
    reasn_req = models.IntegerField()
    dirctrate = models.IntegerField()
    strselec = models.CharField(max_length=10)
    strattch = models.CharField(max_length=50)
    concern_asso = models.IntegerField()
    formattext = models.TextField(blank=True, null=True)
    formatattch = models.CharField(max_length=50)
    type_of_manual = models.IntegerField()
    contact_persn = models.IntegerField()
    reviewer = models.IntegerField()
    needed_bydate = models.DateField()
    hod_fucnl = models.IntegerField()
    hodcmmnts = models.CharField(max_length=300)
    qap_initicmmnts = models.CharField(max_length=500)
    qap_file_initi = models.CharField(max_length=100)
    tar_date = models.DateField()
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_doc_inputs'


class DrawingTotDocInputs041021(models.Model):
    reqid = models.AutoField(primary_key=True)
    empcode = models.CharField(max_length=6)
    ntry_date = models.DateField()
    doc_type = models.IntegerField()
    doc_cate = models.IntegerField()
    responsibility = models.CharField(max_length=100)
    project = models.CharField(max_length=200)
    revno = models.IntegerField()
    documentownership = models.CharField(max_length=10)
    main_code = models.CharField(max_length=100)
    main_desc = models.CharField(max_length=200)
    remarks = models.TextField()
    req_attach = models.CharField(max_length=60)
    bom_history_id = models.IntegerField()
    stuatus = models.IntegerField()
    response = models.IntegerField()
    assign_date = models.DateField()
    released_through = models.IntegerField()
    revertto_user = models.IntegerField()
    me_code = models.IntegerField()
    me_remarks = models.TextField(blank=True, null=True)
    product_new_old = models.IntegerField()
    prod_specf = models.CharField(max_length=150)
    specfattach = models.CharField(max_length=100)
    reasn_req = models.IntegerField()
    dirctrate = models.IntegerField()
    strselec = models.CharField(max_length=10)
    strattch = models.CharField(max_length=50)
    concern_asso = models.IntegerField()
    formattext = models.TextField(blank=True, null=True)
    formatattch = models.CharField(max_length=50)
    type_of_manual = models.IntegerField()
    contact_persn = models.IntegerField()
    reviewer = models.IntegerField()
    needed_bydate = models.DateField()
    hod_fucnl = models.IntegerField()
    hodcmmnts = models.CharField(max_length=300)
    qap_initicmmnts = models.CharField(max_length=500)
    qap_file_initi = models.CharField(max_length=100)
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_doc_inputs_04_10_21'


class DrawingTotDocInputs2210(models.Model):
    reqid = models.AutoField(primary_key=True)
    empcode = models.CharField(max_length=6)
    ntry_date = models.DateField()
    doc_type = models.IntegerField()
    doc_cate = models.IntegerField()
    responsibility = models.CharField(max_length=100)
    project = models.CharField(max_length=200)
    revno = models.IntegerField()
    documentownership = models.CharField(max_length=10)
    main_code = models.CharField(max_length=100)
    main_desc = models.CharField(max_length=200)
    remarks = models.TextField()
    req_attach = models.CharField(max_length=60)
    bom_history_id = models.IntegerField()
    stuatus = models.IntegerField()
    response = models.IntegerField()
    assign_date = models.DateField()
    released_through = models.IntegerField()
    revertto_user = models.IntegerField()
    me_code = models.IntegerField()
    me_remarks = models.TextField(blank=True, null=True)
    product_new_old = models.IntegerField()
    prod_specf = models.CharField(max_length=150)
    specfattach = models.CharField(max_length=100)
    reasn_req = models.IntegerField()
    dirctrate = models.IntegerField()
    strselec = models.CharField(max_length=10)
    strattch = models.CharField(max_length=50)
    concern_asso = models.IntegerField()
    formattext = models.TextField(blank=True, null=True)
    formatattch = models.CharField(max_length=50)
    type_of_manual = models.IntegerField()
    contact_persn = models.IntegerField()
    reviewer = models.IntegerField()
    needed_bydate = models.DateField()
    hod_fucnl = models.IntegerField()
    hodcmmnts = models.CharField(max_length=300)
    qap_initicmmnts = models.CharField(max_length=500)
    qap_file_initi = models.CharField(max_length=100)
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_doc_inputs_22_10'


class DrawingTotEntry(models.Model):
    dwg_tot_id = models.AutoField(primary_key=True)
    dwg_project = models.IntegerField()
    ecode = models.CharField(max_length=50)
    dwg_revrver = models.CharField(db_column='dwg_revRver', max_length=4)  # Field name made lowercase.
    dwg_date = models.DateField()
    dwg_from = models.CharField(max_length=6)
    dwg_to = models.CharField(max_length=6)
    dwg_title = models.TextField(blank=True, null=True)
    dwg_agenda = models.TextField(blank=True, null=True)
    dwg_venu = models.IntegerField()
    dwg_project_e = models.IntegerField()
    dwg_project_m = models.IntegerField()
    spec_code = models.CharField(max_length=50)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_entry'


class DrawingTotIssueDataRequest(models.Model):
    main_code = models.CharField(max_length=50)
    attachment = models.CharField(max_length=100)
    requirement = models.IntegerField()
    type = models.IntegerField()
    reason = models.TextField()
    no_of_copys = models.IntegerField()
    soft_copy_req = models.IntegerField()
    hod = models.IntegerField()
    status = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    todepartment = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_issue_data_request'


class DrawingTotManual(models.Model):
    type = models.CharField(max_length=100)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_manual'


class DrawingTotManualChcklist(models.Model):
    reqid = models.IntegerField()
    topic = models.IntegerField()
    availability_sts = models.CharField(max_length=200)
    reference_doc = models.CharField(max_length=100)
    provider = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_manual_chcklist'


class DrawingTotMnualChcklistTopics(models.Model):
    topic = models.CharField(max_length=100)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_mnual_chcklist_topics'


class DrawingTotMom(models.Model):
    dwg_mom_id = models.AutoField(primary_key=True)
    dwg_tot_id = models.IntegerField()
    project_cft = models.IntegerField()
    dwg_type = models.CharField(max_length=1)
    dwg_mcode = models.CharField(max_length=15)
    dwg_points = models.TextField(blank=True, null=True)
    dwg_rootcause = models.TextField(blank=True, null=True)
    dwg_priority = models.TextField(blank=True, null=True)
    dwg_metrics = models.CharField(max_length=4)
    dwg_metrics_category = models.CharField(max_length=4)
    dwg_action_plan = models.TextField(blank=True, null=True)
    dwg_respons = models.TextField(blank=True, null=True)
    dwg_t_date = models.DateField()
    dwg_status = models.CharField(max_length=100)
    dwg_doc_details = models.TextField(blank=True, null=True)
    dwg_c_date = models.DateField()
    dwg_task_status = models.CharField(max_length=6)
    dwg_ecr = models.TextField(blank=True, null=True)
    hodreview = models.TextField(blank=True, null=True)
    mereview = models.TextField(blank=True, null=True)
    cft_type = models.CharField(max_length=1)
    meeting_count = models.CharField(max_length=3)
    dwg_review_id = models.IntegerField()
    timestamp = models.DateTimeField()
    created = models.CharField(max_length=7)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_mom'


class DrawingTotTemp(models.Model):
    pid = models.AutoField(primary_key=True)
    mcode = models.CharField(max_length=15)
    dwg_tot_id = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'drawing_tot_temp'


class DrawingTotTypeIncrement(models.Model):
    type = models.IntegerField(primary_key=True)
    prefix = models.CharField(max_length=5)
    value = models.IntegerField()
    insert_id = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_tot_type_increment'


class DrawingVersionentry(models.Model):
    versionid = models.IntegerField(primary_key=True)
    drawingid = models.IntegerField()
    empcode = models.IntegerField()
    finallinkone = models.CharField(max_length=200)
    finallinktwo = models.CharField(max_length=200)
    version_no = models.CharField(max_length=10)
    release_no = models.CharField(max_length=10)
    date = models.DateTimeField()
    vsnextra_status = models.IntegerField()
    vsnextra_dnwldtime = models.DateTimeField()
    moved_toexternal = models.IntegerField()
    moved_to_datetime = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_versionentry'


class DrawingVersionentry07112020(models.Model):
    versionid = models.AutoField(primary_key=True)
    drawingid = models.IntegerField()
    empcode = models.IntegerField()
    finallinkone = models.CharField(max_length=200)
    finallinktwo = models.CharField(max_length=200)
    version_no = models.CharField(max_length=10)
    release_no = models.CharField(max_length=10)
    date = models.DateTimeField()
    vsnextra_status = models.IntegerField()
    vsnextra_dnwldtime = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_versionentry_07_11_2020'


class DrawingVersionentry13112020(models.Model):
    versionid = models.AutoField(primary_key=True)
    drawingid = models.IntegerField()
    empcode = models.IntegerField()
    finallinkone = models.CharField(max_length=200)
    finallinktwo = models.CharField(max_length=200)
    version_no = models.CharField(max_length=10)
    release_no = models.CharField(max_length=10)
    date = models.DateTimeField()
    vsnextra_status = models.IntegerField()
    vsnextra_dnwldtime = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_versionentry_13_11_2020'


class DrawingVersionentryDuro(models.Model):
    versionid = models.AutoField(primary_key=True)
    drawingid = models.IntegerField()
    empcode = models.IntegerField()
    finallinkone = models.CharField(max_length=200)
    finallinktwo = models.CharField(max_length=200)
    version_no = models.CharField(max_length=10)
    release_no = models.CharField(max_length=10)
    date = models.DateTimeField()
    vsnextra_status = models.IntegerField()
    vsnextra_dnwldtime = models.DateTimeField()
    moved_toexternal = models.IntegerField()
    moved_to_datetime = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_versionentry_duro'


class DrawingVersionentryTemp(models.Model):
    drawingid = models.IntegerField()
    release_no = models.CharField(max_length=10)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawing_versionentry_temp'


class Dum(models.Model):
    name = models.IntegerField()
    place = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dum'


class DvssKanbanTemp(models.Model):
    part_no = models.CharField(max_length=15)
    desc = models.CharField(max_length=100)
    loc_at1 = models.CharField(max_length=50)
    qty = models.IntegerField()
    uom = models.CharField(max_length=10)
    loc_at2 = models.CharField(max_length=50)
    suplr = models.CharField(max_length=50)
    mfg = models.CharField(max_length=20)
    contact = models.CharField(max_length=25)
    lead_time = models.IntegerField()
    ext = models.CharField(max_length=20)
    sub_assy = models.CharField(max_length=50)
    slip_no = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dvss_kanban_temp'


class EcrAplcbltyMstr(models.Model):
    slno = models.AutoField(primary_key=True)
    cat = models.CharField(max_length=50)
    sub_cat = models.CharField(max_length=70)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_aplcblty_mstr'


class EcrAreaChngMstr(models.Model):
    module = models.IntegerField()
    area_chng = models.CharField(max_length=100)
    area_chng_sub = models.CharField(max_length=100)
    sts = models.CharField(max_length=1)
    s_h_dr = models.CharField(max_length=8)
    no = models.AutoField(primary_key=True)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_area_chng_mstr'


class EcrAttachments(models.Model):
    ecr_no = models.IntegerField()
    file_name = models.CharField(max_length=150)
    temp_file_name = models.CharField(max_length=100)
    size = models.CharField(max_length=30)
    type = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    remarks = models.CharField(max_length=200)
    created = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_attachments'


class EcrAuthenticationMaster(models.Model):
    field = models.CharField(max_length=20)
    emps = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'ecr_authentication_master'


class EcrAvgDaysMaster(models.Model):
    slno = models.IntegerField(unique=True)
    description = models.CharField(max_length=100)
    createdby = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    deleteby = models.CharField(max_length=10)
    deletedate = models.DateField()

    class Meta:
        managed = False
        db_table = 'ecr_avg_days_master'


class EcrDesignTeamStdyMstr(models.Model):
    empcode = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_design_team_stdy_mstr'


class EcrDocCtrl(models.Model):
    ecr_no = models.IntegerField()
    doc_dr_no = models.CharField(max_length=25)
    rev = models.IntegerField()
    complt_on = models.CharField(max_length=100)
    createdby = models.CharField(max_length=6)
    medate = models.CharField(max_length=25)
    status = models.IntegerField()
    doc_send = models.CharField(max_length=6)
    dcdate = models.CharField(max_length=25)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_doc_ctrl'


class EcrDsgnPrdAprlAtt(models.Model):
    slno = models.IntegerField()
    dsgn_prd_att = models.TextField()
    dsgn_prd_name = models.CharField(max_length=50)
    dsgn_prd_ext = models.CharField(max_length=20)
    no = models.AutoField(primary_key=True)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_dsgn_prd_aprl_att'


class EcrDsgnPrdMstr(models.Model):
    slno = models.AutoField(primary_key=True)
    ecr_prnt = models.CharField(max_length=50)
    ecr_mstr = models.CharField(max_length=50)
    ecr_chld = models.CharField(max_length=150)
    enc_ref = models.CharField(max_length=1)
    applicability = models.CharField(max_length=1)
    typeofchange = models.CharField(max_length=1)
    enc_smpl_vis = models.CharField(max_length=1)
    enc_dsgn_prd_aprl = models.CharField(max_length=1)
    ecr_sub_chld = models.CharField(max_length=50)
    ecr_sub = models.CharField(max_length=50)
    createdby = models.CharField(max_length=20)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_dsgn_prd_mstr'


class EcrEcadNtry(models.Model):
    slno = models.IntegerField()
    rcvrs = models.CharField(max_length=500)
    sts = models.IntegerField()
    createdby = models.IntegerField()
    me_date = models.DateField()
    ntryby = models.IntegerField()
    ntryby_date = models.CharField(max_length=19)
    up_sts = models.IntegerField()
    reject_remarks = models.CharField(max_length=200)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_ecad_ntry'


class EcrEcrrbomActions(models.Model):
    ecr_action_slno = models.AutoField(primary_key=True)
    ecr_action_symbol = models.CharField(max_length=10)
    ecr_action_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'ecr_ecrrbom_actions'


class EcrEstimationsNtry(models.Model):
    slno = models.IntegerField()
    ecr_no = models.IntegerField()
    estimation = models.CharField(max_length=250)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_estimations_ntry'


class EcrFaiAttach(models.Model):
    fai_id = models.IntegerField()
    ecr_no = models.IntegerField()
    empcode = models.CharField(max_length=7)
    attachment = models.CharField(max_length=500)
    user_fm_rmks = models.CharField(max_length=500)
    department = models.CharField(max_length=50)
    status = models.IntegerField()
    ntry_date = models.DateField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_fai_attach'


class EcrFaiAuthMaster(models.Model):
    department = models.CharField(max_length=50)
    empcode = models.CharField(max_length=7)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_fai_auth_master'


class EcrFaiDetails(models.Model):
    ecr_no = models.IntegerField()
    doc = models.CharField(max_length=25)
    revision = models.IntegerField()
    department = models.CharField(max_length=30)
    remarks = models.CharField(max_length=200)
    subassembly = models.CharField(max_length=50)
    product = models.IntegerField()
    tooling = models.CharField(max_length=4)
    createdby = models.CharField(max_length=7)
    ntry_date = models.DateField()
    status = models.IntegerField()
    user_fm_dep = models.CharField(max_length=7)
    user_fm_rmks = models.CharField(max_length=200)
    user_fm_date = models.DateField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_fai_details'


class EcrFieldFailureMails(models.Model):
    ecr_no = models.IntegerField()
    to = models.CharField(max_length=150)
    cc = models.CharField(max_length=150)
    subject = models.CharField(max_length=70)
    body = models.TextField()
    sts = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_field_failure_mails'


class EcrGroupMailIdsMaster(models.Model):
    group_name = models.CharField(max_length=50)
    empcode = models.CharField(max_length=250)
    form_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ecr_group_mail_ids_master'


class EcrHspMstr(models.Model):
    hsp_no = models.AutoField(primary_key=True)
    hsp_name = models.CharField(max_length=50)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_hsp_mstr'


class EcrIarOutCmMstr(models.Model):
    slno = models.AutoField(primary_key=True)
    iar_out_cm = models.CharField(max_length=150)
    delete1 = models.IntegerField()
    nick_name = models.CharField(max_length=50)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_iar_out_cm_mstr'


class EcrIarOutCmNtry(models.Model):
    ecr_no = models.CharField(max_length=50)
    iar_membrs_attn = models.CharField(max_length=500)
    iar_membrs_obrs = models.CharField(max_length=500)
    ecr_iar_out_cm_slno = models.IntegerField()
    iar_date = models.CharField(max_length=10)
    iar_rmrks = models.CharField(max_length=150)
    iar_sts = models.CharField(max_length=1)
    cls_st_disp_actbygm = models.CharField(max_length=500)
    cls_st_rew_actnyedp = models.CharField(max_length=500)
    createdby = models.IntegerField()
    iar_cmplt_sts = models.IntegerField()
    iar_cmplt_date = models.DateField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_iar_out_cm_ntry'


class EcrImpctAnlsysNtry(models.Model):
    ecr_no = models.CharField(max_length=50)
    area_chng_slno = models.IntegerField()
    aplcbl = models.IntegerField()
    ddtj_no = models.CharField(max_length=150)
    rspnsblty = models.CharField(max_length=150)
    sts = models.CharField(max_length=150)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_impct_anlsys_ntry'


class EcrInViewMatNtry(models.Model):
    ecr_no = models.IntegerField()
    slno = models.IntegerField()
    eff_module = models.CharField(max_length=500)
    resp = models.CharField(max_length=50)
    sts = models.CharField(max_length=1500)
    mail_sts = models.IntegerField()
    created_by = models.IntegerField()
    ntry_by = models.IntegerField()
    ntry_date = models.DateField()
    mail_group = models.CharField(max_length=30)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_in_view_mat_ntry'


class EcrMatMaster(models.Model):
    number_9smat = models.CharField(db_column='9smat', max_length=15)  # Field renamed because it wasn't a valid Python identifier.
    number_9sdesc = models.CharField(db_column='9sdesc', max_length=50)  # Field renamed because it wasn't a valid Python identifier.
    matnr = models.CharField(max_length=15)
    desc = models.CharField(max_length=50)
    createdeby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_mat_master'


class EcrNtry(models.Model):
    ecr_no = models.CharField(max_length=50)
    ecr_obsrvtn = models.CharField(max_length=1000)
    ecr_rvw_cmty = models.CharField(max_length=500)
    ecr_rvw_pnts = models.CharField(max_length=500)
    ecr_rvw_dt = models.DateField()
    product_sts = models.CharField(max_length=1)
    out_cm = models.IntegerField()
    rmrks = models.CharField(max_length=1500)
    whom_2send = models.CharField(max_length=1000)
    ref_att_name = models.CharField(max_length=50)
    ref_att = models.TextField()
    ref_att_ext = models.CharField(max_length=30)
    createdby = models.IntegerField()
    iar_mbrs_attn = models.CharField(max_length=500)
    iar_date = models.DateField()
    iar_mbrs_obs = models.CharField(max_length=500)
    iar_mbrs_doc = models.CharField(max_length=500)
    iar_ntryby = models.IntegerField()
    assign_to = models.CharField(max_length=500)
    ecr_cl_impl_rmrks = models.CharField(max_length=600)
    mom_attach = models.CharField(max_length=200)
    ecr_put_hold_rmrks = models.CharField(max_length=600)
    ecr_rej_rmrks = models.CharField(max_length=600)
    me_remarks = models.CharField(max_length=2000)
    timestamp = models.DateTimeField()
    mail2_desg_byme = models.CharField(max_length=2)
    mail_todesigners = models.CharField(max_length=50)
    mail_todesgnr_date = models.DateField()
    ass_team = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_ntry'


class EcrOpenPermision(models.Model):
    empcode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_open_permision'


class EcrOtherProductsNtry(models.Model):
    slno = models.IntegerField()
    product_name = models.CharField(max_length=50)
    effected_area = models.CharField(max_length=500)
    decision = models.CharField(max_length=500)
    reason = models.CharField(max_length=500)
    ecrno_if_s = models.CharField(max_length=30)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_other_products_ntry'


class EcrPcbLayoutNtry(models.Model):
    slno = models.IntegerField()
    pcb_name = models.CharField(max_length=100)
    machin_utilization = models.CharField(max_length=50)
    test_points = models.CharField(max_length=100)
    pncl_dr_name = models.CharField(max_length=50)
    pncl_dr_att = models.TextField()
    pncl_dr_ext = models.CharField(max_length=20)
    data_sheet_name = models.CharField(max_length=50)
    data_sheet_att = models.TextField()
    data_sheet_ext = models.CharField(max_length=20)
    eng_pcb_name = models.CharField(max_length=50)
    eng_pcb_att = models.TextField()
    eng_pcb_ext = models.CharField(max_length=20)
    crct_name = models.CharField(max_length=50)
    crct_att = models.TextField()
    crct_ext = models.CharField(max_length=20)
    reason_change = models.CharField(max_length=300)
    report_sent_ntimes = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_pcb_layout_ntry'


class EcrPcbLayoutReasons(models.Model):
    ecr_no = models.IntegerField()
    slno = models.IntegerField()
    reason = models.CharField(max_length=1000)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    me_comments = models.CharField(max_length=500)
    me_com_by = models.IntegerField()
    me_time = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'ecr_pcb_layout_reasons'


class EcrPlngAttach(models.Model):
    ecr_no = models.IntegerField()
    number_9mcode = models.CharField(db_column='9mcode', max_length=15)  # Field renamed because it wasn't a valid Python identifier.
    filename = models.CharField(max_length=500)
    filesize = models.IntegerField()
    filetype = models.CharField(max_length=50)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_plng_attach'


class EcrPlngDetails(models.Model):
    ecr_no = models.IntegerField()
    mat_tm_ip = models.CharField(max_length=500)
    plng_note = models.CharField(max_length=500)
    plng_tm_cnclsn = models.IntegerField()
    plng_hod_aprl_sts = models.CharField(max_length=2)
    plng_hod_aprl_yn = models.IntegerField()
    createdby = models.IntegerField()
    iar_cmplt_sts = models.IntegerField()
    iar_cmplt_date = models.DateField()
    ecr_2plng_sts = models.CharField(max_length=1)
    purch_team_confirm = models.CharField(max_length=1)
    purch_team_remarks = models.CharField(max_length=250)
    purch_by = models.IntegerField()
    purch_date = models.CharField(max_length=10)
    purch_update_status = models.IntegerField()
    bom_drg_type = models.CharField(max_length=100)
    stagef_impl_mech = models.IntegerField()
    timestamp = models.DateTimeField()
    me2plng_date = models.CharField(max_length=18)
    plng2purchase_date = models.CharField(max_length=18)
    purchase2plng_date = models.CharField(max_length=18)
    plng2me_date = models.CharField(max_length=18)
    plng2_me_remarks = models.CharField(max_length=250)
    file_name = models.CharField(max_length=50)
    file_type = models.CharField(max_length=20)
    file_path = models.CharField(max_length=250)
    file_size = models.CharField(max_length=50)
    completed = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'ecr_plng_details'


class EcrPlngNtry(models.Model):
    slno_indl = models.IntegerField()
    ecr_no = models.CharField(max_length=50)
    number_9mcode = models.CharField(db_column='9mcode', max_length=20)  # Field renamed because it wasn't a valid Python identifier.
    mcode = models.CharField(max_length=50)
    qty = models.FloatField()
    adrdlt = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    createdby = models.IntegerField()
    strs = models.CharField(max_length=20)
    ws = models.CharField(max_length=20)
    igi = models.CharField(max_length=20)
    ordrs_pndng = models.CharField(max_length=20)
    pcb_ass = models.CharField(max_length=20)
    sub_sys = models.CharField(max_length=20)
    mech_ass = models.CharField(max_length=20)
    pe = models.CharField(max_length=20)
    systm = models.CharField(max_length=20)
    srvc = models.CharField(max_length=20)
    dlvrd2fld = models.CharField(max_length=20)
    vlf_stk = models.FloatField()
    rmrks = models.CharField(max_length=150)
    prsno = models.CharField(max_length=20)
    indentedon = models.CharField(max_length=10)
    xpecteddate = models.CharField(max_length=10)
    ntryby = models.IntegerField()
    timestamp = models.DateTimeField()
    uniq_slno = models.AutoField(primary_key=True)
    cost = models.CharField(max_length=10)
    rew = models.CharField(max_length=200)
    purp = models.CharField(max_length=200)
    sup = models.CharField(max_length=150)
    scrap = models.CharField(max_length=150)
    resp = models.CharField(max_length=100)
    target = models.CharField(max_length=10)
    purch_confirmed_date = models.CharField(max_length=10)
    purch_remarks = models.CharField(max_length=500)
    imapct_ana_needfchange = models.TextField()
    impact_ana_stock_consu = models.CharField(max_length=300)
    rev = models.IntegerField()
    stagef_impl_mech = models.IntegerField()
    wip = models.FloatField()
    vendor_stock_finished = models.FloatField()
    vendor_stock_wip = models.FloatField()
    total_qty = models.IntegerField()
    job_workorder_no = models.CharField(max_length=30)
    each_price = models.FloatField()
    iar_remarks = models.CharField(max_length=300)
    material_transferto = models.CharField(max_length=20)
    material_transferdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'ecr_plng_ntry'


class EcrPpapAtt(models.Model):
    slno = models.IntegerField()
    xl_bom_att = models.TextField()
    xl_bom_name = models.CharField(max_length=50)
    xl_bom_ext = models.CharField(max_length=100)
    garbers_att = models.TextField()
    garbers_name = models.CharField(max_length=50)
    garbers_ext = models.CharField(max_length=100)
    cnc_det_att = models.TextField()
    cnc_det_name = models.CharField(max_length=50)
    cnc_det_ext = models.CharField(max_length=100)
    spec_att = models.TextField()
    spec_name = models.CharField(max_length=50)
    spec_ext = models.CharField(max_length=100)
    panel_att = models.TextField()
    panel_name = models.CharField(max_length=150)
    panel_ext = models.CharField(max_length=50)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    txfr_drg_att = models.TextField()
    txfr_drg_name = models.CharField(max_length=150)
    txfr_drg_ext = models.CharField(max_length=50)
    txfr_bom_att = models.TextField()
    txfr_bom_name = models.CharField(max_length=150)
    txfr_bom_ext = models.CharField(max_length=50)
    ap_att = models.TextField()
    ap_name = models.CharField(max_length=150)
    ap_ext = models.CharField(max_length=50)
    sf_att = models.TextField()
    sf_name = models.CharField(max_length=150)
    sf_ext = models.CharField(max_length=50)
    stencil_att = models.TextField()
    stencil_name = models.CharField(max_length=150)
    stencil_ext = models.CharField(max_length=50)
    pcb_code_att = models.TextField()
    pcb_code_name = models.CharField(max_length=150)
    pcb_code_ext = models.CharField(max_length=50)
    again_start = models.IntegerField()
    garbers_ecad_att = models.TextField()
    garbers_ecad_name = models.CharField(max_length=150)
    garbers_ecad_ext = models.CharField(max_length=50)
    cnc_det_ecad_att = models.TextField()
    cnc_det_ecad_name = models.CharField(max_length=150)
    cnc_det_ecad_ext = models.CharField(max_length=50)
    spec_ecad_att = models.TextField()
    spec_ecad_name = models.CharField(max_length=150)
    spec_ecad_ext = models.CharField(max_length=50)
    panel_ecad_att = models.TextField()
    panel_ecad_name = models.CharField(max_length=150)
    panel_ecad_ext = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ecr_ppap_att'


class EcrPpapAttOld(models.Model):
    slno = models.IntegerField()
    xl_bom_att = models.TextField()
    xl_bom_name = models.CharField(max_length=50)
    xl_bom_ext = models.CharField(max_length=100)
    garbers_att = models.TextField()
    garbers_name = models.CharField(max_length=50)
    garbers_ext = models.CharField(max_length=100)
    cnc_det_att = models.TextField()
    cnc_det_name = models.CharField(max_length=50)
    cnc_det_ext = models.CharField(max_length=100)
    spec_att = models.TextField()
    spec_name = models.CharField(max_length=50)
    spec_ext = models.CharField(max_length=100)
    panel_att = models.TextField()
    panel_name = models.CharField(max_length=150)
    panel_ext = models.CharField(max_length=50)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    txfr_drg_att = models.TextField()
    txfr_drg_name = models.CharField(max_length=150)
    txfr_drg_ext = models.CharField(max_length=50)
    txfr_bom_att = models.TextField()
    txfr_bom_name = models.CharField(max_length=150)
    txfr_bom_ext = models.CharField(max_length=50)
    ap_att = models.TextField()
    ap_name = models.CharField(max_length=150)
    ap_ext = models.CharField(max_length=50)
    sf_att = models.TextField()
    sf_name = models.CharField(max_length=150)
    sf_ext = models.CharField(max_length=50)
    stencil_att = models.TextField()
    stencil_name = models.CharField(max_length=150)
    stencil_ext = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ecr_ppap_att_old'


class EcrPpapDeptsNtry(models.Model):
    slno = models.IntegerField(unique=True)
    proc_rmrks = models.CharField(max_length=500)
    proc_date = models.DateField()
    proc_ntryby = models.IntegerField()
    proc_final_save = models.IntegerField()
    proc_sts = models.IntegerField()
    plng_rmrks = models.TextField()
    plng_mrs_no = models.TextField()
    plng_indent_date = models.DateField()
    plng_date = models.DateField()
    plng_ntryby = models.IntegerField()
    plng_final_save = models.IntegerField()
    plng_sts = models.IntegerField()
    pcb_rmrks = models.TextField()
    pcb_date = models.DateField()
    pcb_ntryby = models.IntegerField()
    pcb_hod_acc_rej = models.IntegerField()
    pcb_hod_date = models.DateField()
    pcb_hod = models.IntegerField()
    pcb_final_save = models.IntegerField()
    pcb_sts = models.IntegerField()
    tst_rmrks = models.TextField()
    tst_date = models.DateField()
    tst_ntryby = models.IntegerField()
    tst_hod_acc_rej = models.IntegerField()
    tst_hod_date = models.DateField()
    tst_hod = models.IntegerField()
    tst_final_save = models.IntegerField()
    tst_sts = models.IntegerField()
    mech_rmrks = models.TextField()
    mech_date = models.DateField()
    mech_ntryby = models.IntegerField()
    mech_hod_acc_rej = models.IntegerField()
    mech_hod_date = models.DateField()
    mech_hod = models.IntegerField()
    mech_final_save = models.IntegerField()
    mech_sts = models.IntegerField()
    pe_rmrks = models.TextField()
    pe_date = models.DateField()
    pe_ntryby = models.IntegerField()
    pe_hod_acc_rej = models.IntegerField()
    pe_hod_date = models.DateField()
    pe_hod = models.IntegerField()
    pe_final_save = models.IntegerField()
    pe_sts = models.IntegerField()
    fqc_rmrks = models.TextField()
    fqc_date = models.DateField()
    fqc_ntryby = models.IntegerField()
    fqc_hod_acc_rej = models.IntegerField()
    fqc_hod_date = models.DateField()
    fqc_hod = models.IntegerField()
    fqc_final_save = models.IntegerField()
    fqc_sts = models.IntegerField()
    me_sts = models.IntegerField()
    me_ntryby = models.IntegerField()
    me_date = models.DateField()
    me_hod = models.IntegerField()
    me_hod_date = models.DateField()
    me_hod_clear = models.CharField(max_length=1)
    rsn_mod = models.TextField()
    maj_min = models.CharField(max_length=3)
    ecad_sts = models.IntegerField()
    ecad_ntryby = models.IntegerField()
    ecad_date = models.DateField()
    stencil_data = models.CharField(max_length=2)
    aprl_sts = models.IntegerField()
    aprl_rmrks = models.TextField()
    pcb_code = models.CharField(max_length=11)
    pcb_code_rmrks = models.CharField(max_length=1000)
    plng_card_slno = models.CharField(max_length=200)
    sig_rmrks = models.TextField()
    sig_date = models.DateField()
    sig_ntryby = models.IntegerField()
    sig_hod_acc_rej = models.TextField()
    sig_hod_date = models.DateField()
    sig_hod = models.IntegerField()
    sig_final_save = models.IntegerField()
    sig_sts = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    maskinglayout = models.TextField()
    toolsjigs_info = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'ecr_ppap_depts_ntry'


class EcrPpapDeptsNtryOld(models.Model):
    slno = models.IntegerField()
    proc_rmrks = models.CharField(max_length=250)
    proc_date = models.DateField()
    proc_ntryby = models.IntegerField()
    proc_final_save = models.IntegerField()
    proc_sts = models.IntegerField()
    plng_mrs_no = models.CharField(max_length=50)
    plng_indent_date = models.DateField()
    plng_date = models.DateField()
    plng_ntryby = models.IntegerField()
    plng_final_save = models.IntegerField()
    plng_sts = models.IntegerField()
    pcb_rmrks = models.CharField(max_length=250)
    pcb_date = models.DateField()
    pcb_ntryby = models.IntegerField()
    pcb_hod_acc_rej = models.IntegerField()
    pcb_hod_date = models.DateField()
    pcb_hod = models.IntegerField()
    pcb_final_save = models.IntegerField()
    pcb_sts = models.IntegerField()
    tst_rmrks = models.CharField(max_length=250)
    tst_date = models.DateField()
    tst_ntryby = models.IntegerField()
    tst_hod_acc_rej = models.IntegerField()
    tst_hod_date = models.DateField()
    tst_hod = models.IntegerField()
    tst_final_save = models.IntegerField()
    tst_sts = models.IntegerField()
    mech_rmrks = models.CharField(max_length=250)
    mech_date = models.DateField()
    mech_ntryby = models.IntegerField()
    mech_hod_acc_rej = models.IntegerField()
    mech_hod_date = models.DateField()
    mech_hod = models.IntegerField()
    mech_final_save = models.IntegerField()
    mech_sts = models.IntegerField()
    pe_rmrks = models.CharField(max_length=250)
    pe_date = models.DateField()
    pe_ntryby = models.IntegerField()
    pe_hod_acc_rej = models.IntegerField()
    pe_hod_date = models.DateField()
    pe_hod = models.IntegerField()
    pe_final_save = models.IntegerField()
    pe_sts = models.IntegerField()
    fqc_rmrks = models.CharField(max_length=250)
    fqc_date = models.DateField()
    fqc_ntryby = models.IntegerField()
    fqc_hod_acc_rej = models.IntegerField()
    fqc_hod_date = models.DateField()
    fqc_hod = models.IntegerField()
    fqc_final_save = models.IntegerField()
    fqc_sts = models.IntegerField()
    me_sts = models.IntegerField()
    me_ntryby = models.IntegerField()
    me_date = models.DateField()
    me_hod = models.IntegerField()
    me_hod_date = models.DateField()
    me_hod_clear = models.CharField(max_length=1)
    rsn_mod = models.CharField(max_length=500)
    maj_min = models.CharField(max_length=3)
    ecad_sts = models.IntegerField()
    ecad_ntryby = models.IntegerField()
    ecad_date = models.DateField()
    stencil_data = models.CharField(max_length=2)
    aprl_sts = models.IntegerField()
    aprl_rmrks = models.CharField(max_length=250)
    pcb_code = models.CharField(max_length=11)
    pcb_code_rmrks = models.CharField(max_length=200)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_ppap_depts_ntry_old'


class EcrPpapDtsrAprl(models.Model):
    slno = models.IntegerField()
    dtsr_code = models.IntegerField()
    update_sts = models.IntegerField()
    rmrks = models.CharField(max_length=500)
    aprl_sts = models.CharField(max_length=1)
    date = models.DateField()
    no_remarks = models.TextField()
    createdby = models.IntegerField()
    me_date = models.DateField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_ppap_dtsr_aprl'


class EcrPpapDtsrAprlOld(models.Model):
    slno = models.IntegerField()
    dtsr_code = models.IntegerField()
    update_sts = models.IntegerField()
    rmrks = models.CharField(max_length=500)
    aprl_sts = models.CharField(max_length=1)
    date = models.DateField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_ppap_dtsr_aprl_old'


class EcrPpapHoldNtry(models.Model):
    ecr_no = models.IntegerField()
    dept = models.CharField(max_length=10)
    date = models.DateField()
    remarks = models.TextField()
    dtsr = models.TextField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_ppap_hold_ntry'


class EcrPpapNtry(models.Model):
    slno = models.IntegerField(primary_key=True)
    pcb_name_exstng_rev = models.CharField(max_length=50)
    rev_sent_ppap = models.IntegerField()
    req_rsd_by = models.CharField(max_length=20)
    rsn_for_layout_rev = models.TextField()
    pcb_rlsd_by_ecad = models.TextField()
    indent_rsd_qty = models.IntegerField()
    elec_chngs_add = models.TextField()
    mech_chngs_add = models.TextField()
    elec_chngs_del = models.TextField()
    mech_chngs_del = models.TextField()
    indent_pcb_rcvd_me_date = models.DateField()
    pcb_frwrd_date = models.DateField()
    gpno = models.CharField(max_length=50)
    date = models.CharField(max_length=10)
    sent_by_whom = models.CharField(max_length=50)
    sent_to_whom = models.CharField(max_length=50)
    prs_no = models.IntegerField()
    prs_date = models.DateField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_ppap_ntry'


class EcrPpapNtryOld(models.Model):
    slno = models.IntegerField()
    pcb_name_exstng_rev = models.CharField(max_length=50)
    rev_sent_ppap = models.IntegerField()
    req_rsd_by = models.CharField(max_length=20)
    rsn_for_layout_rev = models.CharField(max_length=50)
    pcb_rlsd_by_ecad = models.CharField(max_length=50)
    indent_rsd_qty = models.IntegerField()
    elec_chngs_add = models.CharField(max_length=150)
    mech_chngs_add = models.CharField(max_length=150)
    elec_chngs_del = models.CharField(max_length=150)
    mech_chngs_del = models.CharField(max_length=150)
    indent_pcb_rcvd_me_date = models.DateField()
    pcb_frwrd_date = models.DateField()
    gpno = models.CharField(max_length=50)
    date = models.CharField(max_length=10)
    sent_by_whom = models.CharField(max_length=50)
    sent_to_whom = models.CharField(max_length=50)
    prs_no = models.IntegerField()
    prs_date = models.DateField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_ppap_ntry_old'


class EcrPpapStatusMaster(models.Model):
    sts_no = models.AutoField(primary_key=True)
    sts_name = models.CharField(max_length=15)
    desc = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ecr_ppap_status_master'


class EcrPpapSummaryNtry(models.Model):
    ecr_no = models.IntegerField()
    dept = models.CharField(max_length=10)
    action = models.CharField(max_length=300)
    justi = models.CharField(max_length=300)
    delete1 = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_ppap_summary_ntry'


class EcrPrMgrNtry(models.Model):
    ecr_no = models.CharField(max_length=50)
    slno = models.IntegerField()
    dt = models.DateField()
    rmrks = models.CharField(max_length=1500)
    createdby = models.IntegerField()
    sts = models.IntegerField()
    cc = models.CharField(max_length=150)
    hold = models.IntegerField()
    req_add_inp = models.IntegerField()
    me_remarks = models.CharField(max_length=200)
    me_ntry_by = models.IntegerField()
    me_timestamp = models.CharField(max_length=15)
    timestamp = models.DateTimeField()
    uniq_slno = models.AutoField(primary_key=True)
    sending_uniq = models.IntegerField()
    rel_uniq_slno = models.IntegerField()
    me_sender = models.IntegerField()
    me_sender_date = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'ecr_pr_mgr_ntry'


class EcrPrjctMgrCnclsnMstr(models.Model):
    slno = models.AutoField(primary_key=True)
    prjct_mgr_cnclsn = models.CharField(max_length=150)
    nick_name = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_prjct_mgr_cnclsn_mstr'


class EcrRefAtta(models.Model):
    slno = models.IntegerField()
    attachment = models.TextField()
    attachment1 = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    ext = models.CharField(max_length=50)
    no = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_ref_atta'


class EcrRejectedMaster(models.Model):
    rej_slno = models.AutoField(primary_key=True)
    form_name = models.CharField(max_length=50)
    remarks = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ecr_rejected_master'


class EcrRootCauseMaster(models.Model):
    root_cause = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ecr_root_cause_master'


class EcrRvwCmtyOutcmMstr(models.Model):
    slno = models.AutoField(primary_key=True)
    rvw_outcm = models.CharField(max_length=150)
    frwrd2 = models.CharField(max_length=150)
    nick_name = models.CharField(max_length=30)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_rvw_cmty_outcm_mstr'


class EcrSf1449DocdrTestTemp(models.Model):
    doc_dr = models.CharField(max_length=100)
    field_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ecr_sf1449_docdr_test_temp'


class EcrSf1449Ntry(models.Model):
    slno = models.IntegerField()
    no_mstr = models.IntegerField()
    doc_dr_no = models.CharField(max_length=50)
    nw_old_rev = models.CharField(max_length=50)
    desc_chng = models.CharField(max_length=500)
    doc_ctrl = models.CharField(max_length=5)
    no = models.IntegerField()
    createdby = models.IntegerField()
    resp = models.CharField(max_length=150)
    cmpltd_date = models.CharField(max_length=1500)
    resp_ntry = models.IntegerField()
    resp_ntry_date = models.DateField()
    tooling = models.TextField()
    inspection = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    hori_deply = models.TextField()
    stage_of_imple = models.CharField(max_length=30)
    date_sel = models.CharField(max_length=20)
    fut_date = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ecr_sf1449_ntry'


class EcrSf1449Submaster(models.Model):
    slno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    subname = models.CharField(db_column='subName', max_length=100)  # Field name made lowercase.
    type = models.CharField(max_length=1)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_sf1449_subMaster'


class EcrSmplVisNtry(models.Model):
    slno = models.IntegerField()
    vis_name = models.CharField(max_length=20)
    photo_name = models.CharField(max_length=50)
    photo_att = models.TextField()
    photo_ext = models.CharField(max_length=20)
    gp_no = models.CharField(max_length=20)
    date = models.DateField()
    snd_by_whom = models.CharField(max_length=50)
    snt_2_whom = models.CharField(max_length=50)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_smpl_vis_ntry'


class EcrStagefImplMaster(models.Model):
    slno = models.AutoField(primary_key=True)
    stage_name = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_stagef_impl_master'


class EcrStatusMaster(models.Model):
    sts_no = models.IntegerField()
    sts_name = models.CharField(max_length=50)
    sts_present = models.CharField(max_length=30)
    sts_slno = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_status_master'


class EcrStatusNtry(models.Model):
    ecr_no = models.IntegerField()
    sts_no = models.IntegerField()
    sts_slno = models.IntegerField()
    nick_no = models.CharField(max_length=50)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_status_ntry'


class EcrStdyRprtMstr(models.Model):
    slno = models.AutoField(primary_key=True)
    stdy_rprt = models.CharField(max_length=100)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_stdy_rprt_mstr'


class EcrStdyRprtNtry(models.Model):
    ecr_no = models.CharField(max_length=50)
    slno = models.IntegerField()
    rmrks = models.CharField(max_length=150)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_stdy_rprt_ntry'


class EcrSwNtry(models.Model):
    slno = models.IntegerField()
    vrsn_from = models.CharField(max_length=20)
    vrsn_to = models.CharField(max_length=20)
    file_size = models.CharField(max_length=50)
    checksum = models.CharField(max_length=50)
    file_path = models.CharField(max_length=300)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_sw_ntry'


class EcrTargetDayno(models.Model):
    ecr_main_id = models.IntegerField()
    ecr_sub_id = models.IntegerField()
    noofdays = models.IntegerField()
    ecr_desc = models.CharField(max_length=100)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_target_dayno'


class EcrTargetDays(models.Model):
    ecr_target_id = models.AutoField(primary_key=True)
    ecr_desc = models.TextField()
    ecr_short_desc = models.CharField(max_length=200)
    ecr_type = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_target_days'


class EcrTargetDept(models.Model):
    ecr_id = models.IntegerField()
    ecr_target_id = models.IntegerField()
    ecr_target_count = models.IntegerField()
    days = models.CharField(max_length=150)
    date = models.DateField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_target_dept'


class EcrTargetMaster(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    ecr_type = models.CharField(max_length=200)
    days = models.IntegerField()
    createdby = models.CharField(max_length=6)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_target_master'


class EcrTargetdate(models.Model):
    requestno = models.IntegerField(blank=True, null=True)
    attachment = models.TextField(blank=True, null=True)
    attachment1 = models.TextField(blank=True, null=True)
    repeatid = models.IntegerField(blank=True, null=True)
    reviewid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_targetdate'


class EcrTargetdateOds(models.Model):
    reviewid = models.IntegerField(blank=True, null=True)
    requestno = models.IntegerField(blank=True, null=True)
    c = models.CharField(db_column='C', max_length=10, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=10, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ecr_targetdate.ods'


class EcrTempUpdate(models.Model):
    ecrno = models.IntegerField()
    date = models.DateField()
    sts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_temp_update'


class EcrTypeMstr(models.Model):
    type_no = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=5)
    type_desc = models.CharField(max_length=20)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_type_mstr'


class EcrUsrNtry(models.Model):
    slno = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    usr_req_me = models.IntegerField()
    mdl = models.IntegerField()
    rqstd_dt = models.DateField()
    reqst_date_time = models.CharField(max_length=30)
    ttl = models.CharField(max_length=1000)
    doc_dr = models.CharField(max_length=100)
    rev = models.CharField(max_length=100)
    sys = models.CharField(max_length=100)
    ndf_chng = models.CharField(max_length=5000)
    descf_chng = models.CharField(max_length=5000)
    prjct = models.CharField(max_length=300)
    ecr_dsgn_prd_no = models.IntegerField()
    deptcode = models.IntegerField()
    aplcblty = models.CharField(max_length=1)
    ecr_dept = models.CharField(max_length=30)
    encls_cust_cor = models.CharField(max_length=1)
    tyf_chng = models.CharField(max_length=1)
    encls_smpl_vis = models.CharField(max_length=1)
    hod_sts = models.IntegerField()
    hod_rmrks = models.CharField(max_length=150)
    ecr_no = models.CharField(max_length=50)
    ecr_sts = models.IntegerField()
    ecr_sts_rmrks = models.CharField(max_length=1500)
    ecr_type = models.CharField(max_length=3)
    aplcblity_mstr = models.IntegerField()
    user_aplcblity_mstr = models.IntegerField()
    sw_stage = models.IntegerField()
    hsp_no = models.IntegerField()
    ecr_temp_no = models.IntegerField()
    rvw_cmty_outcum = models.IntegerField()
    cmpltd_date = models.DateField()
    ecr_plng = models.IntegerField()
    cmpltd_by = models.IntegerField()
    ecr_no_e = models.IntegerField()
    ecr_no_m = models.IntegerField()
    ecr_no_em = models.IntegerField()
    ecr_sts_mstr_ntrs = models.CharField(max_length=50)
    estimation_sts = models.IntegerField()
    in_view_date = models.DateField()
    in_view_closing_stmt = models.CharField(max_length=300)
    in_view_fsave = models.IntegerField()
    hod_aprl_date = models.DateField()
    rej_slno = models.IntegerField()
    rej_date = models.DateField()
    rej_by = models.IntegerField()
    in_view_mail_sts = models.IntegerField()
    e_complete_sts = models.IntegerField()
    m_complete_sts = models.IntegerField()
    old_ecr_no = models.BigIntegerField()
    old_superseded_no = models.BigIntegerField()
    acc_rej_date = models.DateField()
    acc_rej_by = models.IntegerField()
    ecr_present_status = models.CharField(max_length=500)
    review_status = models.CharField(max_length=10)
    root_cause = models.TextField()
    timestamp = models.DateTimeField()
    avg_closed = models.IntegerField()
    designer_approval = models.CharField(max_length=2)
    hod_approval = models.CharField(max_length=2)
    hod_dept = models.IntegerField()
    hod_dept_sts = models.IntegerField()
    hod_dept_date = models.DateField()
    hod_dept_remark = models.CharField(max_length=300)
    hod_dept_applicabilty = models.CharField(max_length=2)
    fai_req = models.CharField(max_length=30)
    fai_req_add_ips = models.CharField(max_length=10)
    fai_req_remarks = models.CharField(max_length=200)
    fai_sts = models.CharField(max_length=3)
    fai_req_date = models.DateField()
    fai_rep_date = models.DateField()
    fai_att = models.CharField(max_length=100)
    fai_reply = models.CharField(max_length=50)
    fai_me = models.CharField(max_length=100)
    fai_me_just = models.CharField(max_length=500)
    ecr_usr_ucp_remks = models.TextField()
    ecr_tar_type = models.IntegerField()
    proposed_cmplt_date = models.DateField()
    res_to_chgn = models.CharField(max_length=500)
    rmks_for_delay = models.CharField(max_length=500)
    ucp_cc = models.CharField(max_length=400)
    com_compat = models.CharField(max_length=3)
    com_compat_comm = models.CharField(max_length=500)
    comple_rmsk = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'ecr_usr_ntry'


class EcrUsrNtryAplcblty(models.Model):
    slno = models.IntegerField()
    cat = models.IntegerField()
    sub_cat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_usr_ntry_aplcblty'


class EcrUsrUcpNtry(models.Model):
    uniq = models.AutoField(primary_key=True)
    ecr_no = models.IntegerField()
    status = models.IntegerField()
    createdby = models.CharField(max_length=6)
    me_rmks = models.CharField(max_length=500)
    me_date = models.CharField(max_length=20)
    ucp_usr = models.CharField(max_length=6)
    usr_rmk = models.CharField(max_length=500)
    usr_date = models.CharField(max_length=20)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_usr_ucp_ntry'


class EcrV2Cost(models.Model):
    risk_associated = models.CharField(max_length=200)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_v2_cost'


class EcrV2Docs(models.Model):
    slno = models.AutoField(primary_key=True)
    resp = models.CharField(max_length=50)
    product_code = models.CharField(max_length=100)
    productcode = models.CharField(max_length=50)
    shorttext = models.TextField()
    uom = models.CharField(max_length=10)
    revno = models.CharField(max_length=50)
    type = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    created_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_v2_docs'


class EcrV2DocsBackup(models.Model):
    slno = models.AutoField(primary_key=True)
    resp = models.CharField(max_length=50)
    product_code = models.CharField(max_length=100)
    productcode = models.CharField(max_length=50)
    shorttext = models.TextField()
    uom = models.CharField(max_length=10)
    revno = models.CharField(max_length=50)
    type = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    created_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_v2_docs_backup'


class EcrV2Hsty(models.Model):
    hid = models.AutoField(primary_key=True)
    requestno = models.IntegerField()
    reviewid = models.CharField(max_length=50, blank=True, null=True)
    lineitemno = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    userstatus = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    associate = models.IntegerField()
    repeatid = models.IntegerField()
    date = models.DateTimeField()
    datenew = models.CharField(max_length=15, blank=True, null=True)
    attachment = models.CharField(max_length=100, blank=True, null=True)
    rfd = models.TextField(blank=True, null=True)
    noofdays = models.IntegerField()
    associate_dept = models.IntegerField()
    delete1 = models.IntegerField()
    type_dup = models.IntegerField()
    desc_in = models.IntegerField()
    des_in_cmnt = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecr_v2_hsty'


class EcrV2Hsty0212(models.Model):
    hid = models.AutoField(primary_key=True)
    requestno = models.IntegerField()
    reviewid = models.CharField(max_length=50, blank=True, null=True)
    lineitemno = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    userstatus = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    associate = models.IntegerField()
    repeatid = models.IntegerField()
    date = models.DateTimeField()
    datenew = models.CharField(max_length=15, blank=True, null=True)
    attachment = models.CharField(max_length=100, blank=True, null=True)
    rfd = models.TextField(blank=True, null=True)
    noofdays = models.IntegerField()
    delete1 = models.IntegerField()
    type_dup = models.IntegerField()
    desc_in = models.IntegerField()
    des_in_cmnt = models.CharField(max_length=500, blank=True, null=True)
    date_cnt = models.DateField()
    associate_dept = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_v2_hsty_02_12'


class EcrV2Hsty13072022(models.Model):
    hid = models.AutoField(primary_key=True)
    requestno = models.IntegerField()
    reviewid = models.CharField(max_length=50, blank=True, null=True)
    lineitemno = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    userstatus = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    associate = models.IntegerField()
    repeatid = models.IntegerField()
    date = models.DateTimeField()
    datenew = models.CharField(max_length=15, blank=True, null=True)
    attachment = models.CharField(max_length=100, blank=True, null=True)
    rfd = models.TextField(blank=True, null=True)
    noofdays = models.IntegerField()
    associate_dept = models.IntegerField()
    delete1 = models.IntegerField()
    type_dup = models.IntegerField()
    desc_in = models.IntegerField()
    des_in_cmnt = models.CharField(max_length=500, blank=True, null=True)
    date1 = models.DateField()

    class Meta:
        managed = False
        db_table = 'ecr_v2_hsty_13_07_2022'


class EcrV2HstyAudit(models.Model):
    hid = models.AutoField(primary_key=True)
    requestno = models.IntegerField()
    reviewid = models.CharField(max_length=50, blank=True, null=True)
    lineitemno = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    userstatus = models.IntegerField()
    comment = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    associate = models.IntegerField()
    repeatid = models.IntegerField()
    date = models.DateTimeField()
    datenew = models.CharField(max_length=15, blank=True, null=True)
    attachment = models.CharField(max_length=100, blank=True, null=True)
    rfd = models.TextField(blank=True, null=True)
    noofdays = models.IntegerField()
    associate_dept = models.IntegerField()
    delete1 = models.IntegerField()
    type_dup = models.IntegerField()
    desc_in = models.IntegerField()
    des_in_cmnt = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecr_v2_hsty_audit'


class EcrV2HstyBackup(models.Model):
    hid = models.AutoField(primary_key=True)
    requestno = models.IntegerField()
    reviewid = models.CharField(max_length=50, blank=True, null=True)
    lineitemno = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    userstatus = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    associate = models.IntegerField()
    repeatid = models.IntegerField()
    date = models.DateTimeField()
    datenew = models.CharField(max_length=15, blank=True, null=True)
    attachment = models.CharField(max_length=100, blank=True, null=True)
    rfd = models.TextField(blank=True, null=True)
    noofdays = models.IntegerField()
    associate_dept = models.IntegerField()
    delete1 = models.IntegerField()
    type_dup = models.IntegerField()
    desc_in = models.IntegerField()
    des_in_cmnt = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecr_v2_hsty_backup'


class EcrV2Item(models.Model):
    itemno = models.AutoField(primary_key=True)
    requestno = models.IntegerField()
    type = models.IntegerField()
    header = models.CharField(max_length=500, blank=True, null=True)
    itemcategory = models.IntegerField()
    docno = models.CharField(max_length=500, blank=True, null=True)
    revno = models.CharField(max_length=10, blank=True, null=True)
    changedesc = models.IntegerField()
    referanceno = models.CharField(max_length=50, blank=True, null=True)
    details = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    implementation = models.IntegerField()
    attachment = models.TextField(blank=True, null=True)
    cat_new = models.IntegerField(blank=True, null=True)
    planningdate = models.DateField()
    pono = models.CharField(max_length=100, blank=True, null=True)
    poremarks = models.TextField(blank=True, null=True)
    f1 = models.CharField(max_length=50, blank=True, null=True)
    f2 = models.CharField(max_length=50, blank=True, null=True)
    f3 = models.CharField(max_length=50, blank=True, null=True)
    f4 = models.CharField(max_length=50, blank=True, null=True)
    f5 = models.CharField(max_length=50, blank=True, null=True)
    f6 = models.CharField(max_length=50, blank=True, null=True)
    f7 = models.CharField(max_length=50, blank=True, null=True)
    f8 = models.CharField(max_length=50, blank=True, null=True)
    f9 = models.CharField(max_length=50, blank=True, null=True)
    f10 = models.CharField(max_length=50, blank=True, null=True)
    f11 = models.CharField(max_length=50, blank=True, null=True)
    f12 = models.CharField(max_length=50, blank=True, null=True)
    f13 = models.CharField(max_length=50, blank=True, null=True)
    f14 = models.DateField()
    f15 = models.CharField(max_length=20, blank=True, null=True)
    ivstatus = models.IntegerField()
    ivdate = models.DateField()
    ivdateselection = models.IntegerField()
    ivdfdate = models.DateField()
    ivimpact = models.IntegerField()
    ivimpact1 = models.IntegerField()
    ivimpact2 = models.IntegerField()
    ivimpact3 = models.IntegerField()
    ivimpact4 = models.IntegerField()
    ivimpact5 = models.IntegerField()
    ivimpact6 = models.IntegerField()
    impact_comment = models.TextField(blank=True, null=True)
    faicode = models.CharField(max_length=50, blank=True, null=True)
    faitype = models.IntegerField()
    faitdept = models.CharField(max_length=100, blank=True, null=True)
    faiaction = models.IntegerField()
    faipostedby = models.IntegerField()
    faidate = models.DateField()
    matcat = models.IntegerField()
    bomcat = models.IntegerField()
    bomdesigner = models.IntegerField()
    timestamp = models.DateTimeField()
    responsible = models.IntegerField()
    activites = models.IntegerField()
    linecomments = models.TextField(blank=True, null=True)
    userstatus = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    faimestatus = models.IntegerField()
    faicomments = models.TextField(blank=True, null=True)
    faidesigner = models.CharField(max_length=7, blank=True, null=True)
    faidesinerfeedback = models.IntegerField()
    faidesinercomment = models.TextField(blank=True, null=True)
    mefaidesignerforwardeddate = models.DateTimeField()
    planningfeedback1 = models.IntegerField()
    planningfeedback2 = models.IntegerField()
    planningstatus = models.IntegerField()
    fdate = models.DateField()
    planningpono = models.IntegerField()
    planningpoqty = models.DecimalField(max_digits=10, decimal_places=2)
    modified = models.CharField(max_length=11, blank=True, null=True)
    planningcycle = models.IntegerField()
    vplanningcycle = models.IntegerField()
    podetails = models.CharField(max_length=10, blank=True, null=True)
    rca_status = models.IntegerField()
    faisacode = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_v2_item'


class EcrV2Item13072022(models.Model):
    itemno = models.AutoField(primary_key=True)
    requestno = models.IntegerField()
    type = models.IntegerField()
    header = models.CharField(max_length=500, blank=True, null=True)
    itemcategory = models.IntegerField()
    docno = models.CharField(max_length=500, blank=True, null=True)
    revno = models.CharField(max_length=10, blank=True, null=True)
    changedesc = models.IntegerField()
    referanceno = models.CharField(max_length=50, blank=True, null=True)
    details = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    implementation = models.IntegerField()
    attachment = models.TextField(blank=True, null=True)
    planningdate = models.DateField()
    pono = models.CharField(max_length=100, blank=True, null=True)
    poremarks = models.TextField(blank=True, null=True)
    f1 = models.CharField(max_length=50, blank=True, null=True)
    f2 = models.CharField(max_length=50, blank=True, null=True)
    f3 = models.CharField(max_length=50, blank=True, null=True)
    f4 = models.CharField(max_length=50, blank=True, null=True)
    f5 = models.CharField(max_length=50, blank=True, null=True)
    f6 = models.CharField(max_length=50, blank=True, null=True)
    f7 = models.CharField(max_length=50, blank=True, null=True)
    f8 = models.CharField(max_length=50, blank=True, null=True)
    f9 = models.CharField(max_length=50, blank=True, null=True)
    f10 = models.CharField(max_length=50, blank=True, null=True)
    f11 = models.CharField(max_length=50, blank=True, null=True)
    f12 = models.CharField(max_length=50, blank=True, null=True)
    f13 = models.CharField(max_length=50, blank=True, null=True)
    f14 = models.DateField()
    f15 = models.CharField(max_length=20, blank=True, null=True)
    ivstatus = models.IntegerField()
    ivdate = models.DateField()
    ivdateselection = models.IntegerField()
    ivdfdate = models.DateField()
    ivimpact = models.IntegerField()
    ivimpact1 = models.IntegerField()
    ivimpact2 = models.IntegerField()
    ivimpact3 = models.IntegerField()
    ivimpact4 = models.IntegerField()
    ivimpact5 = models.IntegerField()
    ivimpact6 = models.IntegerField()
    impact_comment = models.TextField(blank=True, null=True)
    faicode = models.CharField(max_length=50, blank=True, null=True)
    faitype = models.IntegerField()
    faitdept = models.CharField(max_length=100, blank=True, null=True)
    faiaction = models.IntegerField()
    faipostedby = models.IntegerField()
    faidate = models.DateField()
    matcat = models.IntegerField()
    bomcat = models.IntegerField()
    bomdesigner = models.IntegerField()
    timestamp = models.DateTimeField()
    responsible = models.IntegerField()
    activites = models.IntegerField()
    linecomments = models.TextField(blank=True, null=True)
    userstatus = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    faimestatus = models.IntegerField()
    faicomments = models.TextField(blank=True, null=True)
    faidesigner = models.CharField(max_length=7, blank=True, null=True)
    faidesinerfeedback = models.IntegerField()
    faidesinercomment = models.TextField(blank=True, null=True)
    mefaidesignerforwardeddate = models.DateTimeField()
    planningfeedback1 = models.IntegerField()
    planningfeedback2 = models.IntegerField()
    planningstatus = models.IntegerField()
    fdate = models.DateField()
    planningpono = models.IntegerField()
    planningpoqty = models.DecimalField(max_digits=10, decimal_places=2)
    modified = models.CharField(max_length=11, blank=True, null=True)
    planningcycle = models.IntegerField()
    vplanningcycle = models.IntegerField()
    podetails = models.CharField(max_length=10, blank=True, null=True)
    rca_status = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_v2_item_13_07_2022'


class EcrV2ItemBackup(models.Model):
    itemno = models.AutoField(primary_key=True)
    requestno = models.IntegerField()
    type = models.IntegerField()
    header = models.CharField(max_length=500, blank=True, null=True)
    itemcategory = models.IntegerField()
    docno = models.CharField(max_length=500, blank=True, null=True)
    revno = models.CharField(max_length=10, blank=True, null=True)
    changedesc = models.IntegerField()
    referanceno = models.CharField(max_length=50, blank=True, null=True)
    details = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    implementation = models.IntegerField()
    attachment = models.TextField(blank=True, null=True)
    planningdate = models.DateField()
    pono = models.CharField(max_length=100, blank=True, null=True)
    poremarks = models.TextField(blank=True, null=True)
    f1 = models.CharField(max_length=50, blank=True, null=True)
    f2 = models.CharField(max_length=50, blank=True, null=True)
    f3 = models.CharField(max_length=50, blank=True, null=True)
    f4 = models.CharField(max_length=50, blank=True, null=True)
    f5 = models.CharField(max_length=50, blank=True, null=True)
    f6 = models.CharField(max_length=50, blank=True, null=True)
    f7 = models.CharField(max_length=50, blank=True, null=True)
    f8 = models.CharField(max_length=50, blank=True, null=True)
    f9 = models.CharField(max_length=50, blank=True, null=True)
    f10 = models.CharField(max_length=50, blank=True, null=True)
    f11 = models.CharField(max_length=50, blank=True, null=True)
    f12 = models.CharField(max_length=50, blank=True, null=True)
    f13 = models.CharField(max_length=50, blank=True, null=True)
    f14 = models.DateField()
    f15 = models.CharField(max_length=20, blank=True, null=True)
    ivstatus = models.IntegerField()
    ivdate = models.DateField()
    ivdateselection = models.IntegerField()
    ivdfdate = models.DateField()
    ivimpact = models.IntegerField()
    ivimpact1 = models.IntegerField()
    ivimpact2 = models.IntegerField()
    ivimpact3 = models.IntegerField()
    ivimpact4 = models.IntegerField()
    ivimpact5 = models.IntegerField()
    ivimpact6 = models.IntegerField()
    impact_comment = models.TextField(blank=True, null=True)
    faicode = models.CharField(max_length=50, blank=True, null=True)
    faitype = models.IntegerField()
    faitdept = models.CharField(max_length=100, blank=True, null=True)
    faiaction = models.IntegerField()
    faipostedby = models.IntegerField()
    faidate = models.DateField()
    matcat = models.IntegerField()
    bomcat = models.IntegerField()
    bomdesigner = models.IntegerField()
    timestamp = models.DateTimeField()
    responsible = models.IntegerField()
    activites = models.IntegerField()
    linecomments = models.TextField(blank=True, null=True)
    userstatus = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    faimestatus = models.IntegerField()
    faicomments = models.TextField(blank=True, null=True)
    faidesigner = models.CharField(max_length=7, blank=True, null=True)
    faidesinerfeedback = models.IntegerField()
    faidesinercomment = models.TextField(blank=True, null=True)
    mefaidesignerforwardeddate = models.DateTimeField()
    planningfeedback1 = models.IntegerField()
    planningfeedback2 = models.IntegerField()
    planningstatus = models.IntegerField()
    fdate = models.DateField()
    planningpono = models.IntegerField()
    planningpoqty = models.DecimalField(max_digits=10, decimal_places=2)
    modified = models.CharField(max_length=11, blank=True, null=True)
    planningcycle = models.CharField(max_length=200, blank=True, null=True)
    vplanningcycle = models.IntegerField()
    podetails = models.CharField(max_length=10, blank=True, null=True)
    rca_status = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_v2_item_backup'


class EcrV2Logc(models.Model):
    logicid = models.AutoField(primary_key=True)
    logicname = models.TextField()
    logicreferenceid = models.CharField(max_length=50)
    logicindexid = models.IntegerField()
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ecr_v2_logc'


class EcrV2Main(models.Model):
    requestno = models.AutoField(primary_key=True)
    company_code = models.IntegerField()
    ecrno = models.CharField(max_length=30, blank=True, null=True)
    createdby = models.IntegerField()
    dept = models.CharField(max_length=10, blank=True, null=True)
    category = models.IntegerField()
    subcategory = models.IntegerField()
    descipline = models.IntegerField()
    reason = models.TextField(blank=True, null=True)
    root_cause = models.TextField(blank=True, null=True)
    name_pcb = models.TextField(blank=True, null=True)
    faicat = models.IntegerField()
    ref_no = models.IntegerField()
    doc_approval = models.CharField(max_length=1, blank=True, null=True)
    fyi = models.IntegerField()
    ehs = models.IntegerField()
    ehsyes = models.TextField(blank=True, null=True)
    ehs_type = models.IntegerField()
    fyi_check = models.CharField(max_length=1, blank=True, null=True)
    totdetails = models.IntegerField()
    m_date = models.DateField()
    attachment = models.TextField(blank=True, null=True)
    applicable = models.IntegerField()
    applicable_attach = models.TextField(blank=True, null=True)
    field_compatibility = models.IntegerField()
    field_compatibility_remarks = models.TextField()
    cost_estimation = models.IntegerField()
    cost_estimation_field = models.IntegerField()
    status = models.IntegerField()
    mee = models.IntegerField()
    mem = models.IntegerField()
    faiprocess = models.IntegerField()
    timestamp = models.DateTimeField()
    date = models.DateField()
    targetdate = models.DateField()
    closeddate = models.DateField()
    supercede = models.IntegerField()
    planningrefresh = models.TextField(blank=True, null=True)
    hod_code = models.IntegerField()
    hod_aprl_sts = models.IntegerField()
    hod_comment = models.CharField(max_length=100, blank=True, null=True)
    delete1 = models.IntegerField()
    delete_reason = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecr_v2_main'


class EcrV2Main13072022(models.Model):
    requestno = models.AutoField(primary_key=True)
    company_code = models.IntegerField()
    ecrno = models.CharField(max_length=30, blank=True, null=True)
    createdby = models.IntegerField()
    dept = models.CharField(max_length=10, blank=True, null=True)
    category = models.IntegerField()
    descipline = models.IntegerField()
    reason = models.TextField(blank=True, null=True)
    root_cause = models.TextField(blank=True, null=True)
    name_pcb = models.TextField(blank=True, null=True)
    faicat = models.IntegerField()
    ref_no = models.IntegerField()
    doc_approval = models.CharField(max_length=1, blank=True, null=True)
    fyi = models.IntegerField()
    ehs = models.IntegerField()
    ehsyes = models.TextField(blank=True, null=True)
    ehs_type = models.IntegerField()
    fyi_check = models.CharField(max_length=1, blank=True, null=True)
    totdetails = models.IntegerField()
    m_date = models.DateField()
    attachment = models.TextField(blank=True, null=True)
    applicable = models.IntegerField()
    applicable_attach = models.TextField(blank=True, null=True)
    field_compatibility = models.IntegerField()
    field_compatibility_remarks = models.TextField()
    cost_estimation = models.IntegerField()
    cost_estimation_field = models.IntegerField()
    status = models.IntegerField()
    mee = models.IntegerField()
    mem = models.IntegerField()
    faiprocess = models.IntegerField()
    timestamp = models.DateTimeField()
    date = models.DateField()
    targetdate = models.DateField()
    closeddate = models.DateField()
    supercede = models.IntegerField()
    planningrefresh = models.TextField(blank=True, null=True)
    hod_code = models.IntegerField()
    hod_aprl_sts = models.IntegerField()
    hod_comment = models.CharField(max_length=100, blank=True, null=True)
    delete1 = models.IntegerField()
    delete_reason = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecr_v2_main_13_07_2022'


class EcrV2MainBackup(models.Model):
    requestno = models.AutoField(primary_key=True)
    company_code = models.IntegerField()
    ecrno = models.CharField(max_length=30, blank=True, null=True)
    createdby = models.IntegerField()
    dept = models.CharField(max_length=10, blank=True, null=True)
    category = models.IntegerField()
    descipline = models.IntegerField()
    reason = models.TextField(blank=True, null=True)
    root_cause = models.TextField(blank=True, null=True)
    name_pcb = models.TextField(blank=True, null=True)
    faicat = models.IntegerField()
    ref_no = models.IntegerField()
    doc_approval = models.CharField(max_length=1, blank=True, null=True)
    fyi = models.IntegerField()
    ehs = models.IntegerField()
    ehsyes = models.TextField(blank=True, null=True)
    ehs_type = models.IntegerField()
    fyi_check = models.CharField(max_length=1, blank=True, null=True)
    totdetails = models.IntegerField()
    m_date = models.DateField()
    attachment = models.TextField(blank=True, null=True)
    applicable = models.IntegerField()
    applicable_attach = models.TextField(blank=True, null=True)
    field_compatibility = models.IntegerField()
    field_compatibility_remarks = models.TextField()
    cost_estimation = models.IntegerField()
    cost_estimation_field = models.IntegerField()
    status = models.IntegerField()
    mee = models.IntegerField()
    mem = models.IntegerField()
    faiprocess = models.IntegerField()
    timestamp = models.DateTimeField()
    date = models.DateField()
    targetdate = models.DateField()
    closeddate = models.DateField()
    supercede = models.IntegerField()
    planningrefresh = models.TextField(blank=True, null=True)
    hod_code = models.IntegerField()
    hod_aprl_sts = models.IntegerField()
    hod_comment = models.CharField(max_length=100, blank=True, null=True)
    delete1 = models.IntegerField()
    delete_reason = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecr_v2_main_backup'


class EcrV2Mcat(models.Model):
    main = models.AutoField(primary_key=True)
    company_code = models.IntegerField()
    category = models.CharField(max_length=100)
    type = models.IntegerField()
    subtype = models.IntegerField()
    enabled = models.IntegerField(blank=True, null=True)
    shortcutname = models.CharField(max_length=100)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_v2_mcat'


class EcrV2Mcat17072024(models.Model):
    main = models.AutoField(primary_key=True)
    company_code = models.IntegerField()
    category = models.CharField(max_length=100)
    type = models.IntegerField()
    subtype = models.IntegerField()
    enabled = models.IntegerField(blank=True, null=True)
    shortcutname = models.CharField(max_length=100)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_v2_mcat_17072024'


class EcrV2McatBackup(models.Model):
    main = models.AutoField(primary_key=True)
    company_code = models.IntegerField()
    category = models.CharField(max_length=100)
    type = models.IntegerField()
    subtype = models.IntegerField()
    enabled = models.IntegerField()
    shortcutname = models.CharField(max_length=100)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ecr_v2_mcat_backup'


class EcrV2Pdcd(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50)
    pchild = models.IntegerField()
    pmee = models.TextField()
    pmeenew = models.CharField(max_length=50)
    pmem = models.TextField()
    pmea = models.TextField()
    training = models.CharField(max_length=50)
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ecr_v2_pdcd'


class EcrV2Pdcd11(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50)
    pchild = models.IntegerField()
    pmee = models.TextField()
    pmeenew = models.CharField(max_length=50)
    pmem = models.TextField()
    pmea = models.TextField()
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ecr_v2_pdcd11'


class EcrV2PdcdA(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50)
    pchild = models.IntegerField()
    pmee = models.TextField()
    pmeenew = models.CharField(max_length=50)
    pmem = models.TextField()
    pmea = models.TextField()
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ecr_v2_pdcd_a'


class EcrV2PdcdBackup(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50)
    pchild = models.IntegerField()
    pmee = models.TextField()
    pmeenew = models.CharField(max_length=50)
    pmem = models.TextField()
    pmea = models.TextField()
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ecr_v2_pdcd_backup'


class EcrV2PdcdBackup1512(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50)
    pchild = models.IntegerField()
    pmee = models.TextField()
    pmeenew = models.CharField(max_length=50)
    pmem = models.TextField()
    pmea = models.TextField()
    training = models.CharField(max_length=50)
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ecr_v2_pdcd_backup_15_12'


class EcrV2PdcdRewamp(models.Model):
    pid = models.IntegerField()
    pmem = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'ecr_v2_pdcd_rewamp'


class EcrV2Poupdationdetails(models.Model):
    pid = models.AutoField(primary_key=True)
    requestno = models.IntegerField()
    potext = models.TextField(blank=True, null=True)
    attachment = models.CharField(max_length=50, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_v2_poupdationdetails'


class EcrV2PriorityMaster(models.Model):
    slno = models.AutoField(primary_key=True)
    priority = models.IntegerField(blank=True, null=True)
    priorityname = models.CharField(max_length=10, blank=True, null=True)
    subcategoryindex = models.IntegerField(blank=True, null=True)
    subcategory = models.CharField(max_length=100, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_v2_priority_master'


class EcrV2Revw(models.Model):
    reviewid = models.AutoField(primary_key=True)
    requestno = models.IntegerField()
    reviewtype = models.IntegerField()
    type = models.IntegerField()
    associate = models.IntegerField()
    reviewoutcomesub = models.CharField(max_length=100, blank=True, null=True)
    me_study = models.TextField(blank=True, null=True)
    repeatid = models.IntegerField()
    cost = models.TextField(blank=True, null=True)
    cost_descr = models.TextField(blank=True, null=True)
    material_cost = models.TextField(blank=True, null=True)
    process_time = models.TextField(blank=True, null=True)
    lead_time = models.TextField(blank=True, null=True)
    inventory = models.TextField(blank=True, null=True)
    manufacturability = models.TextField(blank=True, null=True)
    mat_avali = models.TextField(blank=True, null=True)
    against_failure = models.TextField(blank=True, null=True)
    smooth_chnge = models.TextField(blank=True, null=True)
    materialstatus = models.CharField(max_length=5, blank=True, null=True)
    ptstatus = models.CharField(max_length=5, blank=True, null=True)
    procumentstatus = models.CharField(max_length=5, blank=True, null=True)
    inventorystatus = models.CharField(max_length=5, blank=True, null=True)
    manufastatus = models.CharField(max_length=5, blank=True, null=True)
    matavailstatus = models.CharField(max_length=5, blank=True, null=True)
    failurestatus = models.CharField(max_length=5, blank=True, null=True)
    smoothstatus = models.CharField(max_length=5, blank=True, null=True)
    matatt = models.CharField(max_length=100, blank=True, null=True)
    pttime = models.CharField(max_length=100, blank=True, null=True)
    procurementtime = models.CharField(max_length=100, blank=True, null=True)
    inventoryatta = models.CharField(max_length=100, blank=True, null=True)
    manufactatta = models.CharField(max_length=100, blank=True, null=True)
    matavailatta = models.CharField(max_length=100, blank=True, null=True)
    failureattach = models.CharField(max_length=100, blank=True, null=True)
    smoothatta = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    rcomittee = models.CharField(max_length=1000, blank=True, null=True)
    reviewoutcome = models.CharField(max_length=1000, blank=True, null=True)
    holddate = models.DateField()
    comments = models.TextField(blank=True, null=True)
    overreviewpoints = models.TextField(blank=True, null=True)
    checkpoints = models.CharField(max_length=1000, blank=True, null=True)
    horizantal = models.IntegerField()
    mmtag = models.IntegerField()
    faisubprocess = models.IntegerField()
    tagno = models.IntegerField()
    dept_randd = models.IntegerField()
    ecr_doccat = models.IntegerField()
    mailtopro = models.IntegerField()
    designerfeedback = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    ncstatus = models.IntegerField()
    ncactive = models.IntegerField()
    me_nc_date = models.DateTimeField()
    ncupdate = models.CharField(max_length=1000, blank=True, null=True)
    faiupdate = models.CharField(max_length=1000, blank=True, null=True)
    hattach = models.CharField(max_length=1000, blank=True, null=True)
    informtion = models.TextField(blank=True, null=True)
    checkpointsdesc = models.TextField(blank=True, null=True)
    impactattach = models.CharField(max_length=1000, blank=True, null=True)
    reqdetails = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()
    rfd_review = models.TextField(blank=True, null=True)
    noofdays = models.IntegerField()
    prdct_li = models.IntegerField()
    prdct_comnt = models.CharField(max_length=150, blank=True, null=True)
    delete1 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecr_v2_revw'


class EcrV2RevwBackup(models.Model):
    reviewid = models.AutoField(primary_key=True)
    requestno = models.IntegerField()
    reviewtype = models.IntegerField()
    type = models.IntegerField()
    associate = models.IntegerField()
    reviewoutcomesub = models.CharField(max_length=100)
    me_study = models.TextField()
    cost = models.TextField()
    cost_descr = models.TextField()
    date = models.DateField()
    rcomittee = models.CharField(max_length=1000)
    reviewoutcome = models.CharField(max_length=1000)
    holddate = models.DateField()
    comments = models.TextField()
    overreviewpoints = models.TextField()
    checkpoints = models.CharField(max_length=1000)
    horizantal = models.IntegerField()
    mmtag = models.IntegerField()
    tagno = models.IntegerField()
    dept_randd = models.IntegerField()
    ecr_doccat = models.IntegerField()
    mailtopro = models.IntegerField()
    designerfeedback = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    ncstatus = models.IntegerField()
    ncactive = models.IntegerField()
    me_nc_date = models.DateTimeField()
    ncupdate = models.CharField(max_length=1000, blank=True, null=True)
    faiupdate = models.CharField(max_length=1000, blank=True, null=True)
    hattach = models.CharField(max_length=1000, blank=True, null=True)
    informtion = models.TextField(blank=True, null=True)
    checkpointsdesc = models.TextField(blank=True, null=True)
    impactattach = models.CharField(max_length=1000, blank=True, null=True)
    reqdetails = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()
    rfd_review = models.TextField(blank=True, null=True)
    noofdays = models.IntegerField()
    prdct_li = models.IntegerField()
    prdct_comnt = models.CharField(max_length=150, blank=True, null=True)
    delete1 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecr_v2_revw_backup'


class EcrV2Update(models.Model):
    requestno = models.IntegerField()
    targetdate = models.DateField(blank=True, null=True)
    targetdateupdation = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecr_v2_update'


class EcrV2Updation(models.Model):
    requestno = models.IntegerField(blank=True, null=True)
    targetdate = models.CharField(max_length=10, blank=True, null=True)
    targetdateupdation = models.CharField(max_length=10, blank=True, null=True)
    repeatid = models.IntegerField()
    reviewid = models.CharField(max_length=50)
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ecr_v2_updation'


class EdpDailyactivities(models.Model):
    slno = models.AutoField(primary_key=True)
    ntry_date = models.DateField()
    empcode = models.CharField(max_length=6, blank=True, null=True)
    descr = models.TextField(blank=True, null=True)
    entry_by = models.CharField(max_length=6, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'edp_dailyactivities'


class EmpMail(models.Model):
    empcode = models.IntegerField(unique=True)
    empname = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'emp_mail'


class EmpSkillCertMaster(models.Model):
    cid = models.AutoField(primary_key=True)
    cat = models.IntegerField(blank=True, null=True)
    cert_name = models.CharField(max_length=50)
    tcode_substr = models.CharField(max_length=10, blank=True, null=True)
    createdby = models.CharField(max_length=40)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'emp_skill_cert_master'


class EmpSkillEntry(models.Model):
    main_id = models.AutoField(primary_key=True)
    cert_id = models.IntegerField(blank=True, null=True)
    entry_dt = models.DateField(blank=True, null=True)
    empcode = models.IntegerField(blank=True, null=True)
    skill = models.CharField(max_length=10, blank=True, null=True)
    qua_work = models.CharField(max_length=10, blank=True, null=True)
    qty_eval = models.IntegerField(blank=True, null=True)
    prod_eval = models.CharField(max_length=50, blank=True, null=True)
    tool_id = models.CharField(max_length=50, blank=True, null=True)
    period = models.CharField(max_length=10, blank=True, null=True)
    period_from = models.DateField(blank=True, null=True)
    period_to = models.DateField(blank=True, null=True)
    tota_exp = models.CharField(max_length=10, blank=True, null=True)
    medha_exp = models.CharField(max_length=50, blank=True, null=True)
    eop_years = models.IntegerField(blank=True, null=True)
    eop_months = models.IntegerField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    expert_id = models.IntegerField(blank=True, null=True)
    hod_id = models.IntegerField(blank=True, null=True)
    from_dt = models.DateField(blank=True, null=True)
    to_dt = models.DateField(blank=True, null=True)
    effect_dt = models.DateField(blank=True, null=True)
    support_document = models.CharField(max_length=200, blank=True, null=True)
    apr_sts = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    delete1 = models.IntegerField(blank=True, null=True)
    deptcode = models.IntegerField(blank=True, null=True)
    loccode = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp_skill_entry'


class EmpSkillSubEntry(models.Model):
    sub_id = models.AutoField(primary_key=True)
    main_id = models.IntegerField(blank=True, null=True)
    field_id = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'emp_skill_sub_entry'


class Emppan(models.Model):
    pan = models.CharField(max_length=15)
    empcode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'emppan'


class Equipments(models.Model):
    eqpid = models.CharField(max_length=10)
    eqpname = models.CharField(max_length=100)
    deptcode = models.CharField(max_length=8)
    eqptype = models.CharField(max_length=20)
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'equipments'


class ErrBand(models.Model):
    bandname = models.CharField(max_length=100)
    locality = models.CharField(max_length=300)
    cost = models.DecimalField(max_digits=10, decimal_places=0)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'err_band'


class ErrCodes(models.Model):
    code_no = models.IntegerField()
    description = models.CharField(max_length=250)
    developer_msg = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'err_codes'


class ErrSequence(models.Model):
    increment_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'err_sequence'


class Errhand(models.Model):
    name = models.CharField(max_length=1)
    code = models.CharField(max_length=30)
    course = models.CharField(max_length=20)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'errhand'


class ExpertEmployee(models.Model):
    exp_id = models.AutoField(primary_key=True)
    cid = models.IntegerField(blank=True, null=True)
    expert_empcode = models.IntegerField(blank=True, null=True)
    sub_cat = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'expert_employee'


class ExtnMaster(models.Model):
    name = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    loc = models.CharField(max_length=30)
    extn = models.CharField(max_length=15)
    shrt = models.CharField(max_length=15)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'extn_master'


class FaVisualInsp(models.Model):
    fai_ref = models.IntegerField()
    field_id = models.IntegerField()
    value = models.CharField(max_length=8)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fa_visual_insp'


class FaVisualInspMaster(models.Model):
    field_id = models.AutoField(primary_key=True)
    sno = models.CharField(max_length=2)
    parameter = models.CharField(max_length=200)
    type = models.IntegerField()
    delete1 = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fa_visual_insp_master'


class FaiAttachments(models.Model):
    attach_id = models.AutoField(primary_key=True)
    fai_ref = models.IntegerField()
    category = models.CharField(max_length=50, blank=True, null=True)
    attachment = models.CharField(max_length=200, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fai_attachments'


class FaiCaharactDetails(models.Model):
    fai_ref = models.IntegerField(blank=True, null=True)
    partno = models.CharField(max_length=12, blank=True, null=True)
    charno = models.CharField(max_length=150, blank=True, null=True)
    ref_loc = models.CharField(max_length=150, blank=True, null=True)
    designator = models.CharField(max_length=200, blank=True, null=True)
    require = models.CharField(max_length=150, blank=True, null=True)
    results = models.CharField(max_length=150, blank=True, null=True)
    tooling = models.CharField(max_length=150, blank=True, null=True)
    nonconfor = models.CharField(max_length=150, blank=True, null=True)
    action = models.CharField(max_length=150, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    participants = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fai_caharact_details'


class FaiDetails(models.Model):
    fai_ref = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    ntry_date = models.DateField()
    project = models.IntegerField()
    partno = models.CharField(max_length=12, blank=True, null=True)
    rev = models.CharField(max_length=11, blank=True, null=True)
    draw = models.CharField(max_length=50, blank=True, null=True)
    draw_rev = models.CharField(max_length=11, blank=True, null=True)
    serial = models.CharField(max_length=11, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    full_par = models.CharField(max_length=15, blank=True, null=True)
    resn_par = models.CharField(max_length=150)
    supplier = models.CharField(max_length=20, blank=True, null=True)
    refno = models.CharField(max_length=30, blank=True, null=True)
    pono = models.CharField(max_length=20, blank=True, null=True)
    add_chang = models.CharField(max_length=50, blank=True, null=True)
    internal_supplier = models.CharField(max_length=20, blank=True, null=True)
    organza = models.CharField(max_length=20, blank=True, null=True)
    basepartno = models.CharField(max_length=20, blank=True, null=True)
    rev_level = models.CharField(max_length=10, blank=True, null=True)
    report = models.CharField(max_length=100)
    drawing = models.CharField(max_length=100)
    form1 = models.CharField(max_length=3, blank=True, null=True)
    form1_comm = models.CharField(max_length=100, blank=True, null=True)
    form2 = models.CharField(max_length=3, blank=True, null=True)
    form2_comm = models.CharField(max_length=100, blank=True, null=True)
    form3 = models.CharField(max_length=3, blank=True, null=True)
    form3_comm = models.CharField(max_length=100, blank=True, null=True)
    draw_ball = models.CharField(max_length=3, blank=True, null=True)
    draw_ball_comm = models.CharField(max_length=100, blank=True, null=True)
    bill_of_mat = models.CharField(max_length=3, blank=True, null=True)
    bill_of_mat_comm = models.CharField(max_length=100, blank=True, null=True)
    raw_mat = models.CharField(max_length=3, blank=True, null=True)
    raw_mat_comm = models.CharField(max_length=100, blank=True, null=True)
    process_flow = models.CharField(max_length=3, blank=True, null=True)
    process_flow_comm = models.CharField(max_length=100, blank=True, null=True)
    control_plan = models.CharField(max_length=3, blank=True, null=True)
    control_plan_comm = models.CharField(max_length=100, blank=True, null=True)
    manuf_route = models.CharField(max_length=3, blank=True, null=True)
    manuf_route_comm = models.CharField(max_length=100, blank=True, null=True)
    certificate = models.CharField(max_length=3, blank=True, null=True)
    certificate_comm = models.CharField(max_length=100, blank=True, null=True)
    functest = models.CharField(max_length=3, blank=True, null=True)
    functest_comm = models.CharField(max_length=100, blank=True, null=True)
    final_ins = models.CharField(max_length=3, blank=True, null=True)
    final_ins_comm = models.CharField(max_length=100, blank=True, null=True)
    ncr_details = models.CharField(max_length=3, blank=True, null=True)
    ecr_datails = models.CharField(max_length=40, blank=True, null=True)
    ncr_details_comm = models.CharField(max_length=100, blank=True, null=True)
    sub_com = models.CharField(max_length=3, blank=True, null=True)
    sub_com_comm = models.CharField(max_length=100, blank=True, null=True)
    trace_req = models.CharField(max_length=10, blank=True, null=True)
    trace_req_comm = models.CharField(max_length=50, blank=True, null=True)
    oth_doc = models.CharField(max_length=3, blank=True, null=True)
    oth_doc_comm = models.CharField(max_length=100, blank=True, null=True)
    partcnt = models.IntegerField()
    complete = models.CharField(max_length=3, blank=True, null=True)
    gl = models.CharField(max_length=6, blank=True, null=True)
    gl_sts = models.IntegerField()
    gl_date = models.DateField()
    hod = models.IntegerField()
    hod_date = models.DateField()
    hod_sts = models.IntegerField()
    hod_comm = models.CharField(max_length=250, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    fairefno = models.CharField(max_length=50, blank=True, null=True)
    prepared_by = models.IntegerField()
    approved_by = models.IntegerField()
    prod_qty = models.IntegerField()
    fai_date = models.DateField()
    fai_note = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fai_details'


class FaiForm3Creation(models.Model):
    mid = models.AutoField(primary_key=True)
    partno = models.CharField(max_length=12, blank=True, null=True)
    charno = models.CharField(max_length=150, blank=True, null=True)
    designator = models.CharField(max_length=200, blank=True, null=True)
    requirement = models.CharField(max_length=150, blank=True, null=True)
    results = models.CharField(max_length=150, blank=True, null=True)
    measurement_tool = models.CharField(max_length=150, blank=True, null=True)
    nonconfor = models.CharField(max_length=150, blank=True, null=True)
    action = models.CharField(max_length=150, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fai_form3creation'


class FaiMaster(models.Model):
    mid = models.AutoField(primary_key=True)
    partno = models.CharField(max_length=12, blank=True, null=True)
    project = models.IntegerField(blank=True, null=True)
    rev = models.IntegerField()
    draw = models.CharField(max_length=12, blank=True, null=True)
    draw_rev = models.IntegerField()
    serial = models.CharField(max_length=11)
    type = models.CharField(max_length=20, blank=True, null=True)
    full_par = models.CharField(max_length=15, blank=True, null=True)
    supplier = models.CharField(max_length=10, blank=True, null=True)
    refno = models.CharField(max_length=30, blank=True, null=True)
    pono = models.CharField(max_length=20, blank=True, null=True)
    fairefno = models.CharField(max_length=20, blank=True, null=True)
    prod_qty = models.IntegerField()
    fai_date = models.DateField()
    material = models.CharField(max_length=150, blank=True, null=True)
    specif = models.CharField(max_length=150, blank=True, null=True)
    custno = models.CharField(max_length=150, blank=True, null=True)
    certifno = models.CharField(max_length=150, blank=True, null=True)
    funcno = models.CharField(max_length=150, blank=True, null=True)
    acceptno = models.CharField(max_length=150, blank=True, null=True)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fai_master'


class FaiNcDetails(models.Model):
    nc_id = models.AutoField(primary_key=True)
    fai_ref = models.IntegerField()
    supp = models.IntegerField()
    supplier_selection = models.CharField(max_length=15, blank=True, null=True)
    supp_email = models.CharField(max_length=50, blank=True, null=True)
    supp_mobile = models.CharField(max_length=15, blank=True, null=True)
    cust_name = models.CharField(max_length=50, blank=True, null=True)
    cust_addr = models.CharField(max_length=50, blank=True, null=True)
    cust_mob = models.CharField(max_length=15, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    reason_non = models.TextField(blank=True, null=True)
    measure_non = models.CharField(max_length=50, blank=True, null=True)
    cust_ref = models.CharField(max_length=50, blank=True, null=True)
    respon = models.CharField(max_length=100, blank=True, null=True)
    due_date = models.CharField(max_length=15, blank=True, null=True)
    aff_qty = models.IntegerField()
    appove_by = models.CharField(max_length=15, blank=True, null=True)
    req_app = models.IntegerField()
    rea_rej = models.CharField(max_length=50, blank=True, null=True)
    ord_yes = models.CharField(max_length=50, blank=True, null=True)
    serial_yes = models.CharField(max_length=10, blank=True, null=True)
    eff_qty = models.IntegerField()
    trace_det = models.CharField(max_length=50, blank=True, null=True)
    close_date = models.CharField(max_length=20)
    createdby = models.CharField(max_length=6, blank=True, null=True)
    ntry_date = models.DateField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fai_nc_details'


class FaiPartDetails(models.Model):
    part_ref = models.AutoField(primary_key=True)
    fai_ref = models.IntegerField()
    partno = models.CharField(max_length=50, blank=True, null=True)
    partserno = models.CharField(max_length=50, blank=True, null=True)
    fai_rep_no = models.CharField(max_length=50, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fai_part_details'


class FaiProcessDetails(models.Model):
    proce_id = models.AutoField(primary_key=True)
    fai_ref = models.IntegerField()
    processname = models.CharField(max_length=150)
    processid = models.CharField(max_length=120, blank=True, null=True)
    processpurpose = models.CharField(max_length=120, blank=True, null=True)
    remarks = models.CharField(max_length=150, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fai_process_details'


class FaiProdDetails(models.Model):
    prod_id = models.AutoField(primary_key=True)
    fai_ref = models.IntegerField()
    material = models.CharField(max_length=150, blank=True, null=True)
    specif = models.CharField(max_length=150, blank=True, null=True)
    supplier = models.CharField(max_length=150, blank=True, null=True)
    custno = models.CharField(max_length=150)
    certifno = models.CharField(max_length=150)
    funcno = models.CharField(max_length=150)
    acceptno = models.CharField(max_length=150)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fai_prod_details'


class FailureCategory(models.Model):
    fc_no = models.AutoField(primary_key=True)
    fc_name = models.CharField(max_length=50)
    createdby = models.SmallIntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failure_category'


class FailureStage(models.Model):
    fs_no = models.AutoField(primary_key=True)
    fs_name = models.CharField(max_length=50)
    createdby = models.SmallIntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failure_stage'


class FamDe(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fam_de'


class FatNtry(models.Model):
    rno = models.AutoField(primary_key=True)
    zone = models.IntegerField()
    category = models.CharField(max_length=30)
    station = models.CharField(max_length=150)
    observation = models.TextField()
    attachment = models.CharField(max_length=150)
    createdby = models.CharField(max_length=7)
    ntry_date = models.DateField()
    designer = models.CharField(max_length=7)
    gl = models.CharField(max_length=7)
    gl_comment = models.CharField(max_length=200)
    gl_date = models.DateField()
    status = models.CharField(max_length=10)
    observation_related = models.CharField(max_length=3)
    desgn_comment = models.TextField()
    desgn_date = models.DateField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fat_ntry'


class FatStatusMaster(models.Model):
    status = models.CharField(max_length=100)
    createdby = models.CharField(max_length=7)
    delete1 = models.IntegerField()
    deletedby = models.CharField(max_length=7)
    deleteddate = models.DateField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fat_status_master'


class FfaAttachmentsNtry(models.Model):
    slno = models.IntegerField()
    attachment = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    delete_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'ffa_attachments_ntry'


class FfaNtry(models.Model):
    slno = models.AutoField(primary_key=True)
    frno = models.IntegerField()
    ffarno_date = models.CharField(max_length=30)
    ntry_date = models.DateField()
    product = models.CharField(max_length=100)
    production_name = models.CharField(max_length=50)
    resp_name = models.CharField(max_length=50)
    resp = models.CharField(max_length=100)
    shed = models.CharField(max_length=150)
    loco = models.CharField(max_length=150)
    doc = models.CharField(max_length=30)
    problem_rep = models.CharField(max_length=500)
    prob_cat = models.IntegerField()
    status = models.IntegerField()
    mom_decision = models.CharField(max_length=300)
    mon_ntryby = models.IntegerField()
    mom_date = models.DateField()
    analy_status = models.CharField(max_length=300)
    analy_ntryby = models.IntegerField()
    analy_date = models.DateField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    delete_date = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ffa_ntry'


class FfaProbCatMaster(models.Model):
    prob_cat_no = models.AutoField(primary_key=True)
    prob_cat_name = models.CharField(max_length=50)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    delete_date = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ffa_prob_cat_master'


class FfaStatusMaster(models.Model):
    sts_slno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    delete_date = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ffa_status_master'


class FfaStatusNtry(models.Model):
    slno = models.IntegerField()
    mom_decision = models.CharField(max_length=500)
    mom_date = models.DateField()
    analy_status = models.CharField(max_length=500)
    mom_ntry_sts = models.IntegerField()
    ana_ntry_sts = models.IntegerField()
    date = models.DateField()
    mom_mail_to = models.IntegerField()
    analysis_mail_to = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ffa_status_ntry'


class FfasrMatGrpMster(models.Model):
    matid = models.AutoField(primary_key=True)
    mat_grp = models.IntegerField()
    mat_code = models.CharField(max_length=15, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ffasr_mat_grp_mster'


class FfasrProdIchargedata(models.Model):
    project_no = models.IntegerField()
    project = models.CharField(max_length=100, blank=True, null=True)
    incharge = models.IntegerField()
    category = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ffasr_prod_ichargedata'


class FfasrRepAssign(models.Model):
    parent_reportno = models.IntegerField()
    child_reportno = models.IntegerField()
    empcode = models.IntegerField()
    entrydate = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'ffasr_rep_assign'





class FfasrrootCauseMaster(models.Model):
    project_code = models.CharField(max_length=30, blank=True, null=True)
    mat_grp = models.IntegerField(blank=True, null=True)
    root_cause_cat = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ffasrroot_cause_master'


class Ffasrtest(models.Model):
    reportno = models.IntegerField()
    editdata = models.CharField(max_length=500)
    empcode = models.IntegerField()
    timestamp = models.DateTimeField()
    frbdata_comment = models.CharField(max_length=300)
    frbrepno = models.IntegerField()
    assinee_code = models.CharField(max_length=300)
    currentdate = models.DateField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ffasrtest'


class FontSizeMaster(models.Model):
    size = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'font_size_master'


class Form16Temp(models.Model):
    empcode = models.IntegerField()
    mail_indi = models.CharField(max_length=11)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'form16_temp'


class FormDescriptionMaster(models.Model):
    slno = models.IntegerField()
    form = models.CharField(max_length=1)
    sub_seq_slno = models.CharField(max_length=4)
    desc = models.CharField(max_length=300)
    p = models.IntegerField()
    a = models.IntegerField()
    g = models.IntegerField()
    gp = models.IntegerField()
    e = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=200)
    period_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'form_description_master'


class FormMaster(models.Model):
    formname = models.CharField(primary_key=True, max_length=50)
    section = models.CharField(max_length=40)
    admin = models.SmallIntegerField()
    superuser = models.SmallIntegerField()
    supervisor = models.SmallIntegerField()
    user = models.SmallIntegerField()
    dept = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'form_master'


class FormMasterAdmin(models.Model):
    deptcode = models.IntegerField()
    rolename = models.CharField(max_length=50)
    formname = models.CharField(max_length=50)
    view = models.IntegerField()
    save = models.IntegerField()
    update1 = models.IntegerField()
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'form_master_admin'


class FracasAlphabet(models.Model):
    card_matcode = models.CharField(max_length=30, blank=True, null=True)
    module_matcode = models.CharField(max_length=30, blank=True, null=True)
    alphabet = models.CharField(max_length=20, blank=True, null=True)
    project = models.CharField(max_length=24, blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fracas_alphabet'


class FracasAlphabetOld(models.Model):
    card_matcode = models.CharField(max_length=30, blank=True, null=True)
    module_matcode = models.CharField(max_length=30, blank=True, null=True)
    alphabet = models.CharField(max_length=20, blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fracas_alphabet_old'


class FracasBomData(models.Model):
    sno = models.AutoField(primary_key=True)
    project = models.CharField(max_length=50, blank=True, null=True)
    parent_matcode = models.CharField(max_length=25, blank=True, null=True)
    child_matcode = models.CharField(max_length=25, blank=True, null=True)
    mainlevel = models.IntegerField()
    componentlevel = models.IntegerField()
    qty = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fracas_bom_data'


class FracasBomData2(models.Model):
    sno = models.AutoField(primary_key=True)
    project = models.CharField(max_length=50, blank=True, null=True)
    parent_matcode = models.CharField(max_length=20, blank=True, null=True)
    child_matcode = models.CharField(max_length=20, blank=True, null=True)
    slno_prof = models.CharField(max_length=10, blank=True, null=True)
    qty = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fracas_bom_data2'


class FracasBomDataTest(models.Model):
    sno = models.AutoField(primary_key=True)
    parent_matcode = models.CharField(max_length=20)
    child_matcode = models.CharField(max_length=20)
    qty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fracas_bom_data_test'


class FracasCatMaster(models.Model):
    name = models.CharField(max_length=1000)
    cat_type = models.IntegerField()
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fracas_cat_master'


class FracasColourMaster(models.Model):
    empcode = models.CharField(max_length=6, blank=True, null=True)
    colorcode = models.CharField(max_length=150, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fracas_colour_master'


class FracasCommisionSub(models.Model):
    slno = models.AutoField(primary_key=True)
    uniq_slno = models.IntegerField()
    subsystemcode = models.CharField(max_length=200)
    subsystemname = models.CharField(max_length=500)
    subsystemslno = models.CharField(max_length=500)
    parentid = models.CharField(max_length=500)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fracas_commision_sub'


class FracasFieldCommisioning(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    entrydate = models.DateField()
    instype = models.CharField(max_length=10)
    locono = models.CharField(max_length=500)
    locotype = models.CharField(max_length=500)
    zone = models.CharField(max_length=1000)
    shed = models.CharField(max_length=1000)
    project = models.CharField(max_length=500)
    premarks = models.TextField()
    stardate = models.DateField()
    endate = models.DateField()
    periodno = models.IntegerField()
    periodtype = models.CharField(max_length=500)
    typewarrenty = models.IntegerField()
    tremarks = models.TextField()
    decomm = models.DateField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fracas_field_commisioning'


class FracasFinalScan(models.Model):
    mat_code = models.CharField(max_length=20)
    serial_no = models.IntegerField()
    department_from = models.IntegerField()
    department_to = models.IntegerField()
    empcode = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fracas_final_scan'


class FracasLabelPrinting(models.Model):
    sno = models.AutoField(primary_key=True)
    orderno = models.CharField(max_length=20)
    batchfrom = models.CharField(max_length=50)
    batchto = models.CharField(max_length=50)
    matcode = models.CharField(max_length=20)
    child_matcode = models.CharField(max_length=20)
    project = models.CharField(max_length=50)
    dept = models.IntegerField()
    status = models.IntegerField()
    empcode = models.IntegerField()
    remarks = models.CharField(max_length=80, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fracas_label_printing'


class FracasMain(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    entrydate = models.DateField()
    instype = models.CharField(max_length=10)
    locono = models.CharField(max_length=500)
    locotype = models.CharField(max_length=500)
    zone = models.CharField(max_length=1000)
    shed = models.CharField(max_length=1000)
    project = models.CharField(max_length=500)
    premarks = models.TextField()
    stardate = models.DateField()
    endate = models.DateField()
    periodno = models.IntegerField()
    periodtype = models.CharField(max_length=500)
    typewarrenty = models.IntegerField()
    tremarks = models.TextField()
    decomm = models.DateField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fracas_main'


class FracasMain30082021(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    entrydate = models.DateField()
    instype = models.CharField(max_length=10)
    locono = models.CharField(max_length=500)
    locotype = models.CharField(max_length=500)
    zone = models.CharField(max_length=1000)
    shed = models.CharField(max_length=1000)
    project = models.CharField(max_length=500)
    premarks = models.TextField()
    stardate = models.DateField()
    endate = models.DateField()
    periodno = models.IntegerField()
    periodtype = models.CharField(max_length=500)
    typewarrenty = models.IntegerField()
    tremarks = models.TextField()
    decomm = models.DateField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fracas_main_30-08-2021'


class FracasPlaningdata(models.Model):
    project = models.CharField(max_length=255)
    createdon = models.DateField()
    orderno = models.IntegerField()
    matcode = models.CharField(max_length=250)
    description = models.CharField(max_length=255)
    qty = models.IntegerField()
    batch = models.CharField(max_length=250)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    slno = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'fracas_planingdata'


class FracasPlaningdata1(models.Model):
    slno = models.AutoField(primary_key=True)
    project = models.CharField(max_length=255)
    createdon = models.DateField()
    orderno = models.IntegerField()
    matcode = models.CharField(max_length=250)
    description = models.CharField(max_length=255)
    qty = models.IntegerField()
    batch = models.CharField(max_length=250)
    remarks = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fracas_planingdata1'


class FracasPlaningdummy(models.Model):
    slno = models.AutoField(primary_key=True)
    project = models.CharField(max_length=255)
    createdon = models.DateField()
    orderno = models.IntegerField()
    matcode = models.CharField(max_length=250)
    description = models.CharField(max_length=255)
    qty = models.IntegerField()
    batch = models.CharField(max_length=250)
    remarks = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fracas_planingdummy'


class FracasPopSub(models.Model):
    slno = models.AutoField(primary_key=True)
    uniq_slno = models.IntegerField()
    subsystemcode = models.CharField(max_length=200, blank=True, null=True)
    subsystemname = models.CharField(max_length=500, blank=True, null=True)
    subsystemslno = models.CharField(max_length=500, blank=True, null=True)
    parentid = models.CharField(max_length=500, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fracas_pop_sub'


class FracasProdData(models.Model):
    tag_id = models.AutoField(primary_key=True)
    project = models.CharField(max_length=20, blank=True, null=True)
    parent_code = models.CharField(max_length=20, blank=True, null=True)
    child_id = models.CharField(max_length=50, blank=True, null=True)
    batch = models.CharField(max_length=20, blank=True, null=True)
    prod_order = models.CharField(max_length=40, blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fracas_prod_data'


class FracasTobeAssgn(models.Model):
    order_no = models.IntegerField()
    child_mat = models.CharField(max_length=15)
    child_slno = models.CharField(max_length=11)
    parent_mat = models.CharField(max_length=15)
    parent_slno = models.CharField(max_length=11)
    department = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fracas_tobe_assgn'


class FreightDetailsNtry(models.Model):
    fid = models.AutoField(primary_key=True)
    datetime = models.DateField()
    vehicleno = models.CharField(max_length=20, blank=True, null=True)
    noof_feet = models.CharField(max_length=10, blank=True, null=True)
    goods_by = models.CharField(max_length=50, blank=True, null=True)
    dc_no = models.CharField(max_length=20, blank=True, null=True)
    dc_date = models.DateField()
    vendorname = models.CharField(max_length=100, blank=True, null=True)
    disp_vend = models.CharField(max_length=150, blank=True, null=True)
    noof_items = models.CharField(max_length=50, blank=True, null=True)
    freight_name = models.IntegerField(blank=True, null=True)
    docket_no = models.CharField(max_length=50, blank=True, null=True)
    docket_date = models.DateField()
    noof_pack = models.CharField(max_length=50, blank=True, null=True)
    security_empcode = models.CharField(max_length=11, blank=True, null=True)
    driver_name = models.CharField(max_length=50, blank=True, null=True)
    driver_mobile = models.CharField(max_length=20, blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    update_by = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    intime = models.CharField(max_length=20)
    outtime = models.CharField(max_length=20, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    delay = models.IntegerField()
    delay_reason = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()
    unload_noofpers = models.IntegerField()
    remarks = models.CharField(max_length=100, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'freight_details_ntry'


class Fuelreimbursesubdata(models.Model):
    id = models.BigAutoField(primary_key=True)
    ref_no = models.IntegerField()
    vechicleno = models.CharField(max_length=50)
    bill_no = models.IntegerField()
    bill_date = models.DateField()
    bill_amount = models.IntegerField()
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fuelreimbursesubdata'


class GlUpdateMaster(models.Model):
    empcode = models.IntegerField()
    gl = models.IntegerField()
    mgr = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gl_update_master'


class HcmApprovalMaster(models.Model):
    indicator = models.IntegerField()
    role = models.CharField(max_length=10)
    empcode = models.CharField(max_length=11)
    type = models.CharField(max_length=5)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hcm_approval_master'


class HcmApprovalMaster2(models.Model):
    dept = models.CharField(max_length=20)
    apprentice = models.CharField(db_column='Apprentice', max_length=10)  # Field name made lowercase.
    consultant = models.CharField(db_column='Consultant', max_length=20)  # Field name made lowercase.
    regular = models.CharField(db_column='Regular', max_length=20)  # Field name made lowercase.
    contract = models.CharField(db_column='Contract', max_length=20)  # Field name made lowercase.
    parttime = models.CharField(db_column='PartTime', max_length=20)  # Field name made lowercase.
    type = models.CharField(max_length=10)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hcm_approval_master2'


class HcmApprovalMaster2Old(models.Model):
    dept = models.CharField(max_length=20)
    apprentice = models.CharField(db_column='Apprentice', max_length=10)  # Field name made lowercase.
    consultant = models.CharField(db_column='Consultant', max_length=20)  # Field name made lowercase.
    regular = models.CharField(db_column='Regular', max_length=20)  # Field name made lowercase.
    contract = models.CharField(db_column='Contract', max_length=20)  # Field name made lowercase.
    parttime = models.CharField(db_column='PartTime', max_length=20)  # Field name made lowercase.
    type = models.CharField(max_length=10)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hcm_approval_master2_old'


class HcmApprovalMasterOld(models.Model):
    indicator = models.IntegerField()
    role = models.CharField(max_length=10)
    empcode = models.CharField(max_length=11)
    type = models.CharField(max_length=5)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hcm_approval_master_old'


class HcmCandDetails(models.Model):
    slno = models.AutoField(primary_key=True)
    cid = models.IntegerField(blank=True, null=True)
    res_id = models.IntegerField()
    p_prefix = models.IntegerField()
    p_fname = models.CharField(max_length=40, blank=True, null=True)
    p_lname = models.CharField(max_length=40, blank=True, null=True)
    p_gender = models.CharField(max_length=2)
    p_email = models.CharField(max_length=100, blank=True, null=True)
    p_dob = models.DateField(blank=True, null=True)
    p_mobile = models.CharField(max_length=30, blank=True, null=True)
    p_emobile = models.CharField(max_length=16, blank=True, null=True)
    p_birthplace = models.CharField(max_length=40, blank=True, null=True)
    p_religion = models.CharField(max_length=6, blank=True, null=True)
    p_bloodgroup = models.CharField(max_length=6, blank=True, null=True)
    p_pancard = models.CharField(max_length=30, blank=True, null=True)
    p_aadharno = models.CharField(max_length=30, blank=True, null=True)
    p_aadhar_attach = models.TextField(blank=True, null=True)
    p_pan_attach = models.TextField(blank=True, null=True)
    per_careoff = models.CharField(max_length=40, blank=True, null=True)
    per_street = models.TextField(blank=True, null=True)
    per_address = models.TextField(blank=True, null=True)
    per_pincode = models.CharField(max_length=10, blank=True, null=True)
    per_region = models.CharField(max_length=3, blank=True, null=True)
    per_city = models.CharField(max_length=40, blank=True, null=True)
    per_dist = models.CharField(max_length=40, blank=True, null=True)
    pre_careoff = models.CharField(max_length=40, blank=True, null=True)
    pre_street = models.TextField(blank=True, null=True)
    pre_address = models.TextField(blank=True, null=True)
    pre_pincode = models.CharField(max_length=10, blank=True, null=True)
    pre_region = models.CharField(max_length=3, blank=True, null=True)
    pre_city = models.CharField(max_length=40, blank=True, null=True)
    pre_dist = models.CharField(max_length=40, blank=True, null=True)
    f_fname = models.CharField(max_length=40, blank=True, null=True)
    f_lname = models.CharField(max_length=40, blank=True, null=True)
    f_dob = models.DateField()
    f_gender = models.IntegerField(blank=True, null=True)
    m_fname = models.CharField(max_length=40, blank=True, null=True)
    m_lname = models.CharField(max_length=40, blank=True, null=True)
    m_dob = models.DateField()
    m_gender = models.IntegerField()
    married_status = models.CharField(max_length=10, blank=True, null=True)
    no_of_childrens = models.IntegerField()
    marriage_date = models.DateField()
    s_fname = models.CharField(max_length=40, blank=True, null=True)
    s_lname = models.CharField(max_length=40, blank=True, null=True)
    s_dob = models.DateField()
    s_gender = models.IntegerField()
    edu_est = models.IntegerField()
    edu_course = models.IntegerField()
    inst_name = models.CharField(max_length=80)
    course_dur = models.CharField(max_length=3)
    course_start_date = models.DateField()
    course_end_date = models.DateField()
    course_per = models.CharField(max_length=5, blank=True, null=True)
    exp_status = models.CharField(max_length=4, blank=True, null=True)
    sap_ref = models.CharField(max_length=50)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hcm_cand_details'


class HcmChildDetails(models.Model):
    cslno = models.AutoField(primary_key=True)
    res_id = models.IntegerField(blank=True, null=True)
    cid = models.IntegerField()
    child_no = models.IntegerField()
    c_fname = models.CharField(max_length=40, blank=True, null=True)
    c_lname = models.CharField(max_length=40, blank=True, null=True)
    c_dob = models.DateField()
    c_gender = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hcm_child_details'


class HcmEduCourse(models.Model):
    slno = models.IntegerField(primary_key=True)
    edu_course_index = models.IntegerField(blank=True, null=True)
    edu_index = models.IntegerField(blank=True, null=True)
    edu_name = models.CharField(max_length=40, blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    delete1 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hcm_edu_course'


class HcmEducEst(models.Model):
    slno = models.IntegerField(primary_key=True)
    edu_index = models.IntegerField(blank=True, null=True)
    edu_name = models.CharField(max_length=13, blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    delete1 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hcm_educ_est'


class HcmExperienceDetails(models.Model):
    exp_slno = models.AutoField(primary_key=True)
    cid = models.IntegerField(blank=True, null=True)
    res_id = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    city = models.CharField(max_length=60, blank=True, null=True)
    employer_name = models.CharField(max_length=60)
    salary = models.CharField(max_length=10, blank=True, null=True)
    experience = models.CharField(max_length=5, blank=True, null=True)
    leave_reason = models.CharField(max_length=100, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hcm_experience_details'


class HcmHiring(models.Model):
    res_id = models.IntegerField(primary_key=True)
    jn_date = models.DateField()
    job = models.CharField(max_length=11)
    per_area = models.CharField(max_length=10, blank=True, null=True)
    dept = models.IntegerField()
    report_mgr = models.IntegerField()
    empgroup = models.CharField(max_length=5, blank=True, null=True)
    subempgroup = models.CharField(max_length=5, blank=True, null=True)
    conrt_type = models.IntegerField()
    work_sch = models.CharField(max_length=10, blank=True, null=True)
    tms_status = models.IntegerField()
    eva_gra = models.IntegerField()
    work_loc = models.CharField(max_length=50)
    payscale = models.CharField(max_length=5, blank=True, null=True)
    payscalearea = models.CharField(max_length=5, blank=True, null=True)
    paygroup = models.CharField(max_length=2, blank=True, null=True)
    pay_subempgroup = models.CharField(max_length=3, blank=True, null=True)
    ot_flag = models.CharField(max_length=1)
    restr = models.IntegerField()
    pro_per_no = models.IntegerField()
    dis_empr = models.IntegerField()
    dis_empe = models.IntegerField()
    task_ty = models.IntegerField()
    task_dt = models.DateField()
    ty_core = models.CharField(max_length=10, blank=True, null=True)
    released = models.IntegerField()
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hcm_hiring'


class HcmHiringSal(models.Model):
    salid = models.AutoField(primary_key=True)
    res_id = models.IntegerField()
    conrt_type = models.IntegerField()
    sal_type = models.CharField(max_length=10, blank=True, null=True)
    salary = models.FloatField()
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hcm_hiring_sal'


class HcmJobEvaMaster(models.Model):
    eid = models.AutoField(primary_key=True)
    eva_gra = models.IntegerField()
    descrip = models.CharField(max_length=100, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hcm_job_eva_master'


class HcmJobMaster(models.Model):
    sid = models.IntegerField(primary_key=True)
    job_id = models.IntegerField()
    designation = models.CharField(max_length=50, blank=True, null=True)
    obj_abbr = models.CharField(max_length=15, blank=True, null=True)
    obj_name = models.CharField(max_length=15, blank=True, null=True)
    job_key = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hcm_job_master'


class HcmNomineeDetails(models.Model):
    nom_slno = models.AutoField(primary_key=True)
    res_id = models.IntegerField()
    cid = models.IntegerField()
    name = models.CharField(max_length=70, blank=True, null=True)
    relation = models.CharField(max_length=40, blank=True, null=True)
    dob = models.DateField()
    esi = models.IntegerField()
    pf = models.IntegerField()
    sss = models.IntegerField()
    gratuity = models.IntegerField()
    pension = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hcm_nominee_details'


class HcmPayGrpMaster(models.Model):
    mid = models.AutoField(primary_key=True)
    grp = models.CharField(max_length=2, blank=True, null=True)
    sub_grp = models.CharField(max_length=3, blank=True, null=True)
    category = models.CharField(max_length=5, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hcm_pay_grp_master'


class HcmPaySclMaster(models.Model):
    mas_id = models.AutoField(primary_key=True)
    loc_id = models.CharField(max_length=10, blank=True, null=True)
    pay_scl = models.CharField(max_length=2, blank=True, null=True)
    pay_scl_desc = models.CharField(max_length=30)
    pay_typ = models.CharField(max_length=2, blank=True, null=True)
    pay_typ_desc = models.CharField(max_length=30, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hcm_pay_scl_master'


class HcmPersonReg(models.Model):
    per_ref_no = models.AutoField(primary_key=True)
    person = models.CharField(max_length=100)
    father = models.CharField(max_length=100)
    main_qualif = models.IntegerField()
    sub_qualif = models.IntegerField()
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    dob = models.DateField()
    experi = models.CharField(max_length=30)
    keyskill = models.CharField(max_length=100)
    ref = models.CharField(max_length=20)
    ref_det = models.CharField(max_length=100)
    resume = models.CharField(max_length=100)
    createdby = models.IntegerField()
    active = models.IntegerField()
    ntry_date = models.DateField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hcm_person_reg'


class HcmRefData(models.Model):
    refid = models.AutoField(primary_key=True)
    ack = models.IntegerField()
    res_id = models.IntegerField()
    refassoc = models.IntegerField()
    amt = models.IntegerField()
    paidsts = models.IntegerField()
    paidamt = models.IntegerField()
    paidby = models.IntegerField()
    paidon = models.DateField(blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hcm_ref_data'


class HcmReplaceList(models.Model):
    slno = models.AutoField(primary_key=True)
    ack = models.IntegerField()
    empcode = models.IntegerField()
    leave_reason = models.CharField(max_length=150, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hcm_replace_list'


class HcmReqDetails(models.Model):
    ack = models.AutoField(primary_key=True)
    empcode = models.IntegerField(blank=True, null=True)
    ntry_date = models.DateField()
    main_position = models.CharField(max_length=100, blank=True, null=True)
    sub_position = models.CharField(max_length=100, blank=True, null=True)
    req_dept = models.IntegerField()
    noofvac = models.IntegerField()
    type_vac = models.CharField(max_length=50, blank=True, null=True)
    replaceass = models.CharField(max_length=1000, blank=True, null=True)
    reporteto = models.IntegerField()
    experience = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    station = models.CharField(max_length=20, blank=True, null=True)
    out_sta = models.CharField(max_length=50, blank=True, null=True)
    leadtime = models.CharField(max_length=10, blank=True, null=True)
    lead_days = models.IntegerField()
    nature = models.CharField(max_length=20, blank=True, null=True)
    req_main_qualif = models.CharField(max_length=100, blank=True, null=True)
    req_sub_qualif = models.CharField(max_length=50, blank=True, null=True)
    des_main_qualif = models.CharField(max_length=100, blank=True, null=True)
    des_sub_qualif = models.CharField(max_length=30, blank=True, null=True)
    knowled = models.TextField(blank=True, null=True)
    knowled_des = models.TextField(blank=True, null=True)
    main_dut = models.TextField(blank=True, null=True)
    attach = models.CharField(max_length=100, blank=True, null=True)
    hod = models.IntegerField()
    hod_sts = models.IntegerField()
    hod_comm = models.CharField(max_length=100, blank=True, null=True)
    hod_date = models.DateField()
    head = models.IntegerField()
    head_sts = models.IntegerField()
    head_comm = models.CharField(max_length=200, blank=True, null=True)
    head_date = models.DateField()
    hr = models.IntegerField()
    hr_sts = models.IntegerField()
    hr_comm = models.CharField(max_length=100, blank=True, null=True)
    hr_date = models.DateField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    md = models.IntegerField()
    md_sts = models.IntegerField()
    md_comm = models.CharField(max_length=100, blank=True, null=True)
    md_date = models.DateField()
    hr_assign_sts = models.IntegerField()
    hr_assign = models.CharField(max_length=6, blank=True, null=True)
    hr_assign_date = models.DateField()
    hr_no_vac = models.IntegerField()
    target_date = models.DateField()
    closed_date = models.DateField()
    refamt = models.IntegerField()
    company = models.IntegerField()
    selected = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hcm_req_details'


class HcmReqDetails090322(models.Model):
    ack = models.AutoField(primary_key=True)
    empcode = models.IntegerField(blank=True, null=True)
    ntry_date = models.DateField()
    main_position = models.CharField(max_length=100, blank=True, null=True)
    sub_position = models.CharField(max_length=100, blank=True, null=True)
    req_dept = models.IntegerField()
    noofvac = models.IntegerField()
    type_vac = models.CharField(max_length=50, blank=True, null=True)
    replaceass = models.CharField(max_length=100, blank=True, null=True)
    reporteto = models.IntegerField()
    experience = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    station = models.CharField(max_length=20, blank=True, null=True)
    out_sta = models.CharField(max_length=50, blank=True, null=True)
    leadtime = models.CharField(max_length=10, blank=True, null=True)
    lead_days = models.IntegerField()
    nature = models.CharField(max_length=20, blank=True, null=True)
    req_main_qualif = models.CharField(max_length=100, blank=True, null=True)
    req_sub_qualif = models.CharField(max_length=50, blank=True, null=True)
    des_main_qualif = models.CharField(max_length=100, blank=True, null=True)
    des_sub_qualif = models.CharField(max_length=30, blank=True, null=True)
    knowled = models.TextField(blank=True, null=True)
    knowled_des = models.TextField(blank=True, null=True)
    main_dut = models.TextField(blank=True, null=True)
    attach = models.CharField(max_length=100, blank=True, null=True)
    hod = models.IntegerField()
    hod_sts = models.IntegerField()
    hod_comm = models.CharField(max_length=100, blank=True, null=True)
    hod_date = models.DateField()
    head = models.IntegerField()
    head_sts = models.IntegerField()
    head_comm = models.CharField(max_length=200, blank=True, null=True)
    head_date = models.DateField()
    hr = models.IntegerField()
    hr_sts = models.IntegerField()
    hr_comm = models.CharField(max_length=100, blank=True, null=True)
    hr_date = models.DateField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    md = models.IntegerField()
    md_sts = models.IntegerField()
    md_comm = models.CharField(max_length=100, blank=True, null=True)
    md_date = models.DateField()
    hr_assign_sts = models.IntegerField()
    hr_assign = models.CharField(max_length=6, blank=True, null=True)
    hr_assign_date = models.DateField()
    hr_no_vac = models.IntegerField()
    target_date = models.DateField()
    closed_date = models.DateField()
    refamt = models.IntegerField()
    company = models.IntegerField()
    selected = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hcm_req_details_09_03_22'


class HcmReqDetailsOld(models.Model):
    ack = models.AutoField(primary_key=True)
    empcode = models.IntegerField(blank=True, null=True)
    ntry_date = models.DateField()
    main_position = models.CharField(max_length=100, blank=True, null=True)
    sub_position = models.CharField(max_length=100, blank=True, null=True)
    req_dept = models.IntegerField()
    noofvac = models.IntegerField()
    type_vac = models.CharField(max_length=50, blank=True, null=True)
    replaceass = models.CharField(max_length=100, blank=True, null=True)
    reporteto = models.IntegerField()
    experience = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    station = models.CharField(max_length=20, blank=True, null=True)
    out_sta = models.CharField(max_length=50, blank=True, null=True)
    leadtime = models.CharField(max_length=10, blank=True, null=True)
    lead_days = models.IntegerField()
    nature = models.CharField(max_length=20, blank=True, null=True)
    req_main_qualif = models.CharField(max_length=100, blank=True, null=True)
    req_sub_qualif = models.CharField(max_length=50, blank=True, null=True)
    des_main_qualif = models.CharField(max_length=100, blank=True, null=True)
    des_sub_qualif = models.CharField(max_length=30, blank=True, null=True)
    knowled = models.TextField(blank=True, null=True)
    knowled_des = models.TextField(blank=True, null=True)
    main_dut = models.TextField(blank=True, null=True)
    attach = models.CharField(max_length=100, blank=True, null=True)
    hod = models.IntegerField()
    hod_sts = models.IntegerField()
    hod_comm = models.CharField(max_length=100, blank=True, null=True)
    hod_date = models.DateField()
    head = models.IntegerField()
    head_sts = models.IntegerField()
    head_comm = models.CharField(max_length=200, blank=True, null=True)
    head_date = models.DateField()
    hr = models.IntegerField()
    hr_sts = models.IntegerField()
    hr_comm = models.CharField(max_length=100, blank=True, null=True)
    hr_date = models.DateField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    md = models.IntegerField()
    md_sts = models.IntegerField()
    md_comm = models.CharField(max_length=100, blank=True, null=True)
    md_date = models.DateField()
    hr_assign_sts = models.IntegerField()
    hr_assign = models.CharField(max_length=6, blank=True, null=True)
    hr_assign_date = models.DateField()
    hr_no_vac = models.IntegerField()
    target_date = models.DateField()
    closed_date = models.DateField()
    refamt = models.IntegerField()
    company = models.IntegerField()
    selected = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hcm_req_details_old'


class HcmReqRes(models.Model):
    res_id = models.AutoField(primary_key=True)
    ack = models.IntegerField()
    per_ref_no = models.IntegerField()
    pname = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    aid = models.IntegerField()
    respons = models.IntegerField()
    comm = models.CharField(max_length=100, blank=True, null=True)
    cid = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    ntry_date = models.DateField()
    status = models.IntegerField()
    approval_status = models.IntegerField()
    res_date = models.DateField()
    res_comm = models.CharField(max_length=100, blank=True, null=True)
    others = models.CharField(max_length=600, blank=True, null=True)
    hid = models.IntegerField()
    attach_type = models.CharField(max_length=20, blank=True, null=True)
    attachment = models.CharField(max_length=100, blank=True, null=True)
    complete = models.CharField(max_length=100, blank=True, null=True)
    offer = models.CharField(max_length=100, blank=True, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    noticeperiod = models.CharField(max_length=11, blank=True, null=True)
    negotiation = models.CharField(max_length=11, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    approvaldt = models.DateField()
    joineddt = models.DateField()
    confirm_cand = models.IntegerField(blank=True, null=True)
    hod_dept = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hcm_req_res'


class HcmReqResOld(models.Model):
    res_id = models.AutoField(primary_key=True)
    ack = models.IntegerField()
    per_ref_no = models.IntegerField()
    pname = models.CharField(max_length=28, blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    aid = models.IntegerField()
    respons = models.IntegerField()
    comm = models.CharField(max_length=100, blank=True, null=True)
    cid = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    ntry_date = models.DateField()
    status = models.IntegerField()
    approval_status = models.IntegerField()
    res_date = models.DateField()
    res_comm = models.CharField(max_length=100, blank=True, null=True)
    others = models.CharField(max_length=600, blank=True, null=True)
    hid = models.IntegerField()
    attach_type = models.CharField(max_length=20, blank=True, null=True)
    attachment = models.CharField(max_length=100, blank=True, null=True)
    complete = models.CharField(max_length=100, blank=True, null=True)
    offer = models.CharField(max_length=100, blank=True, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    noticeperiod = models.CharField(max_length=11, blank=True, null=True)
    negotiation = models.CharField(max_length=11, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hcm_req_res_old'


class HcmResHistory(models.Model):
    hid = models.AutoField(primary_key=True)
    res_id = models.IntegerField()
    ack = models.IntegerField()
    per_ref_no = models.IntegerField()
    aid = models.IntegerField()
    respons = models.IntegerField()
    comm = models.CharField(max_length=100, blank=True, null=True)
    cid = models.IntegerField()
    createdby = models.IntegerField()
    ntry_date = models.DateField()
    status = models.IntegerField()
    approval_status = models.IntegerField()
    res_date = models.DateField()
    res_comm = models.CharField(max_length=100, blank=True, null=True)
    others = models.CharField(max_length=600, blank=True, null=True)
    attach_type = models.CharField(max_length=20, blank=True, null=True)
    attachment = models.CharField(max_length=100, blank=True, null=True)
    complete = models.CharField(max_length=100, blank=True, null=True)
    offer = models.CharField(max_length=100, blank=True, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    negotiation = models.CharField(max_length=11, blank=True, null=True)
    noticeperiod = models.CharField(max_length=11, blank=True, null=True)
    type = models.IntegerField()
    attachments = models.CharField(max_length=30, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hcm_res_history'


class HcmResHistoryOl(models.Model):
    hid = models.AutoField(primary_key=True)
    res_id = models.IntegerField()
    ack = models.IntegerField()
    per_ref_no = models.IntegerField()
    aid = models.IntegerField()
    respons = models.IntegerField()
    comm = models.CharField(max_length=100, blank=True, null=True)
    cid = models.IntegerField()
    createdby = models.IntegerField()
    ntry_date = models.DateField()
    status = models.IntegerField()
    approval_status = models.IntegerField()
    res_date = models.DateField()
    res_comm = models.CharField(max_length=100, blank=True, null=True)
    others = models.CharField(max_length=600, blank=True, null=True)
    attach_type = models.CharField(max_length=20, blank=True, null=True)
    attachment = models.CharField(max_length=100, blank=True, null=True)
    complete = models.CharField(max_length=100, blank=True, null=True)
    offer = models.CharField(max_length=100, blank=True, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    negotiation = models.CharField(max_length=11, blank=True, null=True)
    noticeperiod = models.CharField(max_length=11, blank=True, null=True)
    type = models.IntegerField()
    attachments = models.CharField(max_length=30, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hcm_res_history_ol'


class HcmSalMaster(models.Model):
    sa_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    level = models.CharField(max_length=1, blank=True, null=True)
    catgy = models.CharField(max_length=11)
    amt = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hcm_sal_master'


class HolidaysMaster(models.Model):
    slno = models.IntegerField()
    name = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    year = models.IntegerField()
    createdby = models.IntegerField()
    timestampp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'holidays_master'


class HousePropertyIncomeTax(models.Model):
    house_id = models.AutoField(primary_key=True)
    main_id = models.IntegerField()
    empcode = models.IntegerField()
    house_count = models.IntegerField()
    housing_type1 = models.IntegerField()
    house_interest1 = models.IntegerField()
    bank_name_1 = models.CharField(max_length=50)
    bank_pan_1 = models.CharField(max_length=50)
    rent_per_month1 = models.IntegerField()
    repair1 = models.IntegerField()
    income_loss1 = models.IntegerField()
    interest_80ee1 = models.IntegerField()
    interest_80eea1 = models.IntegerField()
    interest_us241 = models.IntegerField()
    property_owner = models.CharField(max_length=300)
    property_address = models.CharField(max_length=1000)
    house_reg_date = models.DateField()
    prop_value = models.IntegerField()
    cons_compdt = models.DateField()
    loan_sancdt = models.DateField()
    loan_amnt = models.IntegerField()
    monthly_emi = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'house_property_income_tax'


class HrAdhocMaster(models.Model):
    matnr = models.IntegerField()
    issue_qty = models.FloatField()
    remarks = models.CharField(max_length=500)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hr_adhoc_master'


class HrColorMaster(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    color_code = models.CharField(max_length=20)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hr_color_master'


class HrFootwearMaster(models.Model):
    uniq_slno_footwaer = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hr_footwear_master'


class HrInventoryAdaptNtry(models.Model):
    slno = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    uniq_slno_matnr = models.IntegerField()
    qty = models.IntegerField()
    months = models.IntegerField()
    issue_qty = models.IntegerField()
    issue_date = models.DateField()
    issue_by = models.IntegerField()
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hr_inventory_adapt_ntry'


class HrInventoryMaster(models.Model):
    uniq_slno_matnr = models.AutoField(primary_key=True)
    matnr = models.IntegerField()
    desc = models.CharField(max_length=200)
    uom = models.CharField(max_length=11)
    size = models.CharField(max_length=11)
    color_code = models.IntegerField()
    minqty = models.IntegerField()
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hr_inventory_master'


class HrLastUpdateMaster(models.Model):
    empcode = models.IntegerField()
    matnr = models.IntegerField()
    last_issue_date = models.DateField()
    last_issue_qty = models.FloatField()
    createdby = models.IntegerField()
    due_date = models.DateField()
    due_sts = models.CharField(max_length=1)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hr_last_update_master'


class HrRecitesMaster(models.Model):
    matnr = models.IntegerField()
    recite_qty = models.FloatField()
    createdby = models.IntegerField()
    ntry_date = models.DateField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hr_recites_master'


class HrStockMaster(models.Model):
    matnr = models.IntegerField(unique=True)
    stock = models.FloatField()
    minqty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hr_stock_master'


class HrUomMaster(models.Model):
    uom_slno = models.AutoField(primary_key=True)
    uom_name = models.CharField(max_length=20)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hr_uom_master'


class HrWeatherMaster(models.Model):
    uniq_slno_weather = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hr_weather_master'


class IgiElecAtta(models.Model):
    uniq_slno = models.IntegerField()
    filename = models.TextField(blank=True, null=True)
    file_type = models.CharField(max_length=200)
    file_size = models.CharField(max_length=11)
    file_ext = models.CharField(max_length=200)
    type = models.IntegerField()
    timestamp = models.DateTimeField()
    createdby = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'igi_elec_atta'


class IgiElecEntry(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    type = models.IntegerField()
    product_code = models.IntegerField()
    doc_no = models.CharField(max_length=500, blank=True, null=True)
    pos_date = models.DateField()
    po_no = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=500, blank=True, null=True)
    part_no = models.CharField(max_length=500, blank=True, null=True)
    make = models.CharField(max_length=500, blank=True, null=True)
    vendor = models.CharField(max_length=500, blank=True, null=True)
    type_rej = models.IntegerField()
    invoice = models.CharField(max_length=500, blank=True, null=True)
    inv_date = models.DateField()
    inv_qty = models.CharField(max_length=200, blank=True, null=True)
    recd_qty = models.CharField(max_length=200, blank=True, null=True)
    rej_qty = models.CharField(max_length=200, blank=True, null=True)
    dept = models.IntegerField()
    method = models.TextField(blank=True, null=True)
    problem_exstr = models.CharField(max_length=500, blank=True, null=True)
    reason_rej = models.TextField(blank=True, null=True)
    slno = models.CharField(max_length=500, blank=True, null=True)
    vend_batch = models.CharField(max_length=500, blank=True, null=True)
    isp_pro = models.CharField(max_length=500, blank=True, null=True)
    cost = models.CharField(max_length=500, blank=True, null=True)
    failure_remarks = models.TextField(blank=True, null=True)
    igi_remrks = models.TextField(blank=True, null=True)
    track_sts = models.IntegerField(blank=True, null=True)
    sud_sts = models.IntegerField()
    sap_stock = models.IntegerField()
    comnts = models.CharField(max_length=500, blank=True, null=True)
    entry_date = models.DateField()
    service_no = models.IntegerField()
    parts_slno = models.IntegerField()
    rewno = models.CharField(max_length=100, blank=True, null=True)
    ven_to_date = models.DateField()
    rec_date = models.DateField()
    mail1 = models.CharField(max_length=100, blank=True, null=True)
    mail2 = models.CharField(max_length=100, blank=True, null=True)
    mail3 = models.CharField(max_length=100, blank=True, null=True)
    raised_dept = models.IntegerField()
    supp_analysis = models.IntegerField()
    created_by = models.IntegerField()
    created_gl = models.IntegerField()
    createdby_dept = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    reworkqty = models.IntegerField()
    uom = models.CharField(max_length=10, blank=True, null=True)
    to = models.CharField(max_length=100, blank=True, null=True)
    cc = models.CharField(max_length=40, blank=True, null=True)
    warrenty_type = models.CharField(max_length=10, blank=True, null=True)
    desc = models.CharField(max_length=100, blank=True, null=True)
    analysis = models.IntegerField()
    cmnts = models.CharField(max_length=300, blank=True, null=True)
    moved_by = models.CharField(max_length=10, blank=True, null=True)
    excl_sts = models.IntegerField()
    currency = models.CharField(max_length=20, blank=True, null=True)
    pg_group = models.CharField(max_length=20, blank=True, null=True)
    pay_terms = models.CharField(max_length=100, blank=True, null=True)
    industry_type = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'igi_elec_entry'


class IgiElecEntry2602(models.Model):
    uniq_slno = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    product_code = models.IntegerField()
    doc_no = models.CharField(max_length=500)
    pos_date = models.DateField()
    po_no = models.CharField(max_length=25)
    item_code = models.CharField(max_length=500)
    part_no = models.CharField(max_length=500)
    make = models.CharField(max_length=500)
    vendor = models.CharField(max_length=500)
    type_rej = models.IntegerField()
    invoice = models.CharField(max_length=500)
    inv_date = models.DateField()
    inv_qty = models.CharField(max_length=200)
    recd_qty = models.CharField(max_length=200)
    rej_qty = models.CharField(max_length=200)
    dept = models.IntegerField()
    method = models.TextField()
    problem_exstr = models.CharField(max_length=500)
    reason_rej = models.TextField()
    slno = models.CharField(max_length=500)
    vend_batch = models.CharField(max_length=500)
    isp_pro = models.CharField(max_length=500)
    cost = models.CharField(max_length=500)
    failure_remarks = models.TextField()
    igi_remrks = models.TextField()
    track_sts = models.IntegerField()
    sud_sts = models.IntegerField()
    entry_date = models.DateField()
    service_no = models.IntegerField()
    parts_slno = models.IntegerField()
    rewno = models.CharField(max_length=100)
    ven_to_date = models.DateField()
    rec_date = models.DateField()
    mail1 = models.CharField(max_length=100)
    mail2 = models.CharField(max_length=100)
    mail3 = models.CharField(max_length=100)
    raised_dept = models.IntegerField()
    supp_analysis = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    reworkqty = models.IntegerField()
    uom = models.CharField(max_length=10)
    to = models.CharField(max_length=40)
    cc = models.CharField(max_length=40)
    warrenty_type = models.CharField(max_length=10)
    desc = models.CharField(max_length=100)
    analysis = models.IntegerField()
    cmnts = models.CharField(max_length=300)
    excl_sts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'igi_elec_entry_26_02'


class IgiElecEntry29122022(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    type = models.IntegerField()
    product_code = models.IntegerField()
    doc_no = models.CharField(max_length=500, blank=True, null=True)
    pos_date = models.DateField()
    po_no = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=500, blank=True, null=True)
    part_no = models.CharField(max_length=500, blank=True, null=True)
    make = models.CharField(max_length=500, blank=True, null=True)
    vendor = models.CharField(max_length=500, blank=True, null=True)
    type_rej = models.IntegerField()
    invoice = models.CharField(max_length=500, blank=True, null=True)
    inv_date = models.DateField()
    inv_qty = models.CharField(max_length=200, blank=True, null=True)
    recd_qty = models.CharField(max_length=200, blank=True, null=True)
    rej_qty = models.CharField(max_length=200, blank=True, null=True)
    dept = models.IntegerField()
    method = models.TextField(blank=True, null=True)
    problem_exstr = models.CharField(max_length=500, blank=True, null=True)
    reason_rej = models.TextField(blank=True, null=True)
    slno = models.CharField(max_length=500, blank=True, null=True)
    vend_batch = models.CharField(max_length=500, blank=True, null=True)
    isp_pro = models.CharField(max_length=500, blank=True, null=True)
    cost = models.CharField(max_length=500, blank=True, null=True)
    failure_remarks = models.TextField(blank=True, null=True)
    igi_remrks = models.TextField(blank=True, null=True)
    track_sts = models.IntegerField()
    sud_sts = models.IntegerField()
    sap_stock = models.IntegerField()
    comnts = models.CharField(max_length=500, blank=True, null=True)
    entry_date = models.DateField()
    service_no = models.IntegerField()
    parts_slno = models.IntegerField()
    rewno = models.CharField(max_length=100, blank=True, null=True)
    ven_to_date = models.DateField()
    rec_date = models.DateField()
    mail1 = models.CharField(max_length=100, blank=True, null=True)
    mail2 = models.CharField(max_length=100, blank=True, null=True)
    mail3 = models.CharField(max_length=100, blank=True, null=True)
    raised_dept = models.IntegerField()
    supp_analysis = models.IntegerField()
    created_by = models.IntegerField()
    created_gl = models.IntegerField()
    createdby_dept = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    reworkqty = models.IntegerField()
    uom = models.CharField(max_length=10, blank=True, null=True)
    to = models.CharField(max_length=100, blank=True, null=True)
    cc = models.CharField(max_length=40, blank=True, null=True)
    warrenty_type = models.CharField(max_length=10, blank=True, null=True)
    desc = models.CharField(max_length=100, blank=True, null=True)
    analysis = models.IntegerField()
    cmnts = models.CharField(max_length=300, blank=True, null=True)
    moved_by = models.CharField(max_length=10, blank=True, null=True)
    excl_sts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'igi_elec_entry_29_12_2022'


class IgiElecEntryOld(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    type = models.IntegerField()
    product_code = models.IntegerField()
    doc_no = models.CharField(max_length=500, blank=True, null=True)
    pos_date = models.DateField()
    po_no = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=500, blank=True, null=True)
    part_no = models.CharField(max_length=500, blank=True, null=True)
    make = models.CharField(max_length=500, blank=True, null=True)
    vendor = models.CharField(max_length=500, blank=True, null=True)
    type_rej = models.IntegerField()
    invoice = models.CharField(max_length=500, blank=True, null=True)
    inv_date = models.DateField()
    inv_qty = models.CharField(max_length=200, blank=True, null=True)
    recd_qty = models.CharField(max_length=200, blank=True, null=True)
    rej_qty = models.CharField(max_length=200, blank=True, null=True)
    dept = models.IntegerField()
    method = models.TextField(blank=True, null=True)
    problem_exstr = models.CharField(max_length=500, blank=True, null=True)
    reason_rej = models.TextField(blank=True, null=True)
    slno = models.CharField(max_length=500, blank=True, null=True)
    vend_batch = models.CharField(max_length=500, blank=True, null=True)
    isp_pro = models.CharField(max_length=500, blank=True, null=True)
    cost = models.CharField(max_length=500, blank=True, null=True)
    failure_remarks = models.TextField(blank=True, null=True)
    igi_remrks = models.TextField(blank=True, null=True)
    track_sts = models.IntegerField()
    sud_sts = models.IntegerField()
    entry_date = models.DateField()
    service_no = models.IntegerField()
    parts_slno = models.IntegerField()
    rewno = models.CharField(max_length=100, blank=True, null=True)
    ven_to_date = models.DateField()
    rec_date = models.DateField()
    mail1 = models.CharField(max_length=100, blank=True, null=True)
    mail2 = models.CharField(max_length=100, blank=True, null=True)
    mail3 = models.CharField(max_length=100, blank=True, null=True)
    raised_dept = models.IntegerField()
    supp_analysis = models.IntegerField()
    created_by = models.IntegerField()
    created_gl = models.IntegerField()
    createdby_dept = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    reworkqty = models.IntegerField()
    uom = models.CharField(max_length=10, blank=True, null=True)
    to = models.CharField(max_length=40, blank=True, null=True)
    cc = models.CharField(max_length=40, blank=True, null=True)
    warrenty_type = models.CharField(max_length=10, blank=True, null=True)
    desc = models.CharField(max_length=100, blank=True, null=True)
    analysis = models.IntegerField()
    cmnts = models.CharField(max_length=300, blank=True, null=True)
    moved_by = models.CharField(max_length=10, blank=True, null=True)
    excl_sts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'igi_elec_entry_old'


class IgiElecHistory(models.Model):
    uniq_slno = models.IntegerField()
    track_sts = models.CharField(max_length=5)
    failure_remarks = models.CharField(max_length=500)
    igi_remrks = models.TextField()
    assocaite = models.CharField(max_length=50)
    delete1 = models.CharField(max_length=1)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'igi_elec_history'


class IgiElecNonwarrenty(models.Model):
    slno = models.AutoField(primary_key=True)
    report_no = models.IntegerField()
    routedate = models.DateField()
    mat_code = models.CharField(max_length=50)
    qty = models.IntegerField()
    reason_rej = models.TextField(blank=True, null=True)
    mat_slno = models.IntegerField()
    cost = models.CharField(max_length=200)
    scrap_type = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    closedate = models.DateField()
    timestamp = models.IntegerField()
    craeted_by = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'igi_elec_nonwarrenty'


class IgiElecStsmaster(models.Model):
    status_name = models.CharField(max_length=200)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=20)
    igi_type = models.CharField(max_length=30)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'igi_elec_stsmaster'


class IgiExcessNtry(models.Model):
    excess_id = models.AutoField(primary_key=True)
    date = models.DateField()
    returned_by = models.IntegerField()
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'igi_excess_ntry'


class IgiExcessNtryLineitems(models.Model):
    lineitem_id = models.AutoField(primary_key=True)
    project = models.CharField(max_length=100)
    material_code = models.CharField(max_length=20)
    excess_id = models.IntegerField()
    part_no = models.CharField(max_length=50)
    make = models.CharField(max_length=100)
    qty = models.IntegerField()
    stock_availability = models.IntegerField()
    reason = models.TextField()
    returned_dept = models.IntegerField()
    date = models.DateField()
    deprtment = models.IntegerField()
    approved_rejected_by = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField()
    approved_to_be = models.IntegerField()
    created_by = models.IntegerField()
    accepted_qty = models.CharField(max_length=100)
    rejected_qty = models.IntegerField()
    rejected_sts = models.IntegerField()
    batch_code = models.CharField(max_length=100)
    inspected_by = models.CharField(max_length=20)
    igi_action_by = models.CharField(max_length=20)
    igi_remarks = models.TextField(blank=True, null=True)
    igi_accepted_date = models.DateField()
    updatedby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'igi_excess_ntry_lineitems'


class IgiExcessNtryLineitems55(models.Model):
    lineitem_id = models.AutoField(primary_key=True)
    project = models.CharField(max_length=100)
    material_code = models.CharField(max_length=20)
    excess_id = models.IntegerField()
    part_no = models.CharField(max_length=50)
    make = models.CharField(max_length=100)
    qty = models.IntegerField()
    stock_availability = models.IntegerField()
    reason = models.TextField()
    returned_dept = models.IntegerField()
    date = models.DateField()
    approved_rejected_by = models.CharField(max_length=20)
    status = models.IntegerField()
    approved_to_be = models.IntegerField()
    created_by = models.IntegerField()
    accepted_qty = models.CharField(max_length=100)
    rejected_qty = models.IntegerField()
    rejected_sts = models.IntegerField()
    batch_code = models.CharField(max_length=100)
    inspected_by = models.CharField(max_length=20)
    igi_action_by = models.CharField(max_length=20)
    igi_remarks = models.TextField()
    igi_accepted_date = models.DateField()
    updatedby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'igi_excess_ntry_lineitems55'


class IgiHistory(models.Model):
    igi_id = models.IntegerField()
    status = models.CharField(max_length=5)
    comments = models.CharField(max_length=500)
    assocaite = models.CharField(max_length=70)
    type = models.CharField(max_length=4)
    active = models.CharField(max_length=1)
    delete1 = models.CharField(max_length=1)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'igi_history'


class IgiMicDataMaster(models.Model):
    matnr = models.CharField(unique=True, max_length=15)
    pcheck = models.TextField()
    fcheck = models.TextField()
    dcheck = models.TextField()
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'igi_mic_data_master'


class IgiNtry(models.Model):
    igi_id = models.AutoField(primary_key=True)
    target_date = models.DateField()
    proc_date = models.DateField()
    dept = models.CharField(max_length=5)
    empcode = models.CharField(max_length=7)
    me_user = models.CharField(max_length=7)
    igi_status = models.CharField(max_length=2)
    igi_mcode = models.CharField(max_length=15)
    igi_reason = models.TextField(blank=True, null=True)
    igi_stage = models.CharField(max_length=4)
    timestamp = models.DateTimeField()
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'igi_ntry'


class IgiReportDimension(models.Model):
    documentnumber = models.CharField(primary_key=True, max_length=20)
    materialcode = models.CharField(max_length=20)
    serialnumber = models.BigIntegerField()
    coloumn_values = models.CharField(max_length=1000, blank=True, null=True)
    inspectedby = models.CharField(max_length=50, blank=True, null=True)
    inspecteddate = models.DateField(blank=True, null=True)
    authorisedby = models.BigIntegerField(blank=True, null=True)
    authoriseddate = models.DateField(blank=True, null=True)
    finalsave = models.CharField(max_length=5)
    createdby = models.BigIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'igi_report_dimension'
        unique_together = (('documentnumber', 'materialcode', 'serialnumber'),)


class IgiReportMaster(models.Model):
    docno = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    no_of_rows = models.SmallIntegerField()
    number_of_columns = models.IntegerField()
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'igi_report_master'


class IgiReportMasterEntry(models.Model):
    material = models.CharField(max_length=20)
    serial_number = models.IntegerField()
    column_heading = models.CharField(max_length=150, blank=True, null=True)
    docno = models.CharField(max_length=20)
    createdby = models.BigIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'igi_report_master_entry'


class IgimDetailedInspection(models.Model):
    materialcode = models.CharField(max_length=20)
    no_of_dimensions = models.IntegerField(blank=True, null=True)
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'igim_detailed_inspection'


class IgimDetailedInspectionDetails(models.Model):
    materialcode = models.BigIntegerField(blank=True, null=True)
    sno = models.IntegerField(blank=True, null=True)
    dimension = models.CharField(max_length=20, blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'igim_detailed_inspection_details'


class IgimDetailedInspectionEntry(models.Model):
    document_number = models.BigIntegerField()
    vendor = models.BigIntegerField()
    materialcode = models.BigIntegerField()
    totalqty = models.IntegerField()
    doc_date = models.DateField()
    dirno = models.BigIntegerField()
    date = models.DateField()
    qty = models.IntegerField()
    createdby = models.BigIntegerField()
    finalsave = models.CharField(max_length=5)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'igim_detailed_inspection_entry'


class IgimDim(models.Model):
    dim = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'igim_dim'


class IgimDimensionDetails(models.Model):
    dirno = models.BigIntegerField(blank=True, null=True)
    documentnumber = models.CharField(max_length=20, blank=True, null=True)
    materialcode = models.CharField(max_length=20, blank=True, null=True)
    serialnumber = models.IntegerField(blank=True, null=True)
    heading1 = models.CharField(max_length=200, blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'igim_dimension_details'


class IncomeTaxDescHeaderMaster(models.Model):
    name = models.CharField(max_length=150)
    del_field = models.IntegerField(db_column='del')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'income_tax_desc_header_master'


class IncomeTaxDescMaster(models.Model):
    description = models.CharField(max_length=1500)
    field_name = models.CharField(max_length=100)
    help_text = models.CharField(max_length=2000)
    delete1 = models.IntegerField()
    desc_header = models.IntegerField()
    sap_id = models.IntegerField()
    seq = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'income_tax_desc_master'


class IncomeTaxDetailEntry(models.Model):
    main_id = models.IntegerField()
    desc_id = models.IntegerField()
    amt = models.CharField(max_length=200)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'income_tax_detail_entry'


class IncomeTaxMainEntry(models.Model):
    empcode = models.IntegerField()
    regim = models.IntegerField()
    pan_card = models.CharField(max_length=15, blank=True, null=True)
    entry_date = models.DateField()
    draft_release = models.IntegerField()
    status = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'income_tax_main_entry'


class InspSubCont(models.Model):
    cid = models.AutoField(primary_key=True)
    sub_type = models.CharField(max_length=10)
    sub_contract = models.CharField(max_length=20)
    mat_code = models.CharField(max_length=15)
    off_qty = models.IntegerField()
    rev_no = models.IntegerField()
    matsh = models.CharField(max_length=5)
    sht_qty = models.IntegerField()
    ins_type = models.CharField(max_length=20)
    matpoava = models.CharField(max_length=5)
    mat_pono = models.CharField(max_length=20)
    po_date = models.DateField()
    confirmation = models.CharField(max_length=6)
    ntry_date = models.DateTimeField()
    createdby = models.CharField(max_length=6)
    igi_sts = models.IntegerField()
    attdate = models.DateField()
    inspsdat = models.DateTimeField()
    inspedat = models.DateTimeField()
    ninspa = models.IntegerField()
    dept = models.IntegerField()
    tinspt = models.IntegerField()
    matacqty = models.IntegerField()
    matreqty = models.IntegerField()
    mat_rej_qty = models.IntegerField()
    devtion = models.CharField(max_length=50)
    file = models.CharField(max_length=10000)
    matacdeqty = models.IntegerField()
    rev_remaks = models.CharField(max_length=500)
    rev_file = models.CharField(max_length=500)
    remkas = models.CharField(max_length=500)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    igi_date = models.DateField()
    igi_ntry = models.CharField(max_length=6)
    deli_date = models.DateField()
    unit_ser_no = models.CharField(max_length=11)
    cc = models.CharField(max_length=10)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'insp_sub_cont'


class InspectionDetails(models.Model):
    material_code = models.CharField(max_length=20, blank=True, null=True)
    serialnumber = models.IntegerField(blank=True, null=True)
    dimension = models.TextField(blank=True, null=True)
    critical = models.IntegerField()
    createdby = models.CharField(max_length=20, blank=True, null=True)
    delete1 = models.IntegerField()
    rmrks = models.CharField(max_length=150, blank=True, null=True)
    nbpages = models.IntegerField(db_column='nbPages')  # Field name made lowercase.
    inst_gauge = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField()
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'inspection_details'


class InspectionDetailsTemp(models.Model):
    material_code = models.CharField(max_length=20, blank=True, null=True)
    serialnumber = models.IntegerField(blank=True, null=True)
    dimension = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.CharField(max_length=20, blank=True, null=True)
    delete1 = models.IntegerField()
    rmrks = models.CharField(max_length=150)
    nbpages = models.IntegerField(db_column='nbPages')  # Field name made lowercase.
    inst_gauge = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inspection_details_temp'


class InspectionDimensions(models.Model):
    material_code = models.CharField(max_length=50, blank=True, null=True)
    uniq_id = models.IntegerField(blank=True, null=True)
    specified_dim = models.TextField(blank=True, null=True)
    serialnumber = models.IntegerField(blank=True, null=True)
    acc_range = models.CharField(max_length=150, blank=True, null=True)
    inst_guage = models.CharField(max_length=100, blank=True, null=True)
    obs_dim = models.CharField(max_length=40, blank=True, null=True)
    rej_qty = models.CharField(max_length=30, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.CharField(max_length=10, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inspection_dimensions'


class InspectionDna(models.Model):
    dna_id = models.AutoField(primary_key=True)
    dna_main = models.IntegerField()
    dns_sub = models.IntegerField()
    dna_sub_unit = models.IntegerField()
    dna_comment = models.TextField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inspection_dna'


class InspectionDnaNotes(models.Model):
    materialcode = models.CharField(max_length=20, blank=True, null=True)
    dna_id = models.IntegerField(blank=True, null=True)
    dna_sub = models.IntegerField(blank=True, null=True)
    dna_sub_unit = models.IntegerField(blank=True, null=True)
    dna_notes = models.IntegerField(blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inspection_dna_notes'


class InspectionMaster(models.Model):
    materialcode = models.CharField(unique=True, max_length=20, blank=True, null=True)
    number_of_dimensions = models.IntegerField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    inspctn_pln = models.CharField(max_length=500, blank=True, null=True)
    timestamp = models.DateTimeField()
    ntry_date = models.DateTimeField()
    update_date = models.DateTimeField()
    revision_sts = models.CharField(max_length=300, blank=True, null=True)
    std_time = models.CharField(max_length=10, blank=True, null=True)
    revision = models.CharField(max_length=11, blank=True, null=True)
    drawfile = models.CharField(max_length=250, blank=True, null=True)
    reginsfile = models.CharField(max_length=200, blank=True, null=True)
    uploadfile = models.CharField(max_length=600)
    up_date = models.DateTimeField()
    date_up_latest = models.DateTimeField()
    dna = models.CharField(max_length=100, blank=True, null=True)
    dna_notes = models.CharField(max_length=100, blank=True, null=True)
    prepared = models.CharField(max_length=50, blank=True, null=True)
    checked = models.CharField(max_length=50, blank=True, null=True)
    approved = models.CharField(max_length=50, blank=True, null=True)
    ecr = models.CharField(max_length=50, blank=True, null=True)
    revdate1 = models.CharField(max_length=50, blank=True, null=True)
    rev1 = models.CharField(max_length=50, blank=True, null=True)
    revdesc1 = models.CharField(max_length=100, blank=True, null=True)
    drawfile1 = models.CharField(max_length=50, blank=True, null=True)
    insp_approval = models.CharField(max_length=7, blank=True, null=True)
    insp_approvaltime = models.DateTimeField()
    insp_approvalstatus = models.CharField(max_length=1, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inspection_master'


class InspectionMasterDetails(models.Model):
    materialcode = models.CharField(max_length=20, blank=True, null=True)
    serialnumber = models.IntegerField(blank=True, null=True)
    specified_dimensions = models.CharField(max_length=50, blank=True, null=True)
    observed_dimensions = models.CharField(max_length=50, blank=True, null=True)
    quantity_rejected = models.CharField(max_length=11, blank=True, null=True)
    remarks = models.TextField()
    createdby = models.BigIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inspection_master_details'


class InspectionMasterDup(models.Model):
    materialcode = models.CharField(max_length=20, blank=True, null=True)
    number_of_dimensions = models.IntegerField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    inspctn_pln = models.CharField(max_length=500)
    timestamp = models.DateTimeField()
    ntry_date = models.DateField()
    update_date = models.DateField()
    revision_sts = models.CharField(max_length=300)
    std_time = models.CharField(max_length=10)
    revision = models.IntegerField()
    drawfile = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'inspection_master_dup'


class InspectionMasterDup1(models.Model):
    materialcode = models.CharField(unique=True, max_length=20, blank=True, null=True)
    number_of_dimensions = models.IntegerField(blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    inspctn_pln = models.CharField(max_length=500)
    timestamp = models.DateTimeField()
    ntry_date = models.DateField()
    update_date = models.DateField()
    revision_sts = models.CharField(max_length=300)
    std_time = models.CharField(max_length=10)
    revision = models.CharField(max_length=11)
    drawfile = models.CharField(max_length=250)
    field_dna = models.CharField(db_column='\tdna', max_length=100)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    dna_notes = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'inspection_master_dup1'


class InspectionMasterEntry(models.Model):
    document_number = models.CharField(max_length=20, blank=True, null=True)
    materialnumber = models.CharField(max_length=20, blank=True, null=True)
    vendor = models.CharField(max_length=8, blank=True, null=True)
    qty_inspected = models.CharField(max_length=50, blank=True, null=True)
    qty_accepted = models.CharField(max_length=50, blank=True, null=True)
    qty_rework = models.CharField(max_length=50, blank=True, null=True)
    qty_rejected = models.CharField(max_length=50, blank=True, null=True)
    insert_date = models.DateField(blank=True, null=True)
    instrument_code = models.CharField(max_length=50, blank=True, null=True)
    sfcode = models.IntegerField(blank=True, null=True)
    aprroved_by = models.CharField(max_length=50, blank=True, null=True)
    finalsave = models.CharField(max_length=5)
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inspection_master_entry'


class InspectionPdfEntry(models.Model):
    uniq_id = models.AutoField(primary_key=True)
    material_code = models.CharField(max_length=30, blank=True, null=True)
    std_time = models.TimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    entry_date = models.DateField()
    qty_ins = models.IntegerField(blank=True, null=True)
    qty_rej = models.IntegerField(blank=True, null=True)
    qty_acc = models.IntegerField(blank=True, null=True)
    qty_rwk = models.IntegerField(blank=True, null=True)
    doc_no = models.IntegerField(blank=True, null=True)
    ins_code = models.CharField(max_length=40, blank=True, null=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.CharField(max_length=15, blank=True, null=True)
    vendor_code = models.CharField(max_length=15, blank=True, null=True)
    inspected_by = models.CharField(max_length=20, blank=True, null=True)
    approved_by = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField()
    gl = models.CharField(max_length=10, blank=True, null=True)
    gl_date = models.DateField()
    hod = models.CharField(max_length=10, blank=True, null=True)
    hod_sts = models.CharField(max_length=5)
    hod_date = models.DateField()
    approve_date = models.DateField()
    insp_unit = models.CharField(max_length=5, blank=True, null=True)
    acc_unit = models.CharField(max_length=5, blank=True, null=True)
    rew_unit = models.CharField(max_length=5, blank=True, null=True)
    rej_unit = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inspection_pdf_entry'


class InspectionRevision(models.Model):
    material_code = models.CharField(max_length=11)
    rev = models.CharField(max_length=11)
    revdate = models.DateField()
    revdesc = models.CharField(max_length=100)
    createdby = models.CharField(max_length=6)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inspection_revision'

class Kanban(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    dept = models.CharField(max_length=50)
    slno = models.IntegerField()
    sub_ass = models.CharField(max_length=18)
    sa_text = models.TextField()
    matnr = models.CharField(max_length=18)
    matnr_text = models.TextField()
    qty = models.IntegerField()
    uom = models.CharField(max_length=10)
    valid_date = models.DateField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kanban'

class KanbanCardMaster(models.Model):
    card_num = models.IntegerField(primary_key=True)
    project = models.CharField(max_length=50, blank=True, null=True)
    sub_assem = models.CharField(max_length=20, blank=True, null=True)
    material = models.CharField(max_length=20, blank=True, null=True)
    qty = models.FloatField()
    floor_loc = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    createdby = models.CharField(max_length=7, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    deleteby = models.CharField(max_length=7, blank=True, null=True)
    delete_date = models.DateField()
    company = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kanban_card_master'


class KanbanCardTemp(models.Model):
    card_num = models.IntegerField()
    project = models.CharField(max_length=50)
    sub_assem = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    qty = models.IntegerField()
    floor_loc = models.CharField(max_length=20)
    user_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'kanban_card_temp'


class KanbanComplaintMaster(models.Model):
    cid = models.AutoField(primary_key=True)
    complaint_type = models.CharField(max_length=100)
    createdby = models.CharField(max_length=7)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    deleteby = models.CharField(max_length=7)
    delete_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'kanban_complaint_master'


class KanbanCompnHistory(models.Model):
    hid = models.AutoField(primary_key=True)
    slno = models.IntegerField()
    unit_no = models.IntegerField()
    responsible = models.CharField(max_length=7)
    ntry_date = models.DateField()
    status = models.IntegerField()
    rootcause = models.TextField()
    kaban_comments = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kanban_compn_history'


class KanbanCompnReg(models.Model):
    slno = models.AutoField(primary_key=True)
    unit_no = models.IntegerField()
    empcode = models.CharField(max_length=7, blank=True, null=True)
    ntry_date = models.DateField()
    storage = models.IntegerField()
    complaint_type = models.IntegerField()
    details = models.CharField(max_length=200, blank=True, null=True)
    card_num = models.CharField(max_length=6, blank=True, null=True)
    responsible = models.CharField(max_length=7, blank=True, null=True)
    update_date = models.DateField()
    status = models.IntegerField()
    rootcause = models.TextField(blank=True, null=True)
    stores = models.CharField(max_length=3)
    rating = models.IntegerField()
    feedback = models.CharField(max_length=50, blank=True, null=True)
    feed_date = models.DateField()
    kaban_comments = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()
    company = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kanban_compn_reg'


class KanbanDataNtry(models.Model):
    project = models.CharField(max_length=20)
    card = models.IntegerField()
    matnr = models.CharField(max_length=11)
    mat_desc = models.CharField(max_length=50)
    qty = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kanban_data_ntry'


class KanbanDataTemp(models.Model):
    project = models.CharField(max_length=20)
    card = models.IntegerField()
    matnr = models.CharField(max_length=11)
    mat_desc = models.CharField(max_length=50)
    qty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kanban_data_temp'


class KanbanFeedback(models.Model):
    fid = models.AutoField(primary_key=True)
    feed = models.CharField(max_length=2)
    feedback = models.CharField(max_length=20)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kanban_feedback'


class KanbanMaster(models.Model):
    slno = models.IntegerField()
    part_no = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)
    loc_at1 = models.CharField(max_length=20)
    qty = models.IntegerField()
    uom = models.CharField(max_length=10)
    loc_at2 = models.CharField(max_length=20)
    suplr = models.CharField(max_length=50)
    mfg = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    lead_time = models.IntegerField()
    ext = models.CharField(max_length=10)
    com_slno = models.IntegerField()
    sub_assy = models.CharField(max_length=50)
    slip_no = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kanban_master'


class KanbanStatusMaster(models.Model):
    sid = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kanban_status_master'


class KssCostDetails(models.Model):
    slno = models.IntegerField()
    save_mat = models.CharField(max_length=11)
    revised_mat = models.CharField(max_length=11)
    costrs = models.IntegerField()
    costrwk = models.IntegerField()
    costrvsd = models.IntegerField()
    consumqty = models.IntegerField()
    qtysaved = models.IntegerField()
    costsaved = models.IntegerField()
    month_req = models.IntegerField()
    monthcost = models.IntegerField()
    yearlycost = models.IntegerField()
    finalcost = models.IntegerField()
    plngcmmts = models.CharField(max_length=300)
    edp_amt = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    rwd_date = models.DateField()
    rwd_attach = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'kss_cost_details'


class KssDateMaster(models.Model):
    ntry_start = models.DateField()
    ntry_end = models.DateField()
    gl_start = models.DateField()
    gl_end = models.DateField()
    hod_start = models.DateField()
    hod_end = models.DateField()
    created_by = models.CharField(max_length=6, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kss_date_master'


class KssNtryTemp(models.Model):
    kss_id = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    tag_no = models.IntegerField()
    impltd_by = models.IntegerField()
    impl_date = models.DateField()
    kss_them = models.TextField()
    current_problem = models.TextField()
    root_cause = models.TextField()
    counter_measures = models.TextField()
    benifits = models.TextField()
    intan_benefits = models.TextField()
    problem_analysis = models.CharField(max_length=300)
    ntry_date = models.DateField()
    user = models.CharField(max_length=6)
    feedback = models.CharField(max_length=50)
    prjct = models.CharField(max_length=100, blank=True, null=True)
    standardization = models.CharField(max_length=1000)
    qnt = models.CharField(max_length=1000)
    spend_amt = models.IntegerField(blank=True, null=True)
    level_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kss_ntry_temp'


class KssNtryView(models.Model):
    deptname = models.CharField(max_length=50, blank=True, null=True)
    empname = models.CharField(max_length=50, blank=True, null=True)
    slno = models.IntegerField()
    sgtn_no = models.CharField(max_length=50)
    empcode = models.IntegerField()
    dept = models.IntegerField()
    ntry_date = models.DateField()
    kss_them = models.TextField()
    problem_analysis = models.CharField(max_length=250)
    tangible_sts = models.CharField(max_length=2)
    benifits = models.CharField(max_length=500)
    intan_benefits = models.CharField(max_length=500)
    current_problem = models.CharField(max_length=1000)
    root_cause = models.CharField(max_length=250)
    counter_measures = models.CharField(max_length=1500)
    horizental_deployement = models.CharField(max_length=1)
    action = models.CharField(max_length=250)
    resp = models.IntegerField()
    target_date = models.DateField()
    actual_date = models.DateField()
    status = models.CharField(max_length=250)
    impltd_by = models.IntegerField()
    kss_dept_slno = models.IntegerField()
    loc = models.CharField(max_length=50)
    prjct = models.CharField(max_length=50)
    qnt = models.CharField(max_length=100)
    createdby = models.IntegerField()
    created_dept = models.CharField(max_length=10)
    horiz_deploy = models.CharField(max_length=250)
    impl_date = models.DateField()
    proc_resp = models.IntegerField()
    priority = models.IntegerField()
    b4_commnets = models.CharField(max_length=300)
    after_comments = models.CharField(max_length=300)
    temp_priority = models.IntegerField()
    production_type = models.CharField(max_length=1)
    impltd_dept = models.IntegerField()
    timestampp = models.DateTimeField()
    hod_aprl_sts = models.IntegerField()
    hod_code = models.IntegerField()
    hod_date = models.DateField()
    ss = models.IntegerField()
    project_any = models.CharField(max_length=300)
    hod = models.IntegerField()
    gl = models.CharField(max_length=60)
    gl_sts = models.IntegerField()
    gl_ntry_date = models.DateField()
    gl_comment = models.CharField(max_length=250)
    gl_ntry_by = models.CharField(max_length=7)
    level_no = models.IntegerField()
    hod_comment = models.CharField(max_length=250)
    amount = models.IntegerField()
    reward_amount = models.IntegerField()
    kss_amt = models.IntegerField()
    attachment = models.CharField(max_length=200)
    cost_saving = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kss_ntry_view'


class KssNtryView12(models.Model):
    deptname = models.CharField(max_length=50, blank=True, null=True)
    empname = models.CharField(max_length=50, blank=True, null=True)
    slno = models.IntegerField()
    sgtn_no = models.CharField(max_length=50)
    empcode = models.IntegerField()
    dept = models.IntegerField()
    ntry_date = models.DateField()
    kss_them = models.TextField()
    problem_analysis = models.CharField(max_length=250)
    tangible_sts = models.CharField(max_length=2)
    benifits = models.CharField(max_length=500)
    intan_benefits = models.CharField(max_length=500)
    current_problem = models.CharField(max_length=1000)
    root_cause = models.CharField(max_length=250)
    counter_measures = models.CharField(max_length=1500)
    horizental_deployement = models.CharField(max_length=1)
    action = models.CharField(max_length=250)
    resp = models.IntegerField()
    target_date = models.DateField()
    actual_date = models.DateField()
    status = models.CharField(max_length=250)
    impltd_by = models.IntegerField()
    kss_dept_slno = models.IntegerField()
    loc = models.CharField(max_length=50)
    prjct = models.CharField(max_length=50)
    qnt = models.CharField(max_length=100)
    createdby = models.IntegerField()
    created_dept = models.CharField(max_length=10)
    horiz_deploy = models.CharField(max_length=250)
    impl_date = models.DateField()
    proc_resp = models.IntegerField()
    priority = models.IntegerField()
    b4_commnets = models.CharField(max_length=300)
    after_comments = models.CharField(max_length=300)
    temp_priority = models.IntegerField()
    production_type = models.CharField(max_length=1)
    impltd_dept = models.IntegerField()
    timestampp = models.DateTimeField()
    hod_aprl_sts = models.IntegerField()
    hod_code = models.IntegerField()
    hod_date = models.DateField()
    ss = models.IntegerField()
    project_any = models.CharField(max_length=300)
    hod = models.IntegerField()
    gl = models.CharField(max_length=60)
    gl_sts = models.IntegerField()
    gl_ntry_date = models.DateField()
    gl_comment = models.CharField(max_length=250)
    gl_ntry_by = models.CharField(max_length=7)
    level_no = models.IntegerField()
    hod_comment = models.CharField(max_length=250)
    amount = models.IntegerField()
    reward_amount = models.IntegerField()
    kss_amt = models.IntegerField()
    attachment = models.CharField(max_length=200)
    cost_saving = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kss_ntry_view12'


class KssPrizes(models.Model):
    empcode = models.IntegerField()
    dept = models.IntegerField()
    kaizens = models.IntegerField()
    ntry_datefrom = models.DateField(db_column='ntry_dateFrom')  # Field name made lowercase.
    ntry_dateto = models.DateField(db_column='ntry_dateTo')  # Field name made lowercase.
    auto_inc = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'kss_prizes'


class KssPurchaseAuth(models.Model):
    empcode = models.CharField(max_length=7)
    gl = models.CharField(max_length=7)
    hod = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'kss_purchase_auth'


class LaptopHistory(models.Model):
    empcode = models.IntegerField()
    laptop_slno = models.CharField(max_length=50)
    responsible = models.IntegerField()
    in_out = models.CharField(max_length=3)
    status = models.CharField(max_length=15)
    ntry_date = models.CharField(max_length=10)
    ntry_time = models.CharField(max_length=5)
    remarks = models.CharField(max_length=150)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'laptop_history'


class LaptopMaster(models.Model):
    empcode = models.IntegerField()
    laptop_make = models.CharField(max_length=50)
    laptop_model = models.CharField(max_length=50)
    laptop_slno = models.CharField(max_length=50)
    laptop_location = models.CharField(max_length=25)
    asset_type = models.CharField(max_length=20)
    created_date = models.DateField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    del_date = models.DateField()
    delete_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'laptop_master'


class LeanMaster(models.Model):
    date = models.DateField()
    ntry_by = models.IntegerField()
    dept = models.IntegerField()
    kaizens = models.IntegerField()
    sugg = models.IntegerField()
    number_5s = models.IntegerField(db_column='5s')  # Field renamed because it wasn't a valid Python identifier.
    lean = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lean_master'


class LeaveCancelData(models.Model):
    can_id = models.AutoField(primary_key=True)
    empcode = models.CharField(max_length=6)
    lea_app_date = models.DateField()
    noofdays = models.FloatField()
    startdate = models.DateField()
    enddate = models.DateField()
    leave_type = models.CharField(max_length=5)
    day_type = models.CharField(max_length=5)
    reason = models.CharField(max_length=500)
    indicator = models.CharField(max_length=11)
    leave_id = models.IntegerField()
    type = models.CharField(max_length=2)
    generate_date = models.DateField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'leave_cancel_data'


class LeaveOtOnOd(models.Model):
    otid = models.AutoField(primary_key=True)
    ack = models.IntegerField()
    empcode = models.IntegerField()
    date = models.DateField()
    day = models.CharField(max_length=15)
    ot_from = models.CharField(max_length=5)
    ot_to = models.CharField(max_length=8)
    ntry_date = models.DateField()
    hod_aprl_sts = models.IntegerField()
    hod = models.IntegerField()
    hod_aprl_date = models.DateField()
    download = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'leave_ot_on_od'


class LeaveOutingDetails(models.Model):
    oid = models.AutoField(primary_key=True)
    associate = models.IntegerField()
    place = models.CharField(max_length=50)
    purpose = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    out = models.CharField(max_length=10)
    in_field = models.CharField(db_column='in', max_length=10)  # Field renamed because it was a Python reserved word.
    ntry_by = models.CharField(max_length=6)
    ntry_date = models.DateField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'leave_outing_details'


class LeaveVisitMgt(models.Model):
    vid = models.AutoField(primary_key=True)
    cat = models.CharField(max_length=10, blank=True, null=True)
    org = models.CharField(max_length=50, blank=True, null=True)
    visitor = models.CharField(max_length=50, blank=True, null=True)
    associate = models.IntegerField()
    place = models.CharField(max_length=50, blank=True, null=True)
    purpose = models.CharField(max_length=50, blank=True, null=True)
    ntry_date = models.DateField()
    comein = models.CharField(max_length=10)
    wentout = models.CharField(max_length=10)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'leave_visit_mgt'


class LeaveWorkflowAccess(models.Model):
    empcode = models.IntegerField()
    modules = models.IntegerField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField()
    timestamp = models.DateField()
    delete1 = models.IntegerField()
    responsible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'leave_workflow_access'


class LeaveWorkflowDepts(models.Model):
    module_name = models.CharField(max_length=100)
    created_by = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'leave_workflow_depts'


class LocOutMaster(models.Model):
    oid = models.AutoField(primary_key=True)
    work_loc = models.CharField(max_length=50, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'loc_out_master'


class LocationMaster(models.Model):
    loid = models.AutoField(primary_key=True)
    loccode = models.CharField(max_length=20)
    locname = models.CharField(max_length=50)
    shortcode = models.CharField(max_length=2)
    full_code = models.CharField(max_length=25)
    time_admin = models.CharField(max_length=150)
    com_id = models.IntegerField()
    plant = models.IntegerField()
    com_name = models.CharField(max_length=10, blank=True, null=True)
    company_address = models.CharField(max_length=250, blank=True, null=True)
    google_map_loc = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'location_master'


class LocationMaster28102022(models.Model):
    loccode = models.CharField(max_length=20)
    locname = models.CharField(max_length=50)
    shortcode = models.CharField(max_length=2)
    time_admin = models.CharField(max_length=150)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'location_master_28_10_2022'


class LocationMasterOld(models.Model):
    loccode = models.CharField(max_length=20)
    locname = models.CharField(max_length=50)
    shortcode = models.CharField(max_length=2)
    time_admin = models.CharField(max_length=150)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'location_master_old'


class LocoType(models.Model):
    lc_no = models.AutoField(primary_key=True)
    lc_name = models.CharField(max_length=50)
    createdby = models.SmallIntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'loco_type'


class LoginDetails(models.Model):
    date = models.DateField()
    login = models.IntegerField()
    login_time = models.CharField(max_length=9)
    logout = models.IntegerField()
    logout_time = models.CharField(max_length=9, blank=True, null=True)
    max_login = models.IntegerField()
    max_logout_time = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login_details'


class LomAlternate(models.Model):
    reqid = models.AutoField(primary_key=True)
    unit_no = models.IntegerField()
    typeofrequest = models.IntegerField()
    status = models.IntegerField()
    priority = models.IntegerField()
    empcode = models.IntegerField()
    dept = models.CharField(max_length=5, blank=True, null=True)
    me_user = models.IntegerField()
    target_date = models.DateField()
    prs_date = models.DateField()
    delivery_date = models.DateField()
    prs_quentity = models.CharField(max_length=10, blank=True, null=True)
    noofitems = models.IntegerField()
    pdt_status = models.CharField(max_length=100, blank=True, null=True)
    designer = models.CharField(max_length=500, blank=True, null=True)
    marketing_eng = models.CharField(max_length=100, blank=True, null=True)
    rdso = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField()
    mcode = models.CharField(max_length=200, blank=True, null=True)
    category = models.IntegerField()
    project = models.CharField(max_length=100, blank=True, null=True)
    po_no_prs = models.CharField(max_length=20, blank=True, null=True)
    draft = models.CharField(max_length=1, blank=True, null=True)
    comparisan_category = models.CharField(max_length=4, blank=True, null=True)
    mdesc = models.TextField(blank=True, null=True)
    existing = models.CharField(max_length=50, blank=True, null=True)
    suggested = models.CharField(max_length=50, blank=True, null=True)
    reason = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField()
    hold_date = models.DateField()
    refmail = models.CharField(max_length=100, blank=True, null=True)
    attachment = models.CharField(max_length=100, blank=True, null=True)
    mailattach = models.CharField(max_length=100, blank=True, null=True)
    user_attach = models.CharField(max_length=100, blank=True, null=True)
    conclusionbyme = models.TextField(blank=True, null=True)
    dateconf = models.DateField()
    actionone = models.IntegerField()
    actiontwo = models.IntegerField()
    actionthree = models.IntegerField()
    actionfour = models.IntegerField()
    actionfive = models.IntegerField()
    actionsix = models.IntegerField()
    hod = models.IntegerField()
    hodapproved = models.CharField(max_length=5, blank=True, null=True)
    alt_part = models.TextField(blank=True, null=True)
    alt_make = models.TextField(blank=True, null=True)
    meattach = models.CharField(max_length=100, blank=True, null=True)
    peer_attach = models.CharField(max_length=100, blank=True, null=True)
    present_status = models.CharField(max_length=20, blank=True, null=True)
    expected_date = models.DateField()
    findby = models.IntegerField()
    delete1 = models.IntegerField()
    mydate = models.DateField()
    m_code = models.CharField(max_length=20, blank=True, null=True)
    shrtage_qty = models.CharField(max_length=11, blank=True, null=True)
    shrtage_prdct = models.CharField(max_length=50, blank=True, null=True)
    single_src_type = models.IntegerField()
    assn_targt_date = models.DateField()
    value_additn = models.IntegerField()
    designer_comm = models.CharField(max_length=200, blank=True, null=True)
    existing_cost = models.FloatField()
    alternate_partcost = models.FloatField()
    sample_qty = models.FloatField()
    gatepass_no = models.CharField(max_length=50, blank=True, null=True)
    potting_details = models.CharField(max_length=50, blank=True, null=True)
    sample_eval_empcode = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lom_alternate'


class LomAlternateDesgnr(models.Model):
    empcode = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lom_alternate_desgnr'


class LomAlternateFields(models.Model):
    field_id = models.AutoField(primary_key=True)
    category = models.IntegerField()
    subcategory = models.IntegerField()
    field_name = models.CharField(max_length=100, blank=True, null=True)
    requiredtrue = models.IntegerField()
    orderbyasc = models.IntegerField()
    direction = models.CharField(max_length=2, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lom_alternate_fields'


class LomAlternateHistory(models.Model):
    reqid = models.IntegerField()
    ref_id = models.IntegerField()
    unit_no = models.IntegerField()
    status = models.CharField(max_length=100, blank=True, null=True)
    hold_date = models.DateField()
    comments = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    assocaite = models.CharField(max_length=100, blank=True, null=True)
    live = models.IntegerField()
    mpnno = models.CharField(db_column='mpnNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    delete1 = models.IntegerField()
    apprv_beforeucp = models.IntegerField()
    attachment = models.CharField(max_length=50, blank=True, null=True)
    no_of_active_sources = models.CharField(max_length=50, blank=True, null=True)
    stores_stock = models.CharField(max_length=100, blank=True, null=True)
    pending_order = models.CharField(max_length=100, blank=True, null=True)
    no_of_live_applications = models.CharField(max_length=100, blank=True, null=True)
    reference_tag_no = models.CharField(max_length=100, blank=True, null=True)
    reviewdata = models.CharField(max_length=300, blank=True, null=True)
    expected_date = models.DateField()
    dependent_reqrmnt = models.CharField(max_length=50)
    alternate_partstatus = models.IntegerField()
    rdso_apprv = models.IntegerField()
    cmpsheet = models.IntegerField()
    cmpsheet_remrks = models.TextField(blank=True, null=True)
    desgnr_feedback = models.IntegerField()
    desner_remarks = models.TextField(blank=True, null=True)
    marketng_date = models.DateField()
    timestamp = models.DateTimeField()
    expected_date_sec = models.DateField()
    peer_ver_attach = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lom_alternate_history'


class LomAlternateMpn(models.Model):
    reqid = models.IntegerField()
    partno_flat = models.CharField(max_length=100, blank=True, null=True)
    make_flat = models.CharField(max_length=100, blank=True, null=True)
    spq = models.CharField(max_length=100, blank=True, null=True)
    tapeandreal = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lom_alternate_mpn'


class LomAlternateParameters(models.Model):
    parameterid = models.AutoField(primary_key=True)
    reqid = models.IntegerField()
    ref_id = models.IntegerField()
    field_id = models.IntegerField()
    field_name = models.CharField(max_length=100, blank=True, null=True)
    empcode = models.IntegerField()
    ext = models.TextField(blank=True, null=True)
    alt = models.TextField(blank=True, null=True)
    uom = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    live = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lom_alternate_parameters'


class LomAlternateParametersMultiple(models.Model):
    alt_id = models.AutoField(primary_key=True)
    reqid = models.IntegerField()
    ref_id = models.IntegerField()
    field_id = models.IntegerField(blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    empcode = models.IntegerField()
    alt_cnt = models.IntegerField(blank=True, null=True)
    alt_cnt_value = models.CharField(max_length=100, blank=True, null=True)
    uom = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    live = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lom_alternate_parameters_multiple'


class LomAlternateSampleEval(models.Model):
    slno = models.AutoField(primary_key=True)
    reqid = models.IntegerField()
    unit_no = models.IntegerField()
    sample_no = models.IntegerField()
    part_no = models.CharField(max_length=50, blank=True, null=True)
    make = models.CharField(max_length=100, blank=True, null=True)
    item_code = models.CharField(max_length=50, blank=True, null=True)
    desc = models.CharField(max_length=100, blank=True, null=True)
    qty = models.IntegerField()
    rec_date = models.DateField()
    gatepass_no = models.CharField(max_length=50, blank=True, null=True)
    send_date = models.DateField()
    me_remarks = models.TextField(blank=True, null=True)
    acc_sts = models.IntegerField()
    acc_rej_date = models.DateField()
    user_remarks = models.TextField(blank=True, null=True)
    attach = models.CharField(max_length=100, blank=True, null=True)
    eval_empcode = models.CharField(max_length=8, blank=True, null=True)
    reply_date = models.DateTimeField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lom_alternate_sample_eval'


class LomAlternateSuggested(models.Model):
    reqid = models.IntegerField()
    suggested_alternate = models.CharField(max_length=200, blank=True, null=True)
    suggested_make = models.CharField(max_length=200, blank=True, null=True)
    createdby = models.IntegerField()
    desnr_conclus = models.IntegerField()
    remarks = models.CharField(max_length=300, blank=True, null=True)
    designer = models.IntegerField()
    designer_date = models.DateField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lom_alternate_suggested'


class LomAlterpart(models.Model):
    reqid = models.IntegerField()
    makeext = models.TextField()
    makeatn = models.TextField()
    partnoext = models.TextField()
    partnoatn = models.TextField()
    packageext = models.TextField()
    packageatn = models.TextField()
    physicalext = models.TextField()
    physicalatn = models.TextField()
    ratingext = models.TextField()
    ratingatn = models.TextField()
    materialext = models.TextField()
    materialatn = models.TextField()
    opttempext = models.TextField()
    opttempatn = models.TextField()
    storagetempext = models.TextField()
    storagetempatn = models.TextField()
    lifespanext = models.TextField()
    lifespanatn = models.TextField()
    supplyext = models.TextField()
    supplyatn = models.TextField()
    priceext = models.FloatField()
    priceatn = models.FloatField()
    comparisionsheet = models.CharField(max_length=100)
    datasheet = models.CharField(max_length=100)
    isexits = models.IntegerField()
    replaceall = models.IntegerField()
    testplan = models.TextField()
    trails = models.IntegerField()
    trailstext = models.TextField()
    durationtrails = models.TextField()
    production_i = models.TextField()
    specified = models.IntegerField()
    approvalsug = models.IntegerField()
    live = models.IntegerField()
    me_comments = models.CharField(max_length=500)
    present_status = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'lom_alterpart'


class LomCatNewMaster(models.Model):
    category = models.CharField(max_length=30)
    num_id = models.IntegerField()
    categoryname = models.CharField(max_length=40)
    mainfamily = models.IntegerField()
    mainfamilyname = models.CharField(max_length=40)
    metric_size_dig1 = models.CharField(max_length=11)
    metric_size_dig2 = models.CharField(max_length=11)
    head = models.CharField(max_length=11)
    length_dig1 = models.CharField(max_length=11)
    length_dig2 = models.CharField(max_length=11)
    material = models.CharField(max_length=11)
    finish = models.CharField(max_length=11)
    suf_dig1 = models.CharField(max_length=11)
    suf_dig2 = models.CharField(max_length=11)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    deletedby = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lom_cat_new_master'


class LomCategoryMaster(models.Model):
    cateoryid = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    delete1 = models.IntegerField()
    createdby = models.CharField(max_length=7)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lom_category_master'


class LomChangesSub(models.Model):
    reqid = models.IntegerField()
    exitsingpart = models.TextField(blank=True, null=True)
    exitsingmake = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    altermake = models.CharField(max_length=100, blank=True, null=True)
    alterpartno = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lom_changes_sub'


class LomDialog(models.Model):
    did = models.AutoField(primary_key=True)
    sub_type = models.IntegerField()
    sequence = models.IntegerField()
    module = models.CharField(max_length=10)
    heading = models.CharField(max_length=30)
    value_content = models.CharField(max_length=100)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lom_dialog'


class LomFieldsMaster(models.Model):
    category = models.IntegerField()
    typeid = models.IntegerField()
    field_name = models.CharField(max_length=25)
    manditory = models.CharField(max_length=1)
    show = models.CharField(max_length=1)
    default = models.CharField(max_length=10)
    position = models.IntegerField()
    status = models.CharField(max_length=10)
    createdby = models.CharField(max_length=7)
    delete1 = models.IntegerField()
    deletedby = models.CharField(max_length=7)
    deleteddate = models.DateField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lom_fields_master'


class LomFieldsNewMaster(models.Model):
    category = models.IntegerField()
    typeid = models.IntegerField()
    sub_type = models.IntegerField()
    field_name = models.CharField(max_length=25)
    manditory = models.CharField(max_length=1)
    show = models.CharField(max_length=1)
    default = models.CharField(max_length=10)
    position = models.IntegerField()
    status = models.CharField(max_length=10)
    createdby = models.CharField(max_length=7)
    delete1 = models.IntegerField()
    deletedby = models.CharField(max_length=7)
    deleteddate = models.DateField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lom_fields_new_master'


class LomFunctionMaster(models.Model):
    fid = models.AutoField(primary_key=True)
    field_name = models.CharField(max_length=40)
    field_to_display = models.CharField(max_length=500)
    fnname = models.CharField(max_length=100)
    isitselection = models.IntegerField()
    createdby = models.CharField(max_length=7)
    delete1 = models.IntegerField()
    deleteddate = models.DateField()
    deletedby = models.CharField(max_length=7)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lom_function_master'


class LomHistory(models.Model):
    reqid = models.IntegerField()
    unit_no = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    date = models.DateField()
    assocaite = models.CharField(max_length=7, blank=True, null=True)
    live = models.IntegerField()
    attachment = models.CharField(max_length=50, blank=True, null=True)
    peersap = models.CharField(max_length=100, blank=True, null=True)
    merequired = models.CharField(max_length=20, blank=True, null=True)
    delete1 = models.IntegerField()
    mecmmntfordsgner = models.TextField(blank=True, null=True)
    reasonforblock = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()
    ucpupdate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lom_history'


class LomInputsSuffix(models.Model):
    sid = models.AutoField(primary_key=True)
    suffix = models.CharField(max_length=10)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    deletedby = models.CharField(max_length=7)
    deleteddate = models.DateField()

    class Meta:
        managed = False
        db_table = 'lom_inputs_suffix'


class LomMakeNtry(models.Model):
    mid = models.AutoField(primary_key=True)
    slno = models.IntegerField()
    lom_makes = models.CharField(max_length=50)
    make_rsn = models.CharField(max_length=100)
    designer = models.CharField(max_length=5)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lom_make_ntry'


class LomMakes(models.Model):
    lom_pid = models.AutoField(primary_key=True)
    lom_make_id = models.CharField(max_length=4)
    lom_makes = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'lom_makes'


class LomMakesNew(models.Model):
    categoryname = models.CharField(max_length=250)
    lom_pid = models.AutoField(primary_key=True)
    lom_make_id = models.IntegerField()
    mainfamilyname = models.CharField(max_length=250)
    subfamilyname = models.CharField(max_length=250)
    lom_makes = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'lom_makes_new'


class LomMakesNew1(models.Model):
    categoryname = models.CharField(max_length=150)
    lom_pid = models.IntegerField()
    lom_make_id = models.IntegerField()
    mainfamilyname = models.CharField(max_length=250)
    subfamilyname = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'lom_makes_new1'


class LomMaterialTeam(models.Model):
    empcode = models.CharField(max_length=7)
    type = models.CharField(max_length=2)
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'lom_material_team'


class LomMelist(models.Model):
    empcode = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lom_melist'


class LomNewCategoryMas(models.Model):
    cid = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)
    cnum = models.CharField(max_length=11)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lom_new_category_mas'


class LomNewSubTypeMas(models.Model):
    sid = models.AutoField(primary_key=True)
    tid = models.IntegerField()
    sub_type = models.CharField(max_length=60)
    snum = models.CharField(max_length=4)
    show3d = models.CharField(max_length=5)
    manufacturer = models.CharField(max_length=200)
    prod_details = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    web_details = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'lom_new_sub_type_mas'


class LomNewTypeMas(models.Model):
    tid = models.AutoField(primary_key=True)
    cid = models.IntegerField()
    type = models.CharField(max_length=50)
    mnum = models.CharField(max_length=2)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lom_new_type_mas'


class LomNewrequest(models.Model):
    reqid = models.AutoField(primary_key=True)
    index_no = models.IntegerField()
    unit_no = models.IntegerField()
    typeofrequest = models.IntegerField()
    status = models.IntegerField()
    flatfiledwn = models.IntegerField()
    empcode = models.IntegerField()
    dept = models.IntegerField()
    me_user = models.IntegerField()
    target_date = models.DateField()
    designer = models.IntegerField()
    hod_sts = models.IntegerField()
    timestamp = models.DateTimeField()
    mcode = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=70, blank=True, null=True)
    subcategory = models.IntegerField()
    subunder = models.IntegerField()
    reply = models.IntegerField()
    othercategory = models.TextField(blank=True, null=True)
    mdesc = models.TextField(blank=True, null=True)
    existing = models.TextField(blank=True, null=True)
    suggested = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    buydate = models.DateField()
    shipdate = models.DateField()
    date = models.DateField()
    blocking = models.CharField(max_length=10, blank=True, null=True)
    code_r_mpn = models.CharField(max_length=10, blank=True, null=True)
    mcode_new = models.CharField(max_length=200, blank=True, null=True)
    refmail = models.CharField(max_length=100, blank=True, null=True)
    attachment = models.CharField(max_length=100, blank=True, null=True)
    pcnattach = models.CharField(max_length=100, blank=True, null=True)
    mecomment = models.CharField(max_length=300, blank=True, null=True)
    user_attach = models.CharField(max_length=100, blank=True, null=True)
    me_desc = models.TextField(blank=True, null=True)
    usercomment = models.TextField(blank=True, null=True)
    conclusionbyme = models.TextField(blank=True, null=True)
    rootcause = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    applicable = models.TextField(blank=True, null=True)
    purchase_reply = models.TextField(blank=True, null=True)
    master_team = models.IntegerField()
    dateconf = models.DateField()
    actionone = models.IntegerField()
    actiontwo = models.IntegerField()
    actionthree = models.IntegerField()
    actionfour = models.IntegerField()
    actionfive = models.IntegerField()
    hod = models.IntegerField(blank=True, null=True)
    hodapproved = models.CharField(max_length=5, blank=True, null=True)
    partno_flat = models.TextField(blank=True, null=True)
    make_flat = models.TextField(blank=True, null=True)
    meattach = models.CharField(max_length=100, blank=True, null=True)
    peer_team = models.CharField(max_length=20, blank=True, null=True)
    make = models.CharField(max_length=500, blank=True, null=True)
    emp_ass = models.CharField(max_length=10, blank=True, null=True)
    pcn_emp = models.CharField(max_length=10, blank=True, null=True)
    reasonforblock = models.TextField(blank=True, null=True)
    delete1 = models.IntegerField()
    mpn_number = models.CharField(max_length=200)
    mnfpart_num = models.CharField(max_length=200)
    hod_tms = models.DateTimeField()
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lom_newrequest'


class LomNtry(models.Model):
    slno = models.AutoField(primary_key=True)
    category = models.IntegerField()
    lomtype = models.CharField(max_length=5, blank=True, null=True)
    sub_type = models.IntegerField()
    value = models.CharField(max_length=15, blank=True, null=True)
    malefe = models.CharField(max_length=7, blank=True, null=True)
    noofpins = models.CharField(max_length=25, blank=True, null=True)
    straightright = models.CharField(max_length=30, blank=True, null=True)
    noofrows = models.CharField(max_length=15, blank=True, null=True)
    pcbthickness = models.CharField(max_length=20, blank=True, null=True)
    sqmm = models.IntegerField()
    noofcores = models.IntegerField()
    noofstrands = models.IntegerField()
    strandthickness = models.FloatField()
    voltagerating = models.CharField(max_length=15, blank=True, null=True)
    currentrating = models.CharField(max_length=15, blank=True, null=True)
    od = models.CharField(max_length=15, blank=True, null=True)
    operatingtemperature = models.CharField(max_length=15, blank=True, null=True)
    uom = models.CharField(max_length=5, blank=True, null=True)
    approximateprice = models.CharField(max_length=15, blank=True, null=True)
    aseriescode = models.CharField(max_length=15, blank=True, null=True)
    drawdocref = models.CharField(max_length=20, blank=True, null=True)
    proprietary = models.CharField(max_length=3, blank=True, null=True)
    product_code = models.CharField(max_length=10, blank=True, null=True)
    connect_pins = models.IntegerField()
    connt_cat = models.IntegerField()
    connt_sub_cat = models.IntegerField()
    ed_no = models.CharField(max_length=10, blank=True, null=True)
    page_r_serial = models.TextField(blank=True, null=True)
    special_ref = models.CharField(max_length=200, blank=True, null=True)
    specialcare = models.CharField(max_length=3, blank=True, null=True)
    specialcaretext = models.CharField(max_length=100, blank=True, null=True)
    periodmaint = models.CharField(max_length=3, blank=True, null=True)
    periodmaint_attach = models.CharField(max_length=250, blank=True, null=True)
    inspectioncriteria = models.TextField(blank=True, null=True)
    partno = models.CharField(max_length=100)
    finishing = models.CharField(max_length=10, blank=True, null=True)
    inserts = models.CharField(max_length=3)
    make = models.CharField(max_length=100, blank=True, null=True)
    tolerance = models.FloatField()
    wattage = models.CharField(max_length=25, blank=True, null=True)
    ppmntcr = models.CharField(max_length=10, blank=True, null=True)
    dimensions = models.CharField(max_length=50, blank=True, null=True)
    package = models.CharField(max_length=15, blank=True, null=True)
    pack_just = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    part_cat = models.CharField(max_length=10, blank=True, null=True)
    createdby = models.CharField(max_length=7, blank=True, null=True)
    me_user = models.CharField(max_length=7, blank=True, null=True)
    ntry_date = models.DateField()
    ntry_time = models.CharField(max_length=10, blank=True, null=True)
    timestamp = models.DateTimeField()
    categorymas = models.CharField(max_length=11, blank=True, null=True)
    mainfamily = models.CharField(max_length=2, blank=True, null=True)
    subfamily = models.CharField(max_length=3, blank=True, null=True)
    copper_value = models.CharField(max_length=10, blank=True, null=True)
    sequencenum = models.CharField(max_length=5, blank=True, null=True)
    cmsnum = models.CharField(max_length=6, blank=True, null=True)
    matnum = models.CharField(max_length=11, blank=True, null=True)
    matdescription = models.CharField(max_length=40, db_collation='utf8_general_ci', blank=True, null=True)
    status = models.IntegerField()
    me_comments = models.TextField(blank=True, null=True)
    user_comment = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    user_status = models.IntegerField()
    mat_type = models.CharField(max_length=50, blank=True, null=True)
    mat_group = models.CharField(max_length=50, blank=True, null=True)
    prod_alloc = models.CharField(max_length=25, blank=True, null=True)
    ind_std_desc = models.CharField(max_length=50, blank=True, null=True)
    round_val = models.IntegerField()
    purch_group = models.CharField(max_length=50, blank=True, null=True)
    batch_mang = models.CharField(max_length=100, blank=True, null=True)
    purch_order_text = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    stor_loc = models.CharField(max_length=25)
    serial_no_profile = models.CharField(max_length=50, blank=True, null=True)
    inspection_setup = models.CharField(max_length=100)
    valuation_class = models.IntegerField()
    closed_or_not = models.IntegerField()
    completed_date = models.DateTimeField()
    lom_team = models.CharField(max_length=7, blank=True, null=True)
    testcertificate = models.CharField(max_length=2, blank=True, null=True)
    fyi = models.CharField(max_length=2)
    contact_details = models.TextField(blank=True, null=True)
    new_or_exist_code = models.CharField(max_length=5, blank=True, null=True)
    leadtime = models.CharField(max_length=20, blank=True, null=True)
    moqdetails = models.CharField(max_length=30, blank=True, null=True)
    replytomeuser = models.TextField(blank=True, null=True)
    sapdownload = models.IntegerField()
    completed = models.IntegerField()
    mail_cc = models.CharField(max_length=250, blank=True, null=True)
    gl = models.CharField(max_length=10, blank=True, null=True)
    glapproved = models.CharField(max_length=5, blank=True, null=True)
    gl_date = models.CharField(max_length=20, blank=True, null=True)
    hod = models.CharField(max_length=10, blank=True, null=True)
    hodapproved = models.CharField(max_length=5, blank=True, null=True)
    approve_date = models.CharField(max_length=20, blank=True, null=True)
    reason = models.IntegerField()
    single_source = models.IntegerField()
    others = models.CharField(max_length=200, blank=True, null=True)
    leadingtime = models.IntegerField()
    moq = models.IntegerField()
    spq = models.IntegerField()
    market_avl = models.IntegerField()
    mark_avail = models.TextField(blank=True, null=True)
    attach_purchase = models.CharField(max_length=100, blank=True, null=True)
    mat_empcode = models.CharField(max_length=7, blank=True, null=True)
    in_sufficient = models.IntegerField()
    in_suff_field1 = models.IntegerField()
    in_suff_field2 = models.TextField(blank=True, null=True)
    ens_dup = models.IntegerField()
    ensure_txt = models.TextField(blank=True, null=True)
    me_e_r_me_m = models.CharField(max_length=2)
    delete1 = models.IntegerField()
    fin_det = models.CharField(max_length=10, blank=True, null=True)
    detail_source = models.IntegerField()
    not_tried_rsn = models.CharField(max_length=500, blank=True, null=True)
    not_date = models.DateField(blank=True, null=True)
    not_date_sts = models.IntegerField()
    mat_code = models.CharField(max_length=13, blank=True, null=True)
    annu_cum = models.CharField(max_length=10, blank=True, null=True)
    applic = models.CharField(max_length=150, blank=True, null=True)
    mtbf = models.CharField(max_length=10, blank=True, null=True)
    msd = models.CharField(max_length=10, blank=True, null=True)
    prog_int = models.CharField(max_length=100, blank=True, null=True)
    prog_toll = models.CharField(max_length=100, blank=True, null=True)
    alt_sts = models.IntegerField()
    file_name = models.CharField(max_length=100, blank=True, null=True)
    product_grade = models.IntegerField()
    intramoving = models.IntegerField()
    dwg_move = models.IntegerField()
    real_move = models.IntegerField()
    datasheet_move = models.IntegerField()
    metric_size_dig1 = models.CharField(max_length=10, blank=True, null=True)
    metric_size_dig2 = models.CharField(max_length=10, blank=True, null=True)
    head = models.CharField(max_length=10, blank=True, null=True)
    length_dig1 = models.CharField(max_length=10, blank=True, null=True)
    length_dig2 = models.CharField(max_length=10, blank=True, null=True)
    material = models.CharField(max_length=10, blank=True, null=True)
    finish = models.CharField(max_length=10, blank=True, null=True)
    suf_dig1 = models.CharField(max_length=10, blank=True, null=True)
    suf_dig2 = models.CharField(max_length=10, blank=True, null=True)
    reas_delay = models.CharField(max_length=100, blank=True, null=True)
    dc_pot = models.CharField(max_length=5, blank=True, null=True)
    user_file = models.CharField(max_length=100, blank=True, null=True)
    ase_ava = models.CharField(max_length=100, blank=True, null=True)
    waranty = models.CharField(max_length=4, blank=True, null=True)
    ethree = models.IntegerField()
    mach_com = models.CharField(max_length=2, blank=True, null=True)
    ctrl_code = models.CharField(max_length=10)
    res_new_code = models.TextField(blank=True, null=True)
    existtool_medha = models.CharField(max_length=20, blank=True, null=True)
    exst_mat_reas = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lom_ntry'


class LomNtry01082021(models.Model):
    slno = models.AutoField(primary_key=True)
    category = models.IntegerField()
    lomtype = models.CharField(max_length=5)
    sub_type = models.IntegerField()
    value = models.CharField(max_length=15)
    malefe = models.CharField(max_length=7)
    noofpins = models.CharField(max_length=25)
    straightright = models.CharField(max_length=30)
    noofrows = models.CharField(max_length=15)
    pcbthickness = models.CharField(max_length=20)
    sqmm = models.IntegerField()
    noofcores = models.IntegerField()
    noofstrands = models.IntegerField()
    strandthickness = models.FloatField()
    voltagerating = models.CharField(max_length=15)
    currentrating = models.CharField(max_length=15)
    od = models.CharField(max_length=15)
    operatingtemperature = models.CharField(max_length=15)
    uom = models.CharField(max_length=5)
    approximateprice = models.CharField(max_length=15)
    aseriescode = models.CharField(max_length=15)
    drawdocref = models.CharField(max_length=20)
    proprietary = models.CharField(max_length=3)
    product_code = models.CharField(max_length=10)
    connect_pins = models.IntegerField()
    connt_cat = models.IntegerField()
    connt_sub_cat = models.IntegerField()
    ed_no = models.CharField(max_length=10)
    page_r_serial = models.CharField(max_length=10)
    special_ref = models.CharField(max_length=200)
    specialcare = models.CharField(max_length=3)
    specialcaretext = models.CharField(max_length=50)
    periodmaint = models.CharField(max_length=3)
    periodmaint_attach = models.CharField(max_length=250)
    inspectioncriteria = models.TextField()
    partno = models.IntegerField()
    finishing = models.CharField(max_length=10)
    inserts = models.CharField(max_length=3)
    make = models.CharField(max_length=25)
    tolerance = models.FloatField()
    wattage = models.CharField(max_length=25)
    ppmntcr = models.CharField(max_length=10)
    dimensions = models.CharField(max_length=15)
    package = models.CharField(max_length=15)
    pack_just = models.CharField(max_length=100)
    description = models.TextField()
    part_cat = models.CharField(max_length=10)
    createdby = models.CharField(max_length=7)
    me_user = models.CharField(max_length=7)
    ntry_date = models.DateField()
    ntry_time = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    categorymas = models.CharField(max_length=11)
    mainfamily = models.CharField(max_length=2)
    subfamily = models.CharField(max_length=3)
    copper_value = models.CharField(max_length=10)
    sequencenum = models.CharField(max_length=5)
    cmsnum = models.CharField(max_length=6)
    matnum = models.CharField(max_length=11)
    matdescription = models.CharField(max_length=40)
    status = models.IntegerField()
    me_comments = models.TextField()
    user_comment = models.TextField()
    user_status = models.IntegerField()
    mat_type = models.CharField(max_length=50)
    mat_group = models.CharField(max_length=50)
    prod_alloc = models.CharField(max_length=25)
    ind_std_desc = models.CharField(max_length=50)
    round_val = models.IntegerField()
    purch_group = models.CharField(max_length=50)
    batch_mang = models.CharField(max_length=100)
    purch_order_text = models.TextField()
    stor_loc = models.CharField(max_length=25)
    serial_no_profile = models.CharField(max_length=50)
    inspection_setup = models.CharField(max_length=100)
    valuation_class = models.IntegerField()
    closed_or_not = models.IntegerField()
    completed_date = models.DateTimeField()
    lom_team = models.CharField(max_length=7)
    testcertificate = models.CharField(max_length=2)
    fyi = models.CharField(max_length=2)
    contact_details = models.TextField()
    new_or_exist_code = models.CharField(max_length=5)
    leadtime = models.CharField(max_length=20)
    moqdetails = models.CharField(max_length=30)
    replytomeuser = models.TextField()
    sapdownload = models.IntegerField()
    completed = models.IntegerField()
    mail_cc = models.CharField(max_length=250)
    gl = models.CharField(max_length=10)
    glapproved = models.CharField(max_length=5)
    gl_date = models.CharField(max_length=20)
    hod = models.CharField(max_length=10)
    hodapproved = models.CharField(max_length=5)
    approve_date = models.CharField(max_length=20)
    reason = models.IntegerField()
    single_source = models.IntegerField()
    others = models.CharField(max_length=200)
    leadingtime = models.IntegerField()
    moq = models.IntegerField()
    spq = models.IntegerField()
    market_avl = models.IntegerField()
    mark_avail = models.TextField()
    attach_purchase = models.CharField(max_length=100)
    mat_empcode = models.CharField(max_length=7)
    in_sufficient = models.IntegerField()
    in_suff_field1 = models.IntegerField()
    in_suff_field2 = models.TextField()
    ens_dup = models.IntegerField()
    ensure_txt = models.TextField()
    me_e_r_me_m = models.CharField(max_length=2)
    delete1 = models.IntegerField()
    fin_det = models.CharField(max_length=10)
    detail_source = models.IntegerField()
    not_tried_rsn = models.CharField(max_length=500)
    not_date = models.DateField(blank=True, null=True)
    not_date_sts = models.IntegerField()
    mat_code = models.CharField(max_length=13)
    annu_cum = models.CharField(max_length=10)
    applic = models.CharField(max_length=20)
    mtbf = models.CharField(max_length=10)
    msd = models.CharField(max_length=10)
    prog_int = models.CharField(max_length=100)
    prog_toll = models.CharField(max_length=100)
    alt_sts = models.IntegerField()
    file_name = models.CharField(max_length=100)
    product_grade = models.IntegerField()
    intramoving = models.IntegerField()
    dwg_move = models.IntegerField()
    real_move = models.IntegerField()
    datasheet_move = models.IntegerField()
    metric_size_dig1 = models.CharField(max_length=10)
    metric_size_dig2 = models.CharField(max_length=10)
    head = models.CharField(max_length=10)
    length_dig1 = models.CharField(max_length=10)
    length_dig2 = models.CharField(max_length=10)
    material = models.CharField(max_length=10)
    finish = models.CharField(max_length=10)
    suf_dig1 = models.CharField(max_length=10)
    suf_dig2 = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'lom_ntry_01_08_2021'


class LomNtry07112022(models.Model):
    slno = models.AutoField(primary_key=True)
    category = models.IntegerField()
    lomtype = models.CharField(max_length=5, blank=True, null=True)
    sub_type = models.IntegerField()
    value = models.CharField(max_length=15, blank=True, null=True)
    malefe = models.CharField(max_length=7, blank=True, null=True)
    noofpins = models.CharField(max_length=25, blank=True, null=True)
    straightright = models.CharField(max_length=30, blank=True, null=True)
    noofrows = models.CharField(max_length=15, blank=True, null=True)
    pcbthickness = models.CharField(max_length=20, blank=True, null=True)
    sqmm = models.IntegerField()
    noofcores = models.IntegerField()
    noofstrands = models.IntegerField()
    strandthickness = models.FloatField()
    voltagerating = models.CharField(max_length=15, blank=True, null=True)
    currentrating = models.CharField(max_length=15, blank=True, null=True)
    od = models.CharField(max_length=15, blank=True, null=True)
    operatingtemperature = models.CharField(max_length=15, blank=True, null=True)
    uom = models.CharField(max_length=5, blank=True, null=True)
    approximateprice = models.CharField(max_length=15, blank=True, null=True)
    aseriescode = models.CharField(max_length=15, blank=True, null=True)
    drawdocref = models.CharField(max_length=20, blank=True, null=True)
    proprietary = models.CharField(max_length=3, blank=True, null=True)
    product_code = models.CharField(max_length=10, blank=True, null=True)
    connect_pins = models.IntegerField()
    connt_cat = models.IntegerField()
    connt_sub_cat = models.IntegerField()
    ed_no = models.CharField(max_length=10, blank=True, null=True)
    page_r_serial = models.CharField(max_length=10, blank=True, null=True)
    special_ref = models.CharField(max_length=200, blank=True, null=True)
    specialcare = models.CharField(max_length=3, blank=True, null=True)
    specialcaretext = models.CharField(max_length=50, blank=True, null=True)
    periodmaint = models.CharField(max_length=3, blank=True, null=True)
    periodmaint_attach = models.CharField(max_length=250, blank=True, null=True)
    inspectioncriteria = models.TextField(blank=True, null=True)
    partno = models.IntegerField()
    finishing = models.CharField(max_length=10, blank=True, null=True)
    inserts = models.CharField(max_length=3)
    make = models.CharField(max_length=25, blank=True, null=True)
    tolerance = models.FloatField()
    wattage = models.CharField(max_length=25, blank=True, null=True)
    ppmntcr = models.CharField(max_length=10, blank=True, null=True)
    dimensions = models.CharField(max_length=15, blank=True, null=True)
    package = models.CharField(max_length=15, blank=True, null=True)
    pack_just = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    part_cat = models.CharField(max_length=10, blank=True, null=True)
    createdby = models.CharField(max_length=7, blank=True, null=True)
    me_user = models.CharField(max_length=7, blank=True, null=True)
    ntry_date = models.DateField()
    ntry_time = models.CharField(max_length=10, blank=True, null=True)
    timestamp = models.DateTimeField()
    categorymas = models.CharField(max_length=11, blank=True, null=True)
    mainfamily = models.CharField(max_length=2, blank=True, null=True)
    subfamily = models.CharField(max_length=3, blank=True, null=True)
    copper_value = models.CharField(max_length=10, blank=True, null=True)
    sequencenum = models.CharField(max_length=5, blank=True, null=True)
    cmsnum = models.CharField(max_length=6, blank=True, null=True)
    matnum = models.CharField(max_length=11, blank=True, null=True)
    matdescription = models.CharField(max_length=40, blank=True, null=True)
    status = models.IntegerField()
    me_comments = models.TextField(blank=True, null=True)
    user_comment = models.TextField(blank=True, null=True)
    user_status = models.IntegerField()
    mat_type = models.CharField(max_length=50, blank=True, null=True)
    mat_group = models.CharField(max_length=50, blank=True, null=True)
    prod_alloc = models.CharField(max_length=25, blank=True, null=True)
    ind_std_desc = models.CharField(max_length=50, blank=True, null=True)
    round_val = models.IntegerField()
    purch_group = models.CharField(max_length=50, blank=True, null=True)
    batch_mang = models.CharField(max_length=100, blank=True, null=True)
    purch_order_text = models.TextField(blank=True, null=True)
    stor_loc = models.CharField(max_length=25)
    serial_no_profile = models.CharField(max_length=50, blank=True, null=True)
    inspection_setup = models.CharField(max_length=100)
    valuation_class = models.IntegerField()
    closed_or_not = models.IntegerField()
    completed_date = models.DateTimeField()
    lom_team = models.CharField(max_length=7, blank=True, null=True)
    testcertificate = models.CharField(max_length=2, blank=True, null=True)
    fyi = models.CharField(max_length=2)
    contact_details = models.TextField(blank=True, null=True)
    new_or_exist_code = models.CharField(max_length=5, blank=True, null=True)
    leadtime = models.CharField(max_length=20, blank=True, null=True)
    moqdetails = models.CharField(max_length=30, blank=True, null=True)
    replytomeuser = models.TextField(blank=True, null=True)
    sapdownload = models.IntegerField()
    completed = models.IntegerField()
    mail_cc = models.CharField(max_length=250, blank=True, null=True)
    gl = models.CharField(max_length=10, blank=True, null=True)
    glapproved = models.CharField(max_length=5, blank=True, null=True)
    gl_date = models.CharField(max_length=20, blank=True, null=True)
    hod = models.CharField(max_length=10, blank=True, null=True)
    hodapproved = models.CharField(max_length=5, blank=True, null=True)
    approve_date = models.CharField(max_length=20, blank=True, null=True)
    reason = models.IntegerField()
    single_source = models.IntegerField()
    others = models.CharField(max_length=200, blank=True, null=True)
    leadingtime = models.IntegerField()
    moq = models.IntegerField()
    spq = models.IntegerField()
    market_avl = models.IntegerField()
    mark_avail = models.TextField(blank=True, null=True)
    attach_purchase = models.CharField(max_length=100, blank=True, null=True)
    mat_empcode = models.CharField(max_length=7, blank=True, null=True)
    in_sufficient = models.IntegerField()
    in_suff_field1 = models.IntegerField()
    in_suff_field2 = models.TextField(blank=True, null=True)
    ens_dup = models.IntegerField()
    ensure_txt = models.TextField(blank=True, null=True)
    me_e_r_me_m = models.CharField(max_length=2)
    delete1 = models.IntegerField()
    fin_det = models.CharField(max_length=10, blank=True, null=True)
    detail_source = models.IntegerField()
    not_tried_rsn = models.CharField(max_length=500, blank=True, null=True)
    not_date = models.DateField(blank=True, null=True)
    not_date_sts = models.IntegerField()
    mat_code = models.CharField(max_length=13, blank=True, null=True)
    annu_cum = models.CharField(max_length=10, blank=True, null=True)
    applic = models.CharField(max_length=20, blank=True, null=True)
    mtbf = models.CharField(max_length=10, blank=True, null=True)
    msd = models.CharField(max_length=10, blank=True, null=True)
    prog_int = models.CharField(max_length=100, blank=True, null=True)
    prog_toll = models.CharField(max_length=100, blank=True, null=True)
    alt_sts = models.IntegerField()
    file_name = models.CharField(max_length=100, blank=True, null=True)
    product_grade = models.IntegerField()
    intramoving = models.IntegerField()
    dwg_move = models.IntegerField()
    real_move = models.IntegerField()
    datasheet_move = models.IntegerField()
    metric_size_dig1 = models.CharField(max_length=10, blank=True, null=True)
    metric_size_dig2 = models.CharField(max_length=10, blank=True, null=True)
    head = models.CharField(max_length=10, blank=True, null=True)
    length_dig1 = models.CharField(max_length=10, blank=True, null=True)
    length_dig2 = models.CharField(max_length=10, blank=True, null=True)
    material = models.CharField(max_length=10, blank=True, null=True)
    finish = models.CharField(max_length=10, blank=True, null=True)
    suf_dig1 = models.CharField(max_length=10, blank=True, null=True)
    suf_dig2 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lom_ntry_07_11_2022'


class LomNtry31072021(models.Model):
    slno = models.AutoField(primary_key=True)
    category = models.IntegerField()
    lomtype = models.CharField(max_length=5)
    sub_type = models.IntegerField()
    value = models.CharField(max_length=15)
    malefe = models.CharField(max_length=7)
    noofpins = models.CharField(max_length=25)
    straightright = models.CharField(max_length=30)
    noofrows = models.CharField(max_length=15)
    pcbthickness = models.CharField(max_length=20)
    sqmm = models.IntegerField()
    noofcores = models.IntegerField()
    noofstrands = models.IntegerField()
    strandthickness = models.FloatField()
    voltagerating = models.CharField(max_length=15)
    currentrating = models.CharField(max_length=15)
    od = models.CharField(max_length=15)
    operatingtemperature = models.CharField(max_length=15)
    uom = models.CharField(max_length=5)
    approximateprice = models.CharField(max_length=15)
    aseriescode = models.CharField(max_length=15)
    drawdocref = models.CharField(max_length=20)
    proprietary = models.CharField(max_length=3)
    product_code = models.CharField(max_length=10)
    connect_pins = models.IntegerField()
    connt_cat = models.IntegerField()
    connt_sub_cat = models.IntegerField()
    ed_no = models.CharField(max_length=10)
    page_r_serial = models.CharField(max_length=10)
    special_ref = models.CharField(max_length=200)
    specialcare = models.CharField(max_length=3)
    specialcaretext = models.CharField(max_length=50)
    periodmaint = models.CharField(max_length=3)
    periodmaint_attach = models.CharField(max_length=250)
    inspectioncriteria = models.TextField()
    partno = models.IntegerField()
    finishing = models.CharField(max_length=10)
    inserts = models.CharField(max_length=3)
    make = models.CharField(max_length=25)
    tolerance = models.FloatField()
    wattage = models.CharField(max_length=25)
    ppmntcr = models.CharField(max_length=10)
    dimensions = models.CharField(max_length=15)
    package = models.CharField(max_length=15)
    pack_just = models.CharField(max_length=100)
    description = models.TextField()
    part_cat = models.CharField(max_length=10)
    createdby = models.CharField(max_length=7)
    me_user = models.CharField(max_length=7)
    ntry_date = models.DateField()
    ntry_time = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    categorymas = models.CharField(max_length=11)
    mainfamily = models.CharField(max_length=2)
    subfamily = models.CharField(max_length=3)
    copper_value = models.CharField(max_length=10)
    sequencenum = models.CharField(max_length=5)
    cmsnum = models.CharField(max_length=6)
    matnum = models.CharField(max_length=11)
    matdescription = models.CharField(max_length=40)
    status = models.IntegerField()
    me_comments = models.TextField()
    user_comment = models.TextField()
    user_status = models.IntegerField()
    mat_type = models.CharField(max_length=50)
    mat_group = models.CharField(max_length=50)
    prod_alloc = models.CharField(max_length=25)
    ind_std_desc = models.CharField(max_length=50)
    round_val = models.IntegerField()
    purch_group = models.CharField(max_length=50)
    batch_mang = models.CharField(max_length=100)
    purch_order_text = models.TextField()
    stor_loc = models.CharField(max_length=25)
    serial_no_profile = models.CharField(max_length=50)
    inspection_setup = models.CharField(max_length=100)
    valuation_class = models.IntegerField()
    closed_or_not = models.IntegerField()
    completed_date = models.DateTimeField()
    lom_team = models.CharField(max_length=7)
    testcertificate = models.CharField(max_length=2)
    fyi = models.CharField(max_length=2)
    contact_details = models.TextField()
    new_or_exist_code = models.CharField(max_length=5)
    leadtime = models.CharField(max_length=20)
    moqdetails = models.CharField(max_length=30)
    replytomeuser = models.TextField()
    sapdownload = models.IntegerField()
    completed = models.IntegerField()
    mail_cc = models.CharField(max_length=250)
    gl = models.CharField(max_length=10)
    glapproved = models.CharField(max_length=5)
    gl_date = models.CharField(max_length=20)
    hod = models.CharField(max_length=10)
    hodapproved = models.CharField(max_length=5)
    approve_date = models.CharField(max_length=20)
    reason = models.IntegerField()
    single_source = models.IntegerField()
    others = models.CharField(max_length=200)
    leadingtime = models.IntegerField()
    moq = models.IntegerField()
    spq = models.IntegerField()
    market_avl = models.IntegerField()
    mark_avail = models.TextField()
    attach_purchase = models.CharField(max_length=100)
    mat_empcode = models.CharField(max_length=7)
    in_sufficient = models.IntegerField()
    in_suff_field1 = models.IntegerField()
    in_suff_field2 = models.TextField()
    ens_dup = models.IntegerField()
    ensure_txt = models.TextField()
    me_e_r_me_m = models.CharField(max_length=2)
    delete1 = models.IntegerField()
    fin_det = models.CharField(max_length=10)
    detail_source = models.IntegerField()
    not_tried_rsn = models.CharField(max_length=500)
    not_date = models.DateField(blank=True, null=True)
    not_date_sts = models.IntegerField()
    mat_code = models.CharField(max_length=13)
    annu_cum = models.CharField(max_length=10)
    applic = models.CharField(max_length=20)
    mtbf = models.CharField(max_length=10)
    msd = models.CharField(max_length=10)
    prog_int = models.CharField(max_length=100)
    prog_toll = models.CharField(max_length=100)
    alt_sts = models.IntegerField()
    file_name = models.CharField(max_length=100)
    product_grade = models.IntegerField()
    intramoving = models.IntegerField()
    dwg_move = models.IntegerField()
    real_move = models.IntegerField()
    datasheet_move = models.IntegerField()
    metric_size_dig1 = models.CharField(max_length=10)
    metric_size_dig2 = models.CharField(max_length=10)
    head = models.CharField(max_length=10)
    length_dig1 = models.CharField(max_length=10)
    length_dig2 = models.CharField(max_length=10)
    material = models.CharField(max_length=10)
    finish = models.CharField(max_length=10)
    suf_dig1 = models.CharField(max_length=10)
    suf_dig2 = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'lom_ntry_31-07-2021'


class LomNtryAlternate(models.Model):
    alt_id = models.AutoField(primary_key=True)
    slno = models.IntegerField()
    category = models.IntegerField()
    main_cat = models.CharField(max_length=11)
    sub_cat = models.CharField(max_length=11)
    ntry_date = models.DateField()
    createdby = models.CharField(max_length=6)
    hod = models.IntegerField()
    hod_sts = models.IntegerField()
    hod_comm = models.CharField(max_length=50)
    hod_date = models.DateField()
    meteam_sts = models.IntegerField()
    meteam = models.CharField(max_length=6)
    meteam_comm = models.CharField(max_length=50)
    peer_sts = models.IntegerField()
    peer = models.CharField(max_length=6)
    peer_comm = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'lom_ntry_alternate'


class LomNtryBack(models.Model):
    slno = models.AutoField(primary_key=True)
    category = models.IntegerField()
    lomtype = models.CharField(max_length=5)
    sub_type = models.IntegerField()
    value = models.CharField(max_length=15)
    malefe = models.CharField(max_length=7)
    noofpins = models.CharField(max_length=25)
    straightright = models.CharField(max_length=30)
    noofrows = models.CharField(max_length=15)
    pcbthickness = models.CharField(max_length=20)
    sqmm = models.IntegerField()
    noofcores = models.IntegerField()
    noofstrands = models.IntegerField()
    strandthickness = models.FloatField()
    voltagerating = models.CharField(max_length=15)
    currentrating = models.CharField(max_length=15)
    od = models.CharField(max_length=15)
    operatingtemperature = models.CharField(max_length=15)
    uom = models.CharField(max_length=5)
    approximateprice = models.CharField(max_length=15)
    aseriescode = models.CharField(max_length=15)
    drawdocref = models.CharField(max_length=20)
    proprietary = models.CharField(max_length=3)
    product_code = models.CharField(max_length=10)
    connect_pins = models.IntegerField()
    connt_cat = models.IntegerField()
    connt_sub_cat = models.IntegerField()
    ed_no = models.CharField(max_length=10)
    page_r_serial = models.CharField(max_length=10)
    special_ref = models.CharField(max_length=200)
    specialcare = models.CharField(max_length=3)
    specialcaretext = models.CharField(max_length=50)
    periodmaint = models.CharField(max_length=3)
    periodmaint_attach = models.CharField(max_length=250)
    inspectioncriteria = models.TextField()
    partno = models.IntegerField()
    finishing = models.CharField(max_length=10)
    inserts = models.CharField(max_length=3)
    make = models.CharField(max_length=25)
    tolerance = models.FloatField()
    wattage = models.CharField(max_length=25)
    ppmntcr = models.CharField(max_length=10)
    dimensions = models.CharField(max_length=15)
    package = models.CharField(max_length=15)
    pack_just = models.CharField(max_length=100)
    description = models.TextField()
    part_cat = models.CharField(max_length=10)
    createdby = models.CharField(max_length=7)
    me_user = models.CharField(max_length=7)
    ntry_date = models.DateField()
    ntry_time = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    categorymas = models.CharField(max_length=11)
    mainfamily = models.CharField(max_length=2)
    subfamily = models.CharField(max_length=3)
    copper_value = models.CharField(max_length=10)
    sequencenum = models.CharField(max_length=5)
    cmsnum = models.CharField(max_length=6)
    matnum = models.CharField(max_length=11)
    matdescription = models.CharField(max_length=40)
    status = models.IntegerField()
    me_comments = models.TextField()
    user_comment = models.TextField()
    user_status = models.IntegerField()
    mat_type = models.CharField(max_length=50)
    mat_group = models.CharField(max_length=50)
    prod_alloc = models.CharField(max_length=25)
    ind_std_desc = models.CharField(max_length=50)
    round_val = models.IntegerField()
    purch_group = models.CharField(max_length=50)
    batch_mang = models.CharField(max_length=100)
    purch_order_text = models.TextField()
    stor_loc = models.CharField(max_length=25)
    serial_no_profile = models.CharField(max_length=50)
    inspection_setup = models.CharField(max_length=100)
    valuation_class = models.IntegerField()
    closed_or_not = models.IntegerField()
    completed_date = models.DateTimeField()
    lom_team = models.CharField(max_length=7)
    testcertificate = models.CharField(max_length=2)
    fyi = models.CharField(max_length=2)
    contact_details = models.TextField()
    new_or_exist_code = models.CharField(max_length=5)
    leadtime = models.CharField(max_length=20)
    moqdetails = models.CharField(max_length=30)
    replytomeuser = models.TextField()
    sapdownload = models.IntegerField()
    completed = models.IntegerField()
    mail_cc = models.CharField(max_length=250)
    gl = models.CharField(max_length=10)
    glapproved = models.CharField(max_length=5)
    gl_date = models.CharField(max_length=20)
    hod = models.CharField(max_length=10)
    hodapproved = models.CharField(max_length=5)
    approve_date = models.CharField(max_length=20)
    reason = models.IntegerField()
    single_source = models.IntegerField()
    others = models.CharField(max_length=200)
    leadingtime = models.IntegerField()
    moq = models.IntegerField()
    spq = models.IntegerField()
    market_avl = models.IntegerField()
    mark_avail = models.TextField()
    attach_purchase = models.CharField(max_length=100)
    mat_empcode = models.CharField(max_length=7)
    in_sufficient = models.IntegerField()
    in_suff_field1 = models.IntegerField()
    in_suff_field2 = models.TextField()
    ens_dup = models.IntegerField()
    ensure_txt = models.TextField()
    me_e_r_me_m = models.CharField(max_length=2)
    delete1 = models.IntegerField()
    fin_det = models.CharField(max_length=10)
    detail_source = models.IntegerField()
    not_tried_rsn = models.CharField(max_length=500)
    not_date = models.DateField(blank=True, null=True)
    not_date_sts = models.IntegerField()
    mat_code = models.CharField(max_length=13)
    annu_cum = models.CharField(max_length=10)
    applic = models.CharField(max_length=20)
    mtbf = models.CharField(max_length=10)
    msd = models.CharField(max_length=10)
    prog_int = models.CharField(max_length=100)
    prog_toll = models.CharField(max_length=100)
    alt_sts = models.IntegerField()
    file_name = models.CharField(max_length=100)
    product_grade = models.IntegerField()
    intramoving = models.IntegerField()
    dwg_move = models.IntegerField()
    real_move = models.IntegerField()
    datasheet_move = models.IntegerField()
    metric_size_dig1 = models.CharField(max_length=10)
    metric_size_dig2 = models.CharField(max_length=10)
    head = models.CharField(max_length=10)
    length_dig1 = models.CharField(max_length=10)
    length_dig2 = models.CharField(max_length=10)
    material = models.CharField(max_length=10)
    finish = models.CharField(max_length=10)
    suf_dig1 = models.CharField(max_length=10)
    suf_dig2 = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'lom_ntry_back'


class LomNtryBackup(models.Model):
    slno = models.AutoField(primary_key=True)
    category = models.IntegerField()
    lomtype = models.CharField(max_length=5)
    sub_type = models.IntegerField()
    value = models.CharField(max_length=15)
    malefe = models.CharField(max_length=7)
    noofpins = models.CharField(max_length=25)
    straightright = models.CharField(max_length=30)
    noofrows = models.CharField(max_length=15)
    pcbthickness = models.CharField(max_length=20)
    sqmm = models.IntegerField()
    noofcores = models.IntegerField()
    noofstrands = models.IntegerField()
    strandthickness = models.FloatField()
    voltagerating = models.CharField(max_length=15)
    currentrating = models.CharField(max_length=15)
    od = models.CharField(max_length=15)
    operatingtemperature = models.CharField(max_length=15)
    uom = models.CharField(max_length=5)
    approximateprice = models.CharField(max_length=15)
    aseriescode = models.CharField(max_length=15)
    drawdocref = models.CharField(max_length=20)
    proprietary = models.CharField(max_length=3)
    product_code = models.CharField(max_length=10)
    connect_pins = models.IntegerField()
    connt_cat = models.IntegerField()
    connt_sub_cat = models.IntegerField()
    ed_no = models.CharField(max_length=10)
    page_r_serial = models.CharField(max_length=10)
    special_ref = models.CharField(max_length=200)
    specialcare = models.CharField(max_length=3)
    specialcaretext = models.CharField(max_length=50)
    periodmaint = models.CharField(max_length=3)
    periodmaint_attach = models.CharField(max_length=250)
    inspectioncriteria = models.TextField()
    partno = models.IntegerField()
    finishing = models.CharField(max_length=10)
    inserts = models.CharField(max_length=3)
    make = models.CharField(max_length=25)
    tolerance = models.FloatField()
    wattage = models.CharField(max_length=25)
    ppmntcr = models.CharField(max_length=10)
    dimensions = models.CharField(max_length=15)
    package = models.CharField(max_length=15)
    pack_just = models.CharField(max_length=100)
    description = models.TextField()
    part_cat = models.CharField(max_length=10)
    createdby = models.CharField(max_length=7)
    me_user = models.CharField(max_length=7)
    ntry_date = models.DateField()
    ntry_time = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    categorymas = models.CharField(max_length=11)
    mainfamily = models.CharField(max_length=2)
    subfamily = models.CharField(max_length=3)
    copper_value = models.CharField(max_length=10)
    sequencenum = models.CharField(max_length=5)
    cmsnum = models.CharField(max_length=6)
    matnum = models.CharField(max_length=11)
    matdescription = models.CharField(max_length=40)
    status = models.IntegerField()
    me_comments = models.TextField()
    user_comment = models.TextField()
    user_status = models.IntegerField()
    mat_type = models.CharField(max_length=50)
    mat_group = models.CharField(max_length=50)
    prod_alloc = models.CharField(max_length=25)
    ind_std_desc = models.CharField(max_length=50)
    round_val = models.IntegerField()
    purch_group = models.CharField(max_length=50)
    batch_mang = models.CharField(max_length=100)
    purch_order_text = models.TextField()
    stor_loc = models.CharField(max_length=25)
    serial_no_profile = models.CharField(max_length=50)
    inspection_setup = models.CharField(max_length=100)
    valuation_class = models.IntegerField()
    closed_or_not = models.IntegerField()
    completed_date = models.DateTimeField()
    lom_team = models.CharField(max_length=7)
    testcertificate = models.CharField(max_length=2)
    fyi = models.CharField(max_length=2)
    contact_details = models.TextField()
    new_or_exist_code = models.CharField(max_length=5)
    leadtime = models.CharField(max_length=20)
    moqdetails = models.CharField(max_length=30)
    replytomeuser = models.TextField()
    sapdownload = models.IntegerField()
    completed = models.IntegerField()
    mail_cc = models.CharField(max_length=250)
    gl = models.CharField(max_length=10)
    glapproved = models.CharField(max_length=5)
    gl_date = models.CharField(max_length=20)
    hod = models.CharField(max_length=10)
    hodapproved = models.CharField(max_length=5)
    approve_date = models.CharField(max_length=20)
    reason = models.IntegerField()
    single_source = models.IntegerField()
    others = models.CharField(max_length=200)
    leadingtime = models.IntegerField()
    moq = models.IntegerField()
    spq = models.IntegerField()
    market_avl = models.IntegerField()
    mark_avail = models.TextField()
    attach_purchase = models.CharField(max_length=100)
    mat_empcode = models.CharField(max_length=7)
    in_sufficient = models.IntegerField()
    in_suff_field1 = models.IntegerField()
    in_suff_field2 = models.TextField()
    ens_dup = models.IntegerField()
    ensure_txt = models.TextField()
    me_e_r_me_m = models.CharField(max_length=2)
    delete1 = models.IntegerField()
    fin_det = models.CharField(max_length=10)
    detail_source = models.IntegerField()
    not_tried_rsn = models.CharField(max_length=500)
    not_date = models.DateField(blank=True, null=True)
    not_date_sts = models.IntegerField()
    mat_code = models.CharField(max_length=13)
    annu_cum = models.CharField(max_length=10)
    applic = models.CharField(max_length=20)
    mtbf = models.CharField(max_length=10)
    msd = models.CharField(max_length=10)
    prog_int = models.CharField(max_length=100)
    prog_toll = models.CharField(max_length=100)
    alt_sts = models.IntegerField()
    file_name = models.CharField(max_length=100)
    product_grade = models.IntegerField()
    intramoving = models.IntegerField()
    dwg_move = models.IntegerField()
    real_move = models.IntegerField()
    datasheet_move = models.IntegerField()
    metric_size_dig1 = models.CharField(max_length=10)
    metric_size_dig2 = models.CharField(max_length=10)
    head = models.CharField(max_length=10)
    length_dig1 = models.CharField(max_length=10)
    length_dig2 = models.CharField(max_length=10)
    material = models.CharField(max_length=10)
    finish = models.CharField(max_length=10)
    suf_dig1 = models.CharField(max_length=10)
    suf_dig2 = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'lom_ntry_backup'


class LomNtryOld(models.Model):
    slno = models.AutoField(primary_key=True)
    category = models.IntegerField()
    lomtype = models.CharField(max_length=5)
    sub_type = models.IntegerField()
    value = models.CharField(max_length=15)
    malefe = models.CharField(max_length=7)
    noofpins = models.CharField(max_length=25)
    straightright = models.CharField(max_length=30)
    noofrows = models.CharField(max_length=15)
    pcbthickness = models.CharField(max_length=20)
    sqmm = models.IntegerField()
    noofcores = models.IntegerField()
    noofstrands = models.IntegerField()
    strandthickness = models.FloatField()
    voltagerating = models.CharField(max_length=15)
    currentrating = models.CharField(max_length=15)
    od = models.CharField(max_length=15)
    operatingtemperature = models.CharField(max_length=15)
    uom = models.CharField(max_length=5)
    approximateprice = models.CharField(max_length=15)
    aseriescode = models.CharField(max_length=15)
    drawdocref = models.CharField(max_length=20)
    proprietary = models.CharField(max_length=3)
    product_code = models.CharField(max_length=10)
    connect_pins = models.IntegerField()
    connt_cat = models.IntegerField()
    connt_sub_cat = models.IntegerField()
    ed_no = models.CharField(max_length=10)
    page_r_serial = models.CharField(max_length=10)
    special_ref = models.CharField(max_length=200)
    specialcare = models.CharField(max_length=3)
    specialcaretext = models.CharField(max_length=50)
    periodmaint = models.CharField(max_length=3)
    periodmaint_attach = models.CharField(max_length=250)
    inspectioncriteria = models.TextField()
    partno = models.IntegerField()
    finishing = models.CharField(max_length=10)
    inserts = models.CharField(max_length=3)
    make = models.CharField(max_length=25)
    tolerance = models.FloatField()
    wattage = models.CharField(max_length=25)
    ppmntcr = models.CharField(max_length=10)
    dimensions = models.CharField(max_length=15)
    package = models.CharField(max_length=15)
    pack_just = models.CharField(max_length=100)
    description = models.TextField()
    part_cat = models.CharField(max_length=10)
    createdby = models.CharField(max_length=7)
    me_user = models.CharField(max_length=7)
    ntry_date = models.DateField()
    ntry_time = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    categorymas = models.CharField(max_length=11)
    mainfamily = models.CharField(max_length=2)
    subfamily = models.CharField(max_length=3)
    copper_value = models.CharField(max_length=10)
    sequencenum = models.CharField(max_length=5)
    cmsnum = models.CharField(max_length=6)
    matnum = models.CharField(max_length=11)
    matdescription = models.CharField(max_length=40)
    status = models.IntegerField()
    me_comments = models.TextField()
    user_comment = models.TextField()
    user_status = models.IntegerField()
    mat_type = models.CharField(max_length=50)
    mat_group = models.CharField(max_length=50)
    prod_alloc = models.CharField(max_length=25)
    ind_std_desc = models.CharField(max_length=50)
    round_val = models.IntegerField()
    purch_group = models.CharField(max_length=50)
    batch_mang = models.CharField(max_length=100)
    purch_order_text = models.TextField()
    stor_loc = models.CharField(max_length=25)
    serial_no_profile = models.CharField(max_length=50)
    inspection_setup = models.CharField(max_length=100)
    valuation_class = models.IntegerField()
    closed_or_not = models.IntegerField()
    completed_date = models.DateTimeField()
    lom_team = models.CharField(max_length=7)
    testcertificate = models.CharField(max_length=2)
    fyi = models.CharField(max_length=2)
    contact_details = models.TextField()
    new_or_exist_code = models.CharField(max_length=5)
    leadtime = models.CharField(max_length=20)
    moqdetails = models.CharField(max_length=30)
    replytomeuser = models.TextField()
    sapdownload = models.IntegerField()
    completed = models.IntegerField()
    mail_cc = models.CharField(max_length=250)
    gl = models.CharField(max_length=10)
    glapproved = models.CharField(max_length=5)
    gl_date = models.CharField(max_length=20)
    hod = models.CharField(max_length=10)
    hodapproved = models.CharField(max_length=5)
    approve_date = models.CharField(max_length=20)
    reason = models.IntegerField()
    single_source = models.IntegerField()
    others = models.CharField(max_length=200)
    leadingtime = models.IntegerField()
    moq = models.IntegerField()
    spq = models.IntegerField()
    market_avl = models.IntegerField()
    mark_avail = models.TextField()
    attach_purchase = models.CharField(max_length=100)
    mat_empcode = models.CharField(max_length=7)
    in_sufficient = models.IntegerField()
    in_suff_field1 = models.IntegerField()
    in_suff_field2 = models.TextField()
    ens_dup = models.IntegerField()
    ensure_txt = models.TextField()
    me_e_r_me_m = models.CharField(max_length=2)
    delete1 = models.IntegerField()
    fin_det = models.CharField(max_length=10)
    detail_source = models.IntegerField()
    not_tried_rsn = models.CharField(max_length=500)
    not_date = models.DateField(blank=True, null=True)
    not_date_sts = models.IntegerField()
    mat_code = models.CharField(max_length=13)
    annu_cum = models.CharField(max_length=10)
    applic = models.CharField(max_length=20)
    mtbf = models.CharField(max_length=10)
    msd = models.CharField(max_length=10)
    prog_int = models.CharField(max_length=100)
    prog_toll = models.CharField(max_length=100)
    alt_sts = models.IntegerField()
    file_name = models.CharField(max_length=100)
    product_grade = models.IntegerField()
    intramoving = models.IntegerField()
    dwg_move = models.IntegerField()
    real_move = models.IntegerField()
    datasheet_move = models.IntegerField()
    metric_size_dig1 = models.CharField(max_length=10)
    metric_size_dig2 = models.CharField(max_length=10)
    head = models.CharField(max_length=10)
    length_dig1 = models.CharField(max_length=10)
    length_dig2 = models.CharField(max_length=10)
    material = models.CharField(max_length=10)
    finish = models.CharField(max_length=10)
    suf_dig1 = models.CharField(max_length=10)
    suf_dig2 = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'lom_ntry_old'


class LomNumMaster(models.Model):
    num_id = models.AutoField(primary_key=True)
    category = models.IntegerField()
    categoryname = models.CharField(max_length=100)
    mainfamily = models.CharField(max_length=2)
    mainfamilyname = models.CharField(max_length=200)
    subfamily = models.CharField(max_length=3)
    subfamilyname = models.CharField(max_length=500)
    startnum = models.CharField(max_length=5)
    subfalimy_shortname = models.CharField(max_length=100)
    sd_num = models.CharField(max_length=8)
    round_val = models.IntegerField()
    msd_valid = models.IntegerField()
    cate_name = models.CharField(max_length=15)
    createdby = models.CharField(max_length=7)
    delete1 = models.IntegerField()
    deletedby = models.CharField(max_length=7)
    deleteddate = models.DateField()

    class Meta:
        managed = False
        db_table = 'lom_num_master'


class LomNumMasterOld(models.Model):
    category = models.CharField(max_length=1)
    num_id = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=100)
    mainfamily = models.CharField(max_length=2)
    mainfamilyname = models.CharField(max_length=200)
    subfamily = models.CharField(max_length=3)
    subfamilyname = models.CharField(max_length=500)
    startnum = models.CharField(max_length=5)
    subfalimy_shortname = models.CharField(max_length=100)
    sd_num = models.CharField(max_length=8)
    round_val = models.IntegerField()
    msd_valid = models.IntegerField()
    cate_name = models.CharField(max_length=15)
    createdby = models.CharField(max_length=7)
    delete1 = models.IntegerField()
    deletedby = models.CharField(max_length=7)
    deleteddate = models.DateField()

    class Meta:
        managed = False
        db_table = 'lom_num_master_old'


class LomPartnoNtry(models.Model):
    pid = models.AutoField(primary_key=True)
    ischecked = models.CharField(max_length=2)
    slno = models.IntegerField()
    partno = models.CharField(max_length=170, db_collation='utf8_general_ci', blank=True, null=True)
    make = models.CharField(max_length=50, blank=True, null=True)
    spq = models.CharField(max_length=100, blank=True, null=True)
    packing = models.CharField(max_length=100, blank=True, null=True)
    mark_code = models.CharField(max_length=25, blank=True, null=True)
    part_cat = models.CharField(max_length=20, blank=True, null=True)
    rdso = models.CharField(max_length=15, blank=True, null=True)
    units = models.CharField(max_length=50, blank=True, null=True)
    rel_data = models.CharField(max_length=50, blank=True, null=True)
    datasheetstatus = models.CharField(max_length=1)
    datasheet_filename = models.CharField(max_length=500, blank=True, null=True)
    datasheet_last_update = models.CharField(max_length=500, blank=True, null=True)
    pcn_name = models.CharField(max_length=1000, blank=True, null=True)
    pcn_attach = models.CharField(max_length=1000, blank=True, null=True)
    pcn_last_update = models.CharField(max_length=500, blank=True, null=True)
    sapdownload = models.IntegerField()
    market_aval = models.CharField(max_length=100, blank=True, null=True)
    due_date = models.DateField()
    file_name = models.CharField(max_length=200, blank=True, null=True)
    real_file = models.CharField(max_length=100, blank=True, null=True)
    valu = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    in_suff_field5 = models.CharField(max_length=10, blank=True, null=True)
    del_by = models.CharField(max_length=10, blank=True, null=True)
    dwg = models.CharField(max_length=50, blank=True, null=True)
    intramoving = models.IntegerField()
    dwg_move = models.IntegerField()
    real_move = models.IntegerField()
    datasheet_move = models.IntegerField()
    rohs = models.IntegerField(blank=True, null=True)
    temperat = models.CharField(max_length=20, blank=True, null=True)
    createdby = models.IntegerField()
    mpndesc = models.CharField(max_length=50, blank=True, null=True)
    pack = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lom_partno_ntry'


class LomPartnoNtry31072021(models.Model):
    pid = models.AutoField(primary_key=True)
    ischecked = models.CharField(max_length=2)
    slno = models.IntegerField()
    partno = models.CharField(max_length=35)
    make = models.CharField(max_length=25)
    spq = models.CharField(max_length=100)
    packing = models.CharField(max_length=100)
    mark_code = models.CharField(max_length=25)
    part_cat = models.CharField(max_length=20)
    rdso = models.CharField(max_length=15)
    units = models.CharField(max_length=50)
    rel_data = models.CharField(max_length=50)
    datasheetstatus = models.CharField(max_length=1)
    datasheet_filename = models.CharField(max_length=500)
    datasheet_last_update = models.CharField(max_length=500)
    pcn_name = models.CharField(max_length=1000)
    pcn_attach = models.CharField(max_length=1000)
    pcn_last_update = models.CharField(max_length=500)
    sapdownload = models.IntegerField()
    market_aval = models.CharField(max_length=100)
    due_date = models.DateField()
    file_name = models.CharField(max_length=200)
    real_file = models.CharField(max_length=100)
    valu = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    in_suff_field5 = models.CharField(max_length=10)
    del_by = models.CharField(max_length=10)
    dwg = models.CharField(max_length=30)
    intramoving = models.IntegerField()
    dwg_move = models.IntegerField()
    real_move = models.IntegerField()
    datasheet_move = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lom_partno_ntry_31-07-2021'


class LomPartnoNtryTemp(models.Model):
    slno = models.IntegerField()
    matnum = models.CharField(max_length=15)
    matdesc = models.CharField(max_length=100)
    partno = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    market_aval = models.CharField(max_length=50)
    due_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'lom_partno_ntry_temp'


class LomSelMaster(models.Model):
    category = models.IntegerField()
    master_type = models.CharField(max_length=50, blank=True, null=True)
    selection = models.CharField(max_length=100, blank=True, null=True)
    suffix = models.CharField(max_length=20, blank=True, null=True)
    sufixes = models.IntegerField()
    conditions = models.CharField(max_length=10, blank=True, null=True)
    createdby = models.CharField(max_length=7, blank=True, null=True)
    delete1 = models.IntegerField()
    deletedate = models.DateField()
    deletedby = models.CharField(max_length=7, blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lom_sel_master'


class LomSelVerMas(models.Model):
    value_id = models.CharField(max_length=50)
    short_form = models.CharField(max_length=200)
    mat_type_group = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lom_sel_ver_mas'


class LomStatusMaster(models.Model):
    sid = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100)
    createdby = models.CharField(max_length=7)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    deletedby = models.CharField(max_length=7)
    deleteddate = models.DateField()

    class Meta:
        managed = False
        db_table = 'lom_status_master'


class LomTargetdays(models.Model):
    request_id = models.IntegerField()
    unit_no = models.IntegerField()
    task = models.IntegerField()
    othertask = models.CharField(max_length=400, blank=True, null=True)
    days = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lom_targetdays'


class LomTargetdaysUpdt(models.Model):
    request_id = models.IntegerField()
    unit_no = models.IntegerField()
    task = models.IntegerField()
    othertask = models.CharField(max_length=400)
    days = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lom_targetdays_updt'


class LomTargethis(models.Model):
    request_id = models.IntegerField()
    unit_no = models.IntegerField()
    target_date = models.DateField()
    justification = models.CharField(max_length=300, blank=True, null=True)
    total_days = models.IntegerField()
    date = models.DateField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lom_targethis'


class LomTargethisUpdt(models.Model):
    request_id = models.IntegerField()
    unit_no = models.IntegerField()
    target_date = models.DateField()
    justification = models.CharField(max_length=300)
    total_days = models.IntegerField()
    date = models.DateField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lom_targethis_updt'


class LomTeam(models.Model):
    empcode = models.CharField(max_length=7)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lom_team'


class LomType(models.Model):
    typeid = models.AutoField(primary_key=True)
    category = models.IntegerField()
    typename = models.CharField(max_length=500)
    createdby = models.CharField(max_length=7)
    delete1 = models.IntegerField()
    deleteby = models.CharField(max_length=7)
    deleteddate = models.DateField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lom_type'


class LomUserMeHis(models.Model):
    slno = models.IntegerField()
    status = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    date = models.DateField()
    assocaite = models.CharField(max_length=7, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lom_user_me_his'


class Ltcreimbursesubdata(models.Model):
    id = models.BigAutoField(primary_key=True)
    ref_no = models.IntegerField()
    jrny_begin = models.DateField()
    jrny_end = models.DateField()
    claming_amount = models.FloatField()
    jrny_strtpoint = models.CharField(max_length=500)
    jrny_endpoint = models.CharField(max_length=500)
    travelmode = models.CharField(max_length=50)
    clasoftravel = models.CharField(max_length=50)
    ticketno = models.CharField(max_length=100)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ltcreimbursesubdata'


class LugsMaster(models.Model):
    slno = models.IntegerField()
    wfno = models.CharField(max_length=25)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    to_lug_type = models.CharField(max_length=15)
    to_ferrule = models.CharField(max_length=50)
    size = models.CharField(max_length=15)
    to_from = models.CharField(max_length=4)
    length = models.IntegerField()
    from_lug_type = models.CharField(max_length=15)
    from_ferrule = models.CharField(max_length=50)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lugs_master'


class LugsMasterTemp(models.Model):
    slno = models.IntegerField()
    wfno = models.CharField(max_length=25)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    to_lug_type = models.CharField(max_length=15)
    to_ferrule = models.CharField(max_length=50)
    size = models.CharField(max_length=15)
    to_from = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'lugs_master_temp'


class LugsMatnrMaster(models.Model):
    matnr = models.CharField(max_length=15)
    desc = models.CharField(max_length=50)
    color = models.CharField(max_length=15)
    photo_type = models.CharField(max_length=5)
    createb_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lugs_matnr_master'


class LunchEntrys(models.Model):
    lunch_id = models.AutoField(primary_key=True)
    ass_guest = models.CharField(max_length=2)
    type_lunch = models.CharField(max_length=2)
    type_guest = models.CharField(max_length=2)
    empcode = models.CharField(max_length=7)
    lunch_desc = models.CharField(max_length=250)
    qty = models.CharField(max_length=3)
    lucch_time = models.CharField(max_length=1)
    lunch_code = models.CharField(max_length=5)
    lunch_date = models.DateField()
    lunch_timestamp = models.DateTimeField()
    enteredby = models.CharField(max_length=7)
    released = models.CharField(max_length=1)
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'lunch_entrys'


class LunchMaster(models.Model):
    lunch_mid = models.IntegerField()
    lunch_name = models.CharField(max_length=50)
    lunch_type = models.CharField(max_length=1)
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'lunch_master'


class Mail(models.Model):
    from_field = models.IntegerField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.IntegerField()
    desc = models.CharField(max_length=500)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mail'


class MailDat(models.Model):
    slno = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    msg = models.CharField(max_length=150)
    rcvr = models.IntegerField()
    sts = models.CharField(max_length=15)
    date = models.DateField()
    break_field = models.IntegerField(db_column='break')  # Field renamed because it was a Python reserved word.
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mail_dat'



class MainDvlprLgin(models.Model):
    slno = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    date = models.DateField()
    in_field = models.TimeField(db_column='in')  # Field renamed because it was a Python reserved word.
    out = models.TimeField()
    type = models.CharField(max_length=20)
    tot_hr = models.TimeField()
    wrkd_hr = models.TimeField()
    rmn_hr = models.TimeField()
    max_updt_time = models.TimeField()
    on_off = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'main_dvlpr_lgin'


class MainEmpTothrs(models.Model):
    empcode = models.IntegerField()
    tot_hrs = models.CharField(max_length=20)
    dvlpr_type = models.CharField(max_length=1)
    module_type = models.CharField(max_length=5)
    empname = models.CharField(max_length=50)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'main_emp_tothrs'


class MainFspecOuttype(models.Model):
    slno = models.AutoField(primary_key=True)
    outtype_name = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'main_fspec_outtype'


class MainFspecTblLgc(models.Model):
    tag_no = models.IntegerField()
    slno = models.IntegerField()
    tbl = models.CharField(max_length=50)
    tbl_desc = models.CharField(max_length=500)
    type = models.CharField(max_length=150)
    mod = models.CharField(max_length=50)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'main_fspec_tbl_lgc'


class MainPrgTypeMaster(models.Model):
    slno = models.AutoField(primary_key=True)
    prg_name = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'main_prg_type_master'


class MainPrgTypeNtry(models.Model):
    tag_no = models.IntegerField()
    prg_slno = models.IntegerField()
    prg_desc = models.CharField(max_length=500)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'main_prg_type_ntry'


class MainSpecIpFlds(models.Model):
    tag_no = models.IntegerField()
    slno = models.IntegerField()
    fld_name = models.CharField(max_length=50)
    fld_ip_type = models.IntegerField()
    mndtry = models.IntegerField()
    rmrks = models.CharField(max_length=100)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'main_spec_ip_flds'


class MainSpecMain(models.Model):
    tag_no = models.IntegerField()
    prcsng_lgc_desc = models.CharField(max_length=1000)
    op_alv = models.CharField(max_length=500)
    op_smrt = models.TextField()
    smrt_ext = models.CharField(max_length=100)
    op_msg = models.CharField(max_length=500)
    fnl_att = models.TextField()
    fnl_ext = models.CharField(max_length=100)
    note = models.CharField(max_length=500)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'main_spec_main'


class MainSpecPrcsngLgc(models.Model):
    tag_no = models.IntegerField()
    slno = models.IntegerField()
    prsng_val = models.CharField(max_length=1000)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'main_spec_prcsng_lgc'


class MainSpecSrtOrdr(models.Model):
    tag_no = models.IntegerField()
    slno = models.IntegerField()
    srt_name = models.CharField(max_length=50)
    srt_type = models.CharField(max_length=4)
    prty = models.CharField(max_length=50)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'main_spec_srt_ordr'


class MainTagTime(models.Model):
    tag_no = models.IntegerField()
    empcode = models.IntegerField()
    sts = models.IntegerField()
    update_sts = models.IntegerField()
    timestamp = models.CharField(max_length=25)
    last_update_tag = models.IntegerField()
    last_update_tag_timestamp = models.CharField(max_length=50)
    temp_time = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'main_tag_time'


class MainTr(models.Model):
    tag_no = models.AutoField(primary_key=True)
    tag_desc = models.TextField(blank=True, null=True)
    req = models.CharField(max_length=100, blank=True, null=True)
    dept = models.IntegerField()
    rq_forum = models.CharField(max_length=20, blank=True, null=True)
    rq_desc = models.CharField(max_length=100, blank=True, null=True)
    priority = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    issue_cat = models.CharField(max_length=100, blank=True, null=True)
    issue_sub_cat = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    tag_ass = models.CharField(max_length=100, blank=True, null=True)
    support = models.CharField(max_length=100, blank=True, null=True)
    pr_start_date = models.DateField()
    pr_cmpltd_date = models.DateField()
    actual_date = models.DateField()
    act_cmpltd_date = models.DateField()
    confirm = models.CharField(max_length=5)
    createdby = models.IntegerField()
    tag_re_ass = models.CharField(max_length=20, blank=True, null=True)
    mod = models.CharField(max_length=20, blank=True, null=True)
    ccat_name = models.CharField(max_length=50, blank=True, null=True)
    tcode = models.CharField(max_length=100, blank=True, null=True)
    prgrm = models.CharField(max_length=500, blank=True, null=True)
    acptby = models.CharField(max_length=50, blank=True, null=True)
    ac_rmrks = models.CharField(max_length=250, blank=True, null=True)
    req_type = models.IntegerField()
    spnd_time = models.TimeField()
    rating = models.IntegerField()
    poor_avg = models.CharField(max_length=500, blank=True, null=True)
    final_closed = models.IntegerField()
    final_closed_by = models.IntegerField()
    final_closed_date = models.DateField()
    rating_aplicability = models.CharField(max_length=2, blank=True, null=True)
    kaizen_user = models.IntegerField()
    last_update_date = models.DateField()
    timestamp = models.DateTimeField()
    supporters = models.CharField(max_length=100, blank=True, null=True)
    prop_compltn_days = models.IntegerField()
    act_compltn_days = models.IntegerField()
    delayed_flag = models.IntegerField()
    new_req_revisionno = models.IntegerField()
    highpriority = models.CharField(max_length=20, blank=True, null=True)
    good_reason = models.CharField(max_length=2000, blank=True, null=True)
    tag_no_inti = models.CharField(max_length=150, blank=True, null=True)
    closed_app_sts = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField()
    reqt_type = models.IntegerField()
    module_nm = models.TextField(blank=True, null=True)
    reson_fr = models.CharField(max_length=1000, blank=True, null=True)
    assign_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'main_tr'


class MainTr1(models.Model):
    tag_no = models.AutoField(primary_key=True)
    tag_desc = models.TextField(blank=True, null=True)
    req = models.CharField(max_length=100, blank=True, null=True)
    dept = models.IntegerField()
    rq_forum = models.CharField(max_length=20, blank=True, null=True)
    rq_desc = models.CharField(max_length=100, blank=True, null=True)
    priority = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    issue_cat = models.CharField(max_length=100, blank=True, null=True)
    issue_sub_cat = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    tag_ass = models.CharField(max_length=100, blank=True, null=True)
    support = models.CharField(max_length=100, blank=True, null=True)
    pr_start_date = models.DateField()
    pr_cmpltd_date = models.DateField()
    actual_date = models.DateField()
    act_cmpltd_date = models.DateField()
    confirm = models.CharField(max_length=5)
    createdby = models.IntegerField()
    tag_re_ass = models.CharField(max_length=20, blank=True, null=True)
    mod = models.CharField(max_length=20, blank=True, null=True)
    ccat_name = models.CharField(max_length=50, blank=True, null=True)
    tcode = models.CharField(max_length=100, blank=True, null=True)
    prgrm = models.CharField(max_length=500, blank=True, null=True)
    acptby = models.CharField(max_length=50, blank=True, null=True)
    ac_rmrks = models.CharField(max_length=250, blank=True, null=True)
    req_type = models.IntegerField()
    spnd_time = models.TimeField()
    rating = models.IntegerField()
    poor_avg = models.CharField(max_length=500, blank=True, null=True)
    final_closed = models.IntegerField()
    final_closed_by = models.IntegerField()
    final_closed_date = models.DateField()
    rating_aplicability = models.CharField(max_length=2, blank=True, null=True)
    kaizen_user = models.IntegerField()
    last_update_date = models.DateField()
    timestamp = models.DateTimeField()
    supporters = models.CharField(max_length=100, blank=True, null=True)
    prop_compltn_days = models.IntegerField()
    act_compltn_days = models.IntegerField()
    delayed_flag = models.IntegerField()
    new_req_revisionno = models.IntegerField()
    highpriority = models.CharField(max_length=20, blank=True, null=True)
    good_reason = models.CharField(max_length=2000, blank=True, null=True)
    tag_no_inti = models.CharField(max_length=150, blank=True, null=True)
    closed_app_sts = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField()
    reqt_type = models.IntegerField()
    module_nm = models.CharField(max_length=350, blank=True, null=True)
    reson_fr = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_tr1'


class MainTr1801(models.Model):
    tag_no = models.AutoField(primary_key=True)
    tag_desc = models.TextField(blank=True, null=True)
    req = models.CharField(max_length=100, blank=True, null=True)
    dept = models.IntegerField()
    rq_forum = models.CharField(max_length=20, blank=True, null=True)
    rq_desc = models.CharField(max_length=100, blank=True, null=True)
    priority = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    issue_cat = models.CharField(max_length=100, blank=True, null=True)
    issue_sub_cat = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    tag_ass = models.CharField(max_length=100, blank=True, null=True)
    support = models.CharField(max_length=100, blank=True, null=True)
    pr_start_date = models.DateField()
    pr_cmpltd_date = models.DateField()
    actual_date = models.DateField()
    act_cmpltd_date = models.DateField()
    confirm = models.CharField(max_length=5)
    createdby = models.IntegerField()
    tag_re_ass = models.CharField(max_length=20, blank=True, null=True)
    mod = models.CharField(max_length=20, blank=True, null=True)
    ccat_name = models.CharField(max_length=50, blank=True, null=True)
    tcode = models.CharField(max_length=100, blank=True, null=True)
    prgrm = models.CharField(max_length=500, blank=True, null=True)
    acptby = models.CharField(max_length=50, blank=True, null=True)
    ac_rmrks = models.CharField(max_length=250, blank=True, null=True)
    req_type = models.IntegerField()
    spnd_time = models.TimeField()
    rating = models.IntegerField()
    poor_avg = models.CharField(max_length=500, blank=True, null=True)
    final_closed = models.IntegerField()
    final_closed_by = models.IntegerField()
    final_closed_date = models.DateField()
    rating_aplicability = models.CharField(max_length=2, blank=True, null=True)
    kaizen_user = models.IntegerField()
    last_update_date = models.DateField()
    timestamp = models.DateTimeField()
    supporters = models.CharField(max_length=100, blank=True, null=True)
    prop_compltn_days = models.IntegerField()
    act_compltn_days = models.IntegerField()
    delayed_flag = models.IntegerField()
    new_req_revisionno = models.IntegerField()
    highpriority = models.CharField(max_length=20, blank=True, null=True)
    good_reason = models.CharField(max_length=2000, blank=True, null=True)
    tag_no_inti = models.CharField(max_length=150, blank=True, null=True)
    closed_app_sts = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField()
    reqt_type = models.IntegerField()
    module_nm = models.CharField(max_length=350, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_tr_18-01'


class MainTrAttachments(models.Model):
    attach_slno = models.AutoField(primary_key=True)
    tag_no = models.IntegerField()
    main_tag_no = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    ext = models.CharField(max_length=50, blank=True, null=True)
    slno = models.IntegerField()
    slno_no = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'main_tr_attachments'


class MainTrDeveloperAttach(models.Model):
    tag_no = models.IntegerField()
    original_attach_filename = models.CharField(max_length=200)
    rename_attach_filename = models.CharField(max_length=200)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'main_tr_developer_attach'


class MainTrImproveMaster(models.Model):
    slno = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=50)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    delete_date = models.DateField()
    delete_reason = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'main_tr_improve_master'


class MainTrNdHistry(models.Model):
    slno = models.AutoField(primary_key=True)
    main_tr_slno = models.IntegerField()
    resp = models.IntegerField()
    user = models.IntegerField()
    date = models.DateField()
    remarks = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'main_tr_nd_histry'


class MainTrNdUsr(models.Model):
    rqstnr = models.IntegerField()
    dept = models.IntegerField()
    desc = models.TextField(blank=True, null=True)
    rqstd_date = models.DateField()
    rqstd_date_time = models.CharField(max_length=50, blank=True, null=True)
    sts = models.IntegerField()
    module = models.CharField(max_length=20, blank=True, null=True)
    slno = models.AutoField(primary_key=True)
    assgn_tag_no = models.IntegerField()
    rmrks = models.CharField(max_length=1000, blank=True, null=True)
    req_up_sts = models.IntegerField()
    tag_confirm_type = models.IntegerField()
    aprove_type = models.CharField(max_length=2, blank=True, null=True)
    usr_sts = models.IntegerField()
    usr_date = models.CharField(max_length=20, blank=True, null=True)
    approve_sts = models.IntegerField()
    approve_by = models.IntegerField(blank=True, null=True)
    appr_by_hd_dr = models.IntegerField()
    hd_app_sts = models.IntegerField()
    hd_app_date = models.CharField(max_length=20)
    approve_timestamp = models.CharField(max_length=20, blank=True, null=True)
    attach_file_rename = models.CharField(max_length=100, blank=True, null=True)
    attach_file_original = models.CharField(max_length=100, blank=True, null=True)
    update_by = models.IntegerField()
    timestamp = models.DateTimeField()
    highpriority_tag = models.CharField(max_length=10)
    high_prioritytag_sts = models.CharField(max_length=10)
    delete1 = models.IntegerField()
    module_nm = models.TextField(blank=True, null=True)
    reqt_type = models.IntegerField()
    loc = models.CharField(max_length=50, blank=True, null=True)
    other_dept = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_tr_nd_usr'


class MainTrNdUsr0723(models.Model):
    rqstnr = models.IntegerField()
    dept = models.IntegerField()
    desc = models.TextField(blank=True, null=True)
    rqstd_date = models.DateField()
    rqstd_date_time = models.CharField(max_length=50, blank=True, null=True)
    sts = models.IntegerField()
    module = models.CharField(max_length=20, blank=True, null=True)
    slno = models.AutoField(primary_key=True)
    assgn_tag_no = models.IntegerField()
    rmrks = models.CharField(max_length=1000, blank=True, null=True)
    req_up_sts = models.IntegerField()
    tag_confirm_type = models.IntegerField()
    aprove_type = models.CharField(max_length=2, blank=True, null=True)
    usr_sts = models.IntegerField()
    usr_date = models.CharField(max_length=20, blank=True, null=True)
    approve_sts = models.IntegerField()
    approve_by = models.IntegerField(blank=True, null=True)
    appr_by_hd_dr = models.IntegerField()
    hd_app_sts = models.IntegerField()
    hd_app_date = models.CharField(max_length=20)
    approve_timestamp = models.CharField(max_length=20, blank=True, null=True)
    attach_file_rename = models.CharField(max_length=100, blank=True, null=True)
    attach_file_original = models.CharField(max_length=100, blank=True, null=True)
    update_by = models.IntegerField()
    timestamp = models.DateTimeField()
    highpriority_tag = models.CharField(max_length=10)
    high_prioritytag_sts = models.CharField(max_length=10)
    delete1 = models.IntegerField()
    module_nm = models.TextField(blank=True, null=True)
    reqt_type = models.IntegerField()
    loc = models.CharField(max_length=50, blank=True, null=True)
    other_dept = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_tr_nd_usr_07_23'


class MainTrNdUsr0909(models.Model):
    rqstnr = models.IntegerField()
    dept = models.IntegerField()
    desc = models.TextField(blank=True, null=True)
    rqstd_date = models.DateField()
    rqstd_date_time = models.CharField(max_length=50, blank=True, null=True)
    sts = models.IntegerField()
    module = models.CharField(max_length=20, blank=True, null=True)
    slno = models.AutoField(primary_key=True)
    assgn_tag_no = models.IntegerField()
    rmrks = models.CharField(max_length=1000, blank=True, null=True)
    req_up_sts = models.IntegerField()
    tag_confirm_type = models.IntegerField()
    aprove_type = models.CharField(max_length=2, blank=True, null=True)
    usr_sts = models.IntegerField()
    usr_date = models.CharField(max_length=20, blank=True, null=True)
    approve_sts = models.IntegerField()
    approve_by = models.IntegerField(blank=True, null=True)
    appr_by_hd_dr = models.IntegerField()
    hd_app_sts = models.IntegerField()
    hd_app_date = models.CharField(max_length=20)
    approve_timestamp = models.CharField(max_length=20, blank=True, null=True)
    attach_file_rename = models.CharField(max_length=100, blank=True, null=True)
    attach_file_original = models.CharField(max_length=100, blank=True, null=True)
    update_by = models.IntegerField()
    timestamp = models.DateTimeField()
    highpriority_tag = models.CharField(max_length=10)
    high_prioritytag_sts = models.CharField(max_length=10)
    delete1 = models.IntegerField()
    module_nm = models.TextField(blank=True, null=True)
    reqt_type = models.IntegerField()
    loc = models.CharField(max_length=50, blank=True, null=True)
    other_dept = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_tr_nd_usr_09_09'


class MainTrNdUsrOld(models.Model):
    rqstnr = models.IntegerField()
    dept = models.IntegerField()
    desc = models.TextField(blank=True, null=True)
    rqstd_date = models.DateField()
    rqstd_date_time = models.CharField(max_length=50, blank=True, null=True)
    sts = models.IntegerField()
    module = models.CharField(max_length=20, blank=True, null=True)
    slno = models.AutoField(primary_key=True)
    assgn_tag_no = models.IntegerField()
    rmrks = models.CharField(max_length=1000, blank=True, null=True)
    req_up_sts = models.IntegerField()
    tag_confirm_type = models.IntegerField()
    aprove_type = models.CharField(max_length=2, blank=True, null=True)
    usr_sts = models.IntegerField()
    usr_date = models.CharField(max_length=20, blank=True, null=True)
    approve_sts = models.IntegerField()
    approve_by = models.IntegerField(blank=True, null=True)
    appr_by_hd_dr = models.IntegerField()
    hd_app_sts = models.IntegerField()
    hd_app_date = models.CharField(max_length=20)
    approve_timestamp = models.CharField(max_length=20, blank=True, null=True)
    attach_file_rename = models.CharField(max_length=100, blank=True, null=True)
    attach_file_original = models.CharField(max_length=100, blank=True, null=True)
    update_by = models.IntegerField()
    timestamp = models.DateTimeField()
    highpriority_tag = models.CharField(max_length=10)
    high_prioritytag_sts = models.CharField(max_length=10)
    delete1 = models.IntegerField()
    module_nm = models.TextField(blank=True, null=True)
    reqt_type = models.IntegerField()
    loc = models.CharField(max_length=50, blank=True, null=True)
    other_dept = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_tr_nd_usr_old'


class MainTrOld(models.Model):
    tag_no = models.AutoField(primary_key=True)
    tag_desc = models.TextField(blank=True, null=True)
    req = models.CharField(max_length=100, blank=True, null=True)
    dept = models.IntegerField()
    rq_forum = models.CharField(max_length=20, blank=True, null=True)
    rq_desc = models.CharField(max_length=100, blank=True, null=True)
    priority = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    issue_cat = models.CharField(max_length=100, blank=True, null=True)
    issue_sub_cat = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    tag_ass = models.CharField(max_length=100, blank=True, null=True)
    support = models.CharField(max_length=100, blank=True, null=True)
    pr_start_date = models.DateField()
    pr_cmpltd_date = models.DateField()
    actual_date = models.DateField()
    act_cmpltd_date = models.DateField()
    confirm = models.CharField(max_length=5)
    createdby = models.IntegerField()
    tag_re_ass = models.CharField(max_length=20, blank=True, null=True)
    mod = models.CharField(max_length=20, blank=True, null=True)
    ccat_name = models.CharField(max_length=50, blank=True, null=True)
    tcode = models.CharField(max_length=100, blank=True, null=True)
    prgrm = models.CharField(max_length=500, blank=True, null=True)
    acptby = models.CharField(max_length=50, blank=True, null=True)
    ac_rmrks = models.CharField(max_length=250, blank=True, null=True)
    req_type = models.IntegerField()
    spnd_time = models.TimeField()
    rating = models.IntegerField()
    poor_avg = models.CharField(max_length=500, blank=True, null=True)
    final_closed = models.IntegerField()
    final_closed_by = models.IntegerField()
    final_closed_date = models.DateField()
    rating_aplicability = models.CharField(max_length=2, blank=True, null=True)
    kaizen_user = models.IntegerField()
    last_update_date = models.DateField()
    timestamp = models.DateTimeField()
    supporters = models.CharField(max_length=100, blank=True, null=True)
    prop_compltn_days = models.IntegerField()
    act_compltn_days = models.IntegerField()
    delayed_flag = models.IntegerField()
    new_req_revisionno = models.IntegerField()
    highpriority = models.CharField(max_length=20, blank=True, null=True)
    good_reason = models.CharField(max_length=2000, blank=True, null=True)
    tag_no_inti = models.CharField(max_length=150, blank=True, null=True)
    closed_app_sts = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField()
    reqt_type = models.IntegerField()
    module_nm = models.CharField(max_length=350, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_tr_old'


class MainTrRatingNtry(models.Model):
    tag_no = models.IntegerField()
    feedback_desc = models.IntegerField()
    rating = models.IntegerField()
    remarks = models.CharField(max_length=250)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    delete_date = models.DateField()
    delete_reason = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'main_tr_rating_ntry'


class MainTrReqDisp(models.Model):
    empcode = models.CharField(max_length=6, blank=True, null=True)
    module = models.IntegerField()
    delete1 = models.IntegerField()
    createdby = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_tr_req_disp'


class MainTrSuppAssign(models.Model):
    sup_slno = models.AutoField(primary_key=True)
    tag_no = models.IntegerField()
    assign_index = models.IntegerField()
    empcode = models.CharField(max_length=7, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'main_tr_supp_assign'


class MainTrTimeCalcu(models.Model):
    tag_no = models.IntegerField()
    status = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    on_off = models.IntegerField()
    brk = models.IntegerField()
    brk_date = models.DateField()
    brk_time = models.TimeField()
    updt_date = models.DateField()
    updt_time = models.TimeField()
    tot_time = models.TimeField()
    createdby = models.IntegerField()
    max_no = models.AutoField(primary_key=True)
    cmplt_date = models.DateField()
    cmplt_time = models.TimeField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'main_tr_time_calcu'


class MaintIndexValues(models.Model):
    maint_entry = models.IntegerField()
    plant = models.IntegerField(blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'maint_index_values'


class MaintenanceCategoryMaster(models.Model):
    cat_no = models.AutoField(primary_key=True)
    location = models.CharField(max_length=8)
    cat_name = models.CharField(max_length=100)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'maintenance_category_master'


class MaintenanceCotegoryMaster(models.Model):
    cat_no = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=50, blank=True, null=True)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'maintenance_cotegory_master'


class MaintenanceEntry(models.Model):
    main_id = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    maintenance_serial_no = models.IntegerField()
    ntry_date = models.DateField()
    ntry_time = models.TimeField()
    desc = models.TextField(blank=True, null=True)
    repeat_mainid = models.IntegerField()
    status = models.IntegerField()
    category = models.IntegerField()
    sub_cat_no = models.IntegerField()
    ss_cat_no = models.IntegerField()
    req_type = models.IntegerField()
    hod_code = models.IntegerField()
    hod_appr = models.IntegerField()
    hod_date = models.DateTimeField()
    assign_code = models.CharField(max_length=100, blank=True, null=True)
    sup_asgn_code = models.CharField(max_length=150, blank=True, null=True)
    completed_date = models.DateField()
    completed_time = models.TimeField()
    total_time = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=5, blank=True, null=True)
    rating = models.IntegerField()
    cost = models.IntegerField()
    attachment = models.CharField(max_length=50, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'maintenance_entry'


class MaintenanceEntry211123(models.Model):
    main_id = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    maintenance_serial_no = models.IntegerField()
    ntry_date = models.DateField()
    ntry_time = models.TimeField()
    desc = models.TextField(blank=True, null=True)
    repeat_mainid = models.IntegerField()
    status = models.IntegerField()
    category = models.IntegerField()
    sub_cat_no = models.IntegerField()
    ss_cat_no = models.IntegerField()
    req_type = models.IntegerField()
    hod_code = models.IntegerField()
    hod_appr = models.IntegerField()
    hod_date = models.DateTimeField()
    assign_code = models.CharField(max_length=100, blank=True, null=True)
    sup_asgn_code = models.CharField(max_length=150, blank=True, null=True)
    completed_date = models.DateField()
    completed_time = models.TimeField()
    total_time = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=5, blank=True, null=True)
    rating = models.IntegerField()
    cost = models.IntegerField()
    attachment = models.CharField(max_length=50, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'maintenance_entry_21_11_23'


class MaintenanceHistory(models.Model):
    seq_slno = models.AutoField(primary_key=True)
    main_id = models.IntegerField()
    status = models.IntegerField()
    comments = models.CharField(max_length=200)
    ntry_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'maintenance_history'


class MaintenanceNtry(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    req = models.IntegerField()
    date = models.DateField()
    req_time = models.TimeField()
    desc = models.CharField(max_length=5000, blank=True, null=True)
    usr_return_comments = models.CharField(max_length=250, blank=True, null=True)
    dept = models.IntegerField()
    category = models.IntegerField()
    sub_cat_no = models.IntegerField()
    type = models.IntegerField()
    approval = models.IntegerField()
    hod_aprl_sent_date = models.DateField()
    hod_aprl_sent_time = models.TimeField()
    hod = models.IntegerField()
    hod_date = models.DateField()
    hod_time = models.TimeField()
    hod_remarks = models.CharField(max_length=150, blank=True, null=True)
    hod_sts = models.IntegerField()
    ass = models.IntegerField()
    suppport = models.CharField(max_length=100, blank=True, null=True)
    re_ass = models.IntegerField()
    sts_slno = models.IntegerField()
    adopt_type = models.CharField(max_length=1, blank=True, null=True)
    adopt_remarks = models.CharField(max_length=200, blank=True, null=True)
    adopt_date = models.DateField()
    adopt_time = models.TimeField()
    completed_date = models.DateField()
    completed_time = models.TimeField()
    area = models.CharField(max_length=5, blank=True, null=True)
    loc = models.CharField(max_length=5, blank=True, null=True)
    ss_cat_no = models.IntegerField()
    hours = models.IntegerField()
    cost = models.FloatField()
    time_applicability = models.CharField(max_length=2, blank=True, null=True)
    rating_applicability = models.CharField(max_length=2, blank=True, null=True)
    rating = models.IntegerField()
    ucp_hold_hours = models.TimeField()
    remarks = models.TextField(blank=True, null=True)
    exceed = models.CharField(max_length=50, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'maintenance_ntry'





class MaintenanceRatingNtry(models.Model):
    uniq_slno = models.IntegerField()
    feedback_desc = models.IntegerField()
    rating = models.IntegerField()
    remarks = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    delete_date = models.DateField()
    delete_reason = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maintenance_rating_ntry'


class MaintenanceSsCategoryMaster(models.Model):
    ssub_id = models.AutoField(primary_key=True)
    cat_no = models.IntegerField(blank=True, null=True)
    sub_cat_no = models.IntegerField(blank=True, null=True)
    ss_cat_no = models.IntegerField(blank=True, null=True)
    ss_cat_name = models.CharField(max_length=164, blank=True, null=True)
    min = models.IntegerField(blank=True, null=True)
    delete1 = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    timestamp = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maintenance_ss_category_master'


class MaintenanceSsCategoryMasterOld(models.Model):
    ssub_id = models.AutoField(primary_key=True)
    cat_no = models.IntegerField()
    sub_cat_no = models.IntegerField()
    ss_cat_no = models.IntegerField()
    ss_cat_name = models.CharField(max_length=250)
    min = models.IntegerField()
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'maintenance_ss_category_master_OLD'


class MaintenanceSsCotegoryMaster(models.Model):
    cat_no = models.IntegerField()
    sub_cat_no = models.IntegerField()
    ss_cat_no = models.IntegerField()
    ss_cat_name = models.CharField(max_length=150, blank=True, null=True)
    hours = models.IntegerField()
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'maintenance_ss_cotegory_master'


class MaintenanceStatusMasterNew(models.Model):
    sts_slno = models.AutoField(primary_key=True)
    show_no = models.IntegerField()
    sts_desc = models.CharField(max_length=50)
    mail_des = models.CharField(max_length=30, blank=True, null=True)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'maintenance_status_master_new'


class MaintenanceStsNtry(models.Model):
    uniq_slno = models.IntegerField()
    comments = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateField()
    sts = models.IntegerField()
    re_ass = models.IntegerField()
    ntry_by = models.IntegerField()
    seq_slno = models.AutoField(primary_key=True)
    ucp_hold_up_sts = models.IntegerField()
    timestampp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'maintenance_sts_ntry'


class MaintenanceSubCategoryMaster(models.Model):
    sub_id = models.AutoField(primary_key=True)
    cat_no = models.IntegerField(blank=True, null=True)
    sub_cat_no = models.IntegerField(blank=True, null=True)
    sub_cat_name = models.CharField(max_length=64, blank=True, null=True)
    delete1 = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    timestamp = models.CharField(max_length=19, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maintenance_sub_category_master'


class MaintenanceSubCategoryMasterOld(models.Model):
    sub_id = models.AutoField(primary_key=True)
    cat_no = models.IntegerField()
    sub_cat_no = models.IntegerField()
    sub_cat_name = models.CharField(max_length=150, blank=True, null=True)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'maintenance_sub_category_master_OLD'


class MaintenanceSubCotegoryMaster(models.Model):
    cat_no = models.IntegerField()
    sub_cat_no = models.IntegerField()
    sub_cat_name = models.CharField(max_length=50, blank=True, null=True)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'maintenance_sub_cotegory_master'


class MaintenanceTimecal(models.Model):
    slno = models.AutoField(primary_key=True)
    main_id = models.IntegerField()
    empcode = models.CharField(max_length=6, blank=True, null=True)
    date = models.DateField()
    time = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'maintenance_timecal'


class MaintenanceTypeMaster(models.Model):
    type_slno = models.AutoField(primary_key=True)
    type_desc = models.CharField(max_length=50, blank=True, null=True)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'maintenance_type_master'


class MaintenenceSubCat(models.Model):
    sub_cat_id = models.AutoField(primary_key=True)
    cat_id = models.IntegerField()
    sub_cat_desc = models.CharField(max_length=200, blank=True, null=True)
    created_by = models.IntegerField(db_column='created by')  # Field renamed to remove unsuitable characters.
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'maintenence_sub_cat'


class MaintenenceSubCategory(models.Model):
    sub_cat_id = models.AutoField(primary_key=True)
    cat_id = models.IntegerField(blank=True, null=True)
    sub_cat_desc = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.IntegerField(db_column='created by', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    delete1 = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'maintenence_sub_category'


class MarketHistory(models.Model):
    sno = models.IntegerField()
    uniq_slno = models.IntegerField()
    status = models.IntegerField()
    description = models.TextField()
    createdby = models.CharField(max_length=7)
    ntry_date = models.DateField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    deleteddate = models.DateField()

    class Meta:
        managed = False
        db_table = 'market_history'


class MarketNtry(models.Model):
    slno = models.IntegerField()
    createdby = models.CharField(max_length=7)
    ntry_date = models.DateField()
    stn_name = models.CharField(max_length=50)
    division = models.CharField(max_length=50)
    zone = models.CharField(max_length=10)
    contractor = models.CharField(max_length=7)
    ordering_auth = models.CharField(max_length=7)
    consignee = models.CharField(max_length=50)
    primary_assoc = models.CharField(max_length=7)
    primary_contact = models.CharField(max_length=11)
    design_assoc = models.CharField(max_length=7)
    design_contact = models.CharField(max_length=11)
    fieldwork_assoc = models.CharField(max_length=7)
    fieldwork_contact = models.CharField(max_length=11)
    fn_involed = models.CharField(max_length=100)
    prime_resposible = models.CharField(max_length=7)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.IntegerField()
    timestamp = models.DateTimeField()
    actual_startdate = models.DateField()
    actual_enddate = models.DateField()

    class Meta:
        managed = False
        db_table = 'market_ntry'


class MarketProjExec(models.Model):
    id = models.CharField(max_length=20)
    sequence_no = models.AutoField(primary_key=True)
    majoractivity = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    responsibility = models.CharField(max_length=50)
    support = models.CharField(max_length=50)
    dependent = models.CharField(max_length=30)
    leadtime = models.IntegerField()
    status = models.CharField(max_length=10)
    createdby = models.CharField(max_length=7)
    delete1 = models.IntegerField()
    deletedby = models.CharField(max_length=7)
    deleteddate = models.DateField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'market_proj_exec'


class MarketScheduling(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    slno = models.IntegerField()
    id = models.CharField(max_length=11)
    sequence_no = models.IntegerField()
    leadtime = models.IntegerField(blank=True, null=True)
    activity_startdate = models.DateField()
    activity_enddate = models.DateField()
    actualstartdate = models.DateField()
    actualenddate = models.DateField()
    status = models.IntegerField()
    createdby = models.CharField(max_length=7)
    ntry_date = models.DateField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'market_scheduling'


class MarketingDept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dept = models.CharField(max_length=10)
    empcodes = models.CharField(max_length=100)
    createdby = models.CharField(max_length=7)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    deletedby = models.CharField(max_length=7)
    deleteddate = models.DateField()

    class Meta:
        managed = False
        db_table = 'marketing_dept'


class MarketingDivisions(models.Model):
    did = models.IntegerField()
    zone = models.IntegerField()
    divisions = models.CharField(max_length=150)
    createdby = models.CharField(max_length=7)
    delete1 = models.IntegerField()
    deletedby = models.CharField(max_length=7)
    deleteddate = models.DateField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'marketing_divisions'



class MarketingStatusMaster(models.Model):
    sid = models.IntegerField()
    status = models.CharField(max_length=50)
    createdby = models.CharField(max_length=7)
    delete1 = models.IntegerField()
    deleteby = models.CharField(max_length=7)
    deleteddate = models.DateField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'marketing_status_master'


class MarketingZones(models.Model):
    zid = models.AutoField(primary_key=True)
    zone = models.CharField(max_length=100)
    createdby = models.CharField(max_length=7)
    delete1 = models.IntegerField()
    deletedby = models.CharField(max_length=7)
    deleteddate = models.DateField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'marketing_zones'


class MaterialMaster(models.Model):
    mat_code = models.CharField(max_length=20, blank=True, null=True)
    mat_desc = models.TextField(blank=True, null=True)
    uom = models.CharField(max_length=50, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'material_master'


class MbomCategory(models.Model):
    category = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=150, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    type = models.IntegerField()
    userid = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mbom_category'


class MbomEntry(models.Model):
    mbom_id = models.AutoField(primary_key=True)
    mbom_project = models.IntegerField()
    partdesc = models.CharField(max_length=500)
    mbom_project_e = models.CharField(max_length=7)
    mbom_project_m = models.CharField(max_length=7)
    mbom_code = models.CharField(max_length=200, blank=True, null=True)
    spec_code = models.CharField(max_length=200, blank=True, null=True)
    mbomdesc = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.IntegerField()
    mbom_date = models.DateField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mbom_entry'


class MbomIndexCodes(models.Model):
    dwg_mcode_id = models.AutoField(primary_key=True)
    dwg_tot_id = models.IntegerField()
    dwg_mcode = models.CharField(max_length=11)
    dwg_category = models.CharField(max_length=3)
    qty = models.IntegerField()
    mqty = models.IntegerField()
    dwg_mcode_ref = models.CharField(max_length=11)
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mbom_index_codes'


class MdchtMsgs(models.Model):
    ordr = models.AutoField(primary_key=True)
    sndr = models.CharField(max_length=15)
    rcvr = models.CharField(max_length=15)
    msg = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'mdcht_msgs'


class MdlDataContent(models.Model):
    id = models.BigAutoField(primary_key=True)
    fieldid = models.PositiveBigIntegerField()
    recordid = models.PositiveBigIntegerField()
    content = models.TextField(blank=True, null=True)
    content1 = models.TextField(blank=True, null=True)
    content2 = models.TextField(blank=True, null=True)
    content3 = models.TextField(blank=True, null=True)
    content4 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_data_content'


class MdlDataRecords(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.PositiveBigIntegerField()
    groupid = models.PositiveBigIntegerField()
    dataid = models.PositiveBigIntegerField()
    timecreated = models.PositiveBigIntegerField()
    timemodified = models.PositiveBigIntegerField()
    approved = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_data_records'

class MeAutoIndividualCardMaster(models.Model):
    indvdl_no = models.AutoField(primary_key=True)
    indvdl_name = models.CharField(max_length=5000)
    dept = models.CharField(max_length=5000)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'me_auto_individual_card_master'


class MeAutoTitleMaster(models.Model):
    title_no = models.AutoField(primary_key=True)
    title_name = models.CharField(max_length=5000)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'me_auto_title_master'


class MeAutoUserMaster(models.Model):
    empcode = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=50)
    dept = models.CharField(max_length=30)
    design = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'me_auto_user_master'


class MeAutoUserPrivileges(models.Model):
    empcode = models.IntegerField()
    form_name = models.CharField(max_length=50)
    save = models.IntegerField()
    veiw = models.IntegerField()
    update1 = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_auto_user_privileges'


class MeAutomationAdditinlHistry(models.Model):
    his_id = models.AutoField(primary_key=True)
    subid = models.IntegerField()
    empcode = models.IntegerField()
    comments = models.TextField()
    date = models.DateField()
    user_file = models.CharField(max_length=150)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_automation_additinl_histry'


class MeAutomationAttchment(models.Model):
    att_id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    subid = models.IntegerField()
    other_attachment = models.CharField(max_length=340)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_automation_attchment'


class MeAutomationAutoTtl(models.Model):
    title_no = models.AutoField(primary_key=True)
    title_name = models.CharField(max_length=5000)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'me_automation_auto_ttl'


class MeAutomationCallreview(models.Model):
    call_id = models.AutoField(primary_key=True)
    subid = models.IntegerField()
    mailsubj = models.CharField(max_length=100)
    mailtext = models.CharField(max_length=500)
    mail_to = models.CharField(max_length=100)
    mail_cc = models.CharField(max_length=100)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_automation_callreview'


class MeAutomationChcklstdoc(models.Model):
    subid = models.IntegerField()
    upload_type = models.IntegerField()
    attachment = models.CharField(max_length=200)
    prev_revision = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_automation_chcklstdoc'


class MeAutomationDbNum(models.Model):
    subid = models.IntegerField()
    dbcardlvl = models.IntegerField()
    dbcardname = models.CharField(max_length=150)
    auto_no = models.CharField(max_length=100)
    auto_ttlmastr = models.CharField(max_length=150)
    indv_no = models.CharField(max_length=100)
    indv_ttlmastr = models.CharField(max_length=150)
    created_by = models.IntegerField()
    timesatmp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_automation_db_num'


class MeAutomationEntry(models.Model):
    main_request = models.IntegerField()
    sub_request = models.IntegerField()
    empcode = models.IntegerField()
    entrydate = models.DateField()
    project = models.IntegerField()
    jigdate = models.DateField()
    file_attach = models.CharField(max_length=100)
    req_desc = models.TextField(blank=True, null=True)
    jig_priority = models.IntegerField()
    costng_attach = models.CharField(max_length=100)
    service_cat = models.IntegerField()
    sub_cat = models.IntegerField()
    test_jigno = models.IntegerField()
    test_jigtitle = models.CharField(max_length=100)
    new_instrmnt = models.IntegerField()
    instr_hod = models.IntegerField()
    instr_hod_sts = models.IntegerField()
    instr_uip_date = models.DateField()
    instr_hod_date = models.DateField()
    instr_hod_cmmnts = models.TextField(blank=True, null=True)
    instr_mehod = models.IntegerField()
    instr_mehod_date = models.DateField()
    instr_mehod_cmmnts = models.TextField(blank=True, null=True)
    assignedtome = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    target_date = models.DateField()
    future_date_updatd = models.DateField()
    compl_instr_attach = models.CharField(max_length=50)
    dtsr_emp = models.IntegerField()
    dtsr_sts = models.IntegerField()
    newjg_subtype = models.IntegerField()
    inst_subcat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_automation_entry'


class MeAutomationFinalhis(models.Model):
    subid = models.IntegerField()
    end_sts = models.IntegerField()
    fnl_attch = models.CharField(max_length=150)
    comments = models.CharField(max_length=3000, blank=True, null=True)
    test_jig_effc_date = models.DateField()
    date = models.DateField()
    replied = models.IntegerField()
    createdby = models.IntegerField()
    fnlusr_attch = models.CharField(max_length=200)
    delay_reason = models.CharField(max_length=500, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_automation_finalhis'


class MeAutomationIndvCard(models.Model):
    indvdl_no = models.AutoField(primary_key=True)
    indvdl_name = models.CharField(max_length=5000)
    dept = models.CharField(max_length=5000)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'me_automation_indv_card'


class MeAutomationInstrtargtParams(models.Model):
    param_id = models.AutoField(primary_key=True)
    param = models.CharField(max_length=250)
    days = models.IntegerField()
    type = models.IntegerField()
    createdby = models.DateTimeField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_automation_instrtargt_params'


class MeAutomationInstrtargtStore(models.Model):
    sid = models.AutoField(primary_key=True)
    param_id = models.IntegerField()
    id = models.IntegerField()
    type = models.IntegerField()
    value = models.IntegerField()
    remarks = models.TextField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_automation_instrtargt_store'


class MeAutomationInstrumentHistry(models.Model):
    his_id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    comments = models.TextField()
    status = models.IntegerField()
    rootcause = models.CharField(max_length=400, blank=True, null=True)
    impact = models.CharField(max_length=50, blank=True, null=True)
    ecr_no = models.CharField(max_length=20, blank=True, null=True)
    delay_reason = models.CharField(max_length=500, blank=True, null=True)
    inputattch = models.CharField(max_length=100, blank=True, null=True)
    compl_instr_attach = models.CharField(max_length=50, blank=True, null=True)
    empna = models.IntegerField()
    reply = models.IntegerField()
    createdby = models.IntegerField()
    date = models.DateField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_automation_instrument_histry'


class MeAutomationRqststs(models.Model):
    subid = models.IntegerField()
    req_type = models.IntegerField()
    rqst_sts = models.IntegerField()
    test_jig_ttl = models.CharField(max_length=100)
    priority_reqst = models.IntegerField()
    reqrddate = models.DateField()
    reqst_attch = models.CharField(max_length=150)
    reqstremarks = models.CharField(max_length=400)
    resposibily_rqst = models.CharField(max_length=200)
    date = models.DateField()
    replied = models.IntegerField()
    createdby = models.IntegerField()
    initialusr_attch = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_automation_rqststs'


class MeAutomationRwmom(models.Model):
    subid = models.IntegerField()
    actn_observ = models.CharField(max_length=200)
    resposibily_rw = models.IntegerField()
    priority_rw = models.IntegerField()
    dateofcomple = models.DateField()
    point_sts = models.IntegerField()
    closed_date = models.DateField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_automation_rwmom'


class MeAutomationStatusMaster(models.Model):
    status = models.CharField(max_length=60)
    instr_hod_sts = models.CharField(max_length=50)
    any_remarks = models.CharField(max_length=200)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_automation_status_master'


class MeAutomationSubentry(models.Model):
    subid = models.AutoField(primary_key=True)
    id = models.IntegerField()
    mat_code = models.CharField(max_length=50)
    qtyperm = models.IntegerField()
    tipermin = models.IntegerField()
    tipermonth = models.IntegerField()
    attch = models.CharField(max_length=100)
    jg_priority = models.IntegerField()
    target_date = models.DateField()
    hod_sts = models.IntegerField()
    hod_date = models.DateField()
    hod = models.IntegerField()
    hod_comm = models.TextField(blank=True, null=True)
    mehod = models.IntegerField()
    mehod_date = models.DateField()
    mehod_comm = models.TextField(blank=True, null=True)
    additional_ipts_commnts = models.TextField(blank=True, null=True)
    assignedto = models.IntegerField()
    generated_req_no = models.CharField(max_length=100)
    rej_file = models.CharField(max_length=100)
    assignedtoplnng = models.IntegerField()
    plann_from = models.DateField()
    plann_to = models.DateField()
    plann_qty = models.IntegerField()
    plann_attch = models.CharField(max_length=100)
    plann_date = models.DateField()
    plann_reply = models.IntegerField()
    mailsubj = models.CharField(max_length=200)
    mailtext = models.TextField(blank=True, null=True)
    mail_to = models.CharField(max_length=200)
    mail_cc = models.CharField(max_length=150)
    call_revw_sts = models.IntegerField()
    members_present = models.CharField(max_length=200)
    req_type = models.IntegerField()
    rqst_sts = models.IntegerField()
    resposibily_rqst = models.CharField(max_length=400)
    endmail_to = models.CharField(max_length=200)
    endmail_cc = models.CharField(max_length=200)
    endusersubj = models.CharField(max_length=300)
    endusertext = models.TextField(blank=True, null=True)
    end_sts = models.IntegerField()
    test_jig_effc_date = models.DateField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    new_req_type = models.IntegerField()
    verification = models.IntegerField()
    approval = models.IntegerField()
    type = models.IntegerField()
    new_or_existngjig = models.IntegerField()
    existng_jigid = models.IntegerField()
    exesup_txt = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'me_automation_subentry'


class MeAutomationTargtParams(models.Model):
    param_id = models.AutoField(primary_key=True)
    param = models.CharField(max_length=50)
    signle_dut = models.IntegerField()
    multiple_dut = models.IntegerField()
    software_dut = models.IntegerField()
    software_mdut = models.IntegerField()
    manual_jig = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_automation_targt_params'


class MeAutomationTargtStore(models.Model):
    param_id = models.IntegerField()
    subid = models.IntegerField()
    type = models.IntegerField()
    value = models.IntegerField()
    remarks = models.TextField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_automation_targt_store'


class MeAutomationTestjig(models.Model):
    test_setup = models.CharField(max_length=100)
    increment = models.IntegerField()
    title = models.CharField(max_length=300)
    instrument_type = models.IntegerField()
    level = models.CharField(max_length=50)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_automation_testjig'


class MeAutomationTestjigNumbr(models.Model):
    subid = models.IntegerField()
    testjg_type = models.IntegerField()
    unit_cardlvl = models.IntegerField()
    test_set_type = models.IntegerField()
    unit_cardname = models.CharField(max_length=100)
    path = models.CharField(max_length=200)
    svn_path = models.CharField(max_length=500, blank=True, null=True)
    test_setup_id = models.IntegerField()
    test_setupno = models.TextField(blank=True, null=True)
    test_setupttl = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.IntegerField()
    timesatmp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_automation_testjig_numbr'


class MeAutomationTestjigdoc(models.Model):
    subid = models.IntegerField()
    upload_type = models.IntegerField()
    attachment = models.CharField(max_length=200)
    prev_revision = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'me_automation_testjigdoc'


class MeetingProjList(models.Model):
    meeting_name = models.IntegerField()
    project = models.IntegerField()
    priority = models.IntegerField()
    empcode = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'meeting_proj_list'


class MeetingProjMaster(models.Model):
    meetingname = models.CharField(max_length=150)
    empcode = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'meeting_proj_master'


class MenusList(models.Model):
    mid = models.AutoField(primary_key=True)
    menu = models.CharField(max_length=50)
    shtcut = models.CharField(max_length=10)
    url = models.CharField(max_length=500)
    sm = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'menus_list'


class MetrackerHistory(models.Model):
    hid = models.AutoField(primary_key=True)
    rid = models.IntegerField()
    response = models.CharField(max_length=6)
    comments = models.CharField(max_length=500, blank=True, null=True)
    action = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'metracker_history'


class MetrackerMainType(models.Model):
    main_id = models.AutoField(primary_key=True)
    main_request = models.CharField(max_length=30)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'metracker_main_type'


class MetrackerMatNtry(models.Model):
    mid = models.AutoField(primary_key=True)
    rid = models.IntegerField()
    materialcode = models.CharField(max_length=20)
    qtyperm = models.IntegerField()
    tipermin = models.IntegerField()
    tipermonth = models.IntegerField()
    delete1 = models.IntegerField()
    revno = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metracker_mat_ntry'


class MetrackerNtry(models.Model):
    rid = models.AutoField(primary_key=True)
    main_request = models.IntegerField()
    sub_request = models.IntegerField()
    project = models.IntegerField()
    req_date = models.DateField()
    mail_cc = models.CharField(max_length=100)
    me_user = models.IntegerField()
    file_attach = models.CharField(max_length=100)
    descript = models.CharField(max_length=2000)
    service_cat = models.CharField(max_length=50)
    sub_cat = models.CharField(max_length=50)
    date = models.DateField()
    empcode = models.CharField(max_length=6)
    delete1 = models.IntegerField()
    hod_sts = models.IntegerField()
    hod = models.IntegerField()
    hod_comm = models.CharField(max_length=100)
    hod_date = models.DateField()
    me_assign = models.CharField(max_length=6)
    me_track_sts = models.IntegerField()
    me_assign_date = models.DateField()
    support = models.IntegerField()
    me_hod_comm = models.CharField(max_length=200)
    me_assign_comm = models.CharField(max_length=300)
    hodate = models.DateField()
    mailto = models.CharField(max_length=7)
    completed_date = models.DateField()
    ecrno_reason = models.CharField(max_length=50)
    feedback = models.CharField(max_length=100)
    benefits = models.CharField(max_length=500, blank=True, null=True)
    quantity = models.CharField(max_length=10, blank=True, null=True)
    pquantity = models.CharField(max_length=10, blank=True, null=True)
    activity = models.CharField(max_length=300, blank=True, null=True)
    b_improv = models.CharField(max_length=300, blank=True, null=True)
    aftr_improv = models.CharField(max_length=300, blank=True, null=True)
    result = models.CharField(max_length=300, blank=True, null=True)
    safety = models.CharField(max_length=20, blank=True, null=True)
    money = models.FloatField()
    detail_feedback = models.IntegerField()
    designer_verific = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metracker_ntry'


class MetrackerServiceCatgry(models.Model):
    cat_id = models.AutoField(primary_key=True)
    service_cat = models.CharField(max_length=1000)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'metracker_service_catgry'


class MetrackerServiceSubcatgry(models.Model):
    sub_cat = models.CharField(max_length=100)
    cat_id = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'metracker_service_subcatgry'


class MetrackerSubType(models.Model):
    sub_id = models.AutoField(primary_key=True)
    main_id = models.IntegerField()
    sub_request = models.CharField(max_length=100)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'metracker_sub_type'


class MmchangeAddrootcause(models.Model):
    slno = models.AutoField(primary_key=True)
    rootcause = models.CharField(max_length=100, blank=True, null=True)
    type = models.IntegerField()
    empcode = models.CharField(max_length=6, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mmchange_addrootcause'


class ModuleMaster(models.Model):
    mod_code = models.IntegerField()
    mod_desc = models.CharField(max_length=100)
    team_mail_id = models.CharField(max_length=500)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'module_master'


class MosModules(models.Model):
    index_no = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=100)
    createby = models.IntegerField()
    module_value = models.IntegerField()
    primary = models.CharField(max_length=20, blank=True, null=True)
    secondary = models.CharField(max_length=10, blank=True, null=True)
    show_sts = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mos_modules'


class MozillaVerions(models.Model):
    ip = models.CharField(max_length=50)
    sys_name = models.CharField(max_length=50)
    version = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'mozilla_verions'


class MrDataMainSubAssMstr(models.Model):
    matnr = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=1)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mr_data_main_sub_ass_mstr'


class MrDataMaster(models.Model):
    date = models.DateField()
    matnr = models.CharField(max_length=20)
    tot_qty = models.IntegerField()
    rej = models.IntegerField()
    rew = models.IntegerField()
    on_off = models.IntegerField()
    type = models.CharField(max_length=1)
    createdby = models.IntegerField()
    timstamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mr_data_master'


class MrDataSubMaster(models.Model):
    date = models.DateField()
    matnr = models.CharField(max_length=20)
    eqpmnt = models.IntegerField()
    type = models.IntegerField()
    on_off = models.IntegerField()
    createdby = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mr_data_sub_master'


class MrDataSubTemp(models.Model):
    date = models.DateField()
    matnr = models.CharField(max_length=20)
    eqpmnt = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mr_data_sub_temp'


class MrDataTemp(models.Model):
    date = models.DateField()
    matnr = models.CharField(max_length=20)
    tot_qty = models.IntegerField()
    rej = models.IntegerField()
    rew = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mr_data_temp'


class MrsMaster(models.Model):
    mrs_slno = models.IntegerField()
    matnr = models.CharField(max_length=15)
    desc = models.CharField(max_length=100)
    slno = models.IntegerField()
    project = models.CharField(max_length=50)
    no_sets = models.IntegerField()
    qty_set = models.FloatField()
    stock = models.FloatField()
    mrs = models.FloatField()
    bal = models.FloatField()
    temp_bal = models.CharField(max_length=10)
    order_slno = models.IntegerField()
    tot_short = models.CharField(max_length=10)
    tot_value = models.CharField(max_length=1500)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mrs_master'


class MrsSlnoMaster(models.Model):
    mrs_slno = models.AutoField(primary_key=True)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mrs_slno_master'


class MrsTemp(models.Model):
    matnr = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)
    slno = models.IntegerField()
    project = models.CharField(max_length=50)
    no_sets = models.IntegerField()
    qty_set = models.FloatField()
    stock = models.FloatField()
    mrs = models.FloatField()
    temp_bal = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'mrs_temp'


class Mtpl5WhyMaster(models.Model):
    why_id = models.AutoField(primary_key=True)
    nc_tag_slno = models.CharField(max_length=250, blank=True, null=True)
    why = models.CharField(max_length=500, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtpl_5why_master'


class MtplAttachments(models.Model):
    sno = models.AutoField(primary_key=True)
    uniq_slno = models.IntegerField()
    file_name = models.CharField(max_length=50)
    file_type = models.CharField(max_length=50)
    file_path = models.CharField(max_length=50)
    full_path = models.CharField(max_length=50)
    raw_name = models.CharField(max_length=50)
    orig_name = models.CharField(max_length=50)
    client_name = models.CharField(max_length=50)
    file_ext = models.CharField(max_length=50)
    file_size = models.CharField(max_length=50)
    is_image = models.CharField(max_length=50)
    image_width = models.CharField(max_length=50)
    image_height = models.CharField(max_length=50)
    image_type = models.CharField(max_length=50)
    image_size_str = models.CharField(max_length=50)
    type = models.CharField(max_length=25)
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mtpl_attachments'


class MtplCaAction(models.Model):
    ca_id = models.AutoField(primary_key=True)
    nc_tag_slno = models.CharField(max_length=250, blank=True, null=True)
    corr_action = models.CharField(max_length=500, blank=True, null=True)
    date_initiation = models.DateField()
    caresponce = models.CharField(db_column='CAresponce', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ca_target = models.DateField(db_column='CA_Target')  # Field name made lowercase.
    castatus = models.CharField(db_column='CAstatus', max_length=250, blank=True, null=True)  # Field name made lowercase.
    catype = models.CharField(db_column='CAType', max_length=250, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtpl_ca_action'


class MtplComponent(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    project = models.CharField(max_length=15)
    component = models.CharField(max_length=15)
    componentsr = models.CharField(db_column='componentSr', max_length=15)  # Field name made lowercase.
    rust = models.CharField(max_length=15)
    rotation = models.CharField(max_length=15)
    cleaning = models.CharField(max_length=15)
    tarpaulin = models.CharField(max_length=15)
    nextdate = models.DateField(blank=True, null=True)
    dispatch = models.IntegerField()
    delete1 = models.IntegerField()
    empcode = models.CharField(max_length=50)
    ntrydate = models.DateField()
    due_date_over = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mtpl_component'


class MtplDomainMaster(models.Model):
    domain_id = models.AutoField(primary_key=True)
    domain_name = models.CharField(max_length=50)
    fullname = models.CharField(db_column='Fullname', max_length=250)  # Field name made lowercase.
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'mtpl_domain_master'


class MtplFailureCategory(models.Model):
    fc_no = models.AutoField(primary_key=True)
    fc_name = models.CharField(max_length=50)
    createdby = models.SmallIntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mtpl_failure_category'


class MtplGeneration(models.Model):
    uniq_slno = models.IntegerField(primary_key=True)
    nc_tag_slno = models.CharField(max_length=500, blank=True, null=True)
    sub_uniq_slno = models.IntegerField()
    empcode = models.IntegerField()
    deptcode = models.IntegerField()
    requesteddate = models.DateField()
    date_of_nc = models.DateField()
    nc_details = models.CharField(max_length=500, blank=True, null=True)
    nc_observed_at = models.IntegerField()
    responcesibility = models.CharField(max_length=250, blank=True, null=True)
    target_date = models.DateField()
    tracebility_no = models.CharField(max_length=200, blank=True, null=True)
    prob_desc = models.CharField(max_length=500, blank=True, null=True)
    project = models.CharField(max_length=500, blank=True, null=True)
    nc_title = models.CharField(max_length=250, blank=True, null=True)
    domain_id = models.IntegerField()
    category_id = models.CharField(max_length=30, blank=True, null=True)
    assign = models.CharField(max_length=500, blank=True, null=True)
    lot_qty = models.CharField(max_length=250, blank=True, null=True)
    aff_qty = models.CharField(max_length=250, blank=True, null=True)
    def_qty = models.CharField(max_length=250, blank=True, null=True)
    wt_prob = models.CharField(max_length=500, blank=True, null=True)
    wh_happend = models.CharField(max_length=500, blank=True, null=True)
    who = models.CharField(max_length=250, blank=True, null=True)
    how = models.CharField(max_length=500, blank=True, null=True)
    who_owner = models.CharField(max_length=500, blank=True, null=True)
    detect_with_prasent = models.CharField(max_length=500, blank=True, null=True)
    nc_prob_attach = models.CharField(max_length=250, blank=True, null=True)
    caaction = models.CharField(db_column='CAaction', max_length=500, blank=True, null=True)  # Field name made lowercase.
    respca = models.CharField(db_column='respCA', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ca_date_completion = models.CharField(db_column='CA_date_completion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    proc_root_cause = models.CharField(max_length=500, blank=True, null=True)
    escape_root_cause = models.CharField(max_length=500, blank=True, null=True)
    closed_attach = models.CharField(max_length=250, blank=True, null=True)
    nc_closing_stmt = models.CharField(max_length=2000, blank=True, null=True)
    nc_analysis = models.CharField(max_length=2000, blank=True, null=True)
    end_user = models.IntegerField()
    date_nc_closer = models.DateField()
    status = models.IntegerField()
    hod_code = models.IntegerField()
    hod_status = models.IntegerField()
    hod_remarks = models.CharField(max_length=500, blank=True, null=True)
    hod_approve_date = models.DateTimeField()
    edp_code = models.IntegerField()
    edp_status = models.IntegerField()
    edp_remarks = models.CharField(max_length=500, blank=True, null=True)
    edp_approve_date = models.DateTimeField()
    created_by = models.IntegerField()
    timestamp = models.IntegerField()
    delete1 = models.IntegerField()
    del_date = models.IntegerField()
    del_by = models.IntegerField()
    no_of_days = models.IntegerField()
    cost_non = models.CharField(max_length=500, blank=True, null=True)
    dfmea = models.CharField(max_length=100, blank=True, null=True)
    pfmea = models.CharField(max_length=100, blank=True, null=True)
    prev_nc = models.CharField(max_length=100, blank=True, null=True)
    reopen_reson = models.TextField(blank=True, null=True)
    area = models.CharField(max_length=150, blank=True, null=True)
    company = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mtpl_generation'


class MtplLaAction(models.Model):
    la_id = models.AutoField(primary_key=True)
    nc_tag_slno = models.CharField(max_length=250, blank=True, null=True)
    proj = models.CharField(max_length=250, blank=True, null=True)
    la_details = models.CharField(max_length=250, blank=True, null=True)
    la_respon = models.CharField(max_length=250, blank=True, null=True)
    la_status = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtpl_la_action'


class MtplMachineMaster(models.Model):
    machine_id = models.AutoField(primary_key=True)
    machine_name = models.CharField(max_length=50)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mtpl_machine_master'


class MtplNtry(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    req = models.CharField(max_length=11)
    date = models.DateField()
    req_time = models.TimeField()
    desc = models.CharField(max_length=200, blank=True, null=True)
    loccode = models.CharField(max_length=11, blank=True, null=True)
    category = models.IntegerField()
    subcat = models.IntegerField()
    machine_id = models.IntegerField()
    deptcode = models.IntegerField()
    type_id = models.IntegerField()
    assigned = models.IntegerField()
    approval = models.IntegerField()
    hod_code = models.CharField(max_length=11)
    hod_status = models.IntegerField()
    hod_remarks = models.CharField(max_length=200, blank=True, null=True)
    hod_apprd_date = models.DateField()
    adopttype = models.CharField(db_column='adoptType', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cost = models.IntegerField()
    remarks = models.CharField(max_length=200, blank=True, null=True)
    user_rmrks = models.CharField(max_length=400, blank=True, null=True)
    comments = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField()
    initiate_date = models.DateField()
    initiate_time = models.TimeField()
    target_date = models.DateField(blank=True, null=True)
    completed_date = models.DateField()
    completed_time = models.TimeField()
    completed_by = models.IntegerField()
    dept_type = models.CharField(max_length=100, blank=True, null=True)
    att_me = models.CharField(max_length=1000, blank=True, null=True)
    rating = models.IntegerField()
    feedback_comments = models.TextField(blank=True, null=True)
    rating_me = models.IntegerField()
    feedbk_cmnts_me = models.TextField(blank=True, null=True)
    sts = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=50, blank=True, null=True)
    user_cmnts = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtpl_ntry'


class MtplPrevAction(models.Model):
    prev_id = models.AutoField(primary_key=True)
    nc_tag_slno = models.CharField(max_length=250, blank=True, null=True)
    docno = models.CharField(max_length=500, blank=True, null=True)
    revno = models.CharField(max_length=250, blank=True, null=True)
    prev_respon = models.CharField(max_length=250, blank=True, null=True)
    prev_status = models.CharField(max_length=250, blank=True, null=True)
    doctype = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField(blank=True, null=True)
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtpl_prev_action'


class MtplSerDept(models.Model):
    dept = models.IntegerField(primary_key=True)
    deptname = models.CharField(max_length=20)
    responsible = models.IntegerField()
    createdby = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mtpl_ser_dept'


class MtplSerHis(models.Model):
    his_id = models.AutoField(primary_key=True)
    req_id = models.IntegerField()
    admin_tar_date = models.DateField()
    admin_rmks = models.CharField(max_length=200)
    status = models.IntegerField()
    response = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mtpl_ser_his'


class MtplSerStatus(models.Model):
    sts_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mtpl_ser_status'


class MtplSerTrack(models.Model):
    req_id = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    ntry_date = models.DateField()
    dept = models.IntegerField()
    nat_of_work = models.TextField()
    req_tar_date = models.DateField()
    status = models.IntegerField()
    response = models.IntegerField()
    admin_tar_date = models.DateField()
    admin_rmks = models.CharField(max_length=300)
    use_req = models.CharField(max_length=200)
    man_hrs = models.CharField(max_length=20)
    mach_hrs = models.CharField(max_length=20)
    cmplt_date = models.DateField()
    user_feed_bck = models.IntegerField()
    user_date = models.DateField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mtpl_ser_track'


class MtplServiceMultipleRoot(models.Model):
    slno = models.AutoField(primary_key=True)
    reportno = models.IntegerField()
    matcode_multi = models.CharField(max_length=250, blank=True, null=True)
    from_loc = models.CharField(max_length=100, blank=True, null=True)
    to_loc = models.CharField(max_length=100, blank=True, null=True)
    root_sts_dept_from = models.IntegerField()
    root_dept = models.IntegerField()
    root_cause_multi = models.TextField(blank=True, null=True)
    action_yn_multi = models.CharField(max_length=20, blank=True, null=True)
    ca_multi = models.TextField(blank=True, null=True)
    datef_impl_multi = models.DateField()
    ecr_no_multi = models.CharField(max_length=200, blank=True, null=True)
    root_sts_dept_to = models.CharField(max_length=250, blank=True, null=True)
    root_from_date = models.DateField()
    root_route_date = models.DateField()
    rc_sts = models.IntegerField()
    route_value = models.IntegerField()
    hod_sts = models.CharField(max_length=15, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    root_time = models.CharField(max_length=100, blank=True, null=True)
    rework_time = models.CharField(max_length=100, blank=True, null=True)
    reason_delay = models.TextField(blank=True, null=True)
    knowledge_appli_multi = models.CharField(max_length=50, blank=True, null=True)
    consult_asso_multi = models.IntegerField()
    mod_det = models.CharField(max_length=200, blank=True, null=True)
    db_type = models.IntegerField()
    type_ref = models.IntegerField()
    type = models.IntegerField()
    master_slno = models.CharField(max_length=100, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mtpl_service_multiple_root'


class MtplServiceReport(models.Model):
    reportno = models.PositiveBigIntegerField()
    detailsreceivedby = models.CharField(max_length=40, blank=True, null=True)
    reportedby = models.CharField(max_length=40, blank=True, null=True)
    reporteddate = models.DateField(blank=True, null=True)
    actualdate = models.DateField(blank=True, null=True)
    report_completed_date = models.DateField()
    actual_time = models.TimeField()
    typeofservice = models.CharField(max_length=20, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    mfddate = models.DateField()
    start_time = models.TimeField()
    completeddate = models.DateField(blank=True, null=True)
    complited_time = models.TimeField()
    zone = models.CharField(max_length=40, blank=True, null=True)
    depot = models.CharField(max_length=40, blank=True, null=True)
    coach = models.CharField(max_length=40, blank=True, null=True)
    shed = models.CharField(max_length=40, blank=True, null=True)
    locono = models.CharField(max_length=40, blank=True, null=True)
    locotype = models.CharField(max_length=40, blank=True, null=True)
    factory = models.CharField(max_length=40, blank=True, null=True)
    engineercode = models.CharField(max_length=30, blank=True, null=True)
    mcode = models.CharField(max_length=20, blank=True, null=True)
    ecode = models.CharField(max_length=20)
    problemdesc = models.CharField(max_length=500, blank=True, null=True)
    rd_analysis = models.CharField(max_length=1000, blank=True, null=True)
    ecr_no = models.CharField(max_length=50, blank=True, null=True)
    symptoms = models.CharField(max_length=500, blank=True, null=True)
    reworkdone = models.CharField(max_length=500, blank=True, null=True)
    failurecategory = models.CharField(max_length=40, blank=True, null=True)
    failuredetails = models.CharField(max_length=300, blank=True, null=True)
    pr_sup_eng_comm = models.CharField(max_length=1000, blank=True, null=True)
    serviceempcode = models.CharField(max_length=20, blank=True, null=True)
    checkedby = models.CharField(max_length=40, blank=True, null=True)
    authorizedby = models.CharField(max_length=40, blank=True, null=True)
    enteredby = models.CharField(max_length=40, blank=True, null=True)
    rework_report = models.IntegerField()
    dept_to = models.CharField(max_length=8, blank=True, null=True)
    project = models.CharField(max_length=30, blank=True, null=True)
    unittype = models.CharField(max_length=10, blank=True, null=True)
    unitno = models.CharField(max_length=20, blank=True, null=True)
    finalsave = models.CharField(max_length=5)
    srvchod_vrjct = models.CharField(max_length=50)
    to_dept_hod = models.IntegerField()
    altd_user = models.IntegerField()
    from_dept_user_report_taken = models.IntegerField()
    createdby = models.BigIntegerField()
    flre_reported_time = models.TimeField()
    datef_cmsn = models.DateField()
    version = models.CharField(max_length=50)
    rplcd_unitslno = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    dump = models.IntegerField()
    aglcode = models.IntegerField()
    agl_sts = models.CharField(max_length=30)
    agl_timestamp = models.CharField(max_length=30)
    disp_act = models.CharField(max_length=1000)
    days = models.IntegerField()
    hours = models.IntegerField()
    mins = models.IntegerField()
    ser_days = models.IntegerField()
    ser_hours = models.IntegerField()
    ser_mins = models.IntegerField()
    ser_time_update_sts = models.IntegerField()
    uniq_slno = models.IntegerField()
    loco_avlbl_sts = models.CharField(max_length=1)
    rack_no = models.CharField(max_length=15, blank=True, null=True)
    attend_at_fact = models.CharField(max_length=1, blank=True, null=True)
    report_ntry_date = models.DateField()
    failure_reported_date = models.DateField()
    failure_reported_time = models.TimeField()
    handed_over_date = models.DateField()
    attachment = models.CharField(max_length=150, blank=True, null=True)
    failure_unit_comments = models.CharField(max_length=10000, blank=True, null=True)
    failure_unit_analysis = models.CharField(max_length=500, blank=True, null=True)
    failur_unit_location = models.CharField(max_length=50, blank=True, null=True)
    repaly_mail_date = models.DateField()
    ffa_by = models.IntegerField()
    mat_rev_date = models.DateField()
    mat_sent_date = models.DateField()
    mat_loccode = models.CharField(max_length=30, blank=True, null=True)
    mat_dept = models.IntegerField()
    mat_problemcategory = models.CharField(max_length=500, blank=True, null=True)
    knowledge_appli = models.CharField(max_length=200, blank=True, null=True)
    consult_asso = models.IntegerField()
    noproblem_zone = models.CharField(max_length=40, blank=True, null=True)
    no_prob_shed = models.CharField(max_length=40, blank=True, null=True)
    no_prob_loco = models.CharField(max_length=40, blank=True, null=True)
    fitted_date = models.DateField()
    remarks = models.CharField(max_length=300, blank=True, null=True)
    status = models.IntegerField()
    to_rd_date = models.DateField()
    capa_eff = models.TextField(blank=True, null=True)
    service_ext_no = models.IntegerField()
    review_corr = models.TextField(blank=True, null=True)
    review_sts = models.IntegerField()
    ntry_date_ext = models.CharField(max_length=50, blank=True, null=True)
    reviewdate = models.CharField(max_length=50, blank=True, null=True)
    entry_ext_int = models.CharField(max_length=50, blank=True, null=True)
    third_type = models.IntegerField()
    close_sts = models.IntegerField()
    num_per = models.IntegerField()
    serv_engg_time_mm = models.CharField(max_length=100, blank=True, null=True)
    new_version_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'mtpl_service_report'


class MtplServiceSubassemblies(models.Model):
    sno = models.AutoField(primary_key=True)
    servicereportno = models.PositiveIntegerField(blank=True, null=True)
    fitemdesc = models.CharField(max_length=100, blank=True, null=True)
    fitemsno = models.CharField(max_length=45, blank=True, null=True)
    fitemmcode = models.CharField(max_length=20, blank=True, null=True)
    replaceditemsno = models.CharField(max_length=20, blank=True, null=True)
    dtf_mnf = models.CharField(max_length=50)
    replaced_item_tested_date = models.CharField(max_length=50)
    ref_sa_code = models.CharField(max_length=200)
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()
    repeat = models.IntegerField()
    service_status = models.IntegerField()
    third_type = models.IntegerField()
    broght_type = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mtpl_service_subassemblies'


class MtplServicereportAttachments(models.Model):
    report_no = models.IntegerField(unique=True)
    file_name = models.CharField(unique=True, max_length=50)
    extension = models.CharField(max_length=20)
    file_size = models.CharField(max_length=50)
    seq_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mtpl_servicereport_attachments'





class MtplStatusMaster(models.Model):
    status = models.SmallAutoField(primary_key=True)
    status_name = models.CharField(max_length=30)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField(blank=True, null=True)
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mtpl_status_master'





class MtplSubcatMaster(models.Model):
    subcat_id = models.AutoField(primary_key=True)
    subcat_name = models.CharField(max_length=50)
    main_id = models.IntegerField()
    location = models.CharField(max_length=20)
    dept_code = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'mtpl_subcat_master'


class MtplSuppDetails(models.Model):
    uniq = models.AutoField(primary_key=True)
    prjscope = models.CharField(max_length=5)
    fai_item_drw = models.CharField(max_length=100, blank=True, null=True)
    fai_quo_com = models.CharField(max_length=100, blank=True, null=True)
    fai_drawfile = models.CharField(max_length=100, blank=True, null=True)
    fai_purch_or = models.CharField(max_length=100, blank=True, null=True)
    faisampcomm = models.CharField(max_length=100, blank=True, null=True)
    faisamppleact = models.CharField(max_length=100, blank=True, null=True)
    startdate = models.DateField()
    targetdate = models.DateField()
    duration = models.CharField(max_length=11, blank=True, null=True)
    itemname = models.CharField(max_length=20)
    commadity = models.IntegerField()
    supp_loc = models.CharField(max_length=50, blank=True, null=True)
    supplier = models.IntegerField()
    suptype = models.IntegerField()
    prj_team = models.IntegerField()
    prj_mentor = models.IntegerField()
    prjtargets = models.CharField(max_length=250)
    model = models.IntegerField()
    ntry_by = models.IntegerField()
    ntry_date = models.DateField()
    vd_head_sts = models.IntegerField()
    vdhead = models.IntegerField()
    vdhead_date = models.DateField()
    prj_app_comm = models.CharField(max_length=200, blank=True, null=True)
    prj_ext_lead = models.CharField(max_length=20, blank=True, null=True)
    prj_risk = models.CharField(max_length=70, blank=True, null=True)
    prjteam = models.CharField(max_length=70, blank=True, null=True)
    pre_study_sts = models.IntegerField()
    pre_study_ntry = models.IntegerField()
    presstudy_date = models.DateField()
    com_reg_doc = models.CharField(max_length=70, blank=True, null=True)
    tech_com = models.CharField(max_length=70, blank=True, null=True)
    quo_pri = models.CharField(max_length=70, blank=True, null=True)
    anoth_file = models.CharField(max_length=100, blank=True, null=True)
    iso_cer = models.CharField(max_length=100, blank=True, null=True)
    other_comm = models.CharField(max_length=70, blank=True, null=True)
    tarprice = models.CharField(max_length=11, blank=True, null=True)
    tarquantity = models.CharField(max_length=11, blank=True, null=True)
    vdhead_pre_sts = models.IntegerField()
    vdhead_pre_ntry = models.IntegerField()
    vdhead_pre_comm = models.CharField(max_length=500, blank=True, null=True)
    vdhead_pre_date = models.DateField()
    sam_fai_pm_sts = models.IntegerField()
    sam_fai_pm_ntry = models.IntegerField()
    sam_fai_pm_date = models.DateField()
    itdrawno = models.CharField(max_length=50, blank=True, null=True)
    draw_rev = models.CharField(max_length=20, blank=True, null=True)
    quo_com = models.CharField(max_length=100, blank=True, null=True)
    drawfile = models.CharField(max_length=100, blank=True, null=True)
    purch_or = models.CharField(max_length=100, blank=True, null=True)
    sam_comm = models.TextField(blank=True, null=True)
    sam_act_date = models.DateField()
    sam_fai_qa_sts = models.IntegerField()
    sam_fai_qa_ntry = models.IntegerField()
    sam_fai_qa_date = models.DateField()
    processflow = models.CharField(max_length=100, blank=True, null=True)
    faireports = models.CharField(max_length=100, blank=True, null=True)
    faianalysis = models.CharField(max_length=100, blank=True, null=True)
    tsacomm = models.CharField(max_length=100, blank=True, null=True)
    fai_comm = models.CharField(max_length=500, blank=True, null=True)
    act_sam_date = models.DateField()
    sample_sts = models.IntegerField()
    app_sub = models.CharField(max_length=3, blank=True, null=True)
    app_test = models.CharField(max_length=3, blank=True, null=True)
    fit_assoc = models.CharField(max_length=20, blank=True, null=True)
    test_assoc = models.CharField(max_length=20, blank=True, null=True)
    fai_comms = models.CharField(max_length=500, blank=True, null=True)
    tsacomms = models.CharField(max_length=100, blank=True, null=True)
    faiana = models.CharField(max_length=100, blank=True, null=True)
    secsam_date = models.DateField()
    phasethree_sts = models.IntegerField()
    fit_comm = models.CharField(max_length=500, blank=True, null=True)
    test_comm = models.CharField(max_length=500, blank=True, null=True)
    fit_att = models.CharField(max_length=100, blank=True, null=True)
    test_att = models.CharField(max_length=100, blank=True, null=True)
    sam_prod_sts = models.IntegerField()
    vdhead_gates_sts = models.IntegerField()
    vdhead_gates_comm = models.CharField(max_length=500, blank=True, null=True)
    vdhead_gaes_ntry = models.IntegerField()
    vhead_gates_date = models.DateField()
    gate_three_sts = models.IntegerField()
    audit_comm = models.CharField(max_length=500, blank=True, null=True)
    auditrep = models.CharField(max_length=100, blank=True, null=True)
    cor_file = models.CharField(max_length=100, blank=True, null=True)
    audit_ntry = models.IntegerField()
    audit_date = models.DateField()
    auditdate = models.DateField()
    audit_list = models.CharField(max_length=500, blank=True, null=True)
    ramp_sts = models.IntegerField()
    ramprep = models.CharField(max_length=100, blank=True, null=True)
    ramp_comm = models.CharField(max_length=500, blank=True, null=True)
    cont_comm = models.CharField(max_length=500, blank=True, null=True)
    rampqty = models.CharField(max_length=11, blank=True, null=True)
    contqty = models.IntegerField()
    contrep = models.CharField(max_length=100, blank=True, null=True)
    ramp_ntry = models.IntegerField()
    ramp_date = models.DateField()
    eva_sts = models.IntegerField()
    prj_fin = models.CharField(max_length=5, blank=True, null=True)
    prj_del_comm = models.CharField(max_length=200, blank=True, null=True)
    tar_set = models.CharField(max_length=5, blank=True, null=True)
    tar_set_comm = models.CharField(max_length=200, blank=True, null=True)
    best_part = models.CharField(max_length=200, blank=True, null=True)
    learning = models.CharField(max_length=200, blank=True, null=True)
    eval_ntry = models.IntegerField()
    eval_date = models.DateField()
    prj_com_sts = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mtpl_supp_details'


class MtplSuppSelMaster(models.Model):
    sel_type = models.CharField(max_length=30)
    sel_value = models.CharField(max_length=50)
    createdby = models.CharField(max_length=6)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mtpl_supp_sel_master'


class MtplTypeMaster(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    dept = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mtpl_type_master'


class MtplVeAction(models.Model):
    ve_id = models.AutoField(primary_key=True)
    nc_tag_slno = models.CharField(max_length=250, blank=True, null=True)
    ve_action = models.CharField(max_length=500, blank=True, null=True)
    ve_respon = models.CharField(max_length=250, blank=True, null=True)
    ve_status = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtpl_ve_action'


class Mtplassembly(models.Model):
    assid = models.IntegerField(primary_key=True)
    daterec = models.DateField()
    proje = models.IntegerField()
    compo = models.CharField(max_length=20, blank=True, null=True)
    compsno = models.IntegerField()
    rust = models.CharField(max_length=1)
    rota = models.CharField(max_length=1)
    accum = models.CharField(max_length=1)
    trap = models.CharField(max_length=1)
    duedate = models.DateField()
    dispatch = models.IntegerField()
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mtplassembly'


class MtplmoduleNtry(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    deptcode = models.IntegerField()
    requesteddate = models.DateField()
    date_of_nc = models.DateField()
    nc_details = models.CharField(max_length=500, blank=True, null=True)
    area_of_nc = models.IntegerField()
    area = models.CharField(max_length=150, blank=True, null=True)
    responcesibility = models.CharField(max_length=250, blank=True, null=True)
    target_date = models.DateField()
    tracebility_no = models.CharField(max_length=200, blank=True, null=True)
    rework_no = models.IntegerField()
    prob_desc = models.CharField(max_length=500, blank=True, null=True)
    project = models.CharField(max_length=500, blank=True, null=True)
    nc_generation_status = models.IntegerField()
    prev_nc = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.IntegerField()
    delete1 = models.IntegerField()
    del_date = models.IntegerField()
    del_by = models.IntegerField()
    company = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mtplmodule_ntry'


class MtplreworkCompdata(models.Model):
    slno = models.AutoField(primary_key=True)
    id = models.IntegerField()
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    qty = models.IntegerField()
    uom = models.CharField(max_length=100, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mtplrework_compdata'


class MtplreworkNtry(models.Model):
    reworkno = models.AutoField(primary_key=True)
    fromdept = models.IntegerField()
    todept = models.IntegerField()
    toassoc = models.IntegerField()
    faildate = models.DateField(blank=True, null=True)
    failserno = models.IntegerField()
    project = models.IntegerField()
    drawno = models.CharField(max_length=20, blank=True, null=True)
    promdesc = models.CharField(max_length=200)
    idestage = models.IntegerField()
    subassem = models.CharField(max_length=200, blank=True, null=True)
    attach = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.IntegerField()
    ntrydate = models.DateField(blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    corrections = models.CharField(max_length=200, blank=True, null=True)
    pro_cat = models.CharField(max_length=100, blank=True, null=True)
    todept_date = models.DateField(blank=True, null=True)
    status = models.IntegerField()
    results = models.CharField(max_length=500, blank=True, null=True)
    releaseto = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtplrework_ntry'


class MtplscarDrawMaster(models.Model):
    did = models.AutoField(primary_key=True)
    project = models.IntegerField()
    drawing = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mtplscar_draw_master'


class MtplscarNtry(models.Model):
    scrap_id = models.AutoField(primary_key=True)
    dept_type = models.CharField(max_length=5)
    ipa_qpa = models.CharField(max_length=10)
    pno = models.CharField(max_length=50)
    supplier = models.CharField(max_length=6)
    raw_supp = models.CharField(max_length=10)
    ref_doc_no = models.CharField(max_length=20)
    attach_file = models.CharField(max_length=50)
    ntry_date = models.DateField()
    created_by = models.CharField(max_length=6)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    hod = models.CharField(max_length=6)
    hod_aprl_sts = models.IntegerField()
    hod_date = models.DateField()
    fur_action = models.CharField(max_length=500, blank=True, null=True)
    buyer = models.CharField(max_length=6)
    inform = models.CharField(max_length=100)
    fin_des = models.CharField(max_length=1000)
    ver_sts = models.IntegerField()
    ver_date = models.DateField()
    verified_by = models.IntegerField()
    copq = models.CharField(max_length=5)
    copq_cst = models.CharField(max_length=11)
    copq_act = models.CharField(max_length=100)
    copq_act_det = models.CharField(max_length=100)
    verify_comments = models.TextField(blank=True, null=True)
    rej_area = models.IntegerField()
    capa_file = models.CharField(max_length=50)
    copq_buyer = models.CharField(max_length=6, blank=True, null=True)
    copq_inform = models.CharField(max_length=6, blank=True, null=True)
    final_sts = models.IntegerField()
    final_date = models.DateField()
    finalised_by = models.CharField(max_length=6, blank=True, null=True)
    final_comm = models.CharField(max_length=100, blank=True, null=True)
    cpa_req = models.CharField(max_length=5, blank=True, null=True)
    store_sts = models.IntegerField()
    store_date = models.DateField()
    store_comm = models.CharField(max_length=100, blank=True, null=True)
    store_by = models.IntegerField()
    final_by = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtplscar_ntry'


class MtplscarSelMaster(models.Model):
    sid = models.AutoField(primary_key=True)
    master_type = models.CharField(max_length=10)
    value = models.CharField(max_length=50)
    show_val = models.CharField(max_length=100)
    createdby = models.CharField(max_length=6)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mtplscar_sel_master'


class MtplscarSubNtry(models.Model):
    subid = models.AutoField(primary_key=True)
    scrap_id = models.IntegerField()
    com_sno = models.CharField(max_length=100, blank=True, null=True)
    project = models.IntegerField()
    drawringno = models.IntegerField()
    part_desc = models.CharField(max_length=50)
    quality = models.IntegerField()
    reason = models.CharField(max_length=1000)
    capa_num = models.CharField(max_length=200)
    root_cause = models.CharField(max_length=200)
    cor_actn = models.CharField(max_length=200)
    cor_actn2 = models.CharField(max_length=200)
    closed_date = models.DateField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mtplscar_sub_ntry'


class NayabFieldsMaster(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    issue_no = models.CharField(max_length=10)
    spec_nyt = models.CharField(max_length=50)
    mdy = models.CharField(max_length=50)
    pages = models.IntegerField()
    pn = models.CharField(max_length=1)
    sn = models.CharField(max_length=1)
    tester = models.CharField(max_length=1)
    date = models.CharField(max_length=1)
    record_blank = models.CharField(max_length=1)
    record_blank_title = models.CharField(max_length=100)
    table = models.CharField(max_length=1)
    bottom_tester = models.CharField(max_length=1)
    bottom_date = models.CharField(max_length=1)
    bottom_start_no = models.IntegerField()
    copyrigth = models.CharField(max_length=150)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nayab_fields_master'


class NayabFieldsNtry(models.Model):
    report_uniq_slno = models.AutoField(primary_key=True)
    uniq_slno = models.IntegerField()
    pn = models.CharField(max_length=20)
    sn = models.CharField(max_length=20)
    tester = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    bottom_tester = models.CharField(max_length=20)
    bottom_date = models.CharField(max_length=20)
    ntry_sts = models.CharField(max_length=1)
    createdby = models.IntegerField()
    ntry_date = models.DateField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    delete_date = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'nayab_fields_ntry'


class NayabHeaderMaster(models.Model):
    uniq_slno = models.IntegerField()
    slno = models.IntegerField()
    h1 = models.CharField(max_length=150)
    h2 = models.CharField(max_length=150)
    h3 = models.CharField(max_length=150)
    rows = models.IntegerField()
    break_point = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nayab_header_master'


class NayabSubHeaderMaster(models.Model):
    uniq_slno = models.IntegerField()
    slno = models.IntegerField()
    seq_slno = models.IntegerField()
    sno = models.CharField(max_length=11)
    subh1 = models.CharField(max_length=100)
    subh2 = models.CharField(max_length=100)
    type = models.CharField(max_length=30)
    break_point = models.IntegerField()
    auto_inc_slno = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'nayab_sub_header_master'


class NayabSubHeaderNtry(models.Model):
    report_uniq_slno = models.IntegerField()
    uniq_slno = models.IntegerField()
    slno = models.IntegerField()
    seq_slno = models.IntegerField()
    sno = models.CharField(max_length=11)
    subh1 = models.CharField(max_length=100)
    subh2 = models.CharField(max_length=100)
    type = models.CharField(max_length=30)
    break_point = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nayab_sub_header_ntry'


class NayabTableNtry(models.Model):
    report_uniq_slno = models.IntegerField()
    uniq_slno = models.IntegerField()
    rot_switch_pos = models.IntegerField()
    l_limit = models.CharField(max_length=20)
    u_limit = models.CharField(max_length=20)
    number_24vdc = models.CharField(db_column='24vdc', max_length=20)  # Field renamed because it wasn't a valid Python identifier.
    number_48vdc = models.CharField(db_column='48vdc', max_length=20)  # Field renamed because it wasn't a valid Python identifier.
    number_18vdc = models.CharField(db_column='18vdc', max_length=20)  # Field renamed because it wasn't a valid Python identifier.
    pf = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'nayab_table_ntry'


class Nc5WhyMaster(models.Model):
    why_id = models.AutoField(primary_key=True)
    nc_tag_slno = models.CharField(max_length=250)
    why = models.CharField(max_length=500, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nc_5why_master'


class NcAppHist(models.Model):
    slno = models.AutoField(primary_key=True)
    uniq_slno = models.IntegerField()
    empcode = models.IntegerField()
    date = models.DateField()
    status = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nc_app_hist'


class NcAttachments(models.Model):
    sno = models.AutoField(primary_key=True)
    uniq_slno = models.IntegerField()
    file_name = models.CharField(max_length=500, blank=True, null=True)
    file_type = models.CharField(max_length=50, blank=True, null=True)
    file_path = models.CharField(max_length=100, blank=True, null=True)
    full_path = models.CharField(max_length=100, blank=True, null=True)
    raw_name = models.CharField(max_length=50, blank=True, null=True)
    orig_name = models.CharField(max_length=50, blank=True, null=True)
    client_name = models.CharField(max_length=50, blank=True, null=True)
    file_ext = models.CharField(max_length=50, blank=True, null=True)
    file_size = models.CharField(max_length=50, blank=True, null=True)
    is_image = models.CharField(max_length=50, blank=True, null=True)
    image_width = models.CharField(max_length=50, blank=True, null=True)
    image_height = models.CharField(max_length=50, blank=True, null=True)
    image_type = models.CharField(max_length=50, blank=True, null=True)
    image_size_str = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=25, blank=True, null=True)
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nc_attachments'


class NcCaAction(models.Model):
    ca_id = models.AutoField(primary_key=True)
    nc_tag_slno = models.CharField(max_length=250, blank=True, null=True)
    corr_action = models.CharField(max_length=500, blank=True, null=True)
    date_initiation = models.DateField()
    caresponce = models.CharField(db_column='CAresponce', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ca_target = models.DateField(db_column='CA_Target')  # Field name made lowercase.
    castatus = models.CharField(db_column='CAstatus', max_length=500, blank=True, null=True)  # Field name made lowercase.
    catype = models.CharField(db_column='CAType', max_length=250, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nc_ca_action'


class NcCategoryMaster(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'nc_category_master'


class NcDomainMaster(models.Model):
    domain_id = models.AutoField(primary_key=True)
    domain_name = models.CharField(max_length=50, blank=True, null=True)
    fullname = models.CharField(db_column='Fullname', max_length=250, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nc_domain_master'


class NcGeneration(models.Model):
    uniq_slno = models.IntegerField(primary_key=True)
    nc_tag_slno = models.CharField(max_length=500, blank=True, null=True)
    sub_uniq_slno = models.IntegerField()
    empcode = models.IntegerField()
    deptcode = models.IntegerField()
    requesteddate = models.DateField()
    date_of_nc = models.DateField()
    nc_details = models.CharField(max_length=500, blank=True, null=True)
    loctn = models.CharField(max_length=50, blank=True, null=True)
    nc_observed_at = models.IntegerField()
    responcesibility = models.CharField(max_length=250, blank=True, null=True)
    target_date = models.DateField()
    tracebility_no = models.CharField(max_length=500, blank=True, null=True)
    prob_desc = models.CharField(max_length=500, blank=True, null=True)
    project = models.CharField(max_length=500, blank=True, null=True)
    nc_title = models.CharField(max_length=250, blank=True, null=True)
    domain_id = models.IntegerField()
    category_id = models.CharField(max_length=30, blank=True, null=True)
    assign = models.CharField(max_length=500, blank=True, null=True)
    lot_qty = models.CharField(max_length=250, blank=True, null=True)
    aff_qty = models.CharField(max_length=250, blank=True, null=True)
    def_qty = models.CharField(max_length=250, blank=True, null=True)
    wt_prob = models.CharField(max_length=500, blank=True, null=True)
    wh_happend = models.CharField(max_length=500, blank=True, null=True)
    who = models.CharField(max_length=250, blank=True, null=True)
    how = models.CharField(max_length=500, blank=True, null=True)
    who_owner = models.CharField(max_length=500, blank=True, null=True)
    detect_with_prasent = models.CharField(max_length=500, blank=True, null=True)
    nc_prob_attach = models.CharField(max_length=250, blank=True, null=True)
    caaction = models.CharField(db_column='CAaction', max_length=500, blank=True, null=True)  # Field name made lowercase.
    respca = models.CharField(db_column='respCA', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ca_date_completion = models.CharField(db_column='CA_date_completion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    proc_root_cause = models.TextField()
    escape_root_cause = models.TextField()
    closed_attach = models.CharField(max_length=250, blank=True, null=True)
    nc_closing_stmt = models.TextField(db_collation='utf8_unicode_ci', blank=True, null=True)
    nc_analysis = models.CharField(max_length=2000, blank=True, null=True)
    end_user = models.IntegerField()
    date_nc_closer = models.DateField()
    status = models.IntegerField()
    hod_code = models.IntegerField()
    hod_status = models.IntegerField()
    hod_remarks = models.CharField(max_length=500, blank=True, null=True)
    hod_approve_date = models.DateTimeField()
    edp_code = models.IntegerField()
    edp_status = models.IntegerField()
    edp_remarks = models.CharField(max_length=500, blank=True, null=True)
    edp_approve_date = models.DateTimeField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.IntegerField()
    del_by = models.IntegerField()
    no_of_days = models.IntegerField()
    cost_non = models.CharField(max_length=500, blank=True, null=True)
    dfmea = models.CharField(max_length=100, blank=True, null=True)
    pfmea = models.CharField(max_length=100, blank=True, null=True)
    prev_nc = models.CharField(max_length=100, blank=True, null=True)
    assoc_prev = models.CharField(max_length=60, blank=True, null=True)
    reopen_reson = models.TextField()
    futuredt_check = models.IntegerField()
    date_future_trg = models.DateField()

    class Meta:
        managed = False
        db_table = 'nc_generation'


class NcLaAction(models.Model):
    la_id = models.AutoField(primary_key=True)
    nc_tag_slno = models.CharField(max_length=250)
    proj = models.IntegerField()
    la_details = models.CharField(max_length=250, blank=True, null=True)
    la_respon = models.CharField(max_length=250, blank=True, null=True)
    la_status = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nc_la_action'


class NcModuleMeeting(models.Model):
    slno = models.AutoField(primary_key=True)
    uniq_slno = models.IntegerField()
    desc = models.CharField(max_length=2000, blank=True, null=True)
    type = models.CharField(max_length=500, blank=True, null=True)
    created_by = models.IntegerField()
    created_date = models.DateField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nc_module_meeting'


class NcPrevAction(models.Model):
    prev_id = models.AutoField(primary_key=True)
    nc_tag_slno = models.CharField(max_length=250, blank=True, null=True)
    docno = models.CharField(max_length=500, blank=True, null=True)
    revno = models.CharField(max_length=250, blank=True, null=True)
    prev_respon = models.CharField(max_length=250, blank=True, null=True)
    prev_status = models.CharField(max_length=250, blank=True, null=True)
    doctype = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nc_prev_action'





class NcStatusMaster(models.Model):
    status = models.SmallAutoField(primary_key=True)
    status_name = models.CharField(max_length=100)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField(blank=True, null=True)
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'nc_status_master'





class NcVeAction(models.Model):
    ve_id = models.AutoField(primary_key=True)
    nc_tag_slno = models.CharField(max_length=250, blank=True, null=True)
    ve_action = models.CharField(max_length=500, blank=True, null=True)
    ve_respon = models.CharField(max_length=250, blank=True, null=True)
    ve_status = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nc_ve_action'


class NcmoduleNtry(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    deptcode = models.IntegerField()
    requesteddate = models.DateField()
    date_of_nc = models.DateField()
    nc_details = models.CharField(max_length=500, blank=True, null=True)
    loctn = models.CharField(max_length=10, blank=True, null=True)
    area_of_nc = models.IntegerField()
    responcesibility = models.CharField(max_length=250, blank=True, null=True)
    target_date = models.DateField()
    rework_no = models.IntegerField()
    prob_desc = models.CharField(max_length=500, blank=True, null=True)
    project = models.CharField(max_length=500, blank=True, null=True)
    nc_generation_status = models.IntegerField()
    prev_nc = models.CharField(max_length=100, blank=True, null=True)
    tracebility_no = models.CharField(max_length=500, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.IntegerField()
    del_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ncmodule_ntry'


class NnsCatMaster(models.Model):
    catid = models.AutoField(primary_key=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nns_cat_master'


class NnsCatSubMaster(models.Model):
    scatid = models.AutoField(primary_key=True)
    catid = models.IntegerField()
    typeid = models.IntegerField(blank=True, null=True)
    subcategory = models.CharField(max_length=50)
    appsts = models.CharField(max_length=10, blank=True, null=True)
    duration = models.FloatField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nns_cat_sub_master'


class NnsCattypeMaster(models.Model):
    typeid = models.AutoField(primary_key=True)
    catid = models.IntegerField(blank=True, null=True)
    typename = models.CharField(max_length=50, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nns_cattype_master'


class NnsHrReqType(models.Model):
    hr_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    catid = models.IntegerField()
    typeid = models.IntegerField()
    scatid = models.IntegerField()
    appr = models.CharField(max_length=10, blank=True, null=True)
    sts = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nns_hr_req_type'


class NnsNtry(models.Model):
    slno = models.IntegerField()
    slno_multi = models.IntegerField()
    desc = models.CharField(max_length=5000, blank=True, null=True)
    date = models.DateField()
    ntryby = models.IntegerField()
    sts_up = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nns_ntry'


class NnsPbTypeMstr(models.Model):
    slno = models.AutoField(primary_key=True)
    pb_type = models.CharField(max_length=100, blank=True, null=True)
    pb_sub_type = models.CharField(max_length=100, blank=True, null=True)
    pb_no = models.IntegerField()
    delete1 = models.IntegerField()
    aprl_type = models.CharField(max_length=1, blank=True, null=True)
    direct_mail = models.IntegerField()
    duration = models.FloatField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nns_pb_type_mstr'


class NnsProjMaster(models.Model):
    proj_master = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nns_proj_master'


class NnsPrtyMstr(models.Model):
    slno = models.AutoField(primary_key=True)
    prty = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nns_prty_mstr'


class NnsRatingNtry(models.Model):
    tag_no = models.IntegerField()
    feedback_desc = models.IntegerField()
    rating = models.IntegerField()
    remarks = models.CharField(max_length=250)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    delete_date = models.DateField()
    delete_reason = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'nns_rating_ntry'


class NnsReq(models.Model):
    req_id = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    ntry_date = models.DateField(blank=True, null=True)
    descrp = models.CharField(max_length=600, blank=True, null=True)
    req_src = models.IntegerField(blank=True, null=True)
    sys_type = models.CharField(max_length=10, blank=True, null=True)
    sys_no = models.CharField(max_length=20, blank=True, null=True)
    catid = models.IntegerField()
    typeid = models.IntegerField(blank=True, null=True)
    scatid = models.IntegerField()
    sts = models.IntegerField()
    approval = models.IntegerField()
    hod_sts = models.IntegerField()
    hod = models.IntegerField()
    md_sts = models.IntegerField()
    md = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    attachments = models.CharField(max_length=300, blank=True, null=True)
    priority = models.IntegerField()
    scat_ft = models.CharField(max_length=100, blank=True, null=True)
    attachment_two = models.CharField(max_length=100, blank=True, null=True)
    assign = models.IntegerField(blank=True, null=True)
    loc = models.CharField(max_length=50, blank=True, null=True)
    dept = models.IntegerField(blank=True, null=True)
    close_type = models.IntegerField(blank=True, null=True)
    sts_tms = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nns_req'


class NnsReqCloseTypeMaster(models.Model):
    cid = models.AutoField(primary_key=True)
    close_catid = models.IntegerField(blank=True, null=True)
    close_cattype = models.IntegerField(blank=True, null=True)
    close_subcat = models.IntegerField(blank=True, null=True)
    close_typename = models.CharField(max_length=100)
    createdby = models.IntegerField(blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nns_req_close_type_master'


class NnsReqHistory(models.Model):
    hid = models.AutoField(primary_key=True)
    req_id = models.IntegerField()
    empcode = models.IntegerField()
    comments = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    stage = models.CharField(max_length=5)
    his_date = models.DateField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    createdby = models.IntegerField(blank=True, null=True)
    work_min = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nns_req_history'


class NnsReqHistoryUpload(models.Model):
    hid = models.AutoField(primary_key=True)
    req_id = models.IntegerField()
    empcode = models.IntegerField()
    comments = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    stage = models.CharField(max_length=5)
    his_date = models.DateField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    createdby = models.IntegerField(blank=True, null=True)
    work_min = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nns_req_history_upload'


class NnsReqMore(models.Model):
    req_id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField()
    createdby = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nns_req_more'


class NnsReqSrcMstr(models.Model):
    slno = models.AutoField(primary_key=True)
    req_src = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nns_req_src_mstr'


class NnsStsMstr(models.Model):
    slno = models.IntegerField()
    desc = models.CharField(max_length=50, blank=True, null=True)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nns_sts_mstr'


class NnsStsUpdtMstr(models.Model):
    slno = models.IntegerField(primary_key=True)
    desc = models.CharField(max_length=50, blank=True, null=True)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    ind1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nns_sts_updt_mstr'


class NnsSysNumbers(models.Model):
    sid = models.AutoField(primary_key=True)
    location = models.CharField(max_length=10, blank=True, null=True)
    sys_type = models.CharField(max_length=10, blank=True, null=True)
    sys_initial = models.CharField(max_length=10, blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nns_sys_numbers'


class NnsTimespentRequests(models.Model):
    tid = models.AutoField(primary_key=True)
    empcode = models.IntegerField(blank=True, null=True)
    his_date = models.DateField(blank=True, null=True)
    req_id = models.IntegerField(blank=True, null=True)
    time_spent = models.TimeField()
    ts_sts = models.IntegerField()
    createdby = models.IntegerField(blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    dup_t = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nns_timespent_requests'


class NnsUsrNtry(models.Model):
    slno = models.AutoField(primary_key=True)
    mod = models.IntegerField()
    req_desc = models.CharField(max_length=5000, blank=True, null=True)
    rqstdby = models.IntegerField()
    sts = models.IntegerField()
    rqstd_dt = models.DateField()
    rjct_rsn = models.CharField(max_length=100, blank=True, null=True)
    hod_dcsn = models.IntegerField()
    hod_cmnts = models.CharField(max_length=500, blank=True, null=True)
    pb_type = models.IntegerField()
    pb_sub_type = models.IntegerField()
    req_src = models.IntegerField()
    prty = models.IntegerField()
    tot_dur = models.CharField(max_length=15, blank=True, null=True)
    ntryby = models.IntegerField()
    sts_up = models.IntegerField()
    assign = models.IntegerField()
    start_time = models.CharField(max_length=20, blank=True, null=True)
    end_time = models.CharField(max_length=20, blank=True, null=True)
    repeat = models.CharField(max_length=20, blank=True, null=True)
    rep = models.IntegerField()
    days = models.IntegerField()
    hrs = models.IntegerField()
    mins = models.IntegerField()
    hod_code = models.IntegerField()
    hod_date = models.DateField()
    hod_time = models.CharField(max_length=10, blank=True, null=True)
    loc = models.CharField(max_length=50, blank=True, null=True)
    attach_file_rename = models.CharField(max_length=100, blank=True, null=True)
    attach_file_original = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField()
    edbd_code = models.CharField(max_length=10, blank=True, null=True)
    edbd_sts = models.IntegerField()
    edbd_date = models.DateField()
    edbd_time = models.CharField(max_length=10, blank=True, null=True)
    edbd_comnt = models.TextField(blank=True, null=True)
    cc_mail_ids = models.CharField(max_length=500, blank=True, null=True)
    vnv_uniq_slno = models.IntegerField()
    trail_months = models.IntegerField()
    trail_days = models.IntegerField()
    ucp_wait_time = models.IntegerField()
    attach_file_rename2 = models.CharField(max_length=100, blank=True, null=True)
    attach_file_original2 = models.CharField(max_length=100, blank=True, null=True)
    initiate_to = models.CharField(max_length=250, blank=True, null=True)
    act_int_time = models.CharField(max_length=250, blank=True, null=True)
    target_time = models.CharField(max_length=250, blank=True, null=True)
    sys_no = models.CharField(max_length=20, blank=True, null=True)
    rating = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nns_usr_ntry'


class NnsUsrNtryOld(models.Model):
    slno = models.AutoField(primary_key=True)
    mod = models.IntegerField()
    req_desc = models.CharField(max_length=5000, blank=True, null=True)
    rqstdby = models.IntegerField()
    sts = models.IntegerField()
    rqstd_dt = models.DateField()
    rjct_rsn = models.CharField(max_length=100, blank=True, null=True)
    hod_dcsn = models.IntegerField()
    hod_cmnts = models.CharField(max_length=500, blank=True, null=True)
    pb_type = models.IntegerField()
    pb_sub_type = models.IntegerField()
    req_src = models.IntegerField()
    prty = models.IntegerField()
    tot_dur = models.CharField(max_length=15, blank=True, null=True)
    ntryby = models.IntegerField()
    sts_up = models.IntegerField()
    assign = models.IntegerField()
    start_time = models.CharField(max_length=20, blank=True, null=True)
    end_time = models.CharField(max_length=20, blank=True, null=True)
    repeat = models.CharField(max_length=20, blank=True, null=True)
    rep = models.IntegerField()
    days = models.IntegerField()
    hrs = models.IntegerField()
    mins = models.IntegerField()
    hod_code = models.IntegerField()
    hod_date = models.DateField()
    hod_time = models.CharField(max_length=10, blank=True, null=True)
    loc = models.CharField(max_length=50, blank=True, null=True)
    attach_file_rename = models.CharField(max_length=100, blank=True, null=True)
    attach_file_original = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField()
    edbd_code = models.CharField(max_length=10, blank=True, null=True)
    edbd_sts = models.IntegerField()
    edbd_date = models.DateField()
    edbd_time = models.CharField(max_length=10, blank=True, null=True)
    edbd_comnt = models.TextField(blank=True, null=True)
    cc_mail_ids = models.CharField(max_length=500, blank=True, null=True)
    vnv_uniq_slno = models.IntegerField()
    trail_months = models.IntegerField()
    trail_days = models.IntegerField()
    ucp_wait_time = models.IntegerField()
    attach_file_rename2 = models.CharField(max_length=100, blank=True, null=True)
    attach_file_original2 = models.CharField(max_length=100, blank=True, null=True)
    initiate_to = models.CharField(max_length=250, blank=True, null=True)
    act_int_time = models.CharField(max_length=250, blank=True, null=True)
    target_time = models.CharField(max_length=250, blank=True, null=True)
    rating = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nns_usr_ntry_old'


class NoteMaster(models.Model):
    note_no = models.AutoField(primary_key=True)
    note_name = models.CharField(max_length=20)
    note_desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'note_master'


class OeeBreakDetails(models.Model):
    break_id = models.AutoField(primary_key=True)
    operator = models.CharField(max_length=6)
    shift = models.CharField(max_length=2)
    ntry_date = models.DateField()
    ntry_time = models.CharField(max_length=6)
    machine = models.IntegerField()
    mach_break_down_from_date = models.DateField()
    mach_break_down_time = models.CharField(max_length=10)
    mach_break_down_to_date = models.DateField()
    mach_break_start_time = models.CharField(max_length=10)
    mach_down_time = models.CharField(max_length=10)
    nat_of_prob = models.TextField()
    err_msg = models.TextField()
    sym_obs = models.TextField()
    root_cause = models.TextField()
    corr_act = models.IntegerField()
    prev_act = models.TextField()
    attendedby = models.CharField(max_length=6)
    reviewby = models.CharField(max_length=6)
    attended_by_op = models.CharField(max_length=15)
    attend = models.CharField(max_length=50)
    dept_type = models.CharField(max_length=100)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oee_break_details'


class OeeBreakMatDetails(models.Model):
    mat_id = models.AutoField(primary_key=True)
    break_id = models.IntegerField()
    indicator = models.CharField(max_length=5)
    materialcode = models.CharField(max_length=12)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oee_break_mat_details'


class OeeCardMaster(models.Model):
    slno = models.AutoField(primary_key=True)
    material = models.CharField(max_length=11)
    card_name = models.CharField(max_length=50, blank=True, null=True)
    project = models.CharField(max_length=20, blank=True, null=True)
    alphabet = models.CharField(max_length=5, blank=True, null=True)
    createdby = models.CharField(max_length=6, blank=True, null=True)
    ntry_date = models.DateField()
    secondmat = models.CharField(max_length=200, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oee_card_master'


class OeeChangeover(models.Model):
    slno = models.AutoField(primary_key=True)
    ntry_date = models.CharField(max_length=15)
    machine = models.IntegerField()
    starttime = models.CharField(max_length=15, blank=True, null=True)
    endtime = models.CharField(max_length=15)
    totaltime = models.CharField(max_length=15)
    remarks = models.CharField(max_length=200, blank=True, null=True)
    empcode = models.CharField(max_length=6, blank=True, null=True)
    delete1 = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oee_changeover'


class OeeCycleMaster(models.Model):
    alphabet = models.CharField(max_length=5, blank=True, null=True)
    machine = models.IntegerField()
    coat_ax = models.CharField(max_length=5, blank=True, null=True)
    cyc_time = models.IntegerField()
    createdby = models.CharField(max_length=6, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    material = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oee_cycle_master'


class OeeDefaultComments(models.Model):
    slno = models.AutoField(primary_key=True)
    type = models.IntegerField()
    description = models.CharField(max_length=150, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oee_default_comments'


class OeeDefaultRemarks(models.Model):
    slno = models.AutoField(primary_key=True)
    reamarks = models.CharField(max_length=100, blank=True, null=True)
    reasons = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oee_default_remarks'


class OeeMachine(models.Model):
    mach_id = models.AutoField(primary_key=True)
    machine = models.CharField(max_length=50, blank=True, null=True)
    createdby = models.CharField(max_length=6, blank=True, null=True)
    ntry_date = models.DateField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oee_machine'


class OeeMaintMaster(models.Model):
    slno = models.AutoField(primary_key=True)
    activity = models.CharField(max_length=150)
    desc = models.CharField(max_length=100)
    frequency = models.CharField(max_length=2)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oee_maint_master'


class OeePcbBarMaster(models.Model):
    pid = models.AutoField(primary_key=True)
    prod_or = models.CharField(max_length=11)
    mat = models.CharField(max_length=11, blank=True, null=True)
    desc = models.CharField(max_length=200, blank=True, null=True)
    qty = models.IntegerField()
    revision = models.CharField(max_length=11, blank=True, null=True)
    createdby = models.CharField(max_length=6, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oee_pcb_bar_master'


class OeePcbBarMaster1708(models.Model):
    pid = models.AutoField(primary_key=True)
    prod_or = models.CharField(max_length=11)
    mat = models.CharField(max_length=11, blank=True, null=True)
    desc = models.CharField(max_length=200, blank=True, null=True)
    qty = models.IntegerField()
    revision = models.CharField(max_length=11, blank=True, null=True)
    createdby = models.CharField(max_length=6, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oee_pcb_bar_master_17_08'


class OeePcbProdDetails(models.Model):
    operator = models.IntegerField()
    ntry_date = models.DateField()
    machine = models.IntegerField()
    shift = models.CharField(max_length=2)
    pcb_barcod = models.CharField(max_length=11)
    cycle_time = models.IntegerField()
    good_boards = models.IntegerField()
    job_date = models.DateField()
    varities = models.IntegerField()
    component = models.IntegerField()
    prod_qty = models.IntegerField()
    frst_ins_by = models.IntegerField()
    aft_frst_ins_by = models.CharField(max_length=6)
    remarks = models.CharField(max_length=500)
    change_start = models.CharField(max_length=9)
    change_end = models.CharField(max_length=9)
    change_time = models.CharField(max_length=9)
    first_start = models.CharField(max_length=9)
    first_end = models.CharField(max_length=9)
    first_time = models.CharField(max_length=9)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oee_pcb_prod_details'


class OeePcbProdDetailsnew(models.Model):
    operator = models.IntegerField()
    ntry_date = models.DateField()
    machine = models.IntegerField()
    shift = models.CharField(max_length=2, blank=True, null=True)
    pcb_barcod = models.CharField(max_length=11, blank=True, null=True)
    cycle_time = models.CharField(max_length=50, blank=True, null=True)
    good_boards = models.IntegerField()
    job_date = models.DateField()
    varities = models.IntegerField()
    component = models.IntegerField()
    prod_qty = models.IntegerField()
    frst_ins_by = models.IntegerField()
    aft_frst_ins_by = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)
    time_type = models.CharField(max_length=20, blank=True, null=True)
    start = models.CharField(max_length=10, blank=True, null=True)
    end = models.CharField(max_length=10, blank=True, null=True)
    total = models.CharField(max_length=10, blank=True, null=True)
    breakdown_time = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oee_pcb_prod_detailsnew'


class OeePcbProdTimings(models.Model):
    time_id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    pcb_barcod = models.IntegerField()
    time_type = models.CharField(max_length=6, blank=True, null=True)
    start = models.CharField(max_length=10, blank=True, null=True)
    end = models.CharField(max_length=10, blank=True, null=True)
    total = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oee_pcb_prod_timings'


class OeePcbShiftTimings(models.Model):
    shift = models.CharField(max_length=5, blank=True, null=True)
    a_810_830 = models.CharField(max_length=2, blank=True, null=True)
    a_110_117 = models.CharField(max_length=2, blank=True, null=True)
    a_1145_1225 = models.CharField(max_length=2, blank=True, null=True)
    gen_11_117 = models.CharField(max_length=2, blank=True, null=True)
    gen_1230_110 = models.CharField(max_length=2, blank=True, null=True)
    gen_16_167 = models.CharField(max_length=2, blank=True, null=True)
    b_4_47 = models.CharField(max_length=2, blank=True, null=True)
    b_1930_2010 = models.CharField(max_length=2, blank=True, null=True)
    c_1_17 = models.CharField(max_length=2, blank=True, null=True)
    timestamp = models.DateTimeField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'oee_pcb_shift_timings'


class OeePrevActivities(models.Model):
    prev_id = models.IntegerField()
    activity = models.IntegerField()
    createdby = models.CharField(max_length=6)
    done_date = models.DateField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oee_prev_activities'


class OeePrevDetails(models.Model):
    prev_id = models.AutoField(primary_key=True)
    operator = models.CharField(max_length=6, blank=True, null=True)
    ntry_date = models.DateField()
    ntry_time = models.CharField(max_length=10, blank=True, null=True)
    machine = models.IntegerField()
    shift = models.CharField(max_length=6, blank=True, null=True)
    maint = models.CharField(max_length=10, blank=True, null=True)
    maint_start = models.CharField(max_length=10, blank=True, null=True)
    maint_end = models.CharField(max_length=10, blank=True, null=True)
    maint_time = models.CharField(max_length=10, blank=True, null=True)
    dept_type = models.CharField(max_length=100, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oee_prev_details'


class OeeProdDetails(models.Model):
    prod_id = models.AutoField(primary_key=True)
    operator = models.CharField(max_length=6)
    ntry_date = models.DateField()
    ntry_time = models.CharField(max_length=10)
    shift = models.CharField(max_length=5)
    machine = models.IntegerField()
    pcb_barcod = models.CharField(max_length=30)
    coat_ax = models.CharField(max_length=10)
    cyc_time = models.CharField(max_length=11)
    prod_start = models.CharField(max_length=10)
    prod_end = models.CharField(max_length=10)
    prod_time = models.CharField(max_length=10)
    jig = models.CharField(max_length=5)
    prod_qty = models.IntegerField()
    acc_qty = models.IntegerField()
    def_det = models.TextField(blank=True, null=True)
    rmrks = models.TextField(blank=True, null=True)
    cngover_rmks = models.CharField(max_length=150, blank=True, null=True)
    tl_coms = models.TextField(blank=True, null=True)
    action = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    material_type = models.IntegerField()
    batch_no = models.CharField(max_length=20)
    tbatch_no = models.CharField(max_length=20)
    main_pcb = models.IntegerField()
    index_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oee_prod_details'


class OeeProdDetailsTemp(models.Model):
    prod_id = models.AutoField(primary_key=True)
    operator = models.CharField(max_length=6)
    ntry_date = models.DateField()
    ntry_time = models.CharField(max_length=10)
    shift = models.CharField(max_length=5)
    machine = models.IntegerField()
    pcb_barcod = models.CharField(max_length=30)
    coat_ax = models.CharField(max_length=10)
    cyc_time = models.CharField(max_length=11)
    prod_start = models.CharField(max_length=10)
    prod_end = models.CharField(max_length=10)
    prod_time = models.CharField(max_length=10)
    jig = models.CharField(max_length=5)
    prod_qty = models.IntegerField()
    acc_qty = models.IntegerField()
    def_det = models.TextField(blank=True, null=True)
    rmrks = models.TextField(blank=True, null=True)
    tl_coms = models.TextField(blank=True, null=True)
    action = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    material_type = models.IntegerField()
    batch_no = models.CharField(max_length=12)
    tbatch_no = models.CharField(max_length=54)
    main_pcb = models.IntegerField()
    index_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oee_prod_details_temp'


class OnlineUserCountMaster(models.Model):
    date = models.DateField()
    time = models.TimeField()
    empcode = models.IntegerField()
    sys_name = models.CharField(max_length=20)
    ip = models.CharField(max_length=20)
    file_name = models.CharField(max_length=256)
    coments = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'online_user_count_master'


class PahrComplaintDetails(models.Model):
    slno = models.AutoField(primary_key=True)
    ntry_date = models.DateField()
    expiry_date = models.DateField()
    completed_date = models.DateField()
    empcode = models.IntegerField()
    mediater = models.CharField(max_length=6)
    design = models.CharField(max_length=100)
    dept = models.IntegerField()
    complaint_main_type = models.IntegerField()
    complaint_type = models.IntegerField()
    description = models.CharField(max_length=1000)
    hod = models.IntegerField()
    hod_aprl_sts = models.IntegerField()
    hod_ntry_date = models.DateField()
    hod_comment = models.CharField(max_length=500)
    pahr_sts = models.IntegerField()
    pahr_assign_by = models.CharField(max_length=10)
    pahr_assign_to = models.CharField(max_length=10)
    pahr_comment = models.CharField(max_length=100)
    pahr_group_mail = models.CharField(max_length=100)
    pahr_group_ids = models.CharField(max_length=200)
    pahr_assign_date = models.DateField()
    status = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pahr_complaint_details'


class PahrComplaintHistory(models.Model):
    slno = models.IntegerField()
    pahr_sts = models.IntegerField()
    desc = models.CharField(max_length=100)
    createdby = models.CharField(max_length=10)
    reassign = models.CharField(max_length=10)
    ntry_date = models.DateField()
    user_sts = models.IntegerField()
    update_sts = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pahr_complaint_history'


class PahrComplaintHistoryNew(models.Model):
    slno = models.AutoField(primary_key=True)
    id = models.IntegerField()
    status = models.IntegerField()
    desc = models.CharField(max_length=400)
    action_by = models.IntegerField()
    ntry_date = models.DateField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pahr_complaint_history_new'


class PahrComplaintNtry(models.Model):
    slno = models.AutoField(primary_key=True)
    ntry_date = models.DateField()
    expiry_date = models.DateField()
    completed_date = models.DateField()
    empcode = models.IntegerField()
    loc = models.CharField(max_length=50)
    dept = models.IntegerField()
    complaint_main_type = models.IntegerField()
    complaint_type = models.IntegerField()
    description = models.CharField(max_length=1000)
    hod = models.IntegerField()
    hod_aprl_sts = models.IntegerField()
    hod_ntry_date = models.DateField()
    hod_comment = models.CharField(max_length=500)
    assign_to = models.CharField(max_length=10)
    assigned_date = models.DateField()
    status = models.IntegerField()
    hr_hod = models.IntegerField()
    created_by = models.IntegerField()
    rating = models.IntegerField()
    feedbck_commnts = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pahr_complaint_ntry'


class PahrIdcardEmplist(models.Model):
    slno = models.AutoField(primary_key=True)
    pa_ref = models.CharField(max_length=200)
    empcode = models.IntegerField()
    issu_date = models.DateField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pahr_idcard_emplist'


class PahrMainComplaintType(models.Model):
    main_id = models.AutoField(primary_key=True)
    complaint_main_type = models.CharField(max_length=50)
    group_mail_id = models.CharField(max_length=100)
    group_ids = models.CharField(max_length=200)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pahr_main_complaint_type'


class PahrStsMaster(models.Model):
    pahr_sts = models.CharField(max_length=50)
    createdby = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    assign_auth = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pahr_sts_master'


class PahrSubComplaintType(models.Model):
    sno = models.AutoField(primary_key=True)
    id = models.IntegerField()
    main_id = models.IntegerField()
    complaint_type = models.CharField(max_length=100)
    expirydays = models.IntegerField()
    assign_to = models.IntegerField()
    msfa_assgn_to = models.IntegerField()
    responsible = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pahr_sub_complaint_type'


class PahrSubComplaintType25072021(models.Model):
    main_id = models.IntegerField()
    complaint_type = models.CharField(max_length=100)
    expirydays = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pahr_sub_complaint_type_25-07-2021'


class PahrSubComplaintTypeLocation(models.Model):
    lid = models.AutoField(primary_key=True)
    id = models.IntegerField()
    main_id = models.IntegerField()
    location = models.CharField(max_length=20)
    assign_to = models.IntegerField()
    responsible = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pahr_sub_complaint_type_location'


class PartsTable(models.Model):
    sno = models.AutoField(primary_key=True)
    reworkreportno = models.BigIntegerField()
    name = models.CharField(max_length=500, blank=True, null=True)
    testedby_multi = models.IntegerField()
    code = models.CharField(max_length=12, blank=True, null=True)
    legend = models.CharField(max_length=5000, blank=True, null=True)
    batchno = models.CharField(max_length=5000, blank=True, null=True)
    make = models.CharField(max_length=5000, blank=True, null=True)
    partretestedat = models.CharField(max_length=100, blank=True, null=True)
    rresults = models.CharField(max_length=1000)
    serialno = models.IntegerField()
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()
    sno_wise = models.IntegerField()
    consm_qty = models.CharField(max_length=100)
    rej_rew_qty = models.IntegerField()
    uom = models.CharField(max_length=10)
    reason = models.TextField()
    rej_rew_sts = models.IntegerField()
    rej_slip_no = models.IntegerField()
    part_no = models.CharField(max_length=50)
    kms = models.FloatField()
    days = models.FloatField()
    megaw_hours = models.FloatField(db_column='megaW_hours')  # Field name made lowercase.
    supplier = models.IntegerField()
    doc_no = models.IntegerField()
    date_igi = models.CharField(max_length=10)
    ntry_by_igi = models.IntegerField()
    fitem_code = models.BigIntegerField()
    fitem_slno = models.IntegerField()
    qty_rej_igi = models.IntegerField()
    igi_remarks = models.CharField(max_length=500)
    timestapm_igi = models.CharField(max_length=20)
    sts_igi = models.IntegerField()
    service_report_no = models.IntegerField()
    sts_slno_purchase = models.IntegerField()
    igi_completed_date = models.DateField()
    totappliofcom = models.IntegerField()
    totcomqty = models.IntegerField()
    acrappl = models.IntegerField()
    totfailure = models.IntegerField()
    ca = models.CharField(max_length=500)
    faildatethird = models.CharField(max_length=12)
    failapp = models.TextField(blank=True, null=True)
    igisampling = models.TextField(blank=True, null=True)
    tl = models.CharField(max_length=6)
    gl = models.CharField(max_length=6)
    compo_wa = models.CharField(max_length=50, blank=True, null=True)
    fag_mail = models.CharField(max_length=250)
    vend_sent_date = models.CharField(max_length=250)
    from_loc = models.CharField(max_length=100)
    to_loc = models.CharField(max_length=100)
    dept_from = models.IntegerField()
    fc_dept = models.CharField(max_length=250)
    analysis_levels_parts = models.IntegerField()
    fc_sts_dept_to = models.CharField(max_length=250)
    matcode_multi = models.CharField(max_length=250)
    rej_atta_name = models.CharField(max_length=500)
    vend_atta_name = models.CharField(max_length=500)
    fc_from_date = models.DateField()
    fc_route_date = models.DateField()
    route_value = models.IntegerField()
    route_value_sub = models.IntegerField()
    hod_sts = models.CharField(max_length=15)
    ca_time = models.CharField(max_length=100)
    rework_time = models.CharField(max_length=100)
    reason_delay = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    type = models.IntegerField()
    db_type = models.IntegerField()
    type_ref = models.IntegerField()
    masterslno = models.IntegerField()
    analysis_comp = models.IntegerField()
    war_period = models.CharField(max_length=100)
    master_slno = models.CharField(max_length=100)
    srap_status = models.IntegerField()
    delete1 = models.IntegerField()
    typeofprocess = models.IntegerField()
    latest_update = models.CharField(max_length=6, blank=True, null=True)
    nonwar = models.IntegerField()
    vendor = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parts_table'


class PartsTable11022022(models.Model):
    sno = models.AutoField(primary_key=True)
    reworkreportno = models.BigIntegerField()
    name = models.CharField(max_length=500, blank=True, null=True)
    testedby_multi = models.IntegerField()
    code = models.CharField(max_length=12, blank=True, null=True)
    legend = models.CharField(max_length=5000, blank=True, null=True)
    batchno = models.CharField(max_length=5000, blank=True, null=True)
    make = models.CharField(max_length=5000, blank=True, null=True)
    partretestedat = models.CharField(max_length=100, blank=True, null=True)
    rresults = models.CharField(max_length=1000)
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()
    sno_wise = models.IntegerField()
    consm_qty = models.IntegerField()
    rej_rew_qty = models.IntegerField()
    uom = models.CharField(max_length=10)
    reason = models.CharField(max_length=500)
    rej_rew_sts = models.IntegerField()
    rej_slip_no = models.IntegerField()
    part_no = models.CharField(max_length=50)
    kms = models.FloatField()
    days = models.FloatField()
    megaw_hours = models.FloatField(db_column='megaW_hours')  # Field name made lowercase.
    supplier = models.IntegerField()
    doc_no = models.IntegerField()
    date_igi = models.CharField(max_length=10)
    ntry_by_igi = models.IntegerField()
    fitem_code = models.BigIntegerField()
    fitem_slno = models.IntegerField()
    qty_rej_igi = models.IntegerField()
    igi_remarks = models.CharField(max_length=500)
    timestapm_igi = models.CharField(max_length=20)
    sts_igi = models.IntegerField()
    service_report_no = models.IntegerField()
    sts_slno_purchase = models.IntegerField()
    igi_completed_date = models.DateField()
    totappliofcom = models.IntegerField()
    totcomqty = models.IntegerField()
    acrappl = models.IntegerField()
    totfailure = models.IntegerField()
    ca = models.CharField(max_length=500)
    faildatethird = models.CharField(max_length=12)
    failapp = models.TextField()
    igisampling = models.TextField()
    tl = models.CharField(max_length=6)
    gl = models.CharField(max_length=6)
    compo_wa = models.CharField(max_length=50)
    fag_mail = models.CharField(max_length=250)
    vend_sent_date = models.CharField(max_length=250)
    from_loc = models.CharField(max_length=100)
    to_loc = models.CharField(max_length=100)
    dept_from = models.IntegerField()
    fc_dept = models.CharField(max_length=250)
    analysis_levels_parts = models.IntegerField()
    fc_sts_dept_to = models.CharField(max_length=250)
    matcode_multi = models.CharField(max_length=250)
    rej_atta_name = models.CharField(max_length=500)
    vend_atta_name = models.CharField(max_length=500)
    fc_from_date = models.DateField()
    fc_route_date = models.DateField()
    route_value = models.IntegerField()
    route_value_sub = models.IntegerField()
    hod_sts = models.CharField(max_length=15)
    ca_time = models.CharField(max_length=100)
    rework_time = models.CharField(max_length=100)
    reason_delay = models.TextField()
    remarks = models.TextField()
    type = models.IntegerField()
    db_type = models.IntegerField()
    type_ref = models.IntegerField()
    masterslno = models.IntegerField()
    analysis_comp = models.IntegerField()
    war_period = models.CharField(max_length=100)
    master_slno = models.CharField(max_length=100)
    srap_status = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'parts_table_11_02_2022'


class PartsTableIgiNtry(models.Model):
    service_report_no = models.IntegerField()
    sno = models.IntegerField()
    igi_remarks = models.CharField(max_length=1500)
    sts_slno = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'parts_table_igi_ntry'


class PartsTablePurchaseNtry(models.Model):
    service_report_no = models.IntegerField()
    sno = models.IntegerField()
    remarks = models.CharField(max_length=1500)
    sts_slno = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'parts_table_purchase_ntry'


class PartsTablePurchaseStsMaster(models.Model):
    sts_slno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'parts_table_purchase_sts_master'


class PcbAssemblyRework(models.Model):
    rework_reference_no = models.IntegerField(primary_key=True)
    sap_production_order_no = models.IntegerField(blank=True, null=True)
    material_code = models.CharField(max_length=20, blank=True, null=True)
    sub_assembly_name = models.CharField(max_length=100, blank=True, null=True)
    sub_assembly_verification_no = models.IntegerField()
    sub_assembly_serial_no = models.IntegerField(blank=True, null=True)
    problem_observe_date = models.DateField(blank=True, null=True)
    problem_oberserved_by = models.CharField(max_length=11, blank=True, null=True)
    problem_observed_stage = models.CharField(max_length=50, blank=True, null=True)
    problem_description = models.TextField(blank=True, null=True)
    root_cause = models.CharField(max_length=1000, blank=True, null=True)
    corr_action = models.CharField(max_length=1000, blank=True, null=True)
    rework_details = models.TextField(blank=True, null=True)
    failure_category = models.CharField(max_length=100, blank=True, null=True)
    problem_done_by = models.CharField(max_length=100, blank=True, null=True)
    rework_done_by = models.CharField(max_length=100, blank=True, null=True)
    rejection_slip_number = models.CharField(max_length=11, blank=True, null=True)
    createdby = models.CharField(max_length=100, blank=True, null=True)
    finalsave = models.CharField(max_length=5, blank=True, null=True)
    timestamp = models.DateTimeField()
    entry_type = models.CharField(max_length=11, blank=True, null=True)
    mount_type = models.IntegerField()
    rew_det2 = models.IntegerField(blank=True, null=True)
    uniq_slno = models.IntegerField()
    qty = models.IntegerField()
    rootcause = models.TextField(blank=True, null=True)
    correctiveactca = models.TextField(blank=True, null=True)
    preventiveactca = models.TextField(blank=True, null=True)
    empcode = models.CharField(max_length=11, blank=True, null=True)
    nc_takenup = models.TextField(blank=True, null=True)
    mis_proof = models.TextField(blank=True, null=True)
    sop_prep = models.TextField(blank=True, null=True)
    doc_update = models.TextField(blank=True, null=True)
    qcc_taken = models.TextField(blank=True, null=True)
    stray_case = models.TextField(blank=True, null=True)
    inspection_by = models.IntegerField()
    delete1 = models.IntegerField()
    comp_solder = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcb_assembly_rework'


class PcbBatchMulti(models.Model):
    slno = models.IntegerField()
    order = models.IntegerField()
    desc = models.CharField(max_length=50)
    from_field = models.IntegerField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pcb_batch_multi'



class PcbMachineManualNtry(models.Model):
    slno = models.AutoField(primary_key=True)
    project = models.CharField(max_length=20, blank=True, null=True)
    material_number = models.CharField(max_length=12, blank=True, null=True)
    machine = models.CharField(max_length=300, blank=True, null=True)
    manual = models.CharField(max_length=300, blank=True, null=True)
    change_done = models.CharField(max_length=50, blank=True, null=True)
    change_date = models.CharField(max_length=10, blank=True, null=True)
    created = models.IntegerField()
    ntry_date = models.DateField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    deleted_by = models.IntegerField()
    delete_date = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcb_machine_manual_ntry'


class PcbMatSlipsTemp(models.Model):
    desc = models.CharField(max_length=100, blank=True, null=True)
    ref_name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=11, blank=True, null=True)
    pcb_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcb_mat_slips_temp'


class PcbMountMstr(models.Model):
    slno = models.AutoField(primary_key=True)
    mount_name = models.CharField(max_length=50)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pcb_mount_mstr'


class PcbObsPrRew(models.Model):
    emp_code = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=50)
    createdby = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pcb_obs_pr_rew'


class PcbPartqtyNtry(models.Model):
    slno = models.IntegerField(primary_key=True)
    project = models.CharField(max_length=250)
    material_number = models.CharField(max_length=25)
    mat_code = models.CharField(max_length=25)
    machine = models.IntegerField()
    qty_per = models.IntegerField()
    req_ma_qty = models.IntegerField()
    mc_qty = models.IntegerField()
    batch_qty = models.IntegerField()
    sap_qty = models.IntegerField()
    createdby = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pcb_partqty_ntry'


class PcbProdLogNtry(models.Model):
    slno = models.IntegerField()
    date = models.DateField()
    prevent_main_from_hr = models.CharField(max_length=10)
    prevent_main_to_hr = models.CharField(max_length=10)
    prevent_main_tot = models.CharField(max_length=10)
    po = models.CharField(max_length=50, blank=True, null=True)
    mat = models.CharField(max_length=15, blank=True, null=True)
    batch_qty = models.IntegerField()
    fromwaitingtime = models.CharField(db_column='fromWaitingTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    towaitingtime = models.CharField(db_column='toWaitingTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    waiting_time_tot = models.CharField(max_length=10, blank=True, null=True)
    from_change_over_time = models.CharField(max_length=10)
    to_change_over_time = models.CharField(max_length=10)
    change_over_time_tot = models.CharField(max_length=10)
    from_board_insp_time = models.CharField(max_length=10)
    to_board_insp_time = models.CharField(max_length=10)
    board_insp_time_tot = models.CharField(max_length=10)
    fb_insp_done_by = models.CharField(max_length=30, blank=True, null=True)
    from_prd_time = models.CharField(max_length=10)
    to_prd_time = models.CharField(max_length=10)
    prd_time_tot = models.CharField(max_length=10)
    produced_qty = models.CharField(max_length=10, blank=True, null=True)
    comps_per_board = models.IntegerField()
    tot_comps_per_lot = models.IntegerField()
    noof_verties_per_card = models.IntegerField()
    from_break_down_time = models.CharField(max_length=10)
    to_break_down_time = models.CharField(max_length=10)
    break_down_tot = models.CharField(max_length=10)
    from_programming_time = models.CharField(max_length=10)
    to_programming_time = models.CharField(max_length=10)
    programming_tot = models.CharField(max_length=10)
    rmrks = models.CharField(max_length=300, blank=True, null=True)
    operator = models.CharField(max_length=30, blank=True, null=True)
    machine_name = models.IntegerField()
    customer = models.CharField(max_length=10, blank=True, null=True)
    model_no = models.CharField(max_length=15, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    uniq_slno = models.AutoField(primary_key=True)
    subassname_rnd = models.CharField(max_length=200, blank=True, null=True)
    cycletime = models.CharField(max_length=11)
    noofgoodboards = models.CharField(max_length=11)
    type = models.CharField(max_length=50, blank=True, null=True)
    defect_det = models.CharField(max_length=150, blank=True, null=True)
    jig = models.CharField(max_length=2, blank=True, null=True)
    tl_coms = models.TextField(blank=True, null=True)
    action = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField()
    coat_axis = models.CharField(max_length=40, blank=True, null=True)
    hei = models.CharField(max_length=40, blank=True, null=True)
    card_slno = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcb_prod_log_ntry'


class PcbProdMachineMaster(models.Model):
    slno = models.AutoField(primary_key=True)
    machine_name = models.CharField(max_length=50, blank=True, null=True)
    model_no = models.CharField(max_length=20, blank=True, null=True)
    machine_hours = models.CharField(max_length=250, blank=True, null=True)
    category = models.CharField(max_length=10, blank=True, null=True)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pcb_prod_machine_master'


class PcbRewDetailsMaster(models.Model):
    slno = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'pcb_rew_details_master'


class PcnCatMaster(models.Model):
    slno = models.AutoField(primary_key=True)
    cat = models.IntegerField()
    change_cat = models.CharField(max_length=100, blank=True, null=True)
    reasonofchange = models.CharField(max_length=100, blank=True, null=True)
    typeofchange = models.CharField(max_length=100, blank=True, null=True)
    conclusionbyme = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcn_cat_master'


class PeriodMaster(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    year = models.IntegerField()
    type = models.CharField(max_length=2)
    coments = models.CharField(max_length=50)
    active_status = models.IntegerField()
    aprsl_start_date = models.DateField()
    aprsl_end_date = models.DateField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'period_master'


class PfData(models.Model):
    empcode = models.IntegerField(primary_key=True)
    uan = models.IntegerField()
    aadhar = models.CharField(max_length=100)
    name = models.CharField(max_length=500)
    dob = models.DateField()
    aadhar_sts = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pf_data'


class PhotoMaster(models.Model):
    empcode = models.IntegerField()
    photo = models.TextField()
    ext = models.CharField(max_length=10)
    createdby = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'photo_master'


class Pix(models.Model):
    pid = models.AutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    imgdata = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pix'


class PlanningDetails(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    empcode = models.CharField(max_length=6, blank=True, null=True)
    ntry_date = models.DateField()
    ntry_time = models.CharField(max_length=10, blank=True, null=True)
    status = models.IntegerField()
    ucpcomm = models.CharField(max_length=500, blank=True, null=True)
    ucp_date = models.DateField()
    hod = models.CharField(max_length=6, blank=True, null=True)
    planning_att = models.CharField(max_length=200, blank=True, null=True)
    admin_plng_att = models.CharField(max_length=200, blank=True, null=True)
    usr_ucp_rmks = models.CharField(max_length=500, blank=True, null=True)
    usr_ucp_date = models.DateField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'planning_details'


class PlanningHistory(models.Model):
    slno = models.IntegerField()
    uniq_slno = models.IntegerField()
    status = models.IntegerField()
    plan_remrks = models.TextField(blank=True, null=True)
    createdby = models.CharField(max_length=6, blank=True, null=True)
    planning_att = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'planning_history'


class PlanningStsMaster(models.Model):
    mid = models.AutoField(primary_key=True)
    status = models.CharField(max_length=30)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'planning_sts_master'


class PlanningSubDetails(models.Model):
    slno = models.AutoField(primary_key=True)
    uniq_slno = models.IntegerField()
    material = models.CharField(max_length=15)
    po = models.TextField(blank=True, null=True)
    uom = models.IntegerField()
    qty = models.IntegerField()
    targetdate = models.DateField()
    project = models.CharField(max_length=20, blank=True, null=True)
    usr_resn = models.TextField(blank=True, null=True)
    priority = models.IntegerField()
    status = models.IntegerField()
    hod_aprl_sts = models.IntegerField()
    hod_date = models.DateField()
    hod_time = models.CharField(max_length=9, blank=True, null=True)
    hod_resn = models.CharField(max_length=100, blank=True, null=True)
    prsno = models.CharField(max_length=25, blank=True, null=True)
    delivery_date = models.DateField()
    indented_date = models.DateField()
    indentedby = models.CharField(max_length=6, blank=True, null=True)
    plan_remrks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'planning_sub_details'


class PoApprovalMaster(models.Model):
    app_id = models.AutoField(primary_key=True)
    plant = models.IntegerField()
    pgroup = models.CharField(max_length=5)
    doctype = models.CharField(max_length=25)
    groupid = models.IntegerField()
    sequence = models.IntegerField()
    description = models.CharField(max_length=20)
    groupmam = models.CharField(max_length=10)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'po_approval_master'


class PoCommentsMaster(models.Model):
    mas_id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=100)
    com_type = models.CharField(max_length=2)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'po_comments_master'


class PoDocMaster(models.Model):
    docid = models.AutoField(primary_key=True)
    doctype = models.CharField(max_length=10, blank=True, null=True)
    docdesc = models.CharField(max_length=150)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'po_doc_master'


class PoGroupMaster(models.Model):
    gid = models.AutoField(primary_key=True)
    gtype = models.CharField(max_length=10)
    plant = models.IntegerField()
    gassociate = models.CharField(max_length=10)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'po_group_master'


class PoHistory(models.Model):
    hid = models.AutoField(primary_key=True)
    sid = models.IntegerField()
    empcode = models.IntegerField()
    comments = models.CharField(max_length=400, blank=True, null=True)
    status = models.CharField(max_length=30)
    type = models.CharField(max_length=70, blank=True, null=True)
    ntry_date_time = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'po_history'


class PoHistory1(models.Model):
    hid = models.AutoField(primary_key=True)
    sid = models.IntegerField()
    empcode = models.IntegerField()
    comments = models.CharField(max_length=400, blank=True, null=True)
    status = models.CharField(max_length=30)
    type = models.CharField(max_length=70, blank=True, null=True)
    ntry_date_time = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'po_history1'


class PoNotReg(models.Model):
    pono = models.CharField(max_length=10)
    move_to_sap = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'po_not_reg'


class PoReleaseMaster(models.Model):
    masid = models.AutoField(primary_key=True)
    plant = models.IntegerField()
    pgroup = models.CharField(max_length=5)
    doctype = models.CharField(max_length=10)
    amtfrom = models.IntegerField()
    amtto = models.IntegerField()
    mis_value = models.IntegerField()
    groupid = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'po_release_master'


class PoSapApp(models.Model):
    app_id = models.AutoField(primary_key=True)
    sid = models.IntegerField()
    seq = models.IntegerField()
    approvalat = models.CharField(max_length=6)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'po_sap_app'


class PoSapAtt(models.Model):
    attach_id = models.AutoField(primary_key=True)
    pono = models.CharField(max_length=10, blank=True, null=True)
    poitem = models.CharField(max_length=10, blank=True, null=True)
    serialno = models.IntegerField()
    filename = models.CharField(max_length=200, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'po_sap_att'


class PoSapData(models.Model):
    sid = models.AutoField(primary_key=True)
    plant = models.IntegerField()
    pono = models.CharField(max_length=10, blank=True, null=True)
    poitem = models.CharField(max_length=8, blank=True, null=True)
    podate = models.DateField(blank=True, null=True)
    vendor = models.CharField(max_length=35, db_collation='utf8_general_ci', blank=True, null=True)
    povalue = models.CharField(max_length=13, blank=True, null=True)
    pogroup = models.CharField(max_length=3, blank=True, null=True)
    project = models.CharField(max_length=10, blank=True, null=True)
    doctype = models.CharField(max_length=10, blank=True, null=True)
    prs_req = models.CharField(max_length=6, blank=True, null=True)
    prs_doc_type = models.CharField(max_length=10, blank=True, null=True)
    level_ini = models.CharField(max_length=2)
    mis_po_ini = models.CharField(max_length=2)
    version = models.IntegerField()
    emp_user = models.CharField(max_length=10, blank=True, null=True)
    doc_pro = models.IntegerField()
    ir_status = models.IntegerField()
    committee = models.CharField(max_length=100, blank=True, null=True)
    sap_status = models.IntegerField()
    groupid = models.IntegerField()
    approvalat = models.CharField(max_length=6, blank=True, null=True)
    approvalsts = models.IntegerField()
    pregroupid = models.IntegerField()
    revert = models.IntegerField()
    ntry_date = models.DateField(blank=True, null=True)
    move_to_sap = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'po_sap_data'


class PoSapData1(models.Model):
    sid = models.AutoField(primary_key=True)
    plant = models.IntegerField()
    pono = models.CharField(max_length=10, blank=True, null=True)
    poitem = models.CharField(max_length=8, blank=True, null=True)
    podate = models.DateField(blank=True, null=True)
    vendor = models.CharField(max_length=35, db_collation='utf8_general_ci', blank=True, null=True)
    povalue = models.CharField(max_length=13, blank=True, null=True)
    pogroup = models.CharField(max_length=3, blank=True, null=True)
    project = models.CharField(max_length=10, blank=True, null=True)
    doctype = models.CharField(max_length=10, blank=True, null=True)
    prs_req = models.CharField(max_length=6, blank=True, null=True)
    prs_doc_type = models.CharField(max_length=10, blank=True, null=True)
    level_ini = models.CharField(max_length=2)
    mis_po_ini = models.CharField(max_length=2)
    version = models.IntegerField()
    emp_user = models.CharField(max_length=10, blank=True, null=True)
    doc_pro = models.IntegerField()
    ir_status = models.IntegerField()
    committee = models.CharField(max_length=100, blank=True, null=True)
    sap_status = models.IntegerField()
    groupid = models.IntegerField()
    approvalat = models.CharField(max_length=6, blank=True, null=True)
    approvalsts = models.IntegerField()
    pregroupid = models.IntegerField()
    revert = models.IntegerField()
    ntry_date = models.DateField(blank=True, null=True)
    move_to_sap = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'po_sap_data1'


class PointkssImprovementMaster(models.Model):
    sgtn_qntfcn_no = models.AutoField(primary_key=True)
    sgtn_qntfcn_name = models.CharField(max_length=100)
    sgtn_qntfcn_nick_name = models.CharField(max_length=1)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pointkss_improvement_master'


class PointkssNtry(models.Model):
    slno = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    dept = models.IntegerField()
    ntry_date = models.DateField()
    kss_them = models.TextField(blank=True, null=True)
    benifits = models.TextField(blank=True, null=True)
    intan_benefits = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    sugg_improvement = models.TextField(blank=True, null=True)
    counter_measures = models.TextField(blank=True, null=True)
    horizental_deployement = models.CharField(max_length=2, blank=True, null=True)
    horiz_dep_sts = models.CharField(max_length=1, blank=True, null=True)
    horiz_dep_details = models.TextField(blank=True, null=True)
    kss_dept_slno = models.IntegerField()
    loc = models.CharField(max_length=50, blank=True, null=True)
    prjct = models.CharField(max_length=50, blank=True, null=True)
    qnt = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.IntegerField()
    created_dept = models.IntegerField()
    horiz_deploy = models.CharField(max_length=250, blank=True, null=True)
    impl_date = models.DateField(blank=True, null=True)
    timestampp = models.DateTimeField()
    project_any = models.CharField(max_length=300, blank=True, null=True)
    amount = models.IntegerField()
    reward_amount = models.IntegerField()
    kss_amt = models.IntegerField()
    attachment = models.CharField(max_length=200, blank=True, null=True)
    rm = models.IntegerField()
    under_rm = models.IntegerField()
    rm_sts = models.IntegerField()
    rm_comments = models.CharField(max_length=500, blank=True, null=True)
    rm_impl_resp = models.CharField(max_length=3, blank=True, null=True)
    rm_ntry_date = models.DateField(blank=True, null=True)
    rm_target_date = models.DateField(blank=True, null=True)
    rm_impl_details = models.TextField(blank=True, null=True)
    rm_impl_sts = models.CharField(max_length=8, blank=True, null=True)
    hod = models.IntegerField()
    under_hod = models.IntegerField()
    hod_sts = models.IntegerField()
    hod_comments = models.TextField(blank=True, null=True)
    hod_impl_resp = models.CharField(max_length=15, blank=True, null=True)
    hod_ntry_date = models.DateField(blank=True, null=True)
    hod_target_date = models.DateField(blank=True, null=True)
    hod_impl_details = models.TextField(blank=True, null=True)
    hod_impl_sts = models.CharField(max_length=8, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    hod_level_no = models.CharField(max_length=2, blank=True, null=True)
    under_lpo = models.IntegerField(blank=True, null=True)
    lpo_sts = models.IntegerField(blank=True, null=True)
    lpo_impl_resp = models.CharField(max_length=15, blank=True, null=True)
    lpo_impl_sts = models.CharField(max_length=10, blank=True, null=True)
    lpo_comments = models.TextField(blank=True, null=True)
    impl_details = models.TextField(blank=True, null=True)
    level_no = models.CharField(max_length=2, blank=True, null=True)
    status = models.IntegerField()
    lpo_ntry_by = models.IntegerField()
    lpo_ntry_date = models.DateField(blank=True, null=True)
    lpo_target_date = models.DateField(blank=True, null=True)
    lpo_kaizen_type = models.CharField(max_length=10, blank=True, null=True)
    project_type = models.CharField(max_length=20, blank=True, null=True)
    rnddept = models.IntegerField()
    rndhod = models.IntegerField(db_column='rndHod')  # Field name made lowercase.
    delgtd_hod_commnts = models.TextField()
    assnd_to = models.IntegerField()
    otherdept_sts = models.IntegerField()
    impdetail = models.TextField(blank=True, null=True)
    impstatus = models.IntegerField(blank=True, null=True)
    hod_finalntry_date = models.DateField(blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pointkss_ntry'


class Post(models.Model):
    post_title = models.TextField(blank=True, null=True)
    post_description = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'


class PostingMtrlMaster(models.Model):
    mat_code = models.CharField(max_length=12)
    pstng_date = models.DateField()
    qty = models.IntegerField()
    mvmnt = models.CharField(max_length=20)
    from_field = models.CharField(db_column='from', max_length=10)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=10)
    up_sts = models.IntegerField()
    timestamp = models.DateTimeField()
    temp = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'posting_mtrl_master'


class PrinterAgreeNtry(models.Model):
    printer_id = models.IntegerField()
    sequence_no = models.IntegerField(primary_key=True)
    agree_no = models.IntegerField(db_column='Agree_no')  # Field name made lowercase.
    valid_from = models.DateField()
    valid_to = models.DateField()
    invoice_no = models.CharField(max_length=150)
    invoice_date = models.DateField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'printer_agree_ntry'


class PrinterAgreePageNtry(models.Model):
    printer_id = models.IntegerField()
    sequence_no = models.IntegerField()
    subsequence_no = models.AutoField(primary_key=True)
    size = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    cost = models.FloatField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'printer_agree_page_ntry'


class PrinterInvoice(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    invoice_no = models.CharField(max_length=50)
    invoice_date = models.DateField()
    printer_id = models.IntegerField()
    agree_no = models.CharField(db_column='Agree_no', max_length=150)  # Field name made lowercase.
    from_field = models.DateField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.DateField()
    cost = models.FloatField()
    vat = models.FloatField()
    tax = models.FloatField()
    net_amount = models.FloatField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'printer_invoice'


class PrinterInvoiceSub(models.Model):
    sub_sequence_no = models.AutoField(primary_key=True)
    sequence_no = models.IntegerField()
    printer_id = models.IntegerField()
    page_size = models.CharField(max_length=150)
    print_type = models.CharField(max_length=150)
    page_cost = models.FloatField()
    prev_reading = models.FloatField()
    to_reading = models.FloatField()
    total_reading = models.FloatField()
    sub_total_cost = models.FloatField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'printer_invoice_sub'


class PrinterMakeMaster(models.Model):
    manufacture_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'printer_make_master'


class PrinterModelMaster(models.Model):
    model_id = models.AutoField(primary_key=True)
    model_name = models.CharField(max_length=50)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'printer_model_master'


class PrinterNtry(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    asset_slno = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    manufacture_id = models.IntegerField()
    printer_slno = models.IntegerField()
    type_id = models.IntegerField()
    model_id = models.IntegerField()
    loccode = models.CharField(max_length=50)
    deptcode = models.IntegerField()
    floor = models.IntegerField()
    instalation_date = models.DateField()
    pono = models.CharField(max_length=50)
    invoice_no = models.CharField(max_length=50)
    cost = models.FloatField()
    used_depts = models.CharField(max_length=250)
    net_read = models.IntegerField()
    life_time_copies = models.IntegerField()
    printer_life_time = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'printer_ntry'


class PrinterProblem(models.Model):
    request_no = models.AutoField(primary_key=True)
    printer_id = models.IntegerField()
    prob_desc = models.CharField(max_length=2000)
    complaint_no = models.CharField(max_length=20)
    complaint_by = models.IntegerField()
    complete_down = models.CharField(max_length=20)
    complaint_date = models.DateField()
    eng_name = models.CharField(max_length=20)
    contact_no = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    follow_by = models.IntegerField()
    status = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'printer_problem'


class PrinterStatusMaster(models.Model):
    status = models.SmallAutoField(primary_key=True)
    status_name = models.CharField(max_length=30)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField(blank=True, null=True)
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'printer_status_master'


class PrinterTrackHistory(models.Model):
    slno = models.IntegerField()
    desc = models.TextField()
    date = models.DateField()
    status = models.IntegerField()
    vendor_response = models.TextField()
    follow_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'printer_track_history'


class PrinterTypeMaster(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'printer_type_master'


class Priority(models.Model):
    pr_no = models.AutoField(primary_key=True)
    prty_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'priority'


class ProblemCategoryMaster(models.Model):
    problem_name = models.CharField(max_length=40, blank=True, null=True)
    problem_category = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.BigIntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'problem_category_master'


class ProblemObservedStage(models.Model):
    pono = models.AutoField(primary_key=True)
    po_name = models.CharField(max_length=50)
    createdby = models.SmallIntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'problem_observed_stage'


class ProductEngineer(models.Model):
    product_code = models.CharField(max_length=30, blank=True, null=True)
    product_name = models.CharField(max_length=200, blank=True, null=True)
    product_incharge = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_engineer'


class ProductMaster(models.Model):
    productcode = models.CharField(max_length=40, blank=True, null=True)
    shorttext = models.CharField(max_length=300, blank=True, null=True)
    uom = models.CharField(max_length=10, blank=True, null=True)
    ext_upload_sts = models.IntegerField()
    intra_upload_sts = models.IntegerField()
    createdby = models.CharField(max_length=10, blank=True, null=True)
    internet_up_sts = models.IntegerField()
    timestamp = models.DateTimeField()
    resp = models.CharField(max_length=1, blank=True, null=True)
    revno = models.IntegerField()
    delete1 = models.IntegerField()
    intra_upload_date = models.DateTimeField()
    block_sts = models.IntegerField()
    block_by = models.IntegerField()
    block_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'product_master'


class ProductMasterTemp(models.Model):
    productcode = models.CharField(max_length=40, blank=True, null=True)
    shorttext = models.CharField(max_length=300, blank=True, null=True)
    uom = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_master_temp'


class ProductMasterUom(models.Model):
    mat = models.CharField(max_length=25)
    uom = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'product_master_uom'


class ProductModInMaster(models.Model):
    modif_in = models.AutoField(primary_key=True)
    modif_name = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_mod_in_master'


class ProductModInchargeMaster(models.Model):
    incharge_code = models.IntegerField(primary_key=True)
    incharge_name = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_mod_incharge_master'


class ProductModNtry(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    mod_no = models.CharField(max_length=20)
    mod_incharge = models.IntegerField()
    ntry_date = models.DateField()
    ref_doc = models.CharField(max_length=500)
    attachment_name = models.CharField(max_length=50)
    mod_in = models.IntegerField()
    mod_type = models.IntegerField()
    project = models.IntegerField()
    sub_ass = models.CharField(max_length=11)
    sub_unit = models.CharField(max_length=11)
    unit = models.CharField(max_length=11)
    sa_mod_id = models.IntegerField()
    su_mod_id = models.IntegerField()
    unit_mod_id = models.IntegerField()
    change_details = models.CharField(max_length=500)
    change_reason = models.CharField(max_length=500)
    change_scope = models.CharField(max_length=10)
    priority = models.IntegerField()
    prod_incharge_remarks = models.CharField(max_length=500)
    role_details = models.CharField(max_length=500)
    ntry_by = models.IntegerField()
    ntry_sts = models.IntegerField()
    sa_slno_eff_from = models.IntegerField()
    mod_eff_from_date = models.DateField()
    testing_remarks = models.CharField(max_length=250)
    testing_sts = models.IntegerField()
    testing_ntry_by = models.IntegerField()
    sa_slno_ass_pe = models.IntegerField()
    unit_slno_ass_pe = models.IntegerField()
    ass_pe_remarks = models.CharField(max_length=250)
    ass_pe_ntry_by = models.IntegerField()
    ass_pe_date = models.DateField()
    ass_pe_sts = models.IntegerField()
    srvc_ntry_by = models.IntegerField()
    srvc_ntry_date = models.DateField()
    srvc_from = models.IntegerField()
    srvc_to = models.IntegerField()
    srvc_tot_rows = models.IntegerField()
    srvc_tot_cmpltd_rows = models.IntegerField()
    srvc_sts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_mod_ntry'


class ProductModRemarksNtry(models.Model):
    uniq_slno = models.IntegerField()
    seq_slno = models.IntegerField()
    slno = models.IntegerField()
    matnr = models.CharField(max_length=11)
    remarks = models.CharField(max_length=400)
    date = models.DateField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_mod_remarks_ntry'


class ProductModSrvcSlnosNtry(models.Model):
    uniq_slno = models.IntegerField()
    slno = models.IntegerField()
    sts = models.IntegerField()
    ntry_by = models.IntegerField()
    ntry_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'product_mod_srvc_slnos_ntry'


class ProductModTypeMaster(models.Model):
    modif_type = models.AutoField(primary_key=True)
    modif_type_name = models.CharField(max_length=50)
    mod_type_short_name = models.CharField(max_length=3)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_mod_type_master'


class ProductPriorityMaster(models.Model):
    priority_no = models.AutoField(primary_key=True)
    priority_name = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_priority_master'


class ProductProjectMaster(models.Model):
    project = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    noofmonths = models.IntegerField()
    project_no = models.AutoField(primary_key=True)
    ecm_sts = models.CharField(max_length=10)
    srvc_sts = models.CharField(max_length=1)
    createdby = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_project_master'


class ProductionOrder(models.Model):
    order_no = models.BigIntegerField()
    order_item_no = models.BigIntegerField()
    order_date = models.DateField()
    material_code = models.CharField(max_length=15)
    qty = models.FloatField()
    uom = models.CharField(max_length=3)
    sl_no = models.CharField(max_length=20)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'production_order'


class ProductsOpportunityMaster(models.Model):
    matnr = models.CharField(max_length=15)
    opportunities = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'products_opportunity_master'


class ProjectMaster(models.Model):
    project_no = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    project_fname = models.CharField(max_length=10)
    project_lname = models.CharField(max_length=10)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    delete_date = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'project_master'


class Projects(models.Model):
    project = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    project_no = models.AutoField(primary_key=True)
    child = models.IntegerField()
    subchild = models.IntegerField()
    main_id = models.IntegerField()
    parenthistory = models.CharField(max_length=1, blank=True, null=True)
    link = models.CharField(max_length=5, blank=True, null=True)
    ecm_sts = models.CharField(max_length=5, blank=True, null=True)
    spec_no = models.CharField(max_length=500, blank=True, null=True)
    createdby = models.CharField(max_length=10, blank=True, null=True)
    project_ic = models.CharField(max_length=150, blank=True, null=True)
    project_ic_second = models.CharField(max_length=150, blank=True, null=True)
    service_proj_mail = models.CharField(max_length=200, blank=True, null=True)
    cc_mail = models.CharField(max_length=50, blank=True, null=True)
    occurence = models.IntegerField()
    intra_upload_sts = models.IntegerField()
    spcial_cat = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'projects'


class ProjectsOld(models.Model):
    project = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    project_no = models.AutoField(primary_key=True)
    child = models.IntegerField()
    subchild = models.IntegerField()
    main_id = models.IntegerField()
    parenthistory = models.CharField(max_length=1, blank=True, null=True)
    link = models.CharField(max_length=5, blank=True, null=True)
    ecm_sts = models.CharField(max_length=5, blank=True, null=True)
    spec_no = models.CharField(max_length=500, blank=True, null=True)
    createdby = models.CharField(max_length=10, blank=True, null=True)
    project_ic = models.CharField(max_length=150, blank=True, null=True)
    project_ic_second = models.CharField(max_length=150, blank=True, null=True)
    service_proj_mail = models.CharField(max_length=200, blank=True, null=True)
    cc_mail = models.CharField(max_length=50, blank=True, null=True)
    occurence = models.IntegerField()
    intra_upload_sts = models.IntegerField()
    spcial_cat = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'projects_old'


class ProjectsPrev(models.Model):
    project = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    project_no = models.AutoField(primary_key=True)
    child = models.IntegerField()
    subchild = models.IntegerField()
    ecm_sts = models.CharField(max_length=5)
    spec_no = models.CharField(max_length=500)
    createdby = models.CharField(max_length=10, blank=True, null=True)
    project_ic = models.CharField(max_length=150)
    project_ic_second = models.CharField(max_length=150)
    service_proj_mail = models.CharField(max_length=200)
    cc_mail = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'projects_prev'


class PrsHistory(models.Model):
    prs_history_id = models.AutoField(primary_key=True)
    prs_ackno = models.IntegerField()
    prs_status = models.CharField(max_length=2, blank=True, null=True)
    prs_associate = models.CharField(max_length=7, blank=True, null=True)
    prs_comment = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'prs_history'


class PrsItems(models.Model):
    prs_item_id = models.AutoField(primary_key=True)
    prs_ack = models.IntegerField()
    prs_pcode = models.CharField(max_length=15, blank=True, null=True)
    prs_qty = models.IntegerField()
    prs_make = models.CharField(max_length=50, blank=True, null=True)
    prs_cost = models.FloatField()
    prs_cmt = models.CharField(max_length=200, blank=True, null=True)
    prs_category = models.IntegerField()
    prs_rdate = models.DateField()
    prs_dsheet = models.CharField(max_length=100, blank=True, null=True)
    prs_esheet = models.CharField(max_length=100, blank=True, null=True)
    prs_itemc_child = models.CharField(max_length=3, blank=True, null=True)
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    prsno = models.CharField(max_length=15, blank=True, null=True)
    po_date = models.DateField()
    prsstatus = models.CharField(max_length=50, blank=True, null=True)
    exp_date = models.DateField()
    prs_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prs_items'


class PrsItems1(models.Model):
    prs_item_id = models.AutoField(primary_key=True)
    prs_ack = models.IntegerField()
    prs_pcode = models.CharField(max_length=15, blank=True, null=True)
    prs_qty = models.IntegerField()
    prs_make = models.CharField(max_length=50, blank=True, null=True)
    prs_cost = models.FloatField()
    prs_cmt = models.CharField(max_length=200, blank=True, null=True)
    prs_category = models.IntegerField()
    prs_rdate = models.DateField()
    prs_dsheet = models.CharField(max_length=100, blank=True, null=True)
    prs_esheet = models.CharField(max_length=100, blank=True, null=True)
    prs_itemc_child = models.CharField(max_length=3, blank=True, null=True)
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    prsno = models.CharField(max_length=15, blank=True, null=True)
    po_date = models.DateField()
    prsstatus = models.CharField(max_length=50, blank=True, null=True)
    exp_date = models.DateField()
    prs_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prs_items1'


class PrsItemsMaterial(models.Model):
    prs_item_id = models.AutoField(primary_key=True)
    materiallocation = models.CharField(max_length=150, blank=True, null=True)
    prs_ack = models.IntegerField()
    prs_pcode = models.CharField(max_length=15, blank=True, null=True)
    prs_qty = models.IntegerField()
    prs_make = models.CharField(max_length=50, blank=True, null=True)
    prs_cost = models.FloatField()
    prs_cmt = models.CharField(max_length=200, blank=True, null=True)
    prs_category = models.IntegerField()
    prs_rdate = models.DateField()
    prs_dsheet = models.CharField(max_length=100, blank=True, null=True)
    prs_esheet = models.CharField(max_length=100, blank=True, null=True)
    prs_itemc_child = models.CharField(max_length=3, blank=True, null=True)
    prs_status = models.IntegerField()
    stack1200 = models.CharField(max_length=100, blank=True, null=True)
    shortage = models.CharField(max_length=100, blank=True, null=True)
    doc_no = models.CharField(max_length=100, blank=True, null=True)
    exp_date = models.DateField()
    target_date = models.CharField(max_length=100, blank=True, null=True)
    review = models.IntegerField()
    location = models.CharField(max_length=50, blank=True, null=True)
    mrs_no = models.CharField(max_length=100, blank=True, null=True)
    mrs_sendto = models.CharField(max_length=500, blank=True, null=True)
    bom_no = models.CharField(max_length=100, blank=True, null=True)
    review_remarks = models.CharField(max_length=100, blank=True, null=True)
    prs_sub_id = models.IntegerField()
    status = models.IntegerField()
    further_act = models.TextField(blank=True, null=True)
    further_act_sts = models.IntegerField()
    plng_status = models.IntegerField()
    plang_remarks = models.TextField(blank=True, null=True)
    stores_status = models.IntegerField()
    stores_remarks = models.TextField(blank=True, null=True)
    priority = models.IntegerField()
    prs_delete = models.IntegerField()
    delete1 = models.IntegerField()
    mrs_num = models.CharField(max_length=150, blank=True, null=True)
    dispatchlocation = models.CharField(max_length=150, blank=True, null=True)
    gateno = models.IntegerField()
    nremarks = models.IntegerField()
    pquantity = models.IntegerField()
    issueddate = models.DateField()
    restatus = models.IntegerField()
    timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'prs_items_material'


class PrsMain(models.Model):
    prs_ackno = models.AutoField(primary_key=True)
    prs_no_sap = models.CharField(max_length=20, blank=True, null=True)
    prs_project = models.IntegerField()
    prs_itemc = models.CharField(max_length=5, blank=True, null=True)
    prs_doc_type = models.CharField(max_length=5, blank=True, null=True)
    reviewtype = models.IntegerField()
    bomcode = models.CharField(max_length=50, blank=True, null=True)
    prs_createdby = models.CharField(max_length=8, blank=True, null=True)
    prs_dept = models.CharField(max_length=4, blank=True, null=True)
    prs_verify = models.CharField(max_length=8, blank=True, null=True)
    prs_approve = models.CharField(max_length=8, blank=True, null=True)
    prs_status = models.CharField(max_length=1, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    lastupdate = models.DateTimeField()
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'prs_main'


class PrsMain1(models.Model):
    prs_ackno = models.AutoField(primary_key=True)
    prs_no_sap = models.CharField(max_length=20, blank=True, null=True)
    prs_project = models.IntegerField()
    prs_itemc = models.CharField(max_length=5, blank=True, null=True)
    prs_doc_type = models.CharField(max_length=5, blank=True, null=True)
    reviewtype = models.IntegerField()
    bomcode = models.CharField(max_length=50, blank=True, null=True)
    prs_createdby = models.CharField(max_length=8, blank=True, null=True)
    prs_dept = models.CharField(max_length=4, blank=True, null=True)
    prs_verify = models.CharField(max_length=8, blank=True, null=True)
    prs_approve = models.CharField(max_length=8, blank=True, null=True)
    prs_status = models.CharField(max_length=1, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    lastupdate = models.DateTimeField()
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'prs_main1'


class PrsMainMaterial(models.Model):
    prs_ackno = models.AutoField(primary_key=True)
    prs_no_sap = models.CharField(max_length=20, blank=True, null=True)
    prs_project = models.IntegerField()
    prs_itemc = models.CharField(max_length=2, blank=True, null=True)
    prs_doc_type = models.CharField(max_length=5, blank=True, null=True)
    reviewtype = models.IntegerField()
    prs_createdby = models.CharField(max_length=6, blank=True, null=True)
    loc = models.CharField(max_length=20, blank=True, null=True)
    prs_dept = models.CharField(max_length=4, blank=True, null=True)
    prs_verify = models.CharField(max_length=6, blank=True, null=True)
    prs_ed_approve = models.IntegerField()
    prs_approve = models.CharField(max_length=6, blank=True, null=True)
    prs_status = models.CharField(max_length=1, blank=True, null=True)
    timestamp = models.DateField()
    lastupdate = models.DateTimeField()
    delete1 = models.CharField(max_length=1)
    priyority = models.CharField(max_length=150, blank=True, null=True)
    materiallocation = models.CharField(max_length=150, blank=True, null=True)
    dession = models.CharField(max_length=150, blank=True, null=True)
    matreialtype = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prs_main_material'


class PrsMaterialHistry(models.Model):
    slno = models.AutoField(primary_key=True)
    prs_ackno = models.CharField(max_length=100, blank=True, null=True)
    prs_sub_id = models.IntegerField()
    itemcode = models.CharField(max_length=100, blank=True, null=True)
    review_status = models.IntegerField()
    review_remarks = models.TextField(blank=True, null=True)
    comman_remarks = models.TextField(blank=True, null=True)
    mrs_send = models.IntegerField()
    status = models.IntegerField()
    further_act = models.CharField(max_length=5000, blank=True, null=True)
    created_by = models.IntegerField()
    date = models.DateField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prs_material_histry'


class PrsRdStatus(models.Model):
    slno = models.IntegerField()
    desc = models.CharField(max_length=100)
    short_text = models.CharField(max_length=25)
    type = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prs_rd_status'


class Prsnew(models.Model):
    pid = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    ntrydate = models.DateField()
    req_type = models.IntegerField()
    project = models.IntegerField()
    partcode = models.CharField(max_length=20, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    make = models.CharField(max_length=50, blank=True, null=True)
    rmks = models.CharField(max_length=50, blank=True, null=True)
    req_date = models.DateField(blank=True, null=True)
    cost = models.IntegerField()
    est_file = models.CharField(max_length=50, blank=True, null=True)
    prs_no = models.CharField(max_length=15, blank=True, null=True)
    status = models.IntegerField()
    approver = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'prsnew'


class PrsnewHist(models.Model):
    hid = models.AutoField(primary_key=True)
    pid = models.IntegerField()
    associate = models.IntegerField()
    rmrks = models.CharField(max_length=50)
    status = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prsnew_hist'


class PunchOct2023(models.Model):
    pid = models.AutoField(db_column='PID', primary_key=True)  # Field name made lowercase.
    pernr = models.IntegerField(db_column='PERNR', blank=True, null=True)  # Field name made lowercase.
    ldate = models.CharField(db_column='LDATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ltime = models.CharField(db_column='LTIME', max_length=8, blank=True, null=True)  # Field name made lowercase.
    satza = models.CharField(db_column='SATZA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    origf = models.CharField(db_column='ORIGF', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dallf = models.CharField(db_column='DALLF', max_length=1, blank=True, null=True)  # Field name made lowercase.
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'punch_oct2023'


class PurchGrnIssueMaster(models.Model):
    uniq_slno = models.IntegerField()
    slno = models.IntegerField()
    po = models.BigIntegerField()
    mat_doc = models.BigIntegerField()
    matnr = models.BigIntegerField()
    qty = models.IntegerField()
    vendor = models.IntegerField()
    group = models.CharField(max_length=10)
    cost = models.FloatField()
    value = models.FloatField()
    upld_date = models.DateField()
    diff_qty = models.IntegerField()
    short_qty = models.IntegerField()
    igi_rmrks = models.CharField(max_length=300)
    sts = models.IntegerField()
    createdby = models.IntegerField()
    purch_rmrks = models.CharField(max_length=500)
    purch_ntry = models.IntegerField()
    purch_date = models.DateField()
    purch_up_sts = models.IntegerField()
    plng_sts = models.IntegerField()
    plng_ntry = models.IntegerField()
    plng_date = models.DateField()
    plng_up_sts = models.IntegerField()
    attachment_sts = models.CharField(max_length=1)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'purch_grn_issue_master'


class PurchGrnIssueRmrks(models.Model):
    uniq_slno = models.IntegerField()
    slno = models.IntegerField()
    rmrks = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'purch_grn_issue_rmrks'


class PurchGrnIssueTemp(models.Model):
    po = models.BigIntegerField()
    mat_doc = models.CharField(max_length=15)
    matnr = models.CharField(max_length=15)
    qty = models.IntegerField()
    vendor = models.IntegerField()
    group = models.CharField(max_length=10)
    cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'purch_grn_issue_temp'


class PurchGroupMaster(models.Model):
    group = models.CharField(max_length=10)
    group_code = models.IntegerField()
    partner = models.CharField(max_length=100)
    igi_to = models.CharField(max_length=150)
    igi_cc = models.CharField(max_length=150)
    purch_to = models.CharField(max_length=150)
    plng_to = models.CharField(max_length=150)
    indl_cc = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'purch_group_master'


class PurchStatusMaster(models.Model):
    sts_slno = models.AutoField(primary_key=True)
    sts_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'purch_status_master'


class PwdHintAns(models.Model):
    empcode = models.IntegerField()
    hintq = models.IntegerField()
    ans = models.CharField(max_length=150)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pwd_hint_ans'


class PwdHintMstr(models.Model):
    slno = models.AutoField(primary_key=True)
    hintq = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pwd_hint_mstr'


class QccDates(models.Model):
    regid = models.IntegerField()
    qcc_date1 = models.CharField(max_length=20)
    qcc_date2 = models.DateField()

    class Meta:
        managed = False
        db_table = 'qcc_dates'


class QccImprovements(models.Model):
    regid = models.IntegerField()
    problem = models.TextField(blank=True, null=True)
    routecause = models.TextField(blank=True, null=True)
    counter_measure = models.TextField(blank=True, null=True)
    type = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'qcc_improvements'


class QccPdfEntry(models.Model):
    regid = models.IntegerField()
    title_before = models.CharField(max_length=200)
    title_after = models.CharField(max_length=200)
    before_text = models.TextField()
    after_text = models.TextField()
    before_file = models.CharField(max_length=100)
    after_file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'qcc_pdf_entry'


class QccRegistration(models.Model):
    regid = models.AutoField(primary_key=True)
    regno = models.IntegerField()
    empcode = models.IntegerField()
    dept = models.IntegerField()
    loc = models.CharField(max_length=10)
    title = models.TextField(blank=True, null=True)
    improvement = models.TextField(blank=True, null=True)
    justification = models.TextField(blank=True, null=True)
    justification2 = models.TextField(blank=True, null=True)
    specify = models.TextField(blank=True, null=True)
    regdate = models.DateTimeField()
    startdate = models.DateField()
    targetdate = models.DateField()
    facilitator = models.IntegerField()
    coordinator = models.IntegerField()
    project_leader = models.IntegerField()
    dy_leader = models.IntegerField()
    teamsize = models.CharField(max_length=500)
    grade = models.CharField(max_length=20)
    delete1 = models.IntegerField()
    teammember3 = models.IntegerField()
    teammember4 = models.IntegerField()
    improvement_category = models.CharField(max_length=50)
    tool = models.IntegerField()
    benefits_achieved = models.TextField(blank=True, null=True)
    start_hr = models.CharField(max_length=10)
    start_min = models.CharField(max_length=10)
    end_hr = models.CharField(max_length=10)
    end_min = models.CharField(max_length=10)
    day = models.IntegerField()
    time = models.CharField(max_length=20)
    isapproved = models.IntegerField()
    project_approved = models.IntegerField()
    project_userid = models.IntegerField()
    project_date = models.CharField(max_length=20)
    project_closer = models.CharField(max_length=100)
    final_approved = models.IntegerField()
    final_userid = models.IntegerField()
    final_date = models.DateField()
    hodapproved = models.IntegerField()
    hod = models.IntegerField()
    hodappcode = models.IntegerField()
    final_closer = models.IntegerField()
    filename = models.CharField(max_length=100)
    finalcopy = models.CharField(max_length=100)
    ppt = models.CharField(max_length=250)
    brain_content = models.TextField(blank=True, null=True)
    yy_analysis = models.TextField(blank=True, null=True)
    tools_used = models.TextField(blank=True, null=True)
    final_benefits = models.TextField(blank=True, null=True)
    challenges = models.TextField(blank=True, null=True)
    graph = models.CharField(max_length=100)
    freeze = models.IntegerField()
    period = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'qcc_registration'


class Query(models.Model):
    vendor = models.CharField(max_length=300)
    qty = models.CharField(max_length=20)
    cost = models.CharField(max_length=20)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'query'


class QuoteMaster(models.Model):
    date = models.DateField()
    quote = models.CharField(max_length=300)
    auth = models.CharField(max_length=50)
    cretaedby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'quote_master'


class RdsoTempmasterNtry(models.Model):
    uniq_slno = models.IntegerField()
    matnr = models.CharField(max_length=15)
    qty = models.IntegerField()
    type_id = models.IntegerField()
    subtype_id = models.IntegerField()
    sts = models.IntegerField()
    values = models.CharField(max_length=10000)
    ntry_by = models.IntegerField()
    ntry_date = models.DateField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rdso_TEMPmaster_ntry'


class RdsoMasterData(models.Model):
    slno = models.AutoField(primary_key=True)
    matnr = models.CharField(max_length=15)
    desc = models.CharField(max_length=150)
    project = models.CharField(max_length=20)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rdso_master_data'


class RdsoMasterNtry(models.Model):
    uniq_slno = models.IntegerField()
    matnr = models.CharField(max_length=15)
    qty = models.IntegerField()
    type_id = models.IntegerField()
    subtype_id = models.IntegerField()
    sts = models.IntegerField()
    values = models.CharField(max_length=10000)
    ntry_by = models.IntegerField()
    ntry_date = models.DateField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rdso_master_ntry'


class RdsoMasterNtryXlTemp(models.Model):
    uniq_slno = models.IntegerField()
    matnr = models.CharField(max_length=30)
    seq_slno = models.IntegerField()
    number_1 = models.IntegerField(db_column='1')  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.IntegerField(db_column='2')  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.IntegerField(db_column='3')  # Field renamed because it wasn't a valid Python identifier.
    number_4 = models.IntegerField(db_column='4')  # Field renamed because it wasn't a valid Python identifier.
    number_5 = models.IntegerField(db_column='5')  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'rdso_master_ntry_xl_temp'


class RdsoMasterSubtype(models.Model):
    subtype_id = models.AutoField(primary_key=True)
    type_id = models.IntegerField()
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'rdso_master_subtype'


class RdsoMasterTemp(models.Model):
    matnr = models.CharField(max_length=15)
    qty = models.IntegerField()
    type = models.IntegerField()
    sub_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rdso_master_temp'


class RdsoMasterType(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'rdso_master_type'


class RdsoMatmasterData(models.Model):
    slno = models.AutoField(primary_key=True)
    matnr = models.CharField(max_length=15)
    desc = models.CharField(max_length=150)
    project = models.CharField(max_length=20)
    type = models.IntegerField()
    sub_type = models.IntegerField()
    delete = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rdso_matmaster_data'


class RdsoModuleMaster(models.Model):
    slno = models.AutoField(primary_key=True)
    main_type = models.CharField(max_length=500)
    mat_num = models.CharField(max_length=250)
    parent_id = models.IntegerField()
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rdso_module_master'


class RdsoNewmasterNtry(models.Model):
    uniq_slno = models.IntegerField()
    matnr = models.CharField(max_length=15)
    qty = models.IntegerField()
    type_id = models.IntegerField()
    subtype_id = models.IntegerField()
    sts = models.IntegerField()
    values = models.CharField(max_length=10000)
    ntry_by = models.IntegerField()
    ntry_date = models.DateField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rdso_newmaster_ntry'


class RdsoNewscanMaster(models.Model):
    matnr = models.CharField(max_length=11)
    slno = models.IntegerField()
    seq_slno = models.IntegerField()
    type = models.IntegerField()
    sub_type = models.IntegerField()
    up_sts = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rdso_newscan_master'


class RdsoScanMaster(models.Model):
    matnr = models.CharField(max_length=11)
    slno = models.IntegerField()
    seq_slno = models.IntegerField()
    type = models.IntegerField()
    sub_type = models.IntegerField()
    up_sts = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rdso_scan_master'


class RdsoUploadInfo(models.Model):
    uniq_slno = models.IntegerField()
    up_sts = models.IntegerField()
    station = models.CharField(max_length=50)
    ntry_date = models.DateField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rdso_upload_info'


class ReimbursementMain(models.Model):
    id = models.BigAutoField(primary_key=True)
    empcode = models.IntegerField()
    category = models.IntegerField()
    totalamount = models.IntegerField()
    requestdate = models.DateField()
    aprl_code = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    aprl_sts = models.IntegerField()
    noofinstall = models.IntegerField(blank=True, null=True)
    noofmonths = models.IntegerField(blank=True, null=True)
    reason = models.IntegerField()
    sap_status = models.CharField(max_length=2, blank=True, null=True)
    remarks = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reimbursement_main'


class Reimbursementmcat(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=500)
    ststype = models.IntegerField()
    subtype = models.IntegerField()
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reimbursementmcat'


class RejRewPriceMstr(models.Model):
    matnr = models.CharField(max_length=20)
    price = models.FloatField()
    month_year = models.CharField(max_length=10)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rej_rew_price_mstr'


class RejRewPriceTempMstr(models.Model):
    matnr = models.CharField(max_length=20)
    price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'rej_rew_price_temp_mstr'


class RejRwrkSlip(models.Model):
    slno = models.BigAutoField(primary_key=True)
    slip_no = models.IntegerField()
    ordr = models.CharField(max_length=15)
    mat = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    qty = models.IntegerField()
    rsn = models.TextField(blank=True, null=True)
    date = models.DateField()
    dept = models.IntegerField()
    mrs = models.CharField(max_length=10)
    uom = models.CharField(max_length=5)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'rej_rwrk_slip'


class RemarksMaster(models.Model):
    rmrk_code = models.IntegerField()
    rmrk_desc = models.CharField(max_length=100)
    rmrk_desc_short = models.CharField(max_length=25)
    temp_no = models.IntegerField()
    delete1 = models.IntegerField()
    sts = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'remarks_master'


class RemarksMaster29102020(models.Model):
    rmrk_code = models.IntegerField()
    rmrk_desc = models.CharField(max_length=100)
    rmrk_desc_short = models.CharField(max_length=25)
    temp_no = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'remarks_master_29_10_2020'


class ReqNameMaster(models.Model):
    req_fm_no = models.AutoField(primary_key=True)
    req_fm_desc = models.CharField(max_length=100)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'req_name_master'


class ReqTypeMaster(models.Model):
    req_type_no = models.AutoField(primary_key=True)
    req_type_name = models.CharField(max_length=50)
    target_days = models.IntegerField()
    target_days_old = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'req_type_master'


class RevisionHistory(models.Model):
    sl_no = models.IntegerField()
    mat_code = models.CharField(max_length=20)
    sf = models.CharField(max_length=10)
    rev = models.CharField(max_length=10)
    rev_nos = models.CharField(max_length=5)
    date = models.CharField(max_length=15)
    rev_desc = models.CharField(max_length=1000)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'revision_history'


class ReworkDeptDetails(models.Model):
    rwk_id = models.AutoField(primary_key=True)
    reworkreportno = models.IntegerField()
    dept = models.CharField(max_length=30, blank=True, null=True)
    time_spent = models.CharField(max_length=12, blank=True, null=True)
    cost = models.IntegerField()
    createdby = models.CharField(max_length=6, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rework_dept_details'


class ReworkDetEdProd(models.Model):
    reworkreportno = models.IntegerField()
    hod = models.IntegerField()
    ed_comm = models.CharField(max_length=500)
    ed_date = models.DateField()
    rvt_date = models.DateField()
    rvt_comm = models.TextField()
    continue_field = models.IntegerField(db_column='continue')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'rework_det_ed_prod'


class ReworkDetails(models.Model):
    reworkreportno = models.AutoField(primary_key=True)
    fromdept = models.CharField(max_length=12, blank=True, null=True)
    todept = models.CharField(max_length=8, blank=True, null=True)
    failure_date = models.DateField()
    engineername = models.BigIntegerField()
    project = models.CharField(max_length=30, blank=True, null=True)
    equipmentslno = models.CharField(max_length=100, blank=True, null=True)
    card_slno = models.CharField(max_length=500, blank=True, null=True)
    materialcode = models.CharField(max_length=20, blank=True, null=True)
    fstage = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)
    problemdesc = models.CharField(max_length=1000, db_collation='utf8_general_ci', blank=True, null=True)
    eqmnt = models.CharField(max_length=500)
    autby = models.CharField(max_length=40, blank=True, null=True)
    sareworkdetails = models.TextField(blank=True, null=True)
    ca = models.TextField(blank=True, null=True)
    reworkdoneby = models.CharField(max_length=40, blank=True, null=True)
    date = models.DateField()
    disposalaction = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    problemcategory = models.CharField(max_length=60, blank=True, null=True)
    rdepthead = models.CharField(max_length=40, blank=True, null=True)
    fdepthead = models.CharField(max_length=40, blank=True, null=True)
    rauthorisedby = models.CharField(max_length=40, blank=True, null=True)
    production_number = models.IntegerField()
    rejectionshipno = models.IntegerField()
    bench = models.CharField(max_length=10, blank=True, null=True)
    bench1 = models.CharField(max_length=10, blank=True, null=True)
    soldering = models.CharField(max_length=10, blank=True, null=True)
    irtester = models.CharField(max_length=10, blank=True, null=True)
    hvtester = models.CharField(max_length=10, blank=True, null=True)
    ps1 = models.CharField(max_length=100, blank=True, null=True)
    ps2 = models.CharField(max_length=10, blank=True, null=True)
    ps3 = models.CharField(max_length=10, blank=True, null=True)
    ps4 = models.CharField(max_length=10, blank=True, null=True)
    ps5 = models.CharField(max_length=10, blank=True, null=True)
    mi1 = models.CharField(max_length=100, blank=True, null=True)
    mi2 = models.CharField(max_length=10, blank=True, null=True)
    mi3 = models.CharField(max_length=10, blank=True, null=True)
    mi4 = models.CharField(max_length=10, blank=True, null=True)
    mi5 = models.CharField(max_length=10, blank=True, null=True)
    any = models.CharField(max_length=10, blank=True, null=True)
    servicereportno = models.BigIntegerField()
    createdby = models.BigIntegerField()
    from_start = models.TimeField()
    from_end = models.TimeField()
    timestamp = models.DateTimeField()
    workto = models.CharField(max_length=10)
    finalsave = models.CharField(max_length=10)
    back_log = models.CharField(max_length=20)
    reject_resion = models.CharField(max_length=200, blank=True, null=True)
    autby_todept = models.CharField(max_length=20, blank=True, null=True)
    reject_resionto = models.CharField(max_length=200, blank=True, null=True)
    user_cnfm = models.CharField(max_length=20)
    to_finalsave = models.CharField(max_length=50, blank=True, null=True)
    hod2agl_prmsn = models.CharField(max_length=20)
    agl_timestamp = models.CharField(max_length=30, blank=True, null=True)
    closedby = models.IntegerField()
    tot_time = models.TimeField()
    ass_rw_rj = models.CharField(max_length=20, blank=True, null=True)
    ass_mrs = models.IntegerField()
    ass_qty = models.CharField(max_length=10)
    pstng_date = models.DateField()
    mn_sb_ass = models.CharField(max_length=25, blank=True, null=True)
    root_cause = models.CharField(max_length=5000, db_collation='utf8_general_ci', blank=True, null=True)
    noof_cards = models.IntegerField()
    oprtr_mstk = models.CharField(max_length=5000, blank=True, null=True)
    eqpmnt_rpr_date = models.DateField()
    mr_data_month = models.IntegerField()
    po_status = models.IntegerField()
    rwrk_time_spent = models.CharField(max_length=6, blank=True, null=True)
    cons_qty = models.IntegerField()
    unit_slno = models.IntegerField()
    uniq_slno = models.IntegerField()
    action_yn = models.CharField(max_length=1, blank=True, null=True)
    datef_impl = models.DateField(blank=True, null=True)
    mrd_year = models.TextField()  # This field type is a guess.
    ed_prod_cmnts = models.CharField(max_length=1500, blank=True, null=True)
    ed_prod_last_up_date = models.DateField()
    ed_prod_first_up_date = models.DateField()
    ed_prod_closed_up_date = models.DateField()
    mail_to = models.IntegerField()
    nc_smm = models.CharField(max_length=100, blank=True, null=True)
    ed_prod_cls_sts = models.IntegerField()
    ed_prod_ntry_by = models.IntegerField()
    edp_rvwd = models.IntegerField()
    nayab_sts = models.IntegerField()
    rajasree = models.CharField(max_length=5)
    delete1 = models.IntegerField()
    totappliofcom = models.IntegerField()
    totcomqty = models.IntegerField()
    acrappl = models.IntegerField()
    totfailure = models.IntegerField()
    modeoffailure = models.TextField(blank=True, null=True)
    faildisrlim = models.TextField(blank=True, null=True)
    igisampling = models.TextField(blank=True, null=True)
    promistake = models.TextField(blank=True, null=True)
    problemsetup = models.TextField(blank=True, null=True)
    tl = models.CharField(max_length=6, blank=True, null=True)
    gl = models.CharField(max_length=6, blank=True, null=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    file_type = models.CharField(max_length=50, blank=True, null=True)
    file_path = models.CharField(max_length=500, blank=True, null=True)
    file_size = models.CharField(max_length=50, blank=True, null=True)
    supplier_code = models.CharField(max_length=10)
    inspection_type = models.CharField(max_length=50, blank=True, null=True)
    faildatethird = models.DateField()
    failapp = models.TextField(blank=True, null=True)
    equipmentfaildate = models.DateField(blank=True, null=True)
    assembly_subtype = models.CharField(max_length=150, blank=True, null=True)
    status = models.IntegerField()
    defectcat = models.TextField(blank=True, null=True)
    inspect = models.CharField(max_length=5, blank=True, null=True)
    sub = models.CharField(max_length=100, blank=True, null=True)
    closed_data = models.CharField(max_length=1000, blank=True, null=True)
    mat_doc_no = models.CharField(max_length=15, blank=True, null=True)
    serial_no = models.CharField(max_length=20, blank=True, null=True)
    effectiveness = models.CharField(max_length=50, blank=True, null=True)
    costmat = models.IntegerField()
    manu_meth = models.CharField(max_length=20, blank=True, null=True)
    prom_type = models.CharField(max_length=30, blank=True, null=True)
    def_cnt = models.IntegerField()
    spec_range = models.CharField(max_length=70, blank=True, null=True)
    acc_range = models.CharField(max_length=70, blank=True, null=True)
    qp_slno = models.IntegerField()
    modify_range = models.CharField(max_length=50, blank=True, null=True)
    move_sap = models.IntegerField()
    mat_comm = models.CharField(max_length=500, blank=True, null=True)
    review = models.IntegerField()
    nc_no = models.CharField(max_length=15, blank=True, null=True)
    mailsent = models.IntegerField()
    vendor = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rework_details'


class ReworkDetails12(models.Model):
    reworkreportno = models.AutoField(primary_key=True)
    fromdept = models.CharField(max_length=8, blank=True, null=True)
    todept = models.CharField(max_length=8, blank=True, null=True)
    failure_date = models.DateField()
    engineername = models.BigIntegerField()
    project = models.CharField(max_length=30, blank=True, null=True)
    equipmentslno = models.CharField(max_length=100, blank=True, null=True)
    card_slno = models.CharField(max_length=500, blank=True, null=True)
    materialcode = models.CharField(max_length=20, blank=True, null=True)
    fstage = models.CharField(max_length=30, blank=True, null=True)
    problemdesc = models.CharField(max_length=1000, blank=True, null=True)
    eqmnt = models.CharField(max_length=500)
    autby = models.CharField(max_length=40, blank=True, null=True)
    sareworkdetails = models.TextField(blank=True, null=True)
    ca = models.TextField(blank=True, null=True)
    reworkdoneby = models.CharField(max_length=40, blank=True, null=True)
    date = models.DateField()
    disposalaction = models.CharField(max_length=200, blank=True, null=True)
    problemcategory = models.CharField(max_length=60, blank=True, null=True)
    rdepthead = models.CharField(max_length=40, blank=True, null=True)
    fdepthead = models.CharField(max_length=40, blank=True, null=True)
    rauthorisedby = models.CharField(max_length=40, blank=True, null=True)
    production_number = models.IntegerField()
    rejectionshipno = models.IntegerField()
    bench = models.CharField(max_length=10, blank=True, null=True)
    bench1 = models.CharField(max_length=10, blank=True, null=True)
    soldering = models.CharField(max_length=10)
    irtester = models.CharField(max_length=10)
    hvtester = models.CharField(max_length=10)
    ps1 = models.CharField(max_length=100)
    ps2 = models.CharField(max_length=10)
    ps3 = models.CharField(max_length=10)
    ps4 = models.CharField(max_length=10)
    ps5 = models.CharField(max_length=10)
    mi1 = models.CharField(max_length=100)
    mi2 = models.CharField(max_length=10)
    mi3 = models.CharField(max_length=10)
    mi4 = models.CharField(max_length=10)
    mi5 = models.CharField(max_length=10)
    any = models.CharField(max_length=10)
    servicereportno = models.BigIntegerField()
    createdby = models.BigIntegerField()
    from_start = models.TimeField()
    from_end = models.TimeField()
    timestamp = models.DateTimeField()
    workto = models.CharField(max_length=10)
    finalsave = models.CharField(max_length=10)
    back_log = models.CharField(max_length=20)
    reject_resion = models.CharField(max_length=200)
    autby_todept = models.CharField(max_length=20)
    reject_resionto = models.CharField(max_length=200)
    user_cnfm = models.CharField(max_length=20)
    to_finalsave = models.CharField(max_length=50)
    hod2agl_prmsn = models.CharField(max_length=20)
    agl_timestamp = models.CharField(max_length=30)
    closedby = models.IntegerField()
    tot_time = models.TimeField()
    ass_rw_rj = models.CharField(max_length=20)
    ass_mrs = models.IntegerField()
    ass_qty = models.IntegerField()
    pstng_date = models.DateField()
    mn_sb_ass = models.CharField(max_length=25)
    root_cause = models.CharField(max_length=5000)
    noof_cards = models.IntegerField()
    oprtr_mstk = models.CharField(max_length=5000)
    eqpmnt_rpr_date = models.DateField()
    mr_data_month = models.IntegerField()
    po_status = models.IntegerField()
    rwrk_time_spent = models.CharField(max_length=6)
    cons_qty = models.IntegerField()
    unit_slno = models.IntegerField()
    uniq_slno = models.IntegerField()
    action_yn = models.CharField(max_length=1)
    datef_impl = models.DateField(blank=True, null=True)
    mrd_year = models.TextField()  # This field type is a guess.
    ed_prod_cmnts = models.CharField(max_length=1500)
    ed_prod_last_up_date = models.DateField()
    ed_prod_first_up_date = models.DateField()
    ed_prod_closed_up_date = models.DateField()
    mail_to = models.IntegerField()
    nc_smm = models.CharField(max_length=100)
    ed_prod_cls_sts = models.IntegerField()
    ed_prod_ntry_by = models.IntegerField()
    edp_rvwd = models.IntegerField()
    nayab_sts = models.IntegerField()
    rajasree = models.CharField(max_length=5)
    delete1 = models.IntegerField()
    totappliofcom = models.IntegerField()
    totcomqty = models.IntegerField()
    acrappl = models.IntegerField()
    totfailure = models.IntegerField()
    modeoffailure = models.TextField()
    faildisrlim = models.TextField()
    igisampling = models.TextField()
    promistake = models.TextField()
    problemsetup = models.TextField()
    tl = models.CharField(max_length=6)
    gl = models.CharField(max_length=6)
    file_name = models.CharField(max_length=50)
    file_type = models.CharField(max_length=50)
    file_path = models.CharField(max_length=250)
    file_size = models.CharField(max_length=50)
    supplier_code = models.IntegerField()
    inspection_type = models.CharField(max_length=20)
    faildatethird = models.DateField()
    failapp = models.TextField()
    equipmentfaildate = models.DateField()
    assembly_subtype = models.CharField(max_length=150)
    status = models.IntegerField()
    defectcat = models.TextField()
    inspect = models.CharField(max_length=5)
    sub = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=100)
    inspection_type1 = models.CharField(max_length=100)
    closed_data = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'rework_details12'


class ReworkDetails123(models.Model):
    reworkreportno = models.AutoField(primary_key=True)
    fromdept = models.CharField(max_length=8, blank=True, null=True)
    todept = models.CharField(max_length=8, blank=True, null=True)
    failure_date = models.DateField()
    engineername = models.BigIntegerField()
    project = models.CharField(max_length=30, blank=True, null=True)
    equipmentslno = models.CharField(max_length=100, blank=True, null=True)
    card_slno = models.CharField(max_length=500, blank=True, null=True)
    materialcode = models.CharField(max_length=20, blank=True, null=True)
    fstage = models.CharField(max_length=30, db_collation='utf8_general_ci', blank=True, null=True)
    problemdesc = models.CharField(max_length=1000, db_collation='utf8_general_ci', blank=True, null=True)
    eqmnt = models.CharField(max_length=500)
    autby = models.CharField(max_length=40, blank=True, null=True)
    sareworkdetails = models.TextField(blank=True, null=True)
    ca = models.TextField(blank=True, null=True)
    reworkdoneby = models.CharField(max_length=40, blank=True, null=True)
    date = models.DateField()
    disposalaction = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    problemcategory = models.CharField(max_length=60, blank=True, null=True)
    rdepthead = models.CharField(max_length=40, blank=True, null=True)
    fdepthead = models.CharField(max_length=40, blank=True, null=True)
    rauthorisedby = models.CharField(max_length=40, blank=True, null=True)
    production_number = models.IntegerField()
    rejectionshipno = models.IntegerField()
    bench = models.CharField(max_length=10, blank=True, null=True)
    bench1 = models.CharField(max_length=10, blank=True, null=True)
    soldering = models.CharField(max_length=10, blank=True, null=True)
    irtester = models.CharField(max_length=10, blank=True, null=True)
    hvtester = models.CharField(max_length=10, blank=True, null=True)
    ps1 = models.CharField(max_length=100, blank=True, null=True)
    ps2 = models.CharField(max_length=10, blank=True, null=True)
    ps3 = models.CharField(max_length=10, blank=True, null=True)
    ps4 = models.CharField(max_length=10, blank=True, null=True)
    ps5 = models.CharField(max_length=10, blank=True, null=True)
    mi1 = models.CharField(max_length=100, blank=True, null=True)
    mi2 = models.CharField(max_length=10, blank=True, null=True)
    mi3 = models.CharField(max_length=10, blank=True, null=True)
    mi4 = models.CharField(max_length=10, blank=True, null=True)
    mi5 = models.CharField(max_length=10, blank=True, null=True)
    any = models.CharField(max_length=10, blank=True, null=True)
    servicereportno = models.BigIntegerField()
    createdby = models.BigIntegerField()
    from_start = models.TimeField()
    from_end = models.TimeField()
    timestamp = models.DateTimeField()
    workto = models.CharField(max_length=10)
    finalsave = models.CharField(max_length=10)
    back_log = models.CharField(max_length=20)
    reject_resion = models.CharField(max_length=200, blank=True, null=True)
    autby_todept = models.CharField(max_length=20, blank=True, null=True)
    reject_resionto = models.CharField(max_length=200, blank=True, null=True)
    user_cnfm = models.CharField(max_length=20)
    to_finalsave = models.CharField(max_length=50, blank=True, null=True)
    hod2agl_prmsn = models.CharField(max_length=20)
    agl_timestamp = models.CharField(max_length=30, blank=True, null=True)
    closedby = models.IntegerField()
    tot_time = models.TimeField()
    ass_rw_rj = models.CharField(max_length=20, blank=True, null=True)
    ass_mrs = models.IntegerField()
    ass_qty = models.CharField(max_length=10)
    pstng_date = models.DateField()
    mn_sb_ass = models.CharField(max_length=25, blank=True, null=True)
    root_cause = models.CharField(max_length=5000, db_collation='utf8_general_ci', blank=True, null=True)
    noof_cards = models.IntegerField()
    oprtr_mstk = models.CharField(max_length=5000, blank=True, null=True)
    eqpmnt_rpr_date = models.DateField()
    mr_data_month = models.IntegerField()
    po_status = models.IntegerField()
    rwrk_time_spent = models.CharField(max_length=6, blank=True, null=True)
    cons_qty = models.IntegerField()
    unit_slno = models.IntegerField()
    uniq_slno = models.IntegerField()
    action_yn = models.CharField(max_length=1, blank=True, null=True)
    datef_impl = models.DateField(blank=True, null=True)
    mrd_year = models.TextField()  # This field type is a guess.
    ed_prod_cmnts = models.CharField(max_length=1500, blank=True, null=True)
    ed_prod_last_up_date = models.DateField()
    ed_prod_first_up_date = models.DateField()
    ed_prod_closed_up_date = models.DateField()
    mail_to = models.IntegerField()
    nc_smm = models.CharField(max_length=100, blank=True, null=True)
    ed_prod_cls_sts = models.IntegerField()
    ed_prod_ntry_by = models.IntegerField()
    edp_rvwd = models.IntegerField()
    nayab_sts = models.IntegerField()
    rajasree = models.CharField(max_length=5)
    delete1 = models.IntegerField()
    totappliofcom = models.IntegerField()
    totcomqty = models.IntegerField()
    acrappl = models.IntegerField()
    totfailure = models.IntegerField()
    modeoffailure = models.TextField(blank=True, null=True)
    faildisrlim = models.TextField(blank=True, null=True)
    igisampling = models.TextField(blank=True, null=True)
    promistake = models.TextField(blank=True, null=True)
    problemsetup = models.TextField(blank=True, null=True)
    tl = models.CharField(max_length=6, blank=True, null=True)
    gl = models.CharField(max_length=6, blank=True, null=True)
    file_name = models.CharField(max_length=50, blank=True, null=True)
    file_type = models.CharField(max_length=50, blank=True, null=True)
    file_path = models.CharField(max_length=500, blank=True, null=True)
    file_size = models.CharField(max_length=50, blank=True, null=True)
    supplier_code = models.IntegerField()
    inspection_type = models.CharField(max_length=20, blank=True, null=True)
    faildatethird = models.DateField()
    failapp = models.TextField(blank=True, null=True)
    equipmentfaildate = models.DateField(blank=True, null=True)
    assembly_subtype = models.CharField(max_length=150, blank=True, null=True)
    status = models.IntegerField()
    defectcat = models.TextField(blank=True, null=True)
    inspect = models.CharField(max_length=5, blank=True, null=True)
    sub = models.CharField(max_length=100, blank=True, null=True)
    vendor_name = models.CharField(max_length=100, blank=True, null=True)
    inspection_type1 = models.CharField(max_length=100, blank=True, null=True)
    closed_data = models.CharField(max_length=250, blank=True, null=True)
    mat_doc_no = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rework_details123'


class ReworkDetailsAttach(models.Model):
    reworkreportno = models.CharField(max_length=50, blank=True, null=True)
    attachment = models.CharField(max_length=500, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rework_details_attach'


class ReworkDetailsEdpCmnts(models.Model):
    reworkreportno = models.IntegerField()
    ed_prod_cmnts = models.CharField(max_length=1500)
    ed_prod_last_up_date = models.DateField()
    ed_prod_cls_sts = models.IntegerField()
    mail_to = models.CharField(max_length=50)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rework_details_edp_cmnts'


class ReworkDetailsThirdFialDetails(models.Model):
    reworkreportno = models.IntegerField()
    code = models.CharField(max_length=15)
    failatprod = models.CharField(max_length=150)
    project = models.CharField(max_length=150)
    saname = models.CharField(max_length=150)
    faildate = models.CharField(max_length=12)
    failstage = models.CharField(max_length=150)
    modeoffail = models.CharField(max_length=150)
    compmake = models.CharField(max_length=150)
    compbatch = models.CharField(max_length=150)
    failqty = models.IntegerField()
    origincountry = models.CharField(max_length=150)
    opermis = models.CharField(max_length=150)
    testsetup = models.CharField(max_length=150)
    slno = models.IntegerField()
    old_reworkreportno = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rework_details_third_fial_details'


class ReworkFailatprodMaster(models.Model):
    dept = models.IntegerField()
    department = models.CharField(max_length=30)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rework_failatprod_master'


class ReworkHodMailIdsMaster(models.Model):
    hod = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rework_hod_mail_ids_master'


class ReworkRejection(models.Model):
    rr_no = models.IntegerField()
    hod = models.IntegerField()
    reason = models.CharField(max_length=200)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rework_rejection'


class ReworkSubUnitNtry(models.Model):
    sno = models.AutoField(primary_key=True)
    reworkreportno = models.BigIntegerField()
    version = models.IntegerField()
    matnr = models.CharField(max_length=20, blank=True, null=True)
    ritemsno = models.CharField(max_length=20, blank=True, null=True)
    fitemsno = models.CharField(max_length=1000, blank=True, null=True)
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()
    failed_qty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rework_sub_unit_ntry'


class ReworkUserTime(models.Model):
    order_no = models.IntegerField()
    mat_code = models.CharField(max_length=20)
    unit_slno = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    tot_time = models.TimeField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rework_user_time'


class RfqCurExHistory(models.Model):
    hid = models.AutoField(primary_key=True)
    id = models.IntegerField()
    valid_from = models.DateField()
    valid_to = models.DateField()
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)
    delete1 = models.IntegerField()
    createdby = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rfq_cur_ex_history'


class RfqCurrencyConversion(models.Model):
    er_type = models.CharField(max_length=2)
    from_currency = models.CharField(max_length=5, blank=True, null=True)
    to_currency = models.CharField(max_length=5, blank=True, null=True)
    valid_from = models.DateField()
    ratio_from = models.IntegerField()
    ration_to = models.IntegerField()
    delete1 = models.IntegerField()
    createdby = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rfq_currency_conversion'


class RfqCurrencyExchangeRates(models.Model):
    er_type = models.CharField(max_length=2)
    from_currency = models.CharField(max_length=5, blank=True, null=True)
    to_currency = models.CharField(max_length=5, blank=True, null=True)
    valid_from = models.DateField()
    valid_to = models.DateField()
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)
    ratio_from = models.IntegerField()
    ration_to = models.IntegerField()
    delete1 = models.IntegerField()
    createdby = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rfq_currency_exchange_rates'


class RfqHist(models.Model):
    his_id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    er_type = models.CharField(max_length=2)
    from_currency = models.CharField(max_length=5)
    to_currency = models.CharField(max_length=5, blank=True, null=True)
    valid_from = models.DateField()
    valid_to = models.DateField()
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    ratio_from = models.IntegerField(blank=True, null=True)
    ration_to = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rfq_hist'


class Rfqdata(models.Model):
    rid = models.AutoField(primary_key=True)
    rfqno = models.CharField(unique=True, max_length=11)
    rfqitem = models.CharField(max_length=5, blank=True, null=True)
    rfq_date = models.DateField()
    ven_id = models.IntegerField()
    rfq_duedate = models.DateField()
    pg = models.CharField(max_length=4, blank=True, null=True)
    pg_empcode = models.IntegerField(blank=True, null=True)
    collect_no = models.CharField(max_length=10, blank=True, null=True)
    mat_code = models.CharField(max_length=18, blank=True, null=True)
    mat_desc = models.CharField(max_length=50, blank=True, null=True)
    make = models.CharField(max_length=50, blank=True, null=True)
    mpn_no = models.CharField(max_length=30, blank=True, null=True)
    mat_grp = models.CharField(max_length=50, blank=True, null=True)
    deli_date_from = models.DateField()
    deli_date_to = models.DateField()
    deli_terms = models.CharField(max_length=50, blank=True, null=True)
    pay_terms = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=10, blank=True, null=True)
    qty = models.IntegerField()
    uom = models.CharField(max_length=11, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    cost = models.DecimalField(max_digits=18, decimal_places=4)
    pg_lead = models.IntegerField()
    moq = models.IntegerField(blank=True, null=True)
    spq = models.IntegerField(blank=True, null=True)
    lead_time = models.CharField(max_length=100, blank=True, null=True)
    rfq_sts = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()
    date = models.DateField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rfqdata'


class RfqdataHistory(models.Model):
    hid = models.AutoField(primary_key=True)
    rid = models.IntegerField()
    cost = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    deli_terms = models.IntegerField(blank=True, null=True)
    pay_terms = models.IntegerField(blank=True, null=True)
    moq = models.IntegerField(blank=True, null=True)
    spq = models.IntegerField(blank=True, null=True)
    lead_time = models.IntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    side = models.IntegerField()
    ven_id = models.IntegerField()
    rfq_sts = models.IntegerField()
    attachment = models.CharField(max_length=50, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'rfqdata_history'


class RoleMaster(models.Model):
    rolename = models.CharField(primary_key=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'role_master'


class RoleMasterAdmin(models.Model):
    empcode = models.IntegerField()
    rolename = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'role_master_admin'


class Sales(models.Model):
    billing_doc = models.CharField(max_length=10)
    item_no = models.IntegerField()
    billing_date = models.DateField()
    customer = models.CharField(max_length=10)
    ship_to_party = models.CharField(max_length=10)
    payer = models.CharField(max_length=10)
    billed_qty = models.IntegerField()
    mat_code = models.CharField(max_length=18)
    sales_doc = models.CharField(max_length=10)
    sales_doc_item = models.IntegerField()
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sales'


class Sample(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sample'


class SampleAcceptCriteria(models.Model):
    document_number = models.CharField(primary_key=True, max_length=20)
    material = models.CharField(max_length=20)
    xlessthanu = models.CharField(db_column='XlessthanU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xgreaterthanl = models.CharField(db_column='XgreaterthanL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rdivide = models.CharField(max_length=100, blank=True, null=True)
    xgreaterthanlpluskr = models.CharField(db_column='xgreaterthanLpluskr', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xlessthanequalu = models.CharField(db_column='xlessthanequalU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(max_length=50, blank=True, null=True)
    createdby = models.BigIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sample_accept_criteria'
        unique_together = (('document_number', 'material'),)


class SampleC(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=50)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'sample_c'


class SampleCategoryMaster(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample_category_master'


class SampleInspectionAttachment(models.Model):
    uniq_slno = models.IntegerField()
    file_name = models.CharField(max_length=50, blank=True, null=True)
    file_type = models.CharField(max_length=50, blank=True, null=True)
    file_path = models.CharField(max_length=100, blank=True, null=True)
    full_path = models.CharField(max_length=100, blank=True, null=True)
    raw_name = models.CharField(max_length=50, blank=True, null=True)
    orig_name = models.CharField(max_length=50, blank=True, null=True)
    client_name = models.CharField(max_length=50, blank=True, null=True)
    file_ext = models.CharField(max_length=50, blank=True, null=True)
    file_size = models.CharField(max_length=50, blank=True, null=True)
    is_image = models.CharField(max_length=50, blank=True, null=True)
    image_width = models.CharField(max_length=50, blank=True, null=True)
    image_height = models.CharField(max_length=50, blank=True, null=True)
    image_type = models.CharField(max_length=50, blank=True, null=True)
    image_size_str = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample_inspection_attachment'


class SampleInspectionNtry(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    supplier_code = models.CharField(max_length=8, blank=True, null=True)
    sup_type = models.CharField(max_length=2, blank=True, null=True)
    non_r_sup_name = models.CharField(max_length=20, blank=True, null=True)
    non_r_place = models.CharField(max_length=50, blank=True, null=True)
    dc_no = models.CharField(max_length=20, blank=True, null=True)
    dc_date = models.DateField()
    matnr = models.CharField(max_length=500, blank=True, null=True)
    qty = models.IntegerField()
    cat_id = models.IntegerField()
    purpose_id = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    hod_code = models.IntegerField()
    hod_status = models.IntegerField()
    hod_timestamp = models.CharField(max_length=18, blank=True, null=True)
    hod_remarks = models.CharField(max_length=500, blank=True, null=True)
    igi_empcode = models.IntegerField()
    received_qty = models.FloatField()
    regected_qty = models.FloatField()
    approved_qty = models.FloatField()
    rework_quantity = models.IntegerField(db_column='Rework_quantity')  # Field name made lowercase.
    inspection_date = models.DateField()
    acp_insep_date = models.DateField()
    igi_sts = models.IntegerField()
    igi_remarks = models.CharField(max_length=500, blank=True, null=True)
    created_by = models.CharField(max_length=6, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateField()
    del_by = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample_inspection_ntry'


class SampleInspectionSubNtry(models.Model):
    slno = models.AutoField(primary_key=True)
    uniq_slno = models.IntegerField()
    matcode = models.IntegerField()
    qty = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sample_inspection_sub_ntry'


class SamplePurposeMaster(models.Model):
    purpose_id = models.AutoField(primary_key=True)
    purpose_name = models.CharField(max_length=50)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'sample_purpose_master'


class SamplesizeDetails(models.Model):
    docno = models.CharField(primary_key=True, max_length=20)
    material = models.CharField(max_length=20)
    slno = models.IntegerField()
    obsvalue = models.CharField(max_length=100, blank=True, null=True)
    rownumber = models.IntegerField(blank=True, null=True)
    rowvalue = models.FloatField(blank=True, null=True)
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'samplesize_details'
        unique_together = (('docno', 'material', 'slno'),)


class Sampletest(models.Model):
    date = models.DateField()
    name = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()
    second = models.DateField()

    class Meta:
        managed = False
        db_table = 'sampletest'


class SamplingInspection(models.Model):
    docno = models.CharField(primary_key=True, max_length=20)
    department = models.CharField(max_length=8)
    lotsize = models.PositiveIntegerField(blank=True, null=True)
    samplesize = models.PositiveIntegerField(blank=True, null=True)
    aqlvalue = models.FloatField(blank=True, null=True)
    constantvalue = models.FloatField(blank=True, null=True)
    rvlvalue = models.FloatField(blank=True, null=True)
    drgdimension = models.CharField(max_length=100, blank=True, null=True)
    parameter = models.CharField(max_length=15, blank=True, null=True)
    x = models.CharField(max_length=10, blank=True, null=True)
    r = models.CharField(max_length=10, blank=True, null=True)
    stage = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()
    teststage = models.CharField(max_length=100)
    material = models.CharField(max_length=20)
    vendor = models.CharField(max_length=8)
    instrumentsino = models.CharField(max_length=11)
    inspectedby = models.BigIntegerField(blank=True, null=True)
    inspecteddate = models.DateField(blank=True, null=True)
    approvedby = models.BigIntegerField(blank=True, null=True)
    approveddate = models.DateField(blank=True, null=True)
    obsvalue = models.CharField(max_length=1000, blank=True, null=True)
    rvalue = models.CharField(max_length=100, blank=True, null=True)
    finalsave = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'sampling_inspection'
        unique_together = (('docno', 'material'),)


class SapFlatfileme(models.Model):
    flatfileid = models.AutoField(primary_key=True)
    dwg_totid = models.IntegerField()
    filedid = models.IntegerField()
    fileddes = models.TextField()
    status = models.IntegerField()
    refitem = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sap_flatfileme'


class ScarDetails(models.Model):
    sid = models.AutoField(primary_key=True)
    scar_type = models.CharField(max_length=10, blank=True, null=True)
    scarno = models.CharField(max_length=200, blank=True, null=True)
    scardate = models.DateField()
    pono = models.CharField(max_length=20, blank=True, null=True)
    docno = models.CharField(max_length=20, blank=True, null=True)
    batchno = models.CharField(max_length=30, blank=True, null=True)
    supplier = models.CharField(max_length=10, blank=True, null=True)
    supp_addr = models.TextField(blank=True, null=True)
    approval = models.CharField(max_length=10, blank=True, null=True)
    partno = models.CharField(max_length=12, blank=True, null=True)
    prob_desc = models.TextField(blank=True, null=True)
    qty_rec = models.IntegerField()
    qty_rej = models.IntegerField()
    uom = models.IntegerField()
    insp_by = models.CharField(max_length=8, blank=True, null=True)
    insp_done = models.IntegerField(blank=True, null=True)
    ntry_by = models.IntegerField(blank=True, null=True)
    ntry_date = models.DateField()
    hod_sts_ini = models.IntegerField()
    hod = models.IntegerField()
    hod_date_ini = models.DateField()
    ven_sts = models.IntegerField()
    cont_act = models.TextField(blank=True, null=True)
    root_cau = models.TextField(blank=True, null=True)
    escape_point = models.TextField(blank=True, null=True)
    corr_act = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    prev_act = models.TextField(blank=True, null=True)
    eff_date = models.DateField()
    supp_desig = models.CharField(max_length=30, blank=True, null=True)
    ven_date = models.DateField()
    hod_ven_sts = models.IntegerField()
    eff_act_plan = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10)
    compl_closed_date = models.DateField()
    supplier_rep_name = models.CharField(max_length=1000, blank=True, null=True)
    entry_att = models.CharField(max_length=500, blank=True, null=True)
    supp_att = models.CharField(max_length=500, blank=True, null=True)
    hod_att = models.CharField(max_length=500, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'scar_details'


class ScarUomMaster(models.Model):
    uid = models.AutoField(primary_key=True)
    uom = models.CharField(max_length=10)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'scar_uom_master'


class SepsaMasData(models.Model):
    matid = models.AutoField(primary_key=True)
    matcode = models.CharField(max_length=20, blank=True, null=True)
    matdesc = models.CharField(max_length=200, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sepsa_mas_data'


class SepsaUsermaster(models.Model):
    customer_id = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    customer_name = models.CharField(max_length=35, blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    postal_code = models.CharField(max_length=50, blank=True, null=True)
    serach_team = models.CharField(max_length=50, blank=True, null=True)
    mail_id = models.CharField(max_length=65, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sepsa_usermaster'


class SeriveCommAttach(models.Model):
    aid = models.AutoField(primary_key=True)
    serviceno = models.IntegerField()
    attachment = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'serive_comm_attach'


class ServiceAmcMaster(models.Model):
    project = models.CharField(max_length=50)
    loco_no = models.IntegerField()
    loco_type = models.CharField(max_length=50)
    version = models.CharField(max_length=30)
    doc = models.DateField()
    type = models.CharField(max_length=30)
    unit_slno = models.IntegerField()
    amc_sts = models.CharField(max_length=15)
    pp = models.IntegerField()
    npp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_amc_master'


class ServiceAuthorization(models.Model):
    slno = models.AutoField(primary_key=True)
    service_no = models.IntegerField()
    hodcode = models.IntegerField()
    hod_status = models.CharField(max_length=200)
    hod_comment = models.CharField(max_length=500)
    hod_rececied_date = models.DateField()
    hod_approveddate = models.DateField()
    review_per = models.IntegerField()
    edp_code = models.IntegerField()
    edp_status = models.CharField(max_length=200)
    edp_comment = models.CharField(max_length=500)
    edp_approveddate = models.DateField()
    review_per_edp = models.IntegerField()
    status = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField(blank=True, null=True)
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'service_authorization'


class ServiceCategory(models.Model):
    group_id = models.IntegerField()
    group_name = models.CharField(max_length=150)
    column_id = models.IntegerField()
    column_name = models.CharField(max_length=150)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_category'


class ServiceCommisingReport(models.Model):
    serviceno = models.IntegerField(blank=True, null=True)
    month_year = models.CharField(max_length=20, blank=True, null=True)
    no_fail = models.IntegerField(blank=True, null=True)
    res_dept = models.CharField(max_length=40, blank=True, null=True)
    rcca = models.TextField(db_column='RCCA', blank=True, null=True)  # Field name made lowercase.
    depts = models.TextField(blank=True, null=True)
    analysisdet = models.TextField(blank=True, null=True)
    failuredata = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    com_date = models.DateField()
    rmks = models.TextField(blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    root_cause = models.TextField(blank=True, null=True)
    fail_det = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_commising_report'


class ServiceDiposal(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_diposal'


class ServiceDummy(models.Model):
    reportno = models.CharField(max_length=20)
    zone = models.CharField(max_length=60)
    shed = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'service_dummy'


class ServiceEnggneers(models.Model):
    engg_code = models.CharField(primary_key=True, max_length=10)
    engg_name = models.CharField(max_length=50)
    cur_desg = models.CharField(max_length=50)
    createdby = models.SmallIntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'service_enggneers'


class ServiceIndirectiveHist(models.Model):
    slno = models.AutoField(primary_key=True)
    report_no = models.IntegerField()
    level_type = models.IntegerField()
    subasscode = models.CharField(max_length=200)
    from_loc = models.CharField(max_length=100)
    to_loc = models.CharField(max_length=100)
    from_dept = models.IntegerField()
    to_dept = models.IntegerField()
    from_level = models.IntegerField()
    to_level = models.IntegerField()
    to_level_slno = models.IntegerField()
    status = models.IntegerField()
    cdb_slno = models.IntegerField()
    routedate = models.DateField()
    route_value = models.IntegerField()
    frd_val = models.IntegerField()
    recived_route = models.IntegerField()
    master_slno = models.CharField(max_length=100)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'service_indirective_hist'


class ServiceIndirectiveHist1(models.Model):
    slno = models.AutoField(primary_key=True)
    report_no = models.IntegerField()
    level_type = models.IntegerField()
    subasscode = models.CharField(max_length=200)
    from_loc = models.CharField(max_length=100)
    to_loc = models.CharField(max_length=100)
    from_dept = models.IntegerField()
    to_dept = models.IntegerField()
    from_level = models.IntegerField()
    to_level = models.IntegerField()
    to_level_slno = models.IntegerField()
    status = models.IntegerField()
    cdb_slno = models.IntegerField()
    routedate = models.DateField()
    route_value = models.IntegerField()
    frd_val = models.IntegerField()
    recived_route = models.IntegerField()
    master_slno = models.CharField(max_length=100)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'service_indirective_hist1'


class ServiceLevelMaster(models.Model):
    id = models.IntegerField(primary_key=True)
    level_name = models.CharField(max_length=100, blank=True, null=True)
    table_name = models.CharField(max_length=100, blank=True, null=True)
    dept_code_auth = models.CharField(max_length=2000, blank=True, null=True)
    loc_auth = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    created_by = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_level_master'


class ServiceMailHist(models.Model):
    slno = models.AutoField(primary_key=True)
    report_no = models.IntegerField()
    mail_hist_from = models.IntegerField()
    mail_hist_to = models.IntegerField()
    mail_text = models.CharField(max_length=500)
    entry_date = models.CharField(max_length=200)
    status = models.IntegerField()
    type_id = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_mail_hist'


class ServiceMailMaster(models.Model):
    slno = models.IntegerField(primary_key=True)
    loccode = models.CharField(max_length=100)
    deptcode = models.IntegerField()
    project_type = models.CharField(max_length=250)
    to = models.CharField(max_length=250)
    cc = models.CharField(max_length=250)
    bcc = models.CharField(max_length=250)
    deptcond = models.CharField(max_length=100)
    type = models.IntegerField()
    mail1 = models.CharField(max_length=1000)
    mail2 = models.CharField(max_length=1000)
    mail3 = models.CharField(max_length=1000)
    created_by = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_mail_master'


class ServiceMiisedData(models.Model):
    servicereportno = models.IntegerField()
    fitemmcode = models.CharField(max_length=100, blank=True, null=True)
    fitemsno = models.CharField(max_length=100, blank=True, null=True)
    fitemmcodeback = models.CharField(max_length=100, blank=True, null=True)
    fitemsnoback = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'service_miised_data'


class ServiceMultiple(models.Model):
    slno = models.AutoField(primary_key=True)
    reportno = models.IntegerField()
    matcode_multi = models.CharField(max_length=250)
    mat_sts_dept_from = models.IntegerField()
    mat_sts_dept = models.IntegerField()
    mat_rev_date_multi = models.DateField()
    mat_sent_date_multi = models.DateField()
    mat_loccode_multi = models.CharField(max_length=200)
    mat_sts_dept_to = models.IntegerField()
    mat_sts = models.IntegerField()
    mat_from_date = models.DateField()
    mat_route_date = models.DateField()
    mat_time = models.CharField(max_length=100)
    unit_sts = models.IntegerField()
    unit_dept = models.IntegerField()
    unit_sts_dept_from = models.IntegerField()
    testedby_multi = models.IntegerField()
    equipmentfaildate_multi = models.DateField()
    equipmentslno_multi = models.IntegerField()
    pbdesc_multi = models.TextField()
    rd_analysis_multi = models.TextField()
    unit_sts_dept_to = models.IntegerField()
    unit_from_date = models.DateField()
    unit_route_date = models.DateField()
    rework_time = models.CharField(max_length=100)
    sa_dept_from = models.IntegerField()
    sa_dept = models.IntegerField()
    sa_from_date = models.DateField()
    rework_sts = models.IntegerField()
    ca_dept_from = models.IntegerField()
    fc_from_date = models.DateField()
    fc_dept = models.IntegerField()
    fc_sts = models.IntegerField()
    rc_sts = models.IntegerField()
    root_sts_dept_from = models.IntegerField()
    root_cause_multi = models.TextField()
    action_yn_multi = models.CharField(max_length=20)
    ca_multi = models.TextField()
    datef_impl_multi = models.DateField()
    ecr_no_multi = models.CharField(max_length=200)
    root_sts_dept_to = models.IntegerField()
    root_dept = models.IntegerField()
    root_from_date = models.DateField()
    root_route_date = models.DateField()
    root_time = models.CharField(max_length=100)
    pse_sts = models.IntegerField()
    pse_sts_dept_from = models.IntegerField()
    pse_dept = models.IntegerField()
    failuredetails_multi = models.TextField()
    pr_sup_eng_comm_multi = models.TextField()
    knowledge_appli_multi = models.CharField(max_length=20)
    consult_asso_multi = models.IntegerField()
    enteredby_multi = models.IntegerField()
    failurecategory_multi = models.CharField(max_length=200)
    checkedby_muti = models.IntegerField()
    pse_sts_dept_to = models.IntegerField()
    pse_from_date = models.DateField()
    pse_route_date = models.DateField()
    problemcategory_multi = models.CharField(max_length=200)
    oprtr_mstk_multi = models.IntegerField()
    disposalaction_multi = models.TextField()
    disp_matcode = models.CharField(max_length=50)
    disp_qty = models.CharField(max_length=50)
    dis_sts_dept_to = models.IntegerField()
    dis_route_date = models.DateField()
    no_prob_loco_multi = models.CharField(max_length=250)
    noproblem_zone_multi = models.CharField(max_length=250)
    no_prob_shed_multi = models.CharField(max_length=250)
    fitted_date_multi = models.DateField()
    nop_dept_multi = models.IntegerField()
    nop_route_date = models.DateField()
    curr_sts = models.IntegerField()
    sub_slno = models.CharField(max_length=100)
    sub_rslno = models.CharField(max_length=100)
    id_ref = models.CharField(max_length=100)
    master_slno = models.CharField(max_length=100)
    third_type = models.IntegerField()
    material_recevie_num = models.IntegerField()
    scrp_wrnty = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'service_multiple'


class ServiceMultipleMat(models.Model):
    slno = models.AutoField(primary_key=True)
    reportno = models.IntegerField()
    matcode_multi = models.CharField(max_length=250)
    mat_sts_dept_from = models.IntegerField()
    mat_sts_dept = models.IntegerField()
    mat_rev_date_multi = models.DateField()
    mat_sent_date_multi = models.DateField()
    mat_loccode_multi = models.CharField(max_length=250)
    mat_sts_dept_to = models.IntegerField()
    mat_sts = models.IntegerField()
    mat_from_date = models.DateField()
    mat_route_date = models.DateField()
    route_value = models.IntegerField()
    mat_time = models.CharField(max_length=100)
    hod_sts = models.CharField(max_length=15)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_multiple_mat'


class ServiceMultiplePse(models.Model):
    slno = models.AutoField(primary_key=True)
    reportno = models.IntegerField()
    matcode_multi = models.CharField(max_length=250)
    from_loc = models.CharField(max_length=100)
    to_loc = models.CharField(max_length=100)
    pse_sts_dept_from = models.IntegerField()
    pse_dept = models.IntegerField()
    failuredetails_multi = models.TextField()
    pr_sup_eng_comm_multi = models.TextField()
    knowledge_appli_multi = models.CharField(max_length=20)
    consult_asso_multi = models.IntegerField()
    enteredby_multi = models.IntegerField()
    failurecategory_multi = models.CharField(max_length=200)
    checkedby_muti = models.IntegerField()
    pse_sts_dept_to = models.IntegerField()
    pse_from_date = models.DateField()
    pse_route_date = models.DateField()
    pse_sts = models.IntegerField()
    route_value = models.IntegerField()
    hod_sts = models.CharField(max_length=15, blank=True, null=True)
    db_type = models.IntegerField()
    type_ref = models.IntegerField()
    uniq_id = models.IntegerField()
    type = models.IntegerField()
    master_slno = models.CharField(max_length=100, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_multiple_pse'


class ServiceMultipleRework(models.Model):
    slno = models.AutoField(primary_key=True)
    reportno = models.IntegerField()
    matcode_multi = models.CharField(max_length=250)
    from_loc = models.CharField(max_length=100)
    to_loc = models.CharField(max_length=100)
    unit_sts_dept_from = models.IntegerField()
    unit_dept = models.IntegerField()
    testedby_multi = models.IntegerField()
    equipmentfaildate_multi = models.DateField()
    equipmentslno_multi = models.CharField(max_length=100)
    pbdesc_multi = models.TextField()
    reason_delay = models.TextField()
    remarks = models.TextField()
    rd_analysis_multi = models.TextField()
    unit_sts_dept_to = models.IntegerField()
    unit_from_date = models.DateField()
    unit_route_date = models.DateField()
    unit_sts = models.IntegerField()
    route_value = models.IntegerField()
    rework_time = models.CharField(max_length=100)
    hod_sts = models.CharField(max_length=15)
    type = models.IntegerField()
    db_type = models.IntegerField()
    type_ref = models.IntegerField()
    other_dept_pend = models.IntegerField()
    analysis_comp = models.IntegerField()
    master_slno = models.CharField(max_length=100)
    attchmentforevrysub = models.CharField(max_length=100)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_multiple_rework'


class ServiceMultipleRoot(models.Model):
    slno = models.AutoField(primary_key=True)
    counts = models.IntegerField()
    reportno = models.IntegerField()
    matcode_multi = models.CharField(max_length=250)
    from_loc = models.CharField(max_length=100)
    to_loc = models.CharField(max_length=100)
    root_sts_dept_from = models.IntegerField()
    root_dept = models.IntegerField()
    root_cause_multi = models.TextField()
    action_yn_multi = models.CharField(max_length=20)
    ca_multi = models.TextField()
    knowledge_appli_multi = models.CharField(max_length=20)
    consult_asso_multi = models.IntegerField()
    datef_impl_multi = models.DateField()
    ecr_no_multi = models.CharField(max_length=200)
    root_sts_dept_to = models.CharField(max_length=250)
    root_from_date = models.DateField()
    root_route_date = models.DateField()
    rc_sts = models.IntegerField()
    route_value = models.IntegerField()
    root_time = models.CharField(max_length=100)
    hod_sts = models.CharField(max_length=15)
    remarks = models.TextField()
    rework_time = models.CharField(max_length=100)
    reason_delay = models.TextField()
    mod_det = models.CharField(max_length=200)
    db_type = models.IntegerField()
    type_ref = models.IntegerField()
    type = models.IntegerField()
    master_slno = models.CharField(max_length=100)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_multiple_root'


class ServiceReport(models.Model):
    reportno = models.PositiveBigIntegerField(primary_key=True)
    detailsreceivedby = models.CharField(max_length=40, blank=True, null=True)
    reportedby = models.CharField(max_length=40, blank=True, null=True)
    reporteddate = models.DateField(blank=True, null=True)
    actualdate = models.DateField(blank=True, null=True)
    report_completed_date = models.DateField()
    actual_time = models.TimeField()
    typeofservice = models.CharField(max_length=20, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    mfddate = models.DateField()
    start_time = models.TimeField()
    completeddate = models.DateField(blank=True, null=True)
    complited_time = models.TimeField()
    zone = models.CharField(max_length=40, blank=True, null=True)
    depot = models.CharField(max_length=40, blank=True, null=True)
    coach = models.CharField(max_length=40, blank=True, null=True)
    shed = models.CharField(max_length=40, blank=True, null=True)
    locono = models.CharField(max_length=40, blank=True, null=True)
    locotype = models.CharField(max_length=40, blank=True, null=True)
    factory = models.CharField(max_length=40, blank=True, null=True)
    engineercode = models.CharField(max_length=30, blank=True, null=True)
    mcode = models.CharField(max_length=20, blank=True, null=True)
    ecode = models.CharField(max_length=20)
    problemdesc = models.CharField(max_length=2000, blank=True, null=True)
    symptoms = models.CharField(max_length=2000, blank=True, null=True)
    reworkdone = models.CharField(max_length=2000, blank=True, null=True)
    failurecategory = models.CharField(max_length=240, blank=True, null=True)
    failuredetails = models.CharField(max_length=300, blank=True, null=True)
    serviceempcode = models.CharField(max_length=20, blank=True, null=True)
    checkedby = models.CharField(max_length=40, blank=True, null=True)
    authorizedby = models.CharField(max_length=40, blank=True, null=True)
    enteredby = models.CharField(max_length=40, blank=True, null=True)
    rework_report = models.IntegerField()
    dept_to = models.CharField(max_length=180, blank=True, null=True)
    project = models.CharField(max_length=30, blank=True, null=True)
    unittype = models.CharField(max_length=150, blank=True, null=True)
    unitno = models.CharField(max_length=20, blank=True, null=True)
    finalsave = models.CharField(max_length=150)
    srvchod_vrjct = models.CharField(max_length=50)
    to_dept_hod = models.IntegerField()
    altd_user = models.IntegerField()
    from_dept_user_report_taken = models.IntegerField()
    createdby = models.BigIntegerField()
    flre_reported_time = models.TimeField()
    datef_cmsn = models.DateField()
    version = models.CharField(max_length=50)
    rplcd_unitslno = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    dump = models.IntegerField()
    aglcode = models.IntegerField()
    agl_sts = models.CharField(max_length=30)
    agl_timestamp = models.CharField(max_length=30)
    disp_act = models.CharField(max_length=1000)
    days = models.IntegerField()
    hours = models.IntegerField()
    mins = models.IntegerField()
    ser_days = models.IntegerField()
    ser_hours = models.IntegerField()
    ser_mins = models.IntegerField()
    ser_time_update_sts = models.IntegerField()
    uniq_slno = models.IntegerField()
    loco_avlbl_sts = models.CharField(max_length=150)
    rack_no = models.CharField(max_length=15)
    attend_at_fact = models.CharField(max_length=1)
    report_ntry_date = models.DateField()
    failure_reported_date = models.DateField()
    failure_reported_time = models.TimeField()
    handed_over_date = models.DateField()
    rd_analysis = models.CharField(max_length=1000)
    ecr_no = models.CharField(max_length=50)
    pr_sup_eng_comm = models.CharField(max_length=1000)
    attachment = models.CharField(max_length=150)
    failure_unit_comments = models.CharField(max_length=1000)
    failure_unit_analysis = models.CharField(max_length=500)
    failur_unit_location = models.CharField(max_length=50)
    repaly_mail_date = models.DateField()
    ffa_by = models.IntegerField()
    mat_rev_date = models.DateField()
    mat_sent_date = models.DateField()
    mat_loccode = models.CharField(max_length=30)
    mat_dept = models.IntegerField()
    mat_problemcategory = models.CharField(max_length=500)
    knowledge_appli = models.CharField(max_length=200)
    consult_asso = models.IntegerField()
    noproblem_zone = models.CharField(max_length=40)
    no_prob_shed = models.CharField(max_length=40)
    no_prob_loco = models.CharField(max_length=40)
    fitted_date = models.DateField()
    remarks = models.CharField(max_length=3000)
    status = models.IntegerField()
    to_rd_date = models.DateField()
    capa_eff = models.TextField(blank=True, null=True)
    service_ext_no = models.IntegerField()
    review_corr = models.TextField(blank=True, null=True)
    review_sts = models.IntegerField()
    ntry_date_ext = models.CharField(max_length=50)
    reviewdate = models.CharField(max_length=50)
    entry_ext_int = models.CharField(max_length=50)
    third_type = models.IntegerField()
    close_sts = models.IntegerField()
    num_per = models.IntegerField()
    serv_engg_time_mm = models.CharField(max_length=100)
    new_version_date = models.DateField()
    attended = models.CharField(max_length=150)
    ffasr_status = models.IntegerField()
    ffasr_cl_comments = models.CharField(max_length=300)
    frb_coments = models.CharField(max_length=250)
    comined_reports = models.CharField(max_length=150)
    frbupdate_date = models.CharField(max_length=15)
    ffasr_cls_date = models.CharField(max_length=150, blank=True, null=True)
    ffasr_cl_empcode = models.IntegerField(blank=True, null=True)
    close_date = models.DateField()
    prereview = models.IntegerField()
    screen_sts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_report'


class ServiceReport1810(models.Model):
    reportno = models.PositiveBigIntegerField(primary_key=True)
    detailsreceivedby = models.CharField(max_length=40, blank=True, null=True)
    reportedby = models.CharField(max_length=40, blank=True, null=True)
    reporteddate = models.DateField(blank=True, null=True)
    actualdate = models.DateField(blank=True, null=True)
    report_completed_date = models.DateField()
    actual_time = models.TimeField()
    typeofservice = models.CharField(max_length=20, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    mfddate = models.DateField()
    start_time = models.TimeField()
    completeddate = models.DateField(blank=True, null=True)
    complited_time = models.TimeField()
    zone = models.CharField(max_length=40, blank=True, null=True)
    depot = models.CharField(max_length=40, blank=True, null=True)
    coach = models.CharField(max_length=40, blank=True, null=True)
    shed = models.CharField(max_length=40, blank=True, null=True)
    locono = models.CharField(max_length=40, blank=True, null=True)
    locotype = models.CharField(max_length=40, blank=True, null=True)
    factory = models.CharField(max_length=40, blank=True, null=True)
    engineercode = models.CharField(max_length=30, blank=True, null=True)
    mcode = models.CharField(max_length=20, blank=True, null=True)
    ecode = models.CharField(max_length=20)
    problemdesc = models.CharField(max_length=2000, blank=True, null=True)
    symptoms = models.CharField(max_length=2000, blank=True, null=True)
    reworkdone = models.CharField(max_length=2000, blank=True, null=True)
    failurecategory = models.CharField(max_length=240, blank=True, null=True)
    failuredetails = models.CharField(max_length=300, blank=True, null=True)
    serviceempcode = models.CharField(max_length=20, blank=True, null=True)
    checkedby = models.CharField(max_length=40, blank=True, null=True)
    authorizedby = models.CharField(max_length=40, blank=True, null=True)
    enteredby = models.CharField(max_length=40, blank=True, null=True)
    rework_report = models.IntegerField()
    dept_to = models.CharField(max_length=180, blank=True, null=True)
    project = models.CharField(max_length=30, blank=True, null=True)
    unittype = models.CharField(max_length=150, blank=True, null=True)
    unitno = models.CharField(max_length=20, blank=True, null=True)
    finalsave = models.CharField(max_length=150)
    srvchod_vrjct = models.CharField(max_length=50)
    to_dept_hod = models.IntegerField()
    altd_user = models.IntegerField()
    from_dept_user_report_taken = models.IntegerField()
    createdby = models.BigIntegerField()
    flre_reported_time = models.TimeField()
    datef_cmsn = models.DateField()
    version = models.CharField(max_length=50)
    rplcd_unitslno = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    dump = models.IntegerField()
    aglcode = models.IntegerField()
    agl_sts = models.CharField(max_length=30)
    agl_timestamp = models.CharField(max_length=30)
    disp_act = models.CharField(max_length=1000)
    days = models.IntegerField()
    hours = models.IntegerField()
    mins = models.IntegerField()
    ser_days = models.IntegerField()
    ser_hours = models.IntegerField()
    ser_mins = models.IntegerField()
    ser_time_update_sts = models.IntegerField()
    uniq_slno = models.IntegerField()
    loco_avlbl_sts = models.CharField(max_length=150)
    rack_no = models.CharField(max_length=15)
    attend_at_fact = models.CharField(max_length=1)
    report_ntry_date = models.DateField()
    failure_reported_date = models.DateField()
    failure_reported_time = models.TimeField()
    handed_over_date = models.DateField()
    rd_analysis = models.CharField(max_length=1000)
    ecr_no = models.CharField(max_length=50)
    pr_sup_eng_comm = models.CharField(max_length=1000)
    attachment = models.CharField(max_length=150)
    failure_unit_comments = models.CharField(max_length=1000)
    failure_unit_analysis = models.CharField(max_length=500)
    failur_unit_location = models.CharField(max_length=50)
    repaly_mail_date = models.DateField()
    ffa_by = models.IntegerField()
    mat_rev_date = models.DateField()
    mat_sent_date = models.DateField()
    mat_loccode = models.CharField(max_length=30)
    mat_dept = models.IntegerField()
    mat_problemcategory = models.CharField(max_length=500)
    knowledge_appli = models.CharField(max_length=200)
    consult_asso = models.IntegerField()
    noproblem_zone = models.CharField(max_length=40)
    no_prob_shed = models.CharField(max_length=40)
    no_prob_loco = models.CharField(max_length=40)
    fitted_date = models.DateField()
    remarks = models.CharField(max_length=3000)
    status = models.IntegerField()
    to_rd_date = models.DateField()
    capa_eff = models.TextField(blank=True, null=True)
    service_ext_no = models.IntegerField()
    no_ser_eng = models.IntegerField()
    main_type = models.CharField(max_length=20, blank=True, null=True)
    ini_rev = models.CharField(max_length=20, blank=True, null=True)
    review_corr = models.TextField(blank=True, null=True)
    review_sts = models.IntegerField()
    ntry_date_ext = models.CharField(max_length=50)
    reviewdate = models.CharField(max_length=50)
    entry_ext_int = models.CharField(max_length=50)
    third_type = models.IntegerField()
    close_sts = models.IntegerField()
    num_per = models.IntegerField()
    serv_engg_time_mm = models.CharField(max_length=100)
    new_version_date = models.DateField()
    attended = models.CharField(max_length=150)
    ffasr_status = models.IntegerField()
    ffasr_statusdate = models.DateTimeField()
    ffasr_cl_comments = models.CharField(max_length=300)
    frb_coments = models.CharField(max_length=250)
    comined_reports = models.CharField(max_length=500)
    frbupdate_date = models.CharField(max_length=15)
    ffasr_cls_date = models.CharField(max_length=150, blank=True, null=True)
    ffasr_cl_empcode = models.IntegerField(blank=True, null=True)
    close_date = models.DateField()
    prereview = models.IntegerField()
    screen_sts = models.IntegerField()
    prj_priority = models.IntegerField()
    root_cause_cat = models.IntegerField()
    assining_status = models.IntegerField()
    rootcause_updatedate = models.DateField()

    class Meta:
        managed = False
        db_table = 'service_report-18-10'


class ServiceReport1(models.Model):
    reportno = models.PositiveBigIntegerField(primary_key=True)
    detailsreceivedby = models.CharField(max_length=40, blank=True, null=True)
    reportedby = models.CharField(max_length=40, blank=True, null=True)
    reporteddate = models.DateField(blank=True, null=True)
    actualdate = models.DateField(blank=True, null=True)
    report_completed_date = models.DateField()
    actual_time = models.TimeField()
    typeofservice = models.CharField(max_length=20, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    mfddate = models.DateField()
    start_time = models.TimeField()
    completeddate = models.DateField(blank=True, null=True)
    complited_time = models.TimeField()
    zone = models.CharField(max_length=40, blank=True, null=True)
    depot = models.CharField(max_length=40, blank=True, null=True)
    coach = models.CharField(max_length=40, blank=True, null=True)
    shed = models.CharField(max_length=40, blank=True, null=True)
    locono = models.CharField(max_length=40, blank=True, null=True)
    locotype = models.CharField(max_length=40, blank=True, null=True)
    factory = models.CharField(max_length=40, blank=True, null=True)
    engineercode = models.CharField(max_length=30, blank=True, null=True)
    mcode = models.CharField(max_length=20, blank=True, null=True)
    ecode = models.CharField(max_length=20)
    problemdesc = models.CharField(max_length=2000, blank=True, null=True)
    symptoms = models.CharField(max_length=2000, blank=True, null=True)
    reworkdone = models.CharField(max_length=2000, blank=True, null=True)
    failurecategory = models.CharField(max_length=40, blank=True, null=True)
    failuredetails = models.CharField(max_length=300, blank=True, null=True)
    serviceempcode = models.CharField(max_length=20, blank=True, null=True)
    checkedby = models.CharField(max_length=40, blank=True, null=True)
    authorizedby = models.CharField(max_length=40, blank=True, null=True)
    enteredby = models.CharField(max_length=40, blank=True, null=True)
    rework_report = models.IntegerField()
    dept_to = models.CharField(max_length=8, blank=True, null=True)
    project = models.CharField(max_length=30, blank=True, null=True)
    unittype = models.CharField(max_length=10, blank=True, null=True)
    unitno = models.CharField(max_length=20, blank=True, null=True)
    finalsave = models.CharField(max_length=5)
    srvchod_vrjct = models.CharField(max_length=50)
    to_dept_hod = models.IntegerField()
    altd_user = models.IntegerField()
    from_dept_user_report_taken = models.IntegerField()
    createdby = models.BigIntegerField()
    flre_reported_time = models.TimeField()
    datef_cmsn = models.DateField()
    version = models.CharField(max_length=50)
    rplcd_unitslno = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    dump = models.IntegerField()
    aglcode = models.IntegerField()
    agl_sts = models.CharField(max_length=30)
    agl_timestamp = models.CharField(max_length=30)
    disp_act = models.CharField(max_length=1000)
    days = models.IntegerField()
    hours = models.IntegerField()
    mins = models.IntegerField()
    ser_days = models.IntegerField()
    ser_hours = models.IntegerField()
    ser_mins = models.IntegerField()
    ser_time_update_sts = models.IntegerField()
    uniq_slno = models.IntegerField()
    loco_avlbl_sts = models.CharField(max_length=1)
    rack_no = models.CharField(max_length=15)
    attend_at_fact = models.CharField(max_length=1)
    report_ntry_date = models.DateField()
    failure_reported_date = models.DateField()
    failure_reported_time = models.TimeField()
    handed_over_date = models.DateField()
    rd_analysis = models.CharField(max_length=1000)
    ecr_no = models.CharField(max_length=50)
    pr_sup_eng_comm = models.CharField(max_length=1000)
    attachment = models.CharField(max_length=150)
    failure_unit_comments = models.CharField(max_length=1000)
    failure_unit_analysis = models.CharField(max_length=500)
    failur_unit_location = models.CharField(max_length=50)
    repaly_mail_date = models.DateField()
    mat_rev_date = models.DateField()
    mat_sent_date = models.DateField()
    mat_loccode = models.CharField(max_length=30)
    mat_dept = models.IntegerField()
    mat_problemcategory = models.CharField(max_length=500)
    knowledge_appli = models.CharField(max_length=200)
    consult_asso = models.IntegerField()
    noproblem_zone = models.CharField(max_length=40)
    no_prob_shed = models.CharField(max_length=40)
    no_prob_loco = models.CharField(max_length=40)
    fitted_date = models.DateField()
    remarks = models.CharField(max_length=3000)
    status = models.IntegerField()
    to_rd_date = models.DateField()
    capa_eff = models.TextField()
    service_ext_no = models.IntegerField()
    review_corr = models.TextField()
    review_sts = models.IntegerField()
    ntry_date_ext = models.CharField(max_length=50)
    reviewdate = models.CharField(max_length=50)
    entry_ext_int = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'service_report1'


class ServiceReportAttachments(models.Model):
    report_no = models.IntegerField(unique=True)
    file_name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    extension = models.CharField(max_length=20, blank=True, null=True)
    file_size = models.CharField(max_length=50, blank=True, null=True)
    seq_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_report_attachments'


class ServiceReportExtfields(models.Model):
    reportno = models.IntegerField()
    orginc = models.IntegerField()
    stage_fail = models.IntegerField()
    engineercode_multiple = models.CharField(max_length=1000, blank=True, null=True)
    mainttype = models.IntegerField()
    loc_non_avf_rom = models.CharField(max_length=100, blank=True, null=True)
    loc_non_avf_to = models.CharField(max_length=100, blank=True, null=True)
    levelofinci = models.IntegerField()
    item_repl = models.CharField(max_length=1000, blank=True, null=True)
    probelm_desc_cust = models.TextField(blank=True, null=True)
    atta = models.CharField(max_length=100, blank=True, null=True)
    incirel = models.IntegerField()
    inccharge = models.CharField(max_length=50, blank=True, null=True)
    fstatus = models.CharField(max_length=50, blank=True, null=True)
    locavail = models.CharField(max_length=100, blank=True, null=True)
    eqavail = models.CharField(max_length=100, blank=True, null=True)
    eqproject = models.CharField(max_length=100, blank=True, null=True)
    buavail = models.CharField(max_length=100, blank=True, null=True)
    rakavail = models.CharField(max_length=100, blank=True, null=True)
    rakavail_fromdate = models.CharField(max_length=100, blank=True, null=True)
    rakavail_todate = models.CharField(max_length=100, blank=True, null=True)
    mttr = models.CharField(max_length=100, blank=True, null=True)
    eqavb = models.CharField(max_length=100, blank=True, null=True)
    buavb = models.CharField(max_length=100, blank=True, null=True)
    ralavb = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'service_report_extfields'


class ServiceScrapNtry(models.Model):
    reportno = models.IntegerField()
    scrapmat = models.CharField(max_length=11, blank=True, null=True)
    scrapslno = models.CharField(max_length=30, blank=True, null=True)
    scrapreason = models.CharField(max_length=300, blank=True, null=True)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'service_scrap_ntry'


class ServiceScrapdata(models.Model):
    reportno = models.IntegerField()
    disp_matcode = models.CharField(max_length=100, blank=True, null=True)
    disp_qty = models.CharField(max_length=50, blank=True, null=True)
    scrp_wrnty = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_scrapdata'


class ServiceSubassemblies(models.Model):
    sno = models.AutoField(primary_key=True)
    servicereportno = models.PositiveBigIntegerField(blank=True, null=True)
    fitemdesc = models.CharField(max_length=100, blank=True, null=True)
    fitemsno = models.CharField(max_length=45, blank=True, null=True)
    fitemmcode = models.CharField(max_length=20, blank=True, null=True)
    replaceditemsno = models.CharField(max_length=20, blank=True, null=True)
    dtf_mnf = models.CharField(max_length=50, blank=True, null=True)
    replaced_item_tested_date = models.CharField(max_length=50, blank=True, null=True)
    ref_sa_code = models.TextField(blank=True, null=True)
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()
    repeat = models.IntegerField()
    service_status = models.IntegerField()
    third_type = models.IntegerField()
    broght_type = models.IntegerField()
    failedamcstatus = models.CharField(max_length=150, blank=True, null=True)
    delete1 = models.IntegerField()
    comments = models.CharField(max_length=200, blank=True, null=True)
    production_rec_date = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'service_subassemblies'


class ServiceTypeMstr(models.Model):
    slno = models.AutoField(primary_key=True)
    catname = models.CharField(max_length=1000, blank=True, null=True)
    cat_type_master = models.CharField(max_length=200, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_type_mstr'


class Sess(models.Model):
    user = models.CharField(max_length=50)
    terminal = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    sess = models.CharField(max_length=50)
    date = models.DateField()
    ip = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sess'


class Sgtn2BSentMaster(models.Model):
    dept_desc = models.CharField(max_length=30)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sgtn_2b_sent_master'


class SgtnB4AftrImage(models.Model):
    slno = models.IntegerField()
    ext = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    size = models.CharField(max_length=10, blank=True, null=True)
    sts = models.CharField(max_length=2)
    seq_slno = models.AutoField(primary_key=True)
    delete1 = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sgtn_b4_aftr_image'


class SgtnBlobMaster(models.Model):
    sgtn_no = models.CharField(max_length=20)
    ext = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=150)
    size = models.IntegerField()
    createdby = models.IntegerField()
    atchmnt_sts = models.IntegerField()
    sgtn_slno = models.IntegerField()
    file_name = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sgtn_blob_master'


class SgtnEdprdNtry(models.Model):
    sgtn_no = models.CharField(max_length=20)
    empcode = models.IntegerField()
    dtls = models.CharField(max_length=500)
    amt = models.FloatField()
    pd_date = models.DateField()
    entered_by = models.IntegerField()
    edprd_sts = models.IntegerField()
    edprd = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sgtn_edprd_ntry'


class SgtnGradeMaster(models.Model):
    sgtn_grd_no = models.AutoField(primary_key=True)
    sgtn_grd_name = models.CharField(max_length=50)
    amt = models.FloatField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sgtn_grade_master'


class SgtnImprmntMaster(models.Model):
    sgtn_no = models.AutoField(primary_key=True)
    sgtn_type = models.CharField(max_length=30)
    sgtn_sub_type = models.CharField(max_length=50)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sgtn_imprmnt_master'


class SgtnNtry(models.Model):
    slno = models.AutoField(primary_key=True)
    sgtn_no = models.CharField(max_length=20)
    empcode = models.IntegerField()
    dept = models.IntegerField()
    loc = models.CharField(max_length=20)
    prjct = models.CharField(max_length=50)
    any_prjct = models.CharField(max_length=100)
    sgtn = models.TextField()
    type_imprmnt = models.CharField(max_length=50)
    any_imprmnt = models.CharField(max_length=100)
    usr_ntry_date = models.DateField()
    fsave = models.CharField(max_length=1)
    vrjct = models.CharField(max_length=20)
    rej_rsn = models.CharField(max_length=1000)
    hod = models.IntegerField()
    hod_date = models.DateField()
    src_rcvd_date = models.DateField()
    whm2snd = models.IntegerField()
    src_cmnts = models.CharField(max_length=1000)
    dnd_acc_rej = models.IntegerField()
    dnd_cmnts = models.CharField(max_length=1500)
    rsp_emp = models.IntegerField()
    ynt_addr = models.CharField(max_length=500)
    src_grd = models.IntegerField()
    src_rjct_rsn = models.CharField(max_length=300)
    src_fsblty = models.CharField(max_length=1000)
    src_qnt_bnft = models.CharField(max_length=1000)
    src_qnt_bnft_othr = models.CharField(max_length=300)
    src_impl_rspblty = models.CharField(max_length=250)
    src_trgt_date = models.DateField()
    src_impl_sts = models.CharField(max_length=10)
    src_impl_date = models.DateField()
    src_rcvd_by = models.IntegerField()
    edprd = models.IntegerField()
    fnl_rprt = models.IntegerField()
    pd_sts = models.IntegerField()
    to_b_sent = models.CharField(max_length=20)
    to_b_sent_cmnts = models.CharField(max_length=500)
    number_2_b_snt_acc_rej = models.IntegerField(db_column='2_b_snt_acc_rej')  # Field renamed because it wasn't a valid Python identifier.
    number_2_b_snt_acc_rej_cmnts = models.CharField(db_column='2_b_snt_acc_rej_cmnts', max_length=500)  # Field renamed because it wasn't a valid Python identifier.
    bnfts = models.CharField(max_length=500)
    clr = models.CharField(max_length=20)
    paid = models.IntegerField()
    paid_date = models.DateField()
    prcs_resp = models.IntegerField()
    paid_sts = models.CharField(max_length=2)
    number_2_b_snt_frwrd_date = models.DateField(db_column='2_b_snt_frwrd_date')  # Field renamed because it wasn't a valid Python identifier.
    mvd_sts = models.IntegerField()
    crtfct = models.IntegerField()
    crtfct_date = models.DateField()
    kss_sts = models.IntegerField()
    delete1 = models.IntegerField()
    delete_details = models.CharField(max_length=50)
    cmpltd_date = models.DateField()
    number_2_b_snt_accrej_date = models.DateField(db_column='2_b_snt_accrej_date')  # Field renamed because it wasn't a valid Python identifier.
    sugg_type = models.IntegerField()
    src_sts = models.CharField(max_length=1)
    number_2_b_impltd = models.CharField(db_column='2_b_impltd', max_length=50)  # Field renamed because it wasn't a valid Python identifier.
    priority = models.IntegerField()
    sugg_cert_event_date = models.DateField()
    edp_target_date = models.DateField()
    sgtn_status = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sgtn_ntry'


class SgtnPrizes(models.Model):
    empcode = models.IntegerField()
    dept = models.IntegerField()
    kaizens = models.IntegerField()
    ntry_datefrom = models.DateField(db_column='ntry_dateFrom')  # Field name made lowercase.
    ntry_dateto = models.DateField(db_column='ntry_dateTo')  # Field name made lowercase.
    auto_inc = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'sgtn_prizes'


class SgtnProcRespMaster(models.Model):
    empcode = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sgtn_proc_resp_master'


class SgtnQntfctnMaster(models.Model):
    sgtn_qntfcn_no = models.AutoField(primary_key=True)
    sgtn_qntfcn_name = models.CharField(max_length=100)
    sgtn_qntfcn_nick_name = models.CharField(max_length=1)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sgtn_qntfctn_master'


class SgtnStatusMaster(models.Model):
    slno = models.IntegerField()
    status = models.CharField(max_length=20)
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sgtn_status_master'


class SgtnTypeMaster(models.Model):
    sgtn_type = models.CharField(max_length=1)
    sgtn_desc = models.CharField(max_length=30)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sgtn_type_master'


class SkillFieldMaster(models.Model):
    field_id = models.AutoField(primary_key=True)
    field_value = models.CharField(max_length=50, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)
    input = models.CharField(max_length=600, blank=True, null=True)
    createdby = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateField()
    cert_id = models.IntegerField()
    skill = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skill_field_master'


class SkillFieldMasterv1(models.Model):
    field_id = models.AutoField(primary_key=True)
    field_value = models.CharField(max_length=50, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)
    createdby = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateField()
    cert_id = models.IntegerField()
    skill = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skill_field_masterV1'


class SkillFields(models.Model):
    skill_id = models.IntegerField(primary_key=True)
    field_name = models.CharField(max_length=50)
    createdby = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'skill_fields'


class StatusMaster(models.Model):
    st_code = models.CharField(max_length=10)
    st_desc = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'status_master'


class StoresMaster(models.Model):
    uniq_slno = models.IntegerField()
    matnr = models.CharField(max_length=11)
    desc = models.CharField(max_length=50)
    qty = models.IntegerField()
    slno = models.IntegerField()
    color_code = models.CharField(max_length=20)
    size = models.IntegerField()
    bold = models.CharField(max_length=1)
    italic = models.CharField(max_length=1)
    under_line = models.CharField(max_length=1)
    align = models.CharField(max_length=1)
    mat_color = models.CharField(max_length=10)
    mat_size = models.IntegerField()
    mat_bold = models.CharField(max_length=1)
    mat_italic = models.CharField(max_length=1)
    mat_unln = models.CharField(max_length=1)
    mat_align = models.CharField(max_length=1)
    desc_color = models.CharField(max_length=10)
    desc_size = models.IntegerField()
    desc_bold = models.CharField(max_length=1)
    desc_italic = models.CharField(max_length=1)
    desc_unln = models.CharField(max_length=1)
    desc_align = models.CharField(max_length=1)
    qty_color = models.CharField(max_length=10)
    qty_size = models.IntegerField()
    qty_bold = models.CharField(max_length=1)
    qty_italic = models.CharField(max_length=1)
    qty_unln = models.CharField(max_length=1)
    qty_align = models.CharField(max_length=1)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stores_master'


class StoresTemp(models.Model):
    matnr = models.CharField(max_length=11)
    desc = models.CharField(max_length=60)
    qty = models.IntegerField()
    slno = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'stores_temp'


class SubAssyNtry(models.Model):
    sinofrom = models.CharField(max_length=150, blank=True, null=True)
    sito = models.CharField(max_length=150, blank=True, null=True)
    modification_text = models.DateField()
    entry_text = models.CharField(max_length=150, blank=True, null=True)
    reference = models.CharField(max_length=150, blank=True, null=True)
    ecr = models.CharField(max_length=150, blank=True, null=True)
    cpa = models.CharField(max_length=150, blank=True, null=True)
    mail = models.CharField(max_length=150, blank=True, null=True)
    project = models.CharField(max_length=150, blank=True, null=True)
    sub_project = models.CharField(db_column='sub_Project', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sub_assy_code = models.CharField(max_length=150, blank=True, null=True)
    short_text = models.CharField(max_length=150, blank=True, null=True)
    mdetails = models.CharField(max_length=150, blank=True, null=True)
    sticker_details = models.CharField(max_length=150, blank=True, null=True)
    scope_change = models.CharField(db_column='scope_Change', max_length=150, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(max_length=150, blank=True, null=True)
    attachment = models.CharField(max_length=150, blank=True, null=True)
    reports = models.CharField(max_length=150, blank=True, null=True)
    moved_internet = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sub_assy_ntry'


class SubTr(models.Model):
    tag_no = models.IntegerField()
    pr_desc = models.TextField(blank=True, null=True)
    date = models.DateField()
    remarks = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.IntegerField()
    re_assigned = models.IntegerField()
    slno = models.AutoField(primary_key=True)
    hod_sts = models.IntegerField()
    usr_cmnts = models.CharField(max_length=1000, blank=True, null=True)
    usr_dt = models.DateField()
    usr_sts = models.IntegerField()
    timestamp = models.DateTimeField()
    report_time = models.TimeField()
    mail2rqstnr = models.IntegerField()
    auto_mail_bg_date = models.DateField()
    auto_mail_bg_times = models.IntegerField()
    auto_mail_bg_history = models.CharField(max_length=1000, blank=True, null=True)
    draft_sts = models.IntegerField()
    pr_cmpltd_date = models.DateField()
    pr_cmpltd_date_changed = models.DateField()
    kaizen = models.TextField(blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sub_tr'


class SubTr1(models.Model):
    tag_no = models.IntegerField()
    pr_desc = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateField()
    remarks = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.IntegerField()
    re_assigned = models.IntegerField()
    slno = models.AutoField(primary_key=True)
    hod_sts = models.IntegerField()
    usr_cmnts = models.CharField(max_length=1000, blank=True, null=True)
    usr_dt = models.DateField()
    usr_sts = models.IntegerField()
    timestamp = models.DateTimeField()
    report_time = models.TimeField()
    mail2rqstnr = models.IntegerField()
    auto_mail_bg_date = models.DateField()
    auto_mail_bg_times = models.IntegerField()
    auto_mail_bg_history = models.CharField(max_length=1000, blank=True, null=True)
    draft_sts = models.IntegerField()
    pr_cmpltd_date = models.DateField()
    pr_cmpltd_date_changed = models.DateField()
    kaizen = models.TextField(blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sub_tr1'


class SubTrOld(models.Model):
    tag_no = models.IntegerField()
    pr_desc = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateField()
    remarks = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.IntegerField()
    re_assigned = models.IntegerField()
    slno = models.AutoField(primary_key=True)
    hod_sts = models.IntegerField()
    usr_cmnts = models.CharField(max_length=1000, blank=True, null=True)
    usr_dt = models.DateField()
    usr_sts = models.IntegerField()
    timestamp = models.DateTimeField()
    report_time = models.TimeField()
    mail2rqstnr = models.IntegerField()
    auto_mail_bg_date = models.DateField()
    auto_mail_bg_times = models.IntegerField()
    auto_mail_bg_history = models.CharField(max_length=1000, blank=True, null=True)
    draft_sts = models.IntegerField()
    pr_cmpltd_date = models.DateField()
    pr_cmpltd_date_changed = models.DateField()
    kaizen = models.TextField(blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sub_tr_old'


class Subassemblies(models.Model):
    sno = models.AutoField(primary_key=True)
    reworkreportno = models.BigIntegerField()
    matcode_multi = models.CharField(max_length=250)
    from_loc = models.CharField(max_length=100)
    to_loc = models.CharField(max_length=100)
    dept_from = models.IntegerField()
    sa_dept = models.IntegerField()
    fitemdesc = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=150, blank=True, null=True)
    fitemmcode = models.CharField(max_length=20, blank=True, null=True)
    ritemsno = models.CharField(max_length=20, blank=True, null=True)
    fitemsno = models.CharField(max_length=1000, blank=True, null=True)
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()
    rd_mat = models.CharField(max_length=20)
    sno_wise = models.IntegerField()
    ass_rej_qty = models.IntegerField()
    sa_qty = models.IntegerField()
    replaced_item_tested_date = models.DateField()
    eq_test_by_multi = models.IntegerField()
    eq_test_date_multi = models.DateField()
    sareworkdetails_multi = models.TextField(blank=True, null=True)
    ass_dept_to = models.IntegerField()
    analysis_levels_sa = models.IntegerField()
    route_from_date = models.DateField()
    route_date = models.DateField()
    route_value = models.IntegerField()
    route_value_sub = models.IntegerField()
    hod_sts = models.CharField(max_length=15)
    sa_time = models.CharField(max_length=100)
    fapcbmfg = models.CharField(max_length=100)
    pcb_test_date = models.CharField(max_length=100)
    rework_time = models.CharField(max_length=100)
    reason_delay = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    type = models.IntegerField()
    db_type = models.IntegerField()
    type_ref = models.IntegerField()
    service_report_no = models.IntegerField()
    other_dept_pend = models.IntegerField()
    masterslno = models.IntegerField()
    analysis_comp = models.IntegerField()
    master_slno = models.CharField(max_length=100)
    attachment = models.CharField(max_length=1000)
    delete1 = models.IntegerField()
    any_other_rework = models.IntegerField()
    other_reqork_no = models.IntegerField()
    conclusion = models.CharField(max_length=200)
    card_disposal = models.IntegerField()
    material_slno = models.IntegerField()
    matcode_qty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subassemblies'


class SubcatMaster(models.Model):
    cat_code = models.IntegerField()
    scat_code = models.AutoField(primary_key=True)
    s_desc = models.CharField(max_length=100)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subcat_master'


class SuggFacNtry(models.Model):
    sno = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    ntry_date = models.DateField()
    category = models.CharField(max_length=11)
    project = models.IntegerField()
    curr_prob = models.CharField(max_length=200)
    suggestion = models.CharField(max_length=200)
    tangile = models.CharField(max_length=200)
    intangile = models.CharField(max_length=200)
    attachment = models.CharField(max_length=100)
    createdby = models.IntegerField()
    status = models.IntegerField()
    lpo_status = models.IntegerField()
    lpo_emp = models.IntegerField()
    lpo_comm = models.CharField(max_length=100)
    lpofile = models.CharField(max_length=100)
    lpo_date = models.DateField()
    edp_sts = models.IntegerField()
    edprod = models.IntegerField()
    edp_comm = models.CharField(max_length=200)
    edp_date = models.DateField()
    impl_comm = models.CharField(max_length=200)
    impl_date = models.DateField()
    complete = models.IntegerField()
    rwd_amt = models.IntegerField()
    process_attach = models.CharField(max_length=100)
    impl_ntry = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sugg_fac_ntry'


class SuggFacStsMstr(models.Model):
    sid = models.AutoField(primary_key=True)
    status = models.CharField(max_length=30)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sugg_fac_sts_mstr'


class SupplierMaster(models.Model):
    supplier_code = models.CharField(primary_key=True, max_length=8)
    supplier_name = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    createdby = models.CharField(max_length=40, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'supplier_master'


class TarqueMeterMaster(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    model = models.CharField(max_length=20)
    slno = models.CharField(max_length=20)
    desc_g = models.CharField(max_length=100)
    mod_g = models.CharField(max_length=100)
    code_g = models.CharField(max_length=100)
    accu_g = models.CharField(max_length=100)
    range_g = models.CharField(max_length=100)
    cal_on_g = models.DateField()
    cal_due_g = models.CharField(max_length=10)
    cal_months_g = models.IntegerField()
    desc_i = models.CharField(max_length=100)
    mod_i = models.CharField(max_length=100)
    code_i = models.CharField(max_length=100)
    accu_i = models.CharField(max_length=100)
    range_i = models.CharField(max_length=100, blank=True, null=True)
    cal_valid_i = models.DateField()
    trace_i = models.CharField(max_length=100, blank=True, null=True)
    cert_no = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    sdno = models.CharField(max_length=100, blank=True, null=True)
    loc = models.CharField(max_length=30, blank=True, null=True)
    instru_condi = models.CharField(max_length=100)
    acc_limits = models.CharField(max_length=100, blank=True, null=True)
    room_temp = models.IntegerField()
    disp_act = models.CharField(max_length=200, blank=True, null=True)
    ntry_date = models.DateField()
    ntryby = models.IntegerField()
    make = models.CharField(max_length=150, blank=True, null=True)
    timestamp = models.DateTimeField()
    calib_by = models.CharField(max_length=6, blank=True, null=True)
    approved_by = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarque_meter_master'


class TarqueMeterMasterNtry(models.Model):
    uniq_slno = models.IntegerField()
    scale = models.IntegerField()
    set = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    values = models.CharField(max_length=150, blank=True, null=True)
    sigma = models.FloatField()
    max_a = models.FloatField()
    min_b = models.FloatField()
    c = models.FloatField()
    a_b = models.FloatField()
    per = models.FloatField()
    ntryby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tarque_meter_master_ntry'


class TblEmployee(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    gender = models.CharField(max_length=10)
    designation = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_employee'


class TblEmployeeOld(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=11, blank=True, null=True)
    designation = models.CharField(max_length=20, blank=True, null=True)
    age = models.CharField(max_length=11, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_employee_old'


class TcodeMaster(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    tcode = models.CharField(max_length=50, blank=True, null=True)
    desc = models.CharField(max_length=200, blank=True, null=True)
    createduser = models.CharField(max_length=7, blank=True, null=True)
    createdby = models.IntegerField()
    created_date = models.DateField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField(blank=True, null=True)
    delete_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'tcode_master'


class TestDetails(models.Model):
    no = models.AutoField(db_column='No', primary_key=True)  # Field name made lowercase.
    material_number = models.CharField(max_length=20, blank=True, null=True)
    heading = models.CharField(max_length=200, blank=True, null=True)
    subheading = models.CharField(max_length=500, blank=True, null=True)
    test = models.CharField(max_length=500, blank=True, null=True)
    acceptance = models.CharField(max_length=500, blank=True, null=True)
    sf = models.CharField(max_length=20)
    rev = models.CharField(max_length=5)
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'test_details'


class TestEntry(models.Model):
    report_id_main = models.IntegerField()
    reportno = models.PositiveBigIntegerField(blank=True, null=True)
    material_number = models.CharField(max_length=20)
    model_number = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    heading = models.CharField(max_length=200, blank=True, null=True)
    subheading = models.CharField(max_length=200, blank=True, null=True)
    test = models.CharField(max_length=500)
    acceptance = models.CharField(max_length=500)
    result = models.CharField(max_length=50, blank=True, null=True)
    instid = models.CharField(max_length=30)
    empname = models.CharField(max_length=40, blank=True, null=True)
    testdate = models.DateField(blank=True, null=True)
    authorisedby = models.CharField(max_length=40, blank=True, null=True)
    authoriseddate = models.DateField(blank=True, null=True)
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()
    dummy = models.AutoField(primary_key=True)
    empcode_date = models.TextField()
    reporttype = models.CharField(max_length=50)
    report_type_inc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'test_entry'




class TestPdfreportEntry(models.Model):
    ref = models.CharField(max_length=3)
    sfrev = models.IntegerField()
    cardslno = models.IntegerField()
    unit_no = models.IntegerField()
    prodno = models.IntegerField()
    loc_code = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    stage = models.CharField(max_length=2)
    delete1 = models.CharField(max_length=1)
    mail = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'test_pdfreport_entry'


class TestPdfreportEntry080822(models.Model):
    ref = models.CharField(max_length=3)
    sfrev = models.IntegerField()
    cardslno = models.IntegerField()
    unit_no = models.IntegerField()
    prodno = models.IntegerField()
    loc_code = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    stage = models.CharField(max_length=2)
    delete1 = models.CharField(max_length=1)
    mail = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'test_pdfreport_entry_08_08_22'


class TestPdfreportTrans(models.Model):
    tid = models.AutoField(primary_key=True)
    id = models.IntegerField()
    stage = models.CharField(max_length=1)
    field = models.CharField(max_length=10)
    value = models.CharField(max_length=200)
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'test_pdfreport_trans'


class TestStudent(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    city = models.CharField(max_length=10)
    email = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'test_student'


class TestTableTwofields(models.Model):
    project = models.CharField(db_column='Project', max_length=100)  # Field name made lowercase.
    cc = models.CharField(db_column='CC', max_length=50)  # Field name made lowercase.
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'test_table_twofields'


class TestdriveNtry(models.Model):
    project = models.IntegerField()
    doc_no = models.CharField(max_length=100)
    description = models.TextField()
    revision_no = models.IntegerField()
    attachment = models.CharField(max_length=150)
    date = models.DateField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'testdrive_ntry'


class TestingReportMasterEntry(models.Model):
    report_id = models.AutoField(primary_key=True)
    production_no = models.IntegerField(blank=True, null=True)
    material_code = models.CharField(max_length=20, blank=True, null=True)
    model_number = models.BigIntegerField(blank=True, null=True)
    inspected_by = models.CharField(max_length=50, blank=True, null=True)
    approved_date = models.DateField(blank=True, null=True)
    serialnumber = models.IntegerField()
    card_sl_no = models.CharField(max_length=20)
    mvstb = models.CharField(max_length=20)
    finalsave = models.CharField(max_length=5)
    start_time = models.TimeField()
    end_time = models.TimeField()
    tot_time = models.TimeField()
    sfcode = models.CharField(max_length=20)
    rev = models.CharField(max_length=20)
    result = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    createdby = models.BigIntegerField()
    auto_calcu = models.CharField(max_length=20)
    auto_calcu_status = models.CharField(max_length=10)
    auto_calcu_date = models.DateField()
    reporttype = models.CharField(max_length=50)
    report_type_inc = models.IntegerField()
    inter_exter = models.CharField(max_length=10)
    instrumentids = models.TextField()
    note = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'testing_report_master_entry'


class TestingUserTime(models.Model):
    order_no = models.IntegerField()
    mat_code = models.CharField(max_length=20)
    unit_slno = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    tot_time = models.TimeField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'testing_user_time'


class TestingpdfMaster(models.Model):
    type = models.AutoField(primary_key=True)
    category = models.CharField(max_length=1)
    name = models.CharField(max_length=50)
    unit_code = models.BigIntegerField()
    sf_no = models.CharField(max_length=15)
    sf_rev = models.IntegerField()
    card_code = models.BigIntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'testingpdf_master'


class TestingpdfMaster080822(models.Model):
    type = models.AutoField(primary_key=True)
    category = models.CharField(max_length=1)
    name = models.CharField(max_length=50)
    unit_code = models.BigIntegerField()
    sf_no = models.CharField(max_length=15)
    sf_rev = models.IntegerField()
    card_code = models.BigIntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'testingpdf_master_08_08_22'


class Testingpdfs(models.Model):
    ref = models.IntegerField()
    sfrev = models.IntegerField()
    cardslno = models.IntegerField()
    unit_no = models.IntegerField()
    prodno = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    date = models.DateField()
    m1 = models.FloatField()
    m2 = models.FloatField()
    m3 = models.FloatField()
    m4 = models.FloatField()
    m5 = models.FloatField()
    m6 = models.FloatField()
    m7 = models.FloatField()
    m8 = models.FloatField()
    m9 = models.FloatField()
    m10 = models.FloatField()
    m11 = models.FloatField()
    m12 = models.FloatField()
    m13 = models.FloatField()
    s429 = models.CharField(max_length=20)
    s10 = models.CharField(max_length=20)
    s11 = models.CharField(max_length=20)
    s12 = models.CharField(max_length=20)
    check12 = models.CharField(max_length=10)
    xfor1 = models.FloatField()
    xfor2 = models.FloatField()
    xfor3 = models.FloatField()
    xfor4 = models.FloatField()
    xfor5 = models.FloatField()
    xrev6 = models.FloatField()
    xrev7 = models.FloatField()
    xrev8 = models.FloatField()
    xrev9 = models.FloatField()
    xrev10 = models.FloatField()
    afor1 = models.FloatField()
    afor2 = models.FloatField()
    afor3 = models.FloatField()
    afor4 = models.FloatField()
    afor5 = models.FloatField()
    arev6 = models.FloatField()
    arev7 = models.FloatField()
    arev8 = models.FloatField()
    arev9 = models.FloatField()
    arev10 = models.FloatField()
    yfor1 = models.FloatField()
    yfor2 = models.FloatField()
    yfor3 = models.FloatField()
    yfor4 = models.FloatField()
    yfor5 = models.FloatField()
    yrev6 = models.FloatField()
    yrev7 = models.FloatField()
    yrev8 = models.FloatField()
    yrev9 = models.FloatField()
    yrev10 = models.FloatField()
    bfor1 = models.FloatField()
    bfor2 = models.FloatField()
    bfor3 = models.FloatField()
    bfor4 = models.FloatField()
    bfor5 = models.FloatField()
    brev6 = models.FloatField()
    brev7 = models.FloatField()
    brev8 = models.FloatField()
    brev9 = models.FloatField()
    brev10 = models.FloatField()
    scan2nd = models.CharField(max_length=20)
    empcode1 = models.IntegerField()
    empcode2 = models.IntegerField()
    empcode3 = models.IntegerField()
    empcode4 = models.IntegerField()
    empcode5 = models.IntegerField()
    assign_empcode = models.IntegerField()
    measure18 = models.FloatField()
    measure19 = models.FloatField()
    scan18 = models.CharField(max_length=20)
    scan19 = models.CharField(max_length=20)
    scan20 = models.CharField(max_length=20)
    scan21 = models.CharField(max_length=20)
    scan22 = models.CharField(max_length=20)
    scan23 = models.CharField(max_length=20)
    scan24 = models.CharField(max_length=20)
    check15 = models.CharField(max_length=10)
    check16 = models.CharField(max_length=10)
    check17 = models.CharField(max_length=10)
    check19 = models.CharField(max_length=10)
    check20 = models.CharField(max_length=10)
    check31 = models.IntegerField()
    check32 = models.IntegerField()
    a1 = models.FloatField()
    a2 = models.FloatField()
    a3 = models.FloatField()
    a4 = models.FloatField()
    a5 = models.FloatField()
    a6 = models.FloatField()
    b1 = models.FloatField()
    b2 = models.FloatField()
    b3 = models.FloatField()
    b4 = models.FloatField()
    b5 = models.FloatField()
    b6 = models.FloatField()
    c1 = models.FloatField()
    c2 = models.FloatField()
    c3 = models.FloatField()
    c4 = models.FloatField()
    c5 = models.FloatField()
    c6 = models.FloatField()
    ins = models.TextField()
    lastdate = models.DateField()
    stage1 = models.IntegerField()
    stage2 = models.IntegerField()
    stage3 = models.IntegerField()
    stage4 = models.IntegerField()
    stage5 = models.IntegerField()
    delete1 = models.IntegerField()
    mail = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'testingpdfs'


class TestingreportMaster(models.Model):
    material_code = models.CharField(max_length=20)
    sfcode = models.CharField(max_length=100)
    test_properties = models.IntegerField()
    note = models.TextField()
    rev = models.CharField(max_length=5)
    title = models.CharField(max_length=100)
    prpd = models.CharField(max_length=20)
    chkd = models.CharField(max_length=20)
    appd = models.CharField(max_length=20)
    date = models.CharField(max_length=12)
    instrmno = models.IntegerField()
    instrumentids = models.CharField(max_length=300)
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'testingreport_master'


class TestjigsMaster(models.Model):
    testjigcode = models.CharField(primary_key=True, max_length=30)
    testjigname = models.CharField(max_length=50, blank=True, null=True)
    dept = models.IntegerField()
    createdby = models.CharField(max_length=40, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'testjigs_master'


class TestreportFields(models.Model):
    fid = models.AutoField(primary_key=True)
    trid = models.IntegerField()
    field_name = models.CharField(max_length=20, blank=True, null=True)
    field_val = models.CharField(max_length=100, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'testreport_fields'


class TestreportNtry(models.Model):
    trid = models.AutoField(primary_key=True)
    prjid = models.IntegerField()
    result = models.CharField(max_length=10, blank=True, null=True)
    instr_id = models.CharField(max_length=20, blank=True, null=True)
    testtedby = models.IntegerField(db_column='testtedBy')  # Field name made lowercase.
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'testreport_ntry'


class TestreportPrj(models.Model):
    prjid = models.AutoField(primary_key=True)
    prj_name = models.CharField(max_length=100, blank=True, null=True)
    sfno = models.CharField(max_length=30, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'testreport_prj'


class TestreportPrjMaster(models.Model):
    flid = models.AutoField(primary_key=True)
    prjid = models.IntegerField()
    seq_no = models.IntegerField()
    test = models.CharField(max_length=200, blank=True, null=True)
    acc_cri = models.CharField(max_length=200, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'testreport_prj_master'


class Testtable(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    age = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'testtable'


class TiffinMaster(models.Model):
    slno = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50)
    date = models.DateField()
    loc = models.CharField(max_length=4)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tiffin_master'


class TorquePdfEntry(models.Model):
    slno = models.AutoField(primary_key=True)
    uniq_slno = models.IntegerField()
    std_dim = models.TextField()
    obs_val = models.FloatField()
    error = models.CharField(max_length=150)
    created_by = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'torque_pdf_entry'


class TourAdvEnty(models.Model):
    company_code = models.IntegerField()
    loc = models.CharField(max_length=100, blank=True, null=True)
    dept = models.IntegerField()
    adv_for = models.IntegerField()
    adv_for_act = models.IntegerField()
    zone = models.CharField(max_length=200, blank=True, null=True)
    shed = models.CharField(max_length=200, blank=True, null=True)
    product = models.CharField(max_length=500, blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
    bank_type = models.IntegerField()
    acc_no = models.CharField(max_length=100, blank=True, null=True)
    adv_req_amt = models.FloatField()
    pd_adv_amt = models.FloatField()
    pd_adv_reason = models.TextField(blank=True, null=True)
    track_sts = models.IntegerField()
    adm_sts = models.IntegerField()
    adm_empcode = models.IntegerField()
    adm_remarks = models.TextField(blank=True, null=True)
    adm_app_date = models.DateField()
    hod_sts = models.IntegerField()
    hod_code = models.IntegerField()
    hod_remarks = models.TextField(blank=True, null=True)
    hod_app_date = models.DateField()
    next_approve = models.IntegerField()
    acc_sts = models.IntegerField()
    acc_remarks = models.TextField(blank=True, null=True)
    acc_app_date = models.DateField()
    bill_type = models.IntegerField()
    bill_type_ref = models.IntegerField()
    vendor = models.CharField(max_length=500, blank=True, null=True)
    document_date = models.DateField()
    payment_doc = models.CharField(max_length=500, blank=True, null=True)
    payment_doc_date = models.DateField()
    check_no_cash = models.CharField(max_length=500, blank=True, null=True)
    check_date = models.DateField()
    clearing_date = models.DateField()
    file_status = models.IntegerField()
    file_posting_date = models.DateField()
    tour_from_date = models.DateField()
    tour_to_date = models.DateField()
    warrenty_type = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_adv_enty'


class TourAdvHistory(models.Model):
    slno = models.AutoField(primary_key=True)
    uniq_slno = models.IntegerField()
    empcode = models.IntegerField()
    date = models.DateField()
    status = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    modified_amount = models.FloatField()
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tour_adv_history'


class TourAdvTrackSts(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=200)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_adv_track_sts'


class TourAdvanceCategory(models.Model):
    slno = models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=200, blank=True, null=True)
    cat_full_name = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_advance_category'


class TourAdvanceLimit(models.Model):
    slno = models.AutoField(primary_key=True)
    loc = models.CharField(max_length=100, blank=True, null=True)
    dept = models.IntegerField()
    ass_code = models.IntegerField()
    cat = models.IntegerField()
    type = models.IntegerField()
    limit = models.FloatField()
    check_perm = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_advance_limit'


class TourAdvanceLimit1508(models.Model):
    slno = models.AutoField(primary_key=True)
    loc = models.CharField(max_length=100, blank=True, null=True)
    dept = models.IntegerField()
    ass_code = models.IntegerField()
    cat = models.IntegerField()
    type = models.IntegerField()
    limit = models.FloatField()
    check_perm = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_advance_limit_15-08'


class TourBankDetails(models.Model):
    empcode = models.IntegerField()
    bankname = models.CharField(max_length=50, blank=True, null=True)
    acc_no = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_bank_details'


class TourExtBillEntry(models.Model):
    entry_id = models.AutoField(primary_key=True)
    ext_or_int = models.CharField(max_length=50)
    empcode = models.IntegerField()
    tour_startdate = models.DateField()
    tour_returneddate = models.DateField()
    actual_amount = models.FloatField()
    approval_amount = models.FloatField()
    approved_to_be = models.IntegerField()
    bill_submsn_date = models.DateField()
    admin_code = models.CharField(max_length=100)
    rep_loc = models.CharField(max_length=100)
    rep_dept = models.CharField(max_length=100)
    ref_id = models.IntegerField()
    payment_doc = models.CharField(max_length=500)
    payment_doc_date = models.DateField()
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    status = models.IntegerField()
    gl_check = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_ext_bill_entry'


class TourExtCategories(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    categories = models.CharField(max_length=1000)
    parent = models.IntegerField()
    display = models.IntegerField()
    header_id = models.IntegerField()
    group_id = models.IntegerField()
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tour_ext_categories'


class TourExtCities(models.Model):
    city_id = models.IntegerField(primary_key=True)
    cities = models.CharField(max_length=50)
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tour_ext_cities'


class TourExtFields(models.Model):
    field_id = models.AutoField(primary_key=True)
    cat_id = models.IntegerField()
    field_name = models.CharField(max_length=100)
    display = models.CharField(max_length=100)
    file_type = models.IntegerField()
    header_id = models.IntegerField()
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tour_ext_fields'


class TourExtGlcodes(models.Model):
    glcode = models.IntegerField()
    cat_id = models.IntegerField()
    parent = models.IntegerField()
    desc = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tour_ext_glcodes'


class TourExtHistory(models.Model):
    slno = models.AutoField(primary_key=True)
    entry_id = models.IntegerField()
    cat_id = models.IntegerField()
    actual_amount = models.FloatField()
    cat_iterinary = models.IntegerField()
    empcode = models.IntegerField()
    date = models.DateField()
    status = models.IntegerField()
    approval_amount = models.FloatField()
    approvremark = models.CharField(max_length=400)
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tour_ext_history'


class TourExtNatureofvisit(models.Model):
    nature_id = models.AutoField(primary_key=True)
    purpose_of_visit = models.CharField(max_length=200)
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tour_ext_natureofvisit'


class TourExtRules(models.Model):
    tour_ext_rules_id = models.IntegerField(primary_key=True)
    cat_id = models.IntegerField()
    class_id = models.IntegerField()
    level = models.CharField(max_length=20)
    amount = models.CharField(max_length=50)
    type = models.IntegerField()
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tour_ext_rules'


class TourExtSubbill(models.Model):
    subbill_id = models.AutoField(primary_key=True)
    ext_or_int = models.CharField(max_length=50)
    entry_id = models.IntegerField()
    cat_iterinary = models.IntegerField()
    cat_id = models.IntegerField()
    sub_type = models.CharField(max_length=200)
    cat_value = models.CharField(max_length=200)
    amount_type = models.IntegerField()
    subref_id = models.IntegerField()
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tour_ext_subbill'


class TourExtTrackSts(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=200)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_ext_track_sts'


class TourExtTrackStsNew(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=200)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_ext_track_sts_new'


class TourPaymentAuth(models.Model):
    id = models.IntegerField(primary_key=True)
    dept = models.IntegerField()
    app_auth = models.IntegerField()
    petty_cash = models.FloatField()
    tour_cash = models.FloatField()
    created_by = models.IntegerField()
    timestamp = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_payment_auth'


class TourPendAmt(models.Model):
    companycode = models.IntegerField()
    empcode = models.AutoField(primary_key=True)
    adv_type = models.CharField(max_length=200, blank=True, null=True)
    amount = models.FloatField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_pend_amt'


class TrainingCatMaster(models.Model):
    cat_no = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'training_cat_master'


class TrainingCompanyMaster(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    addr = models.TextField()
    city = models.CharField(max_length=50, blank=True, null=True)
    contact = models.IntegerField()
    extn = models.IntegerField()
    url = models.CharField(max_length=50, blank=True, null=True)
    official_mail = models.CharField(max_length=50, blank=True, null=True)
    pin = models.IntegerField()
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'training_company_master'


class TrainingCoordinatorMaster(models.Model):
    coordinator = models.IntegerField()
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    del_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'training_coordinator_master'


class TrainingCourseMaster(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=200, blank=True, null=True)
    course_desc = models.TextField(blank=True, null=True)
    course_category = models.CharField(max_length=15, blank=True, null=True)
    course_credits = models.IntegerField()
    trainer_details = models.CharField(max_length=3, blank=True, null=True)
    trainer = models.CharField(max_length=50, blank=True, null=True)
    course_event_id = models.IntegerField()
    course_duration = models.CharField(max_length=15, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    dalete_date = models.CharField(max_length=20, blank=True, null=True)
    delete_reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'training_course_master'


class TrainingDisplayTypeMaster(models.Model):
    display_id = models.AutoField(primary_key=True)
    display_name = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'training_display_type_master'


class TrainingEventNtry(models.Model):
    event_id = models.AutoField(primary_key=True)
    course_id = models.IntegerField()
    events = models.IntegerField()
    start_date = models.DateField()
    start_time = models.CharField(max_length=8, blank=True, null=True)
    end_date = models.DateField()
    end_time = models.CharField(max_length=8, blank=True, null=True)
    dur_hrs = models.IntegerField()
    dur_mns = models.IntegerField()
    customer = models.CharField(max_length=3, blank=True, null=True)
    company_id = models.IntegerField()
    trainer = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.BigIntegerField()
    alt_contact = models.BigIntegerField()
    email = models.CharField(max_length=50, blank=True, null=True)
    hall_id = models.IntegerField()
    coordinator = models.IntegerField()
    event_location = models.CharField(max_length=5, blank=True, null=True)
    feedback_necessary = models.IntegerField()
    training_eval = models.IntegerField()
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'training_event_ntry'


class TrainingExtTrainerMaster(models.Model):
    ext_trainer_slno = models.AutoField(primary_key=True)
    trainer_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    addr = models.TextField()
    mobile = models.IntegerField()
    alt_contact = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'training_ext_trainer_master'


class TrainingHallMaster(models.Model):
    hall_id = models.AutoField(primary_key=True)
    hall_location = models.CharField(max_length=4, blank=True, null=True)
    hall_name = models.CharField(max_length=25, blank=True, null=True)
    hall_addr = models.TextField(blank=True, null=True)
    seating_capacity = models.CharField(max_length=20, blank=True, null=True)
    display_id = models.IntegerField()
    board_size = models.CharField(max_length=30, blank=True, null=True)
    extn_no = models.CharField(max_length=30, blank=True, null=True)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'training_hall_master'


class TrainingHistory(models.Model):
    event_id = models.IntegerField()
    nominee = models.IntegerField()
    date = models.DateField()
    hod = models.IntegerField()
    createdby = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'training_history'


class TrainingHoursMaster(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    loc = models.CharField(max_length=5)
    dept_series = models.IntegerField()
    desc = models.CharField(max_length=150)
    level = models.CharField(max_length=20)
    hours = models.IntegerField()
    ass_role = models.CharField(max_length=4)
    status = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'training_hours_master'


class TrainingIndEntry(models.Model):
    sno = models.AutoField(primary_key=True)
    ind_id = models.IntegerField()
    jsp_val = models.IntegerField()
    course_id = models.CharField(max_length=11, blank=True, null=True)
    others = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField(blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'training_ind_entry'


class TrainingIndcSubMaster(models.Model):
    cat_id = models.IntegerField()
    ind_sub_cat = models.CharField(max_length=500, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'training_indc_sub_master'


class TrainingIndctn(models.Model):
    ind_id = models.AutoField(primary_key=True)
    trainee = models.CharField(max_length=6, blank=True, null=True)
    carried_by = models.CharField(max_length=6, blank=True, null=True)
    carried_by1 = models.CharField(max_length=6, blank=True, null=True)
    gnrl_indc_date = models.DateField()
    gnrl_indc_date1 = models.CharField(max_length=250)
    doj = models.DateField()
    js_reprt = models.CharField(max_length=10, blank=True, null=True)
    loc = models.CharField(max_length=20, blank=True, null=True)
    dept = models.IntegerField(blank=True, null=True)
    gl = models.CharField(max_length=6, blank=True, null=True)
    gl_sts = models.IntegerField()
    hod = models.CharField(max_length=6, blank=True, null=True)
    hod_sts = models.IntegerField()
    hod_rmks = models.CharField(max_length=250, blank=True, null=True)
    gl_rmks = models.CharField(max_length=250, blank=True, null=True)
    hod_app_time = models.DateTimeField()
    timestamp = models.DateTimeField()
    created_by = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'training_indctn'


class TrainingIndctnMaster(models.Model):
    ind_id = models.AutoField(primary_key=True)
    induction_desc = models.CharField(max_length=300, blank=True, null=True)
    created_by = models.CharField(max_length=6, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'training_indctn_master'


class TrainingInductionMaster(models.Model):
    ind_id = models.IntegerField()
    jsp_sub_data = models.CharField(max_length=100, blank=True, null=True)
    sub_cnt = models.IntegerField()
    course_id = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'training_induction_master'


class TrainingJsEntry(models.Model):
    sno = models.AutoField(primary_key=True)
    id = models.IntegerField()
    it_main_data = models.CharField(max_length=300, blank=True, null=True)
    it_check_data = models.CharField(max_length=10, blank=True, null=True)
    it_sub_check_data = models.CharField(max_length=50, blank=True, null=True)
    others = models.TextField(blank=True, null=True)
    created_by = models.CharField(max_length=6, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'training_js_entry'


class TrainingJspMaster(models.Model):
    slno = models.AutoField(primary_key=True)
    it_main_data = models.IntegerField(blank=True, null=True)
    it_sub_check_data = models.IntegerField(blank=True, null=True)
    event_type = models.IntegerField(blank=True, null=True)
    delete1 = models.IntegerField(blank=True, null=True)
    timestamp = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'training_jsp_master'


class TrainingMeetingTemp(models.Model):
    empcode = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'training_meeting_temp'


class TrainingNomineeIndData(models.Model):
    slno = models.AutoField(primary_key=True)
    trainee = models.CharField(max_length=8, blank=True, null=True)
    event_type = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    status = models.CharField(max_length=50, blank=True, null=True)
    event_id = models.IntegerField()
    location = models.CharField(max_length=5, blank=True, null=True)
    dept = models.CharField(max_length=6, blank=True, null=True)
    created_by = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'training_nominee_ind_data'


class TrainingNomineeIndData1682021(models.Model):
    slno = models.AutoField(primary_key=True)
    trainee = models.CharField(max_length=8)
    event_type = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=50)
    event_id = models.IntegerField()
    location = models.CharField(max_length=5)
    dept = models.CharField(max_length=6)
    created_by = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'training_nominee_ind_data_16_8_2021'


class TrainingNomineeIndDataOld(models.Model):
    slno = models.AutoField(primary_key=True)
    trainee = models.CharField(max_length=8)
    event_type = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=50)
    event_id = models.IntegerField()
    location = models.CharField(max_length=5)
    dept = models.CharField(max_length=6)
    created_by = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'training_nominee_ind_data_old'


class TrainingNomineesAttendance(models.Model):
    event_id = models.IntegerField()
    nominee = models.IntegerField()
    attended_date = models.DateField()
    attended_time = models.CharField(max_length=5)
    status = models.CharField(max_length=1)
    dur_hrs = models.IntegerField()
    dur_mns = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    dalete_date = models.DateField()
    delete_reason = models.TextField()

    class Meta:
        managed = False
        db_table = 'training_nominees_attendance'


class TrainingNomineesNtry(models.Model):
    slno = models.AutoField(primary_key=True)
    event_id = models.IntegerField()
    nominee = models.IntegerField()
    date = models.DateField()
    type = models.CharField(max_length=1, blank=True, null=True)
    status = models.IntegerField()
    event_date = models.DateField()
    dept = models.IntegerField()
    loc = models.CharField(max_length=10, blank=True, null=True)
    hod = models.CharField(max_length=6, blank=True, null=True)
    pay_level = models.CharField(max_length=20, blank=True, null=True)
    created_by = models.IntegerField()
    pre_test_per = models.IntegerField()
    post_test_per = models.IntegerField()
    training_objectives = models.IntegerField()
    training_skill_learnt = models.IntegerField()
    overall = models.IntegerField()
    approved_by = models.IntegerField()
    approved_date = models.DateField()
    mail_status = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    dalete_date = models.DateField()
    delete_reason = models.TextField(blank=True, null=True)
    repeat_reason = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'training_nominees_ntry'


class TrainingOnJob(models.Model):
    job_uniq = models.AutoField(primary_key=True)
    emp_id = models.CharField(max_length=10, blank=True, null=True)
    trainer_id = models.CharField(max_length=10, blank=True, null=True)
    loc = models.CharField(max_length=20, blank=True, null=True)
    dept = models.CharField(max_length=20, blank=True, null=True)
    entry_date = models.DateField()
    job = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=50, blank=True, null=True)
    hod = models.CharField(max_length=10, blank=True, null=True)
    hod_date = models.DateField()
    hod_sts = models.IntegerField()
    rmks = models.TextField(blank=True, null=True)
    attachment = models.TextField(blank=True, null=True)
    task_new = models.IntegerField()
    created_by = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'training_on_job'


class TrainingOnJobCmnts(models.Model):
    uniq_id = models.AutoField(primary_key=True)
    job_uniq = models.IntegerField()
    category = models.CharField(max_length=30, blank=True, null=True)
    comments = models.CharField(max_length=300, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    from_date = models.DateField()
    to_date = models.DateField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'training_on_job_cmnts'


class TransationWelfare(models.Model):
    particulars = models.IntegerField()
    date_of_distri = models.DateField()
    status = models.IntegerField()
    comments = models.TextField()
    created_by = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transation_welfare'


class UnitLevelEntry(models.Model):
    from_field = models.CharField(db_column='from', max_length=11, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=11, blank=True, null=True)
    reference = models.CharField(max_length=11, blank=True, null=True)
    reference2 = models.CharField(max_length=150, blank=True, null=True)
    reference2num = models.CharField(max_length=150, blank=True, null=True)
    ecrdata = models.CharField(db_column='ecrData', max_length=11, blank=True, null=True)  # Field name made lowercase.
    subcategory = models.CharField(max_length=11, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    materialcode = models.CharField(max_length=11, blank=True, null=True)
    product_code = models.CharField(max_length=11, blank=True, null=True)
    subproject = models.CharField(max_length=150, blank=True, null=True)
    partserialnumber = models.CharField(db_column='partSerialNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    servicecompatability = models.TextField(db_column='serviceCompatability', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(blank=True, null=True)
    new_or_exist_code = models.CharField(max_length=11, blank=True, null=True)
    materialcode1 = models.CharField(max_length=11, blank=True, null=True)
    request_date_cft = models.DateField()
    request = models.CharField(max_length=150, blank=True, null=True)
    shorttext = models.CharField(max_length=250, blank=True, null=True)
    request_date_ffarm = models.DateField()
    scope = models.CharField(max_length=100, blank=True, null=True)
    revno = models.CharField(max_length=10, blank=True, null=True)
    wf = models.CharField(max_length=50, blank=True, null=True)
    details1 = models.CharField(max_length=100, blank=True, null=True)
    details = models.CharField(max_length=100, blank=True, null=True)
    drg = models.CharField(max_length=50, blank=True, null=True)
    mdesc = models.CharField(max_length=500, blank=True, null=True)
    sop = models.CharField(max_length=50)
    software = models.CharField(max_length=20, blank=True, null=True)
    material_code = models.CharField(max_length=300, blank=True, null=True)
    detailsofchanges = models.CharField(db_column='detailsOfChanges', max_length=252, blank=True, null=True)  # Field name made lowercase.
    requiredqty = models.CharField(max_length=50, blank=True, null=True)
    attachment1 = models.CharField(max_length=500, blank=True, null=True)
    attachment2 = models.CharField(max_length=500, blank=True, null=True)
    attachment3 = models.CharField(max_length=500, blank=True, null=True)
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    cpacomments = models.CharField(max_length=100)
    timestap = models.DateTimeField()
    moved_internet = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unit_level_entry'





class UnitTypeSubMaster(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    unit_slno = models.IntegerField()
    unit_name = models.CharField(max_length=50)
    unit_sub_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'unit_type_sub_master'


class UplodedFiles(models.Model):
    slno = models.AutoField(primary_key=True)
    formname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    ext = models.CharField(max_length=50)
    data = models.TextField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'uploded_files'


class UserBloodGroupMaster(models.Model):
    group = models.IntegerField()
    group_name = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_blood_group_master'


class UserCoffLapse(models.Model):
    empcode = models.IntegerField()
    days = models.FloatField()
    upto = models.DateField(blank=True, null=True)
    cate = models.CharField(max_length=5, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    update_by = models.IntegerField()
    update_timestamp = models.CharField(max_length=20, blank=True, null=True)
    delete1 = models.IntegerField()
    cid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'user_coff_lapse'



class UserCoffMaster(models.Model):
    bukrs = models.IntegerField()
    werks = models.CharField(max_length=4)
    stdaz = models.FloatField()
    uname = models.IntegerField()
    aedtm = models.DateTimeField()
    delete1 = models.IntegerField()
    uname1 = models.IntegerField()
    aedtm1 = models.DateField()
    delete_reason = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'user_coff_master'


class UserCountryMaster(models.Model):
    country = models.IntegerField()
    country_name = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_country_master'


class UserData(models.Model):
    dept_code = models.CharField(max_length=50)
    emp_code = models.IntegerField()
    date = models.DateField()
    worked_hrs = models.TimeField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user_data'


class UserEmpData(models.Model):
    dept_code = models.CharField(max_length=50)
    emp_code = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user_emp_data'


class UserEntryForm(models.Model):
    dept_code = models.IntegerField()
    date = models.DateField()
    emp_code = models.IntegerField()
    h1 = models.TimeField()
    pr1 = models.CharField(max_length=100)
    h2 = models.TimeField()
    pr2 = models.CharField(max_length=50)
    h3 = models.TimeField()
    pr3 = models.CharField(max_length=50)
    h4 = models.TimeField()
    pr4 = models.CharField(max_length=50)
    createdby = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_entry_form'


class UserExtnTemp(models.Model):
    empcode = models.IntegerField()
    extn = models.CharField(max_length=50)
    shrt = models.CharField(max_length=50)
    build_no = models.CharField(max_length=4)
    room_no = models.CharField(max_length=3)
    local_std_code = models.CharField(max_length=8)
    sys_no = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'user_extn_temp'


class UserGndrMaster(models.Model):
    gndr = models.IntegerField()
    gndr_name = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_gndr_master'


class UserGroupMaster(models.Model):
    empgroup = models.CharField(max_length=10)
    groupname = models.CharField(max_length=30)
    empsubgroup = models.CharField(max_length=10)
    subgroupname = models.CharField(max_length=30)
    uniq_slno = models.AutoField(primary_key=True)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_group_master'


class UserLanguMaster(models.Model):
    langu = models.IntegerField()
    langu_name = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_langu_master'


class UserLeaveApply(models.Model):
    empcode = models.IntegerField()
    apply_date = models.DateField()
    days = models.FloatField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    beguz = models.TimeField(blank=True, null=True)
    enduz = models.TimeField(blank=True, null=True)
    leave_type = models.CharField(max_length=5, blank=True, null=True)
    day_type = models.CharField(max_length=2, blank=True, null=True)
    reason = models.CharField(max_length=300, blank=True, null=True)
    ack = models.IntegerField()
    ack_inid = models.AutoField(primary_key=True)
    qms_no = models.IntegerField()
    sap_no = models.CharField(max_length=20)
    approve_status = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    delete_date = models.DateField(blank=True, null=True)
    delete_reason = models.CharField(max_length=150, blank=True, null=True)
    moved_sap = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'user_leave_apply'


class UserLeaveApplyAck(models.Model):
    ack = models.IntegerField(primary_key=True)
    empcode = models.IntegerField()
    apply_date = models.DateField(blank=True, null=True)
    apply_time = models.CharField(max_length=10, blank=True, null=True)
    days = models.FloatField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    delete_date = models.DateField(blank=True, null=True)
    delete_reason = models.CharField(max_length=150, blank=True, null=True)
    approved_by = models.IntegerField()
    approve_date = models.DateField(blank=True, null=True)
    approve_time = models.TimeField()
    approve_status = models.IntegerField()
    auto_approve = models.CharField(max_length=10, blank=True, null=True)
    reject_reason = models.CharField(max_length=100, blank=True, null=True)
    escalate_status = models.IntegerField()
    escalate_by = models.IntegerField(blank=True, null=True)
    cancel_timestamp = models.CharField(max_length=20, blank=True, null=True)
    cancel_reason = models.CharField(max_length=500, blank=True, null=True)
    approve_cancel_timestamp = models.CharField(max_length=20, blank=True, null=True)
    approve_cancel_reason = models.CharField(max_length=500, blank=True, null=True)
    resp_assign = models.CharField(max_length=200, blank=True, null=True)
    disabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_leave_apply_ack'





class UserLeaveApplyValid(models.Model):
    valid_id = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    apply_date = models.DateField()
    leave_date = models.DateField()
    beguz = models.TimeField()
    enduz = models.TimeField()
    leave_type = models.CharField(max_length=5, blank=True, null=True)
    day_type = models.CharField(max_length=2, blank=True, null=True)
    reason = models.CharField(max_length=300, blank=True, null=True)
    ack = models.IntegerField()
    days = models.FloatField()
    approve_status = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    delete_date = models.DateField(blank=True, null=True)
    delete_reason = models.CharField(max_length=150, blank=True, null=True)
    uniq_slno = models.IntegerField()
    seq_slno = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_leave_apply_valid'


class UserLeaveApplyValidTemp(models.Model):
    empcode = models.IntegerField()
    leave_date = models.DateField()
    leave_type = models.CharField(max_length=5, blank=True, null=True)
    day_type = models.CharField(max_length=2, blank=True, null=True)
    reason = models.CharField(max_length=300, blank=True, null=True)
    days = models.FloatField()
    seq_slno = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_leave_apply_valid_temp'


class UserLeaveBalance(models.Model):
    empcode = models.IntegerField(primary_key=True)
    el = models.FloatField()
    cl = models.FloatField()
    sl = models.FloatField()
    coff = models.FloatField()
    clnew = models.FloatField()
    fl = models.FloatField()
    flnew = models.FloatField()
    sap_no = models.CharField(max_length=20, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    del_date = models.DateField(blank=True, null=True)
    delete_reason = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_leave_balance'





class UserLeaveMaster(models.Model):
    company_id = models.IntegerField()
    leave_type = models.CharField(max_length=5)
    desc = models.CharField(max_length=150)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    delete_date = models.DateField()
    delete_reason = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'user_leave_master'


class UserLeaveOdPermissionHistory(models.Model):
    ack = models.IntegerField()
    empcode = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    day_type = models.CharField(max_length=3, blank=True, null=True)
    type = models.CharField(max_length=15, blank=True, null=True)
    hours = models.IntegerField()
    approve_status = models.IntegerField()
    created_by = models.IntegerField()
    timestampp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField(blank=True, null=True)
    del_reason = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_leave_od_permission_history'


class UserLeaveOdPermissionNtry(models.Model):
    ack = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    apply_date = models.DateField()
    apply_time = models.CharField(max_length=10, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.CharField(max_length=20, blank=True, null=True)
    end_time = models.CharField(max_length=20, blank=True, null=True)
    day_type = models.CharField(max_length=3, blank=True, null=True)
    type = models.CharField(max_length=15, blank=True, null=True)
    hours = models.IntegerField()
    tr_type = models.CharField(max_length=2, blank=True, null=True)
    visit_place = models.CharField(max_length=40, blank=True, null=True)
    purpose = models.CharField(max_length=50, blank=True, null=True)
    approved_by = models.IntegerField()
    approve_date = models.DateField(blank=True, null=True)
    approve_time = models.TimeField()
    approve_status = models.IntegerField()
    approve_cancel_timestamp = models.CharField(max_length=25, blank=True, null=True)
    auto_approve = models.CharField(max_length=5, blank=True, null=True)
    reject_reason = models.CharField(max_length=150, blank=True, null=True)
    created_by = models.IntegerField()
    sap_no = models.CharField(max_length=30)
    timestampp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField(blank=True, null=True)
    del_reason = models.CharField(max_length=150, blank=True, null=True)
    moved_sap = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_leave_od_permission_ntry'



class UserLeaveOtNtry(models.Model):
    empcode = models.IntegerField()
    date = models.DateField()
    hours = models.FloatField()
    final_hours = models.FloatField()
    approve_status = models.IntegerField()
    remarks = models.CharField(max_length=500)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user_leave_ot_ntry'


class UserLeavePermission(models.Model):
    per_id = models.AutoField(primary_key=True)
    empcode = models.CharField(max_length=6)
    ntry_date = models.DateField()
    day_type = models.CharField(max_length=10)
    reason = models.CharField(max_length=50, blank=True, null=True)
    hod = models.IntegerField()
    hr = models.IntegerField()
    hod_sts = models.IntegerField()
    hod_date = models.DateTimeField(blank=True, null=True)
    cancel_sts = models.IntegerField()
    sap_no = models.CharField(max_length=30)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_leave_permission'


class UserLeaveShiftMaster(models.Model):
    tprog = models.CharField(max_length=4)
    begin_1 = models.TimeField()
    end_1 = models.TimeField()
    begin_2 = models.TimeField()
    end_2 = models.TimeField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_by = models.IntegerField()
    del_date = models.DateField()
    delete_reason = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'user_leave_shift_master'


class UserLeaveSplReq(models.Model):
    sid = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    leave_type = models.CharField(max_length=4, blank=True, null=True)
    start_date = models.DateField()
    relation = models.CharField(max_length=5)
    ntry_date = models.DateField()
    hr_sts = models.IntegerField()
    hr = models.IntegerField()
    hr_comm = models.CharField(max_length=50, blank=True, null=True)
    hr_date = models.DateField()
    sap_no = models.CharField(max_length=30)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_leave_spl_req'


class UserLeaveStatusMaster(models.Model):
    slno = models.IntegerField()
    desc = models.CharField(max_length=100)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'user_leave_status_master'


class UserLeaveTemp(models.Model):
    empcode = models.CharField(max_length=6)
    leave_type = models.CharField(max_length=5)
    days = models.CharField(max_length=10)
    delete1 = models.IntegerField()
    valid = models.CharField(max_length=15)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_leave_temp'


class UserLeaveTimeAdminMaster(models.Model):
    empcode = models.IntegerField()
    loc = models.CharField(max_length=6)
    type = models.CharField(max_length=15)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'user_leave_time_admin_master'


class UserLeaveTimecard(models.Model):
    tid = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    date_on = models.DateField()
    mor_eve = models.CharField(max_length=11, blank=True, null=True)
    timechan = models.CharField(max_length=9)
    status = models.IntegerField()
    ntry_date = models.DateField(blank=True, null=True)
    hr = models.IntegerField()
    hod = models.IntegerField()
    hod_date = models.CharField(max_length=20, blank=True, null=True)
    hod_comm = models.CharField(max_length=50, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_leave_timecard'


class UserLevelMaster(models.Model):
    payscale_level = models.CharField(max_length=15)
    desc = models.CharField(max_length=150)
    welfare_group = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    period_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_level_master'


class UserLocation(models.Model):
    empcode = models.IntegerField()
    loc = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'user_location'


class UserLoginTime(models.Model):
    sno = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    login = models.TimeField()
    logout = models.TimeField()
    date = models.DateField()
    on_off = models.IntegerField()
    ip = models.CharField(max_length=20)
    admn_warn = models.IntegerField()
    admn_date = models.DateField()
    usrcnfrm = models.IntegerField(db_column='usrCnfrm')  # Field name made lowercase.
    sess_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_login_time'


class UserMailMaster(models.Model):
    slno = models.AutoField(primary_key=True)
    emp_code = models.IntegerField()
    internal_mail_req = models.CharField(max_length=10)
    internal_mail_id = models.CharField(max_length=50, blank=True, null=True)
    system_required = models.CharField(max_length=10)
    external_mail_req = models.CharField(max_length=10)
    external_mail_id = models.CharField(max_length=50, blank=True, null=True)
    comments = models.CharField(max_length=200)
    status = models.IntegerField(blank=True, null=True)
    config_id_mail = models.CharField(max_length=250)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    deleted_by = models.IntegerField(blank=True, null=True)
    deleted_date = models.DateField(blank=True, null=True)
    delete_reason = models.CharField(max_length=150, blank=True, null=True)
    executive_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user_mail_master'






        managed = False
        db_table = 'user_master_27_09_2022'









        managed = False
        db_table = 'user_master_temp'


class UserMediclaimPolicy(models.Model):
    cardid = models.CharField(max_length=23, blank=True, null=True)
    empcode = models.IntegerField(blank=True, null=True)
    suminsured = models.IntegerField(blank=True, null=True)
    policyno = models.CharField(max_length=24, blank=True, null=True)
    policy_holder = models.CharField(max_length=52, blank=True, null=True)
    insurance_name = models.CharField(max_length=52, blank=True, null=True)
    relationship = models.CharField(max_length=13, blank=True, null=True)
    gender = models.CharField(max_length=9, blank=True, null=True)
    indication = models.IntegerField(blank=True, null=True)
    date_of_birth = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    crnt_sts = models.IntegerField(blank=True, null=True)
    dep_add = models.IntegerField(blank=True, null=True)
    delete1 = models.IntegerField()
    timstamp = models.DateTimeField()
    deletedby = models.IntegerField(blank=True, null=True)
    deleteddate = models.CharField(max_length=19, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_mediclaim_policy'


class UserMediclaimPolicyHis(models.Model):
    hid = models.AutoField(primary_key=True)
    id = models.IntegerField()
    field = models.CharField(max_length=30)
    before = models.CharField(max_length=200)
    after = models.CharField(max_length=200)
    date = models.DateField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_mediclaim_policy_his'


class UserNationMaster(models.Model):
    nation = models.IntegerField()
    nation_name = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_nation_master'


class UserPrivil(models.Model):
    empcode = models.CharField(max_length=6, blank=True, null=True)
    dept = models.IntegerField()
    form_name = models.CharField(max_length=200)
    save = models.IntegerField()
    edit = models.IntegerField()
    delete = models.IntegerField()
    view = models.IntegerField()
    disabled = models.IntegerField()
    createdby = models.CharField(max_length=7)
    category = models.CharField(max_length=5)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_privil'


class UserPrivileges(models.Model):
    empcode = models.BigIntegerField()
    formname = models.CharField(max_length=50, blank=True, null=True)
    view = models.CharField(max_length=1, blank=True, null=True)
    save = models.CharField(max_length=1, blank=True, null=True)
    update1 = models.CharField(max_length=1, blank=True, null=True)
    delete1 = models.CharField(max_length=1, blank=True, null=True)
    createdby = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_privileges'


class UserPunchDailyStatus(models.Model):
    empcode = models.CharField(max_length=6)
    yesterday_date = models.DateField()
    today_date = models.DateField()
    punch_out = models.CharField(max_length=8)
    punch_in = models.CharField(max_length=8)
    lateby = models.CharField(max_length=8)
    shift = models.CharField(max_length=10)
    leave = models.CharField(max_length=100)
    end_date = models.DateField()
    loc = models.CharField(max_length=4)
    created_by = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    last_update = models.CharField(max_length=20)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_punch_daily_status'


class UserPunchDailyStatusTemp(models.Model):
    empcode = models.CharField(max_length=6)
    yesterday_date = models.DateField()
    today_date = models.DateField()
    punch_out = models.CharField(max_length=8)
    punch_in = models.CharField(max_length=8)
    lateby = models.CharField(max_length=8)
    shift = models.CharField(max_length=10)
    leave = models.CharField(max_length=100)
    end_date = models.DateField()
    created_by = models.CharField(max_length=10)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_punch_daily_status_temp'


class UserPunchMaster(models.Model):
    empcode = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    day_status = models.CharField(max_length=4, blank=True, null=True)
    in_field = models.TimeField(db_column='in')  # Field renamed because it was a Python reserved word.
    out = models.TimeField()
    total = models.CharField(max_length=10, blank=True, null=True)
    reason = models.CharField(max_length=40, blank=True, null=True)
    week = models.CharField(max_length=3, blank=True, null=True)
    od_in = models.TimeField()
    od_out = models.TimeField()
    leave_in = models.TimeField()
    leave_out = models.TimeField()
    lateby = models.CharField(max_length=5, blank=True, null=True)
    un_shift = models.CharField(max_length=5, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    punch_id = models.AutoField(primary_key=True)
    in_sap_no = models.CharField(max_length=30, blank=True, null=True)
    out_sap_no = models.CharField(max_length=30, blank=True, null=True)
    pr_sap_no = models.CharField(max_length=30, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_punch_master'


class UserPunchMaster141023(models.Model):
    empcode = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    day_status = models.CharField(max_length=4, blank=True, null=True)
    in_field = models.TimeField(db_column='in')  # Field renamed because it was a Python reserved word.
    out = models.TimeField()
    total = models.CharField(max_length=10, blank=True, null=True)
    reason = models.CharField(max_length=40, blank=True, null=True)
    week = models.CharField(max_length=3, blank=True, null=True)
    od_in = models.TimeField()
    od_out = models.TimeField()
    leave_in = models.TimeField()
    leave_out = models.TimeField()
    lateby = models.CharField(max_length=5, blank=True, null=True)
    un_shift = models.CharField(max_length=5, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    punch_id = models.AutoField(primary_key=True)
    in_sap_no = models.CharField(max_length=30, blank=True, null=True)
    out_sap_no = models.CharField(max_length=30, blank=True, null=True)
    pr_sap_no = models.CharField(max_length=30, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_punch_master_14-10-23'



class UserRelignMaster(models.Model):
    relign = models.IntegerField()
    relign_name = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_relign_master'


class UserSalutationMaster(models.Model):
    sal_no = models.AutoField(primary_key=True)
    sal_name = models.CharField(max_length=5)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_salutation_master'


class UserShiftHis(models.Model):
    sid = models.AutoField(primary_key=True)
    shift_id = models.IntegerField()
    empcode = models.CharField(max_length=6, blank=True, null=True)
    shift = models.CharField(max_length=11, blank=True, null=True)
    shift_date = models.DateField(blank=True, null=True)
    rsn = models.CharField(max_length=200, blank=True, null=True)
    sap_upload = models.IntegerField()
    moved_time = models.CharField(max_length=30)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_shift_his'


class UserShiftHisTesttable(models.Model):
    sid = models.AutoField(primary_key=True)
    shift_id = models.IntegerField()
    empcode = models.CharField(max_length=6, blank=True, null=True)
    shift = models.CharField(max_length=11, blank=True, null=True)
    shift_date = models.DateField(blank=True, null=True)
    rsn = models.CharField(max_length=200, blank=True, null=True)
    sap_upload = models.IntegerField()
    moved_time = models.CharField(max_length=30)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_shift_his_testtable'


class UserShiftMaster(models.Model):
    sid = models.AutoField(primary_key=True)
    shift = models.CharField(max_length=10)
    sname = models.CharField(max_length=20)
    timings = models.CharField(max_length=20)
    createdby = models.CharField(max_length=6)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_shift_master'


class UserShiftMasterNew(models.Model):
    sid = models.AutoField(primary_key=True)
    shift = models.CharField(max_length=10)
    sname = models.CharField(max_length=20)
    timings = models.CharField(max_length=20)
    fromtime = models.CharField(max_length=12, blank=True, null=True)
    totime = models.CharField(max_length=12, blank=True, null=True)
    createdby = models.CharField(max_length=6)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_shift_master_new'


class UserShiftNtry(models.Model):
    shift_id = models.AutoField(primary_key=True)
    ntry_by = models.CharField(max_length=6, blank=True, null=True)
    ntry_date = models.DateField(blank=True, null=True)
    empcode = models.CharField(max_length=6, blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_shift_ntry'


class UserShiftTime(models.Model):
    slno = models.AutoField(primary_key=True)
    shift = models.CharField(max_length=6, blank=True, null=True)
    sname = models.CharField(max_length=20)
    fromtime = models.TimeField(blank=True, null=True)
    totime = models.CharField(max_length=20, blank=True, null=True)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_shift_time'


class UserSpclLeave(models.Model):
    empcode = models.IntegerField()
    days = models.FloatField()
    start_date = models.DateField(blank=True, null=True)
    upto = models.DateField(blank=True, null=True)
    cate = models.CharField(max_length=5, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    update_by = models.IntegerField()
    update_timestamp = models.CharField(max_length=20, blank=True, null=True)
    delete1 = models.IntegerField()
    cid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'user_spcl_leave'


class UserStateMaster(models.Model):
    state = models.IntegerField()
    state_name = models.CharField(max_length=50)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_state_master'


class UserTransportNtry(models.Model):
    empcode = models.IntegerField()
    pick_point = models.CharField(max_length=15, blank=True, null=True)
    drop_point = models.CharField(max_length=150, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.CharField(max_length=20, blank=True, null=True)
    time_other = models.CharField(max_length=30, blank=True, null=True)
    snaks = models.CharField(max_length=10, blank=True, null=True)
    tea = models.CharField(max_length=1, blank=True, null=True)
    dinner = models.CharField(max_length=30, blank=True, null=True)
    dinner_other = models.CharField(max_length=150, blank=True, null=True)
    purp_staying = models.CharField(max_length=500, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField(blank=True, null=True)
    del_reason = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_transport_ntry'


class UserTransportNtry12(models.Model):
    empcode = models.IntegerField()
    pick_point = models.CharField(max_length=15, blank=True, null=True)
    drop_point = models.CharField(max_length=150, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.CharField(max_length=20, blank=True, null=True)
    time_other = models.CharField(max_length=30, blank=True, null=True)
    snaks = models.CharField(max_length=10, blank=True, null=True)
    tea = models.CharField(max_length=1, blank=True, null=True)
    dinner = models.CharField(max_length=30, blank=True, null=True)
    dinner_other = models.CharField(max_length=150, blank=True, null=True)
    purp_staying = models.CharField(max_length=500, blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField(blank=True, null=True)
    del_reason = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_transport_ntry12'


class UsermasterMailid(models.Model):
    empcode = models.IntegerField()
    mail_id = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'usermaster_mailid'


class Uservb(models.Model):
    empcode = models.IntegerField()
    senior = models.IntegerField()
    super_senior = models.IntegerField()
    senior_dept = models.IntegerField()
    super_senior_dept = models.IntegerField()
    date = models.DateField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'uservb'


class VdssCategoryMaster(models.Model):
    cat_id = models.AutoField(primary_key=True)
    issue_category = models.CharField(max_length=100)
    createdby = models.CharField(max_length=7)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    delete_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'vdss_category_master'


class VdssDetails(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    empcode = models.CharField(max_length=7)
    ntry_date = models.DateField()
    ntry_time = models.CharField(max_length=7)
    month = models.CharField(max_length=10)
    issue_category = models.IntegerField()
    project = models.IntegerField()
    vendor = models.IntegerField()
    materialcode = models.CharField(max_length=200, blank=True, null=True)
    qty = models.IntegerField()
    remarks = models.TextField()
    attachment = models.CharField(max_length=100)
    status = models.IntegerField()
    assignby = models.CharField(max_length=7)
    assign_date = models.DateField()
    assign_time = models.CharField(max_length=7)
    action_points = models.TextField()
    assign_to = models.CharField(max_length=7)
    target_date = models.DateField()
    vdss_remarks = models.TextField()
    cmplt_date = models.DateField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vdss_details'


class VdssDetailsHistory(models.Model):
    uniq_slno = models.IntegerField()
    empcode = models.CharField(max_length=7)
    assign_to = models.CharField(max_length=7)
    ntry_date = models.DateField()
    ntry_time = models.CharField(max_length=10)
    target_date = models.DateField()
    action_points = models.TextField()
    vdds_remarks = models.TextField()
    status = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vdss_details_history'


class VdssPrjctMaster(models.Model):
    proj_id = models.AutoField(primary_key=True)
    project = models.CharField(max_length=30)
    createdby = models.CharField(max_length=7)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    deleted_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'vdss_prjct_master'


class VdssStatusMaster(models.Model):
    sid = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vdss_status_master'


class VdssTeam(models.Model):
    empcode = models.IntegerField(primary_key=True)
    createdby = models.CharField(max_length=7)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vdss_team'


class VdssVendMastrer(models.Model):
    ven_id = models.CharField(primary_key=True, max_length=1000)
    vendor = models.CharField(max_length=100)
    mailid = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.CharField(max_length=7, blank=True, null=True)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vdss_vend_mastrer'


class VdssVendMastrer28112022(models.Model):
    ven_id = models.CharField(primary_key=True, max_length=1000)
    vendor = models.CharField(max_length=100)
    mailid = models.CharField(max_length=100)
    createdby = models.CharField(max_length=7)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vdss_vend_mastrer_28_11_2022'


class VdssVendMastrerDjango(models.Model):
    ven_id = models.CharField(primary_key=True, max_length=1000)
    vendor = models.CharField(max_length=100)
    mailid = models.CharField(max_length=100)
    createdby = models.CharField(max_length=7)
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vdss_vend_mastrer_django'


class VendorDirEntry(models.Model):
    main_cat_id = models.IntegerField()
    sub_data = models.CharField(max_length=250)
    child_data = models.CharField(max_length=250)
    file_name = models.CharField(max_length=250)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vendor_dir_entry'


class VendorMainCatMaster(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=200)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'vendor_main_cat_master'


class VendorMaster(models.Model):
    vendor_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    cty = models.CharField(max_length=10)
    street = models.CharField(max_length=30)
    post_code = models.IntegerField()
    city = models.CharField(max_length=20)
    group = models.CharField(max_length=30)
    notes = models.CharField(max_length=30)
    building = models.CharField(max_length=20)
    floor = models.CharField(max_length=20)
    room = models.CharField(max_length=20)
    telephone = models.CharField(max_length=12)
    fax = models.CharField(max_length=15)
    street2 = models.CharField(max_length=30)
    street3 = models.CharField(max_length=30)
    street4 = models.CharField(max_length=30)
    street5 = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    crncy = models.CharField(max_length=10)
    salesperson = models.CharField(max_length=30)
    incot = models.CharField(max_length=10)
    inco2 = models.CharField(max_length=10)
    gr = models.CharField(max_length=10)
    ctr = models.CharField(max_length=10)
    payment_term = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=10)
    payment_method_desc = models.CharField(max_length=30)
    po_org = models.CharField(max_length=30)
    po_grp = models.CharField(max_length=20)
    po_org_desc = models.CharField(max_length=30)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()
    d = models.IntegerField()
    e = models.IntegerField()
    f = models.IntegerField()
    g = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vendor_master'


class VendorPojectsMaster(models.Model):
    prj_slno = models.AutoField(primary_key=True)
    prj_desc = models.CharField(max_length=30)
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vendor_pojects_master'


class VendorRating2BMaster(models.Model):
    slno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    sub_name = models.CharField(max_length=1)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vendor_rating_2b_master'


class VendorRatingNtry(models.Model):
    vendor_uniq_slno = models.AutoField(primary_key=True)
    vendor_code = models.IntegerField()
    po = models.IntegerField()
    po_date = models.DateField()
    dc = models.CharField(max_length=20)
    dc_date = models.DateField()
    inv = models.IntegerField()
    inv_date = models.DateField()
    desc = models.CharField(max_length=500)
    drg = models.CharField(max_length=50)
    prj_slno = models.IntegerField()
    r = models.IntegerField()
    d = models.IntegerField()
    q = models.IntegerField()
    cfd = models.IntegerField()
    cfj = models.IntegerField()
    vendor_rate = models.FloatField()
    check_no = models.CharField(max_length=30)
    check_date = models.DateField()
    check_amt = models.FloatField()
    entry_by = models.IntegerField()
    entry_date = models.DateField()
    entry_sts = models.IntegerField()
    checked_by = models.IntegerField()
    checked_date = models.DateField()
    checked_sts = models.IntegerField()
    approved_by = models.IntegerField()
    approved_date = models.DateField()
    approved_sts = models.IntegerField()
    inv_without_tax = models.FloatField()
    inv_with_tax = models.FloatField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vendor_rating_ntry'


class VnvEntry(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    product_code = models.CharField(max_length=50, blank=True, null=True)
    specification_no = models.CharField(max_length=500, blank=True, null=True)
    mod_name = models.CharField(max_length=500, blank=True, null=True)
    version = models.CharField(max_length=250, blank=True, null=True)
    file_size = models.IntegerField()
    file_type = models.CharField(max_length=50, blank=True, null=True)
    file_name = models.CharField(max_length=150, blank=True, null=True)
    file_created_timestamp1 = models.CharField(max_length=50, blank=True, null=True)
    file_size2 = models.CharField(max_length=10, blank=True, null=True)
    file_type2 = models.CharField(max_length=10, blank=True, null=True)
    file_name2 = models.CharField(max_length=150, blank=True, null=True)
    file_created_timestamp2 = models.CharField(max_length=50, blank=True, null=True)
    file_size3 = models.CharField(max_length=10, blank=True, null=True)
    file_type3 = models.CharField(max_length=10, blank=True, null=True)
    file_name3 = models.CharField(max_length=150, blank=True, null=True)
    file_created_timestamp3 = models.CharField(max_length=50, blank=True, null=True)
    std_path = models.CharField(max_length=500, blank=True, null=True)
    alt_path = models.CharField(max_length=200, blank=True, null=True)
    rel_type = models.IntegerField()
    rel_note = models.CharField(max_length=4000, blank=True, null=True)
    rel_date = models.CharField(max_length=50, blank=True, null=True)
    rel_by = models.IntegerField()
    circu_list = models.CharField(max_length=500, blank=True, null=True)
    circu_list_me = models.CharField(max_length=2000, blank=True, null=True)
    ntry_sts = models.IntegerField()
    ntry_by = models.IntegerField()
    ntry_date = models.DateField()
    pl_remarks = models.CharField(max_length=250, blank=True, null=True)
    pl_by = models.IntegerField()
    pl_date = models.DateField()
    pl_sts = models.IntegerField()
    vnv_remarks = models.CharField(max_length=250, blank=True, null=True)
    vnv_by = models.IntegerField()
    vnv_date = models.DateField()
    vnv_sts = models.IntegerField()
    approve_sts = models.IntegerField()
    release_sts = models.CharField(max_length=10, blank=True, null=True)
    released_status = models.CharField(max_length=500, blank=True, null=True)
    auto_remind = models.CharField(max_length=10, blank=True, null=True)
    release_date = models.DateField()
    release_recipients_list = models.CharField(max_length=100, blank=True, null=True)
    me_release_ntry_by = models.IntegerField()
    me_release_ntry_date = models.DateField()
    ecr_no = models.CharField(max_length=25, blank=True, null=True)
    type = models.CharField(max_length=4, blank=True, null=True)
    product_ic = models.IntegerField()
    product_ic_sts = models.IntegerField()
    product_ic_date = models.DateField()
    product_ic_time = models.CharField(max_length=250, blank=True, null=True)
    sub_type = models.CharField(max_length=50, blank=True, null=True)
    whom_2release = models.CharField(max_length=200, blank=True, null=True)
    sr_no = models.CharField(max_length=12, blank=True, null=True)
    me_status = models.IntegerField()
    timestamp = models.DateTimeField()
    nns_slno = models.IntegerField()
    checksum = models.CharField(max_length=40, blank=True, null=True)
    card_name = models.CharField(max_length=50, blank=True, null=True)
    ic_name = models.CharField(max_length=50, blank=True, null=True)
    prog_interface = models.CharField(max_length=1000, blank=True, null=True)
    prog_tool = models.CharField(max_length=1000, db_collation='utf8_general_ci', blank=True, null=True)
    clr_buffer = models.CharField(max_length=50, blank=True, null=True)
    eff_from = models.CharField(max_length=50, blank=True, null=True)
    type_loco = models.CharField(max_length=1000, blank=True, null=True)
    under_second = models.IntegerField()
    hod_code = models.IntegerField()
    hod_date = models.DateField()
    hod_status = models.IntegerField()
    track_status = models.IntegerField()
    title_ntry = models.CharField(max_length=500, blank=True, null=True)
    rev_no = models.CharField(max_length=200, blank=True, null=True)
    checked_by = models.CharField(max_length=200, blank=True, null=True)
    approved_by = models.CharField(max_length=200, blank=True, null=True)
    doc_no = models.CharField(max_length=200, blank=True, null=True)
    pdf_note = models.CharField(max_length=2000, blank=True, null=True)
    req_soft = models.CharField(max_length=500, blank=True, null=True)
    start_menu = models.CharField(max_length=500, blank=True, null=True)
    def_desti = models.CharField(max_length=500, blank=True, null=True)
    icon_name = models.CharField(max_length=500, blank=True, null=True)
    sf_cat = models.IntegerField()
    sd_re_date = models.DateField()
    zip_name_time = models.TextField(blank=True, null=True)
    zip_size = models.TextField(blank=True, null=True)
    zipfname = models.TextField(blank=True, null=True)
    groupid = models.CharField(max_length=250, blank=True, null=True)
    product_sec_ic = models.IntegerField()
    main_hod = models.IntegerField()
    rev_date = models.TextField(blank=True, null=True)
    nnspath = models.TextField(blank=True, null=True)
    pdf_ent_date = models.CharField(max_length=50, blank=True, null=True)
    delete1 = models.IntegerField()
    ecrno_updation = models.CharField(max_length=50, blank=True, null=True)
    servreq = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vnv_entry'


class VnvFileSavng(models.Model):
    uniq_slno = models.IntegerField()
    filename = models.TextField()
    foldername = models.CharField(max_length=20)
    file_type = models.CharField(max_length=200)
    file_size = models.IntegerField()
    file_ext = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    createdby = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vnv_file_savng'


class VnvHistory(models.Model):
    hid = models.AutoField(primary_key=True)
    id = models.IntegerField()
    field = models.CharField(max_length=30)
    before = models.CharField(max_length=200)
    after = models.CharField(max_length=200)
    date = models.DateField()
    timestamp = models.DateTimeField()
    createdby = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vnv_history'


class VnvPdfData(models.Model):
    slno = models.IntegerField()
    prd_by = models.CharField(max_length=50)
    rev_sof_hist = models.TextField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vnv_pdf_data'


class VnvProgMaster(models.Model):
    matcode = models.TextField()
    prog_int = models.CharField(max_length=500)
    prog_toll = models.CharField(max_length=500)
    filetype = models.CharField(max_length=200)
    ref_code = models.CharField(max_length=200)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vnv_prog_master'


class VnvSub(models.Model):
    slno = models.AutoField(primary_key=True)
    uniq_slno = models.IntegerField()
    remarks = models.TextField()
    createdby = models.IntegerField()
    date = models.DateField()
    status = models.IntegerField()
    to_mail = models.CharField(max_length=500)
    cc_mail = models.CharField(max_length=2000)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vnv_sub'


class VnvTrackStatusMaster(models.Model):
    status = models.SmallAutoField(primary_key=True)
    status_name = models.CharField(max_length=30)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField(blank=True, null=True)
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'vnv_track_status_master'


class VocherAllowanceMaster(models.Model):
    aid = models.AutoField(primary_key=True)
    cid = models.IntegerField(blank=True, null=True)
    fromdate = models.CharField(max_length=10, blank=True, null=True)
    todate = models.CharField(max_length=10, blank=True, null=True)
    amount = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    createdby = models.IntegerField()
    delete1 = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vocher_allowance_master'


class VocherAttachments(models.Model):
    aid = models.AutoField(primary_key=True)
    vid = models.IntegerField()
    name = models.CharField(max_length=100, blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vocher_attachments'


class VocherCategoryMaster(models.Model):
    cid = models.AutoField(primary_key=True)
    glaccount = models.IntegerField()
    cat_name = models.CharField(max_length=31, blank=True, null=True)
    delete1 = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vocher_category_master'


class VocherHistory(models.Model):
    hid = models.AutoField(primary_key=True)
    vid = models.IntegerField()
    status = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    empcode = models.CharField(max_length=10, blank=True, null=True)
    delete1 = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vocher_history'


class VocherLimitMaster(models.Model):
    mid = models.AutoField(primary_key=True)
    loc = models.CharField(max_length=4, blank=True, null=True)
    deptcode = models.IntegerField(blank=True, null=True)
    head1 = models.IntegerField(blank=True, null=True)
    limit1 = models.IntegerField(blank=True, null=True)
    head2 = models.IntegerField(blank=True, null=True)
    limit2 = models.IntegerField(blank=True, null=True)
    delete1 = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vocher_limit_master'


class VocherNtry(models.Model):
    vid = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    ntry_date = models.DateField()
    status = models.IntegerField()
    totalamount = models.CharField(max_length=11)
    head1 = models.IntegerField()
    head1_sts = models.IntegerField()
    head2 = models.IntegerField()
    head2_sts = models.IntegerField()
    pay_type = models.CharField(max_length=2, blank=True, null=True)
    acc_doc = models.CharField(max_length=20, blank=True, null=True)
    pay_doc = models.CharField(max_length=12, blank=True, null=True)
    chequeno = models.CharField(max_length=15, blank=True, null=True)
    clearing_date = models.DateField(blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vocher_ntry'


class VocherStatusMaster(models.Model):
    sid = models.AutoField(primary_key=True)
    status = models.IntegerField()
    sname = models.CharField(max_length=20)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vocher_status_master'


class VocherSubCategory(models.Model):
    sid = models.AutoField(primary_key=True)
    cid = models.IntegerField(blank=True, null=True)
    sname = models.CharField(max_length=81, blank=True, null=True)
    delete1 = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vocher_sub_category'


class VocherTransaction(models.Model):
    tid = models.AutoField(primary_key=True)
    vid = models.IntegerField()
    billno = models.CharField(max_length=18, blank=True, null=True)
    billdate = models.DateField()
    category = models.IntegerField()
    subcat = models.IntegerField()
    amount = models.CharField(max_length=10)
    remarks = models.TextField(blank=True, null=True)
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()
    startdate = models.DateField()
    enddate = models.DateField()
    pay_type = models.CharField(max_length=2, blank=True, null=True)
    acc_doc = models.CharField(max_length=20, blank=True, null=True)
    pay_doc = models.CharField(max_length=12, blank=True, null=True)
    chequeno = models.CharField(max_length=15, blank=True, null=True)
    clearing_date = models.DateField()
    indexno = models.IntegerField()
    vocher_project = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vocher_transaction'


class VoucherEntrys(models.Model):
    voucher_no = models.IntegerField()
    transporter = models.CharField(max_length=3, blank=True, null=True)
    movement = models.DateField()
    from_field = models.CharField(db_column='from', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=100, blank=True, null=True)
    lr_no = models.CharField(max_length=20, blank=True, null=True)
    docs_no = models.CharField(max_length=20, blank=True, null=True)
    amt = models.DecimalField(max_digits=10, decimal_places=2)
    scancopy = models.CharField(max_length=100, blank=True, null=True)
    empcode = models.CharField(max_length=8, blank=True, null=True)
    dept = models.CharField(max_length=5, blank=True, null=True)
    status = models.CharField(max_length=1)
    timestamp = models.DateTimeField()
    delete1 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'voucher_entrys'


class Warranty(models.Model):
    materialcode = models.CharField(primary_key=True, max_length=20)
    noofmonths = models.IntegerField()
    createdby = models.BigIntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'warranty'


class WelfareAdapt(models.Model):
    slno = models.IntegerField(primary_key=True)
    comp_code = models.IntegerField()
    loc = models.CharField(max_length=50)
    dept = models.IntegerField()
    empcode = models.IntegerField()
    uniq_slno_matnr = models.CharField(max_length=250)
    qty = models.IntegerField()
    months = models.IntegerField()
    issue_qty = models.IntegerField()
    issue_date = models.DateField()
    issue_by = models.IntegerField()
    type = models.IntegerField()
    reason = models.TextField()
    size = models.CharField(max_length=25)
    delete1 = models.IntegerField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'welfare_adapt'


class WelfareCal(models.Model):
    particulars = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'welfare_cal'


class WelfareCalender(models.Model):
    slno = models.AutoField(primary_key=True)
    particulars = models.TextField()
    period = models.IntegerField(blank=True, null=True)
    period_unit = models.IntegerField()
    tenure = models.IntegerField()
    tenure_unit = models.IntegerField(db_column='tenure_Unit')  # Field name made lowercase.
    alert = models.IntegerField(blank=True, null=True)
    alert_unit = models.IntegerField(db_column='alert_Unit')  # Field name made lowercase.
    visibility = models.IntegerField()
    responsibility = models.IntegerField()
    authorization = models.IntegerField()
    timsetamp = models.DateTimeField()
    created_by = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'welfare_calender'


class WelfareCalenderDump(models.Model):
    slno = models.AutoField(primary_key=True)
    particulars = models.TextField()
    period = models.CharField(max_length=3, blank=True, null=True)
    period_unit = models.IntegerField()
    tenure = models.IntegerField()
    tenure_unit = models.IntegerField(db_column='tenure_Unit')  # Field name made lowercase.
    alert = models.CharField(max_length=3, blank=True, null=True)
    alert_unit = models.IntegerField(db_column='alert_Unit')  # Field name made lowercase.
    visibility = models.IntegerField()
    responsibility = models.IntegerField()
    authorization = models.IntegerField()
    timsetamp = models.DateTimeField()
    created_by = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'welfare_calender_dump'


class WelfareInventoryMaster2(models.Model):
    slno = models.AutoField(primary_key=True)
    matcode = models.CharField(max_length=25)
    group = models.CharField(max_length=11)
    subgroup = models.CharField(max_length=25)
    category = models.CharField(max_length=250)
    uom = models.CharField(max_length=150)
    size = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    due_date = models.CharField(max_length=150)
    tobe_issued = models.CharField(max_length=10)
    min_qty = models.CharField(max_length=25)
    act_qty = models.IntegerField()
    rec_qty = models.IntegerField()
    indent_slno = models.IntegerField()
    created_by = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'welfare_inventory_master2'


class WelfareMcat2(models.Model):
    main = models.AutoField(primary_key=True)
    company_code = models.IntegerField()
    matcode = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    group = models.CharField(max_length=11)
    subgroup = models.CharField(max_length=100)
    createdby = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'welfare_mcat2'


class WelfarePoDetails(models.Model):
    slno = models.IntegerField(primary_key=True)
    matcode = models.CharField(max_length=150)
    stack_entry_date = models.DateField()
    entry_qty = models.IntegerField()
    ind_no = models.CharField(max_length=150)
    ind_date = models.DateField()
    ven_name = models.CharField(max_length=150)
    po_num = models.CharField(max_length=150)
    po_date = models.DateField()
    ven_addr = models.TextField()
    created_by = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'welfare_po_details'


class WelfareValidationData(models.Model):
    slno = models.AutoField(primary_key=True)
    valid_main_id = models.IntegerField()
    type_id = models.IntegerField()
    subtype_id = models.IntegerField()
    qty = models.IntegerField()
    due_date = models.DateField()
    eff_from = models.DateField()
    eff_to = models.DateField()
    active = models.IntegerField()
    created_by = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'welfare_validation_data'


class WorkShopMaster(models.Model):
    crtn_date = models.DateField()
    order_no = models.IntegerField()
    mat_code = models.CharField(max_length=20)
    mat_desc = models.CharField(max_length=50)
    tot_qty = models.IntegerField()
    prdcd_qty = models.IntegerField()
    status = models.IntegerField()
    rej_qty = models.IntegerField()
    acc_qty = models.IntegerField()
    rej_per = models.FloatField()
    remarks = models.CharField(max_length=250)
    filled_date = models.DateField()
    createdby = models.BigIntegerField()
    slno = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'work_shop_master'


class WorkShopNtry(models.Model):
    sno = models.AutoField(primary_key=True)
    slno = models.IntegerField()
    prdcd_from_date = models.DateField()
    prdcd_to_date = models.DateField()
    prdcd_qty = models.IntegerField()
    rej_qty = models.IntegerField()
    acc_qty = models.IntegerField()
    per_qty = models.FloatField()
    ntry_date = models.DateField()
    createdby = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'work_shop_ntry'


class WorkShopRejReson(models.Model):
    sno = models.AutoField(primary_key=True)
    rej_reson = models.CharField(max_length=100)
    date = models.DateField()
    rmrks = models.CharField(max_length=250)
    createdby = models.IntegerField()
    slno = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'work_shop_rej_reson'


class WorkshopLpoNtry(models.Model):
    uniq_slno = models.AutoField(primary_key=True)
    empcode = models.IntegerField()
    deptcode = models.IntegerField()
    matnr = models.CharField(max_length=20, blank=True, null=True)
    purpose_id = models.IntegerField()
    qty = models.FloatField()
    remarks = models.TextField(blank=True, null=True)
    actuval_req_date = models.DateField(blank=True, null=True)
    hod_code = models.IntegerField()
    hod_status = models.IntegerField()
    hod_timestamp = models.CharField(max_length=18)
    hod_remarks = models.CharField(max_length=500)
    request_date = models.DateField(blank=True, null=True)
    completedby = models.CharField(max_length=50)
    status = models.SmallIntegerField()
    pqty = models.IntegerField()
    actuval_proposed_start_date = models.DateField(blank=True, null=True)
    actuval_proposed_end_date = models.DateField(blank=True, null=True)
    actuval_proposed_start_time = models.TimeField(blank=True, null=True)
    actuval_proposed_end_time = models.TimeField(blank=True, null=True)
    proposed_start_date = models.DateField(blank=True, null=True)
    proposed_end_date = models.DateField(blank=True, null=True)
    proposed_start_time = models.TimeField(blank=True, null=True)
    proposed_end_time = models.TimeField(blank=True, null=True)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateField(blank=True, null=True)
    del_by = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'workshop_lpo_ntry'


class WorkshopPurposeMasterLpo(models.Model):
    purpose_id = models.AutoField(primary_key=True)
    purpose_name = models.CharField(max_length=50)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'workshop_purpose_master_lpo'


class WorkshopStatusMaster(models.Model):
    status = models.SmallAutoField(primary_key=True)
    status_name = models.CharField(max_length=30)
    created_by = models.IntegerField()
    timestamp = models.DateTimeField(blank=True, null=True)
    delete1 = models.IntegerField()
    del_by = models.IntegerField()
    del_date = models.DateField()
    del_reason = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'workshop_status_master'


class WorshopLpoAttachment(models.Model):
    uniq_slno = models.IntegerField()
    file_name = models.CharField(max_length=50)
    file_type = models.CharField(max_length=50)
    file_path = models.CharField(max_length=50)
    full_path = models.CharField(max_length=50)
    raw_name = models.CharField(max_length=50)
    orig_name = models.CharField(max_length=50)
    client_name = models.CharField(max_length=50)
    file_ext = models.CharField(max_length=50)
    file_size = models.CharField(max_length=50)
    is_image = models.CharField(max_length=50)
    image_width = models.CharField(max_length=50)
    image_height = models.CharField(max_length=50)
    image_type = models.CharField(max_length=50)
    image_size_str = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    delete1 = models.IntegerField()
    del_date = models.DateTimeField()
    del_by = models.IntegerField()
    del_reason = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'worshop_lpo_attachment'


class WorshopTrackHistory(models.Model):
    slno = models.IntegerField()
    comments = models.TextField()
    date = models.DateField()
    status = models.IntegerField()
    remarks = models.TextField()
    pqty = models.IntegerField()
    created_by = models.IntegerField()
    timestamp = models.DateTimeField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'worshop_track_history'


class YearMasterNew(models.Model):
    date = models.DateField()
    year = models.IntegerField()
    day = models.CharField(max_length=2)
    dws = models.CharField(max_length=4)
    hci = models.IntegerField()
    dt = models.IntegerField()
    loc = models.CharField(max_length=4)
    created = models.IntegerField()
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'year_master_new'


class YeasrMaster(models.Model):
    date = models.DateField()
    year = models.IntegerField()
    day = models.CharField(max_length=2, blank=True, null=True)
    dws = models.CharField(max_length=4, blank=True, null=True)
    hci = models.IntegerField()
    dt = models.IntegerField()
    loc = models.CharField(max_length=4)
    created = models.IntegerField()
    delete1 = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'yeasr_master'





class YeasrMasterTemp(models.Model):
    date = models.DateField()
    day = models.CharField(max_length=2)
    dws = models.CharField(max_length=4)
    hci = models.IntegerField()
    dt = models.IntegerField()
    loc = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'yeasr_master_temp'



class ZoneShed(models.Model):
    zone_name = models.CharField(max_length=40, blank=True, null=True)
    shed_name = models.CharField(max_length=40, blank=True, null=True)
    zone_short_name = models.CharField(max_length=10)
    shed_short_name = models.CharField(max_length=10)
    delete1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zone_shed'

