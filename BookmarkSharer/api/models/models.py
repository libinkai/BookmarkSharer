# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
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


class TLabel(models.Model):
    name = models.CharField(max_length=128)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_label'


class TSite(models.Model):
    name = models.CharField(max_length=255)
    base_url = models.CharField(max_length=255)
    click_num = models.IntegerField()
    status = models.IntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_site'


class TSiteLabelRef(models.Model):
    site_id = models.PositiveIntegerField()
    label_id = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_site_label_ref'


class TTest(models.Model):
    name = models.CharField(max_length=64)
    birthday = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_test'


class TUser(models.Model):
    nick_name = models.CharField(max_length=64)
    avatar = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    status = models.IntegerField()
    github_uuid = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 't_user'


class TUserClickLog(models.Model):
    site_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_user_click_log'


class TUserLabelRef(models.Model):
    user_id = models.PositiveIntegerField()
    label_id = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_user_label_ref'
