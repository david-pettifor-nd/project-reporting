# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.apps import apps
from django.contrib.auth.models import User
import datetime


class AgileColors(models.Model):
    container_id = models.IntegerField(blank=True, null=True)
    container_type = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agile_colors'


class AgileData(models.Model):
    issue_id = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    story_points = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agile_data'


class Attachments(models.Model):
    container_id = models.IntegerField(blank=True, null=True)
    container_type = models.CharField(max_length=30, blank=True, null=True)
    filename = models.CharField(max_length=255)
    disk_filename = models.CharField(max_length=255)
    filesize = models.IntegerField()
    content_type = models.CharField(max_length=255, blank=True, null=True)
    digest = models.CharField(max_length=40)
    downloads = models.IntegerField()
    author_id = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    disk_directory = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachments'


class Boards(models.Model):
    project_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    topics_count = models.IntegerField()
    messages_count = models.IntegerField()
    last_message_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boards'


class Center(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'center'


class Changes(models.Model):
    changeset_id = models.IntegerField()
    action = models.CharField(max_length=1)
    path = models.TextField()
    from_path = models.TextField(blank=True, null=True)
    from_revision = models.CharField(max_length=255, blank=True, null=True)
    revision = models.CharField(max_length=255, blank=True, null=True)
    branch = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'changes'


class ChangesetParents(models.Model):
    changeset_id = models.IntegerField()
    parent_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'changeset_parents'


class Changesets(models.Model):
    repository_id = models.IntegerField()
    revision = models.CharField(max_length=255)
    committer = models.CharField(max_length=255, blank=True, null=True)
    committed_on = models.DateTimeField()
    comments = models.TextField(blank=True, null=True)
    commit_date = models.DateField(blank=True, null=True)
    scmid = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'changesets'
        unique_together = (('repository_id', 'revision'),)


class ChangesetsIssues(models.Model):
    changeset_id = models.IntegerField(primary_key=True)
    issue_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'changesets_issues'
        unique_together = (('changeset_id', 'issue_id'), ('changeset_id', 'issue_id'),)


class ChargeRates(models.Model):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    charge_rate_id = models.BigAutoField(primary_key=True)
    internal = models.NullBooleanField()
    cores_display = models.TextField(blank=True, null=True)
    center = models.ForeignKey(Center, models.DO_NOTHING, db_column='center', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'charge_rates'


class ChecklistTemplateCategories(models.Model):
    name = models.TextField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checklist_template_categories'


class ChecklistTemplates(models.Model):
    name = models.TextField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    is_public = models.NullBooleanField()
    template_items = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checklist_templates'


class Checklists(models.Model):
    is_done = models.NullBooleanField()
    subject = models.TextField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    issue_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checklists'


class Closings(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'closings'


class Comments(models.Model):
    commented_type = models.CharField(max_length=30)
    commented_id = models.IntegerField()
    author_id = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comments'


class CustomFields(models.Model):
    type = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    field_format = models.CharField(max_length=30)
    possible_values = models.TextField(blank=True, null=True)
    regexp = models.CharField(max_length=255, blank=True, null=True)
    min_length = models.IntegerField(blank=True, null=True)
    max_length = models.IntegerField(blank=True, null=True)
    is_required = models.BooleanField()
    is_for_all = models.BooleanField()
    is_filter = models.BooleanField()
    position = models.IntegerField(blank=True, null=True)
    searchable = models.NullBooleanField()
    default_value = models.TextField(blank=True, null=True)
    editable = models.NullBooleanField()
    visible = models.BooleanField()
    multiple = models.NullBooleanField()
    format_store = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_fields'


class CustomFieldsProjects(models.Model):
    custom_field_id = models.IntegerField()
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custom_fields_projects'
        unique_together = (('custom_field_id', 'project_id'),)


class CustomFieldsRoles(models.Model):
    custom_field_id = models.IntegerField()
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custom_fields_roles'
        unique_together = (('custom_field_id', 'role_id'),)


class CustomFieldsTrackers(models.Model):
    custom_field_id = models.IntegerField()
    tracker_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custom_fields_trackers'
        unique_together = (('custom_field_id', 'tracker_id'),)


class CustomValues(models.Model):
    customized_type = models.CharField(max_length=30)
    customized_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_values'


class Documents(models.Model):
    project_id = models.IntegerField()
    category_id = models.IntegerField()
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents'


class EmailAddresses(models.Model):
    user_id = models.IntegerField()
    address = models.TextField()
    is_default = models.BooleanField()
    notify = models.BooleanField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'email_addresses'


class EnabledModules(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'enabled_modules'


class Enumerations(models.Model):
    name = models.CharField(max_length=30)
    position = models.IntegerField(blank=True, null=True)
    is_default = models.BooleanField()
    type = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField()
    project_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    position_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enumerations'


class GlobalIssueTemplates(models.Model):
    title = models.TextField(blank=True, null=True)
    issue_title = models.TextField(blank=True, null=True)
    tracker_id = models.IntegerField(blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    enabled = models.NullBooleanField()
    position = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'global_issue_templates'


class GlobalIssueTemplatesProjects(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    global_issue_template_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'global_issue_templates_projects'


class GroupsUsers(models.Model):
    group_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'groups_users'
        unique_together = (('group_id', 'user_id'), ('group_id', 'user_id'),)


class IssueCategories(models.Model):
    project_id = models.IntegerField()
    name = models.CharField(max_length=30)
    assigned_to_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_categories'


class IssueRelations(models.Model):
    issue_from_id = models.IntegerField()
    issue_to_id = models.IntegerField()
    relation_type = models.CharField(max_length=255)
    delay = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_relations'
        unique_together = (('issue_from_id', 'issue_to_id'),)


class IssueStatuses(models.Model):
    name = models.CharField(max_length=30)
    is_closed = models.BooleanField()
    position = models.IntegerField(blank=True, null=True)
    default_done_ratio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_statuses'


class IssueTemplateSettings(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    help_message = models.TextField(blank=True, null=True)
    enabled = models.NullBooleanField()
    should_replaced = models.NullBooleanField()
    inherit_templates = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'issue_template_settings'


class IssueTemplates(models.Model):
    title = models.TextField()
    project_id = models.IntegerField(blank=True, null=True)
    tracker_id = models.IntegerField()
    author_id = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    enabled = models.NullBooleanField()
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    issue_title = models.TextField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    is_default = models.NullBooleanField()
    enabled_sharing = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'issue_templates'


class Issues(models.Model):
    tracker_id = models.IntegerField()
    project_id = models.IntegerField()
    subject = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField()
    assigned_to_id = models.IntegerField(blank=True, null=True)
    priority_id = models.IntegerField()
    fixed_version_id = models.IntegerField(blank=True, null=True)
    author_id = models.IntegerField()
    lock_version = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    done_ratio = models.IntegerField()
    estimated_hours = models.FloatField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    root_id = models.IntegerField(blank=True, null=True)
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    is_private = models.BooleanField()
    closed_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issues'


class JournalDetails(models.Model):
    journal_id = models.IntegerField()
    property = models.CharField(max_length=30)
    prop_key = models.CharField(max_length=30)
    old_value = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'journal_details'


class Journals(models.Model):
    journalized_id = models.IntegerField()
    journalized_type = models.CharField(max_length=30)
    user_id = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField()
    private_notes = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'journals'


class MemberRoles(models.Model):
    member_id = models.IntegerField()
    role_id = models.IntegerField()
    inherited_from = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_roles'


class Members(models.Model):
    user_id = models.IntegerField()
    project_id = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    mail_notification = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'members'
        unique_together = (('user_id', 'project_id'),)


class Messages(models.Model):
    board_id = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)
    replies_count = models.IntegerField()
    last_reply_id = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    locked = models.NullBooleanField()
    sticky = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class News(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=60)
    summary = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    author_id = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    comments_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'news'


class Programmers(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    active = models.NullBooleanField()
    manager = models.NullBooleanField()
    supervisor = models.ForeignKey('Users', models.DO_NOTHING, db_column='supervisor', blank=True, null=True, related_name='programmer_supervisor_user')

    class Meta:
        managed = False
        db_table = 'programmers'


class ProjectDistribution(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='user', blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING, db_column='project', blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    from_field = models.DateField(db_column='from', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.DateField(blank=True, null=True)
    prospective_project = models.ForeignKey('ProspectiveProjects', models.DO_NOTHING, db_column='prospective_project', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_distribution'


class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    is_public = models.BooleanField()
    parent_id = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    inherit_members = models.BooleanField()

    @property
    def start_date(self):
        CustomValues = apps.get_model('management', 'CustomValues')
        start_date = CustomValues.objects.filter(customized_id=self.id, custom_field_id=CustomFields.objects.get(name='Start Date').id)
        if start_date is None or len(start_date) == 0 or start_date[0].value == '':
            # print "No start date found"
            return None
        else:
            return datetime.datetime.strptime(start_date.first().value, '%Y-%m-%d')
    
    @property
    def is_cssr_project(self):
        try:
            return self.parent_id == Projects.objects.get(name="Center for Social Science Research Projects").id
        except:
            return False

    @property
    def end_date(self):
        CustomValues = apps.get_model('management', 'CustomValues')
        end_date = CustomValues.objects.filter(customized_id=self.id, custom_field_id=CustomFields.objects.get(name='Target End Date').id)
        if end_date is None or len(end_date) == 0 or end_date[0].value == '':
            # print "No start date found"
            return None
        else:
            return datetime.datetime.strptime(end_date.first().value, '%Y-%m-%d')
    
    @property
    def is_active_project(self):
        CustomValues = apps.get_model('management', 'CustomValues')
        active_project = CustomValues.objects.filter(customized_id=self.id, custom_field_id=CustomFields.objects.get(name='Active Project').id)
        if active_project is None or len(active_project) == 0 or active_project[0].value == '':
            return None
        else:
            return active_project[0].value == '1'

    def is_in_active_time(self, start_date=None, end_date=None, delta=None):
        if start_date:
            start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        else:
            start = datetime.datetime.today()

        if end_date and not delta:
            end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        elif delta:
            try:
                delta_int = int(delta)
                end = start + datetime.timedelta(days=delta)
            except TypeError:
                end = datetime.datetime.today()
        else:
            end = datetime.datetime.today()
        
        if start <= self.start_date or self.start_date <= end or \
            start <= self.end_date or self.end_date <= end:
            return True
        else: 
            return False
    
    def get_remaining_spend_series(self, start_date=None, end_date=None, delta=None):
        # first figure out forward-looking burnable funds by day
        start = datetime.datetime.today()
        end = self.end_date

        budget = CustomValues.objects.filter(customized_id=self.id,
                                            custom_field_id=CustomFields.objects.get(name='Budget $').id)
        if budget is None or len(budget) == 0 or budget[0].value == '':
            # print "No budget found"
            return []

        accumulative = CustomValues.objects.filter(customized_id=self.id, custom_field_id=CustomFields.objects.get(name='Accumulative $').id)
        if accumulative is None or len(accumulative) == 0 or accumulative[0].value == '':
            # print "No accumulative found"
            return []
        
        remaining = round(float(budget[0].value) - float(accumulative[0].value),2)

        week_count = round(((end - start).days + 1)/7.0, 2)
        # print dir(day_count)
        spend_per_week = max(round(((remaining / float(week_count)) / 38.0) / 77.0, 1), 0)
        print "target spending:", spend_per_week, "per week"

        series_start = start_date if start_date else start
        if end_date:
            series_end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        elif delta:
            try:
                delta_int = int(delta)
                series_end = series_start + datetime.timedelta(days=delta)
            except TypeError:
                series_end = series_start + datetime.timedelta(days=180)
        else:
            series_end = datetime.datetime.today() + datetime.timedelta(days=180)
        
        series_day_count = (series_end - series_start).days + 1

        spend_series = []
        date = series_start
        while date <= series_end:
            if date >= self.start_date and date <= self.end_date:
                spend_series.append(spend_per_week)
            else:
                spend_series.append(0)
            date = date + datetime.timedelta(days=7)

        return spend_series

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'projects'


class ProjectsTrackers(models.Model):
    project_id = models.IntegerField(primary_key=True)
    tracker_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projects_trackers'
        unique_together = (('project_id', 'tracker_id'), ('project_id', 'tracker_id'),)


class ProspectiveProjects(models.Model):
    name = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    fte_requirements = models.FloatField(blank=True, null=True)
    budget = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prospective_projects'


class Queries(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    filters = models.TextField(blank=True, null=True)
    user_id = models.IntegerField()
    column_names = models.TextField(blank=True, null=True)
    sort_criteria = models.TextField(blank=True, null=True)
    group_by = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    visibility = models.IntegerField(blank=True, null=True)
    options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'queries'


class QueriesRoles(models.Model):
    query_id = models.IntegerField()
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'queries_roles'
        unique_together = (('query_id', 'role_id'),)


class Repositories(models.Model):
    project_id = models.IntegerField()
    url = models.CharField(max_length=255)
    login = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    root_url = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    path_encoding = models.CharField(max_length=64, blank=True, null=True)
    log_encoding = models.CharField(max_length=64, blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    is_default = models.NullBooleanField()
    created_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repositories'


class Roles(models.Model):
    name = models.CharField(max_length=30)
    position = models.IntegerField(blank=True, null=True)
    assignable = models.NullBooleanField()
    builtin = models.IntegerField()
    permissions = models.TextField(blank=True, null=True)
    issues_visibility = models.CharField(max_length=30)
    users_visibility = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'roles'


class SchemaMigrations(models.Model):
    version = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class SelfTrainingTime(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='user', blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    hours = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'self_training_time'


class Settings(models.Model):
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settings'


class TimeEntries(models.Model):
    project_id = models.IntegerField()
    user_id = models.IntegerField()
    issue_id = models.IntegerField(blank=True, null=True)
    hours = models.FloatField()
    comments = models.CharField(max_length=255, blank=True, null=True)
    activity_id = models.IntegerField()
    spent_on = models.DateField()
    tyear = models.IntegerField()
    tmonth = models.IntegerField()
    tweek = models.IntegerField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'time_entries'


class TimeEntryLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.TextField(blank=True, null=True)
    old_record = models.TextField(blank=True, null=True)
    new_record = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    target = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_entry_log'


class Tokens(models.Model):
    user_id = models.IntegerField()
    action = models.CharField(max_length=30)
    value = models.CharField(unique=True, max_length=40)
    created_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tokens'


class Trackers(models.Model):
    name = models.CharField(max_length=30)
    is_in_chlog = models.BooleanField()
    position = models.IntegerField(blank=True, null=True)
    is_in_roadmap = models.BooleanField()
    fields_bits = models.IntegerField(blank=True, null=True)
    default_status_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trackers'


class UserPreferences(models.Model):
    user_id = models.IntegerField()
    others = models.TextField(blank=True, null=True)
    hide_mail = models.NullBooleanField()
    time_zone = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_preferences'


class Users(models.Model):
    login = models.CharField(max_length=255)
    hashed_password = models.CharField(max_length=40)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=255)
    admin = models.BooleanField()
    status = models.IntegerField()
    last_login_on = models.DateTimeField(blank=True, null=True)
    language = models.CharField(max_length=5, blank=True, null=True)
    auth_source_id = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    identity_url = models.CharField(max_length=255, blank=True, null=True)
    mail_notification = models.CharField(max_length=255, blank=True, null=True)
    salt = models.CharField(max_length=64, blank=True, null=True)
    must_change_passwd = models.BooleanField()
    passwd_changed_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Versions(models.Model):
    project_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    wiki_page_title = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    sharing = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'versions'


class Watchers(models.Model):
    watchable_type = models.CharField(max_length=255)
    watchable_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'watchers'


class WikiContentVersions(models.Model):
    wiki_content_id = models.IntegerField()
    page_id = models.IntegerField()
    author_id = models.IntegerField(blank=True, null=True)
    data = models.BinaryField(blank=True, null=True)
    compression = models.CharField(max_length=6, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    updated_on = models.DateTimeField()
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wiki_content_versions'


class WikiContents(models.Model):
    page_id = models.IntegerField()
    author_id = models.IntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    updated_on = models.DateTimeField()
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wiki_contents'


class WikiPages(models.Model):
    wiki_id = models.IntegerField()
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField()
    protected = models.BooleanField()
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wiki_pages'


class WikiRedirects(models.Model):
    wiki_id = models.IntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    redirects_to = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField()
    redirects_to_wiki_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wiki_redirects'


class Wikis(models.Model):
    project_id = models.IntegerField()
    start_page = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wikis'


class Workflows(models.Model):
    tracker_id = models.IntegerField()
    old_status_id = models.IntegerField()
    new_status_id = models.IntegerField()
    role_id = models.IntegerField()
    assignee = models.BooleanField()
    author = models.BooleanField()
    type = models.CharField(max_length=30, blank=True, null=True)
    field_name = models.CharField(max_length=30, blank=True, null=True)
    rule = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workflows'


###################################################################
# ScrumWatch Functionality
###################################################################

class PipelineStep(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#1ABB9C')  # <-- Meant to be Hex, example: '#ff0000' for red
    step_number = models.IntegerField()
    fontawesome_icon = models.CharField(max_length=50, blank=True,
                            null=True, default="fa-pencil")  # <-- Meant to be a font-awesome icon class

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['step_number']
        managed = False
        db_table = 'integration_pipelinestep'


class PotentialProject(models.Model):
    name = models.CharField(max_length=1000)
    redmine_project = models.ForeignKey('Projects', blank=True, null=True)
    active = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def completion_color(self):
        color = '#73879C'
        for step in self.project_pipelinestep.all():
            if step.completed:
                color = step.step.color
        return color

    class Meta:
        managed = False
        db_table = 'integration_potentialproject'


class PotentialProjectPipelineStep(models.Model):
    project = models.ForeignKey('PotentialProject', related_name='project_pipelinestep')
    step = models.ForeignKey('PipelineStep', related_name='pipelinestep')
    completed = models.BooleanField(default=False)
    date_completed = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.project.name + ': ' + self.step.name

    class Meta:
        ordering = ['project', 'step']
        managed = False
        db_table = 'integration_potentialprojectpipelinestep'


class Sprint(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    name = models.CharField(max_length=1024)
    cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    owner = models.ForeignKey(User, related_name='user_sprints')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['start_date', 'end_date', 'name']
        managed = False
        db_table = 'integration_sprint'


class SprintSlice(models.Model):
    sprint = models.ForeignKey('Sprint', related_name='sprint_slice')
    redmine_project = models.ForeignKey('Projects', related_name='project_sprint_slice')
    percentage = models.IntegerField(default=100)

    def __unicode__(self):
        return self.sprint.name + ': ' + self.redmine_project.name + ' ('+str(self.percentage)+'%)'

    def get_slice_cost(self, last_date, last_cost):
        # starting at the last date on the cost_to_date...
        last_date = (datetime.datetime.strptime(last_date, '%Y-%m-%d') + datetime.timedelta(days=0)).date()

        if last_date < self.sprint.start_date:
            last_date = self.sprint.start_date

        # multiply this by the percentage of this slice
        sprint_data = [
            {
                'spent_on': last_date.strftime('%Y, %m, %d').split(', '),
                'sum': last_cost
            },
            {
                'spent_on': self.sprint.end_date.strftime('%Y, %m, %d').split(', '),
                'sum': float(last_cost + (float(self.sprint.cost) * float(self.percentage / 100.0)))
            }
        ]

        return sprint_data

    class Meta:
        ordering = ['-percentage', 'redmine_project__name']
        managed = False
        db_table = 'integration_sprintslice'


class ProductOwnerProjects(models.Model):
    owner = models.ForeignKey(User, related_name='po_projects')
    project = models.ForeignKey('Projects', related_name='projects_po')

    def __unicode__(self):
        if self.owner.first_name and self.owner.last_name:
            return self.owner.first_name + ' ' + self.owner.first_name + ': ' + self.project.name
        else:
            return self.owner.username + ': ' + self.project.name

    def get_cost_to_date(self):
        spent_on_dict = {}
        data = []
        total = 0.0
        time_entries = TimeEntries.objects.filter(project_id=self.project.id).order_by('spent_on')
        for entry in time_entries:
            # does the activity have "non-billable" in the name?
            activity = Enumerations.objects.get(id=entry.activity_id)
            if 'non-billable' in activity.name.lower():
                continue

            # get the category for this entry
            category = CustomValues.objects.get(customized_id=entry.id)
            # get the rate for this date
            rate = ChargeRates.objects.filter(start_date__lte=entry.spent_on,
                                              end_date__gte=entry.spent_on,
                                              category=category.value)
            if len(rate) >= 1:
                cost_rate = rate[0].rate
            else:
                cost_rate = 0

            total += (entry.hours * int(cost_rate))
            spent_on_dict[entry.spent_on] = total

        for key,val in spent_on_dict.iteritems():
            data.append({
                'spent_on': key.strftime('%Y, %m, %d').split(', '),
                'sum': val
            })

        actual = sorted(data, key=lambda k: k['spent_on'])

        # now fill in the gaps...
        boundary_start = None
        boundary_end = None
        days_to_add = []
        for entry in actual:
            if boundary_start is None:
                boundary_start = entry
                continue
            if boundary_end is None:
                boundary_end = entry

            # at this point, we should have a boundary start (previous date)
            #   and a boundary end (current date)
            # is their difference greater than 1 day between the two?
            if (datetime.datetime.strptime('-'.join(boundary_end['spent_on']), '%Y-%m-%d') - datetime.datetime.strptime('-'.join(boundary_start['spent_on']), '%Y-%m-%d')).days > 1:
                # then compute the difference
                # cost_change = boundary_end['sum'] - boundary_start['sum']

                # how many days difference?
                days_difference = (datetime.datetime.strptime('-'.join(boundary_end['spent_on']), '%Y-%m-%d') - datetime.datetime.strptime('-'.join(boundary_start['spent_on']), '%Y-%m-%d')).days

                # how much per day do we averagely increase?  (is averagely a word?  probably not...)
                # cost_difference_per_day = float(cost_change) / float(days_difference)

                # now add the days/difference
                current = datetime.datetime.strptime('-'.join(boundary_start['spent_on']), '%Y-%m-%d') + datetime.timedelta(days=1)
                current_sum = boundary_start['sum'] #+ cost_difference_per_day
                ending = datetime.datetime.strptime('-'.join(boundary_end['spent_on']), '%Y-%m-%d')
                while current < ending:
                    days_to_add.append({
                        'spent_on': current.strftime('%Y, %m, %d').split(', '),
                        'sum': float("%.2f" % current_sum)
                    })
                    current += datetime.timedelta(days=1)
                    # current_sum += cost_difference_per_day
            boundary_start = boundary_end
            boundary_end = entry

        # the last boundary still needs to be checked...
        if (datetime.datetime.strptime('-'.join(boundary_end['spent_on']), '%Y-%m-%d') - datetime.datetime.strptime(
                '-'.join(boundary_start['spent_on']), '%Y-%m-%d')).days > 1:
            # then compute the difference
            # cost_change = boundary_end['sum'] - boundary_start['sum']

            # how many days difference?
            days_difference = (
            datetime.datetime.strptime('-'.join(boundary_end['spent_on']), '%Y-%m-%d') - datetime.datetime.strptime(
                '-'.join(boundary_start['spent_on']), '%Y-%m-%d')).days

            # how much per day do we averagely increase?  (is averagely a word?  probably not...)
            # cost_difference_per_day = float(cost_change) / float(days_difference)

            # now add the days/difference
            current = datetime.datetime.strptime('-'.join(boundary_start['spent_on']), '%Y-%m-%d') + datetime.timedelta(
                days=1)
            current_sum = boundary_start['sum']  # + cost_difference_per_day
            ending = datetime.datetime.strptime('-'.join(boundary_end['spent_on']), '%Y-%m-%d')
            while current < ending:
                days_to_add.append({
                    'spent_on': current.strftime('%Y, %m, %d').split(', '),
                    'sum': float("%.2f" % current_sum)
                })
                current += datetime.timedelta(days=1)


        if len(days_to_add) > 0:
            total = actual + days_to_add
            total = sorted(total, key=lambda k: k['spent_on'])
        else:
            total = actual

        return total

    def get_target_burn_rate(self):
        target_sum_to_date = 0

        start_date = CustomValues.objects.filter(customized_id=self.project.id,
                                              custom_field_id=CustomFields.objects.get(name='Start Date').id)
        if start_date is None or len(start_date) == 0 or start_date[0].value == '':
            # print "No start date found"
            return []


        end_date = CustomValues.objects.filter(customized_id=self.project.id,
                                            custom_field_id=CustomFields.objects.get(name='Target End Date').id)
        if end_date is None or len(end_date) == 0 or end_date[0].value == '':
            # print "No end date found"
            return []

        budget = CustomValues.objects.filter(customized_id=self.project.id,
                                            custom_field_id=CustomFields.objects.get(name='Budget $').id)

        if budget is None or len(budget) == 0 or budget[0].value == '':
            # print "No budget found"
            return []

        # how many days are there?
        start = datetime.datetime.strptime(start_date[0].value, '%Y-%m-%d')
        end = datetime.datetime.strptime(end_date[0].value, '%Y-%m-%d')

        day_count = (end - start).days + 1
        # print dir(day_count)
        spend_per_day = float(budget[0].value) / float(day_count)
        print "target spending:", spend_per_day, "per day"

        target_burn_days = []
        current_date = start
        while current_date <= end:
            target_sum_to_date += spend_per_day
            target_burn_days.append({
                'spent_on': current_date.strftime('%Y, %m, %d').split(', '),
                'sum': ('%.2f' % target_sum_to_date)
            })
            current_date += datetime.timedelta(days=1)

        return target_burn_days

    class Meta:
        ordering = ['owner', 'project__name']
        managed = False
        db_table = 'integration_productownerprojects'
