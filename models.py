# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activities(models.Model):
    activity_id = models.AutoField(primary_key=True)
    activity_type = models.CharField(max_length=20, blank=True, null=True)
    activity_start_date = models.DateTimeField(blank=True, null=True)
    activity_end_date = models.DateTimeField(blank=True, null=True)
    activity_max_students = models.IntegerField(blank=True, null=True)
    activity_created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Activities'


class Activityassignments(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey('Teachers', models.DO_NOTHING, blank=True, null=True)
    course = models.ForeignKey('Courses', models.DO_NOTHING, blank=True, null=True)
    laboratory = models.ForeignKey('Laboratories', models.DO_NOTHING, blank=True, null=True)
    seminar = models.ForeignKey('Seminars', models.DO_NOTHING, blank=True, null=True)
    course_weight = models.IntegerField(blank=True, null=True)
    laboratory_weight = models.IntegerField(blank=True, null=True)
    seminar_weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ActivityAssignments'


class Activityregistrations(models.Model):
    registration_id = models.AutoField(primary_key=True)
    activity = models.ForeignKey('Groupactivities', models.DO_NOTHING, blank=True, null=True)
    student = models.ForeignKey('Students', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ActivityRegistrations'


class Admins(models.Model):
    admin = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'Admins'


class Authentications(models.Model):
    authentication_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    authentication_username = models.CharField(max_length=15)
    authentication_password = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'Authentications'


class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=15, blank=True, null=True)
    course_description = models.CharField(max_length=100, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Courses'


class Enrollments(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Students', models.DO_NOTHING, blank=True, null=True)
    activity = models.ForeignKey(Activities, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Enrollments'


class Grades(models.Model):
    grade_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Students', models.DO_NOTHING, blank=True, null=True)
    grade_value = models.IntegerField(blank=True, null=True)
    course = models.ForeignKey(Courses, models.DO_NOTHING, blank=True, null=True)
    laboratory = models.ForeignKey('Laboratories', models.DO_NOTHING, blank=True, null=True)
    seminar = models.ForeignKey('Seminars', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Grades'


class Groupactivities(models.Model):
    activity_id = models.AutoField(primary_key=True)
    group = models.ForeignKey('Studygroups', models.DO_NOTHING, blank=True, null=True)
    student = models.ForeignKey('Students', models.DO_NOTHING, blank=True, null=True)
    activity_name = models.CharField(max_length=50, blank=True, null=True)
    activity_date = models.DateTimeField(blank=True, null=True)
    activity_duration = models.IntegerField(blank=True, null=True)
    min_participants = models.IntegerField(blank=True, null=True)
    expiration_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GroupActivities'


class Groupmembers(models.Model):
    member_id = models.AutoField(primary_key=True)
    group = models.ForeignKey('Studygroups', models.DO_NOTHING, blank=True, null=True)
    student = models.ForeignKey('Students', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GroupMembers'


class Groupmessages(models.Model):
    message_id = models.AutoField(primary_key=True)
    group = models.ForeignKey('Studygroups', models.DO_NOTHING, blank=True, null=True)
    student = models.ForeignKey('Students', models.DO_NOTHING, blank=True, null=True)
    message_context = models.CharField(max_length=255, blank=True, null=True)
    message_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GroupMessages'


class Laboratories(models.Model):
    laboratory_id = models.AutoField(primary_key=True)
    laboratory_name = models.CharField(max_length=15, blank=True, null=True)
    laboratory_description = models.CharField(max_length=100, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Laboratories'


class Seminars(models.Model):
    seminar_id = models.AutoField(primary_key=True)
    seminar_name = models.CharField(max_length=15, blank=True, null=True)
    seminar_description = models.CharField(max_length=100, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Seminars'


class Studentenrollments(models.Model):
    student_enrollment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Students', models.DO_NOTHING, blank=True, null=True)
    teacher = models.ForeignKey('Teachers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'StudentEnrollments'


class Students(models.Model):
    student = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    student_study_year = models.IntegerField()
    student_hours = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Students'


class Studygroups(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=30, blank=True, null=True)
    group_description = models.CharField(max_length=255, blank=True, null=True)
    group_password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'StudyGroups'


class Superadmins(models.Model):
    super_admin = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'SuperAdmins'


class Teachers(models.Model):
    teacher = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    teacher_department = models.CharField(max_length=30)
    teacher_min_hours = models.IntegerField()
    teacher_max_hours = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Teachers'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_pic = models.CharField(db_column='user_PIC', max_length=20)  # Field name made lowercase.
    user_first_name = models.CharField(max_length=20)
    user_last_name = models.CharField(max_length=20)
    user_address = models.CharField(max_length=50)
    user_phone_number = models.CharField(max_length=20)
    user_email = models.CharField(max_length=50)
    user_iban = models.CharField(db_column='user_IBAN', max_length=30)  # Field name made lowercase.
    user_contract_number = models.IntegerField()
    user_type = models.CharField(max_length=15)
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Users'


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
