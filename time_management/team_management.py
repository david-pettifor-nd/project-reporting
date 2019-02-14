from django.shortcuts import HttpResponse, render
from django.db import connection
import json
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.decorators import login_required
from time_management.models import TeamMember, RedmineUser
from time_management.decorators import user_is_in_manager_group

@login_required
@user_passes_test(lambda u: u.is_superuser)
def team_management(request):
    return render(request, 'teams.html', {'team_list': get_team_list(),
                                          'users': RedmineUser.objects.all().order_by('lastname', 'firstname')})

def get_team_list():
    # get a list of team managers
    managers = TeamMember.objects.values('manager').distinct()

    # for each manager, get a list of team members
    team_list = []
    for manager in managers:
        redmine_manager = RedmineUser.objects.get(id=manager['manager'])
        members = TeamMember.objects.filter(manager=manager['manager']).values('member').distinct()

        member_list = []
        for member in members:
            redmine_user = RedmineUser.objects.get(id=member['member'])
            member_list.append({
                'name': str(redmine_user),
                'id': member['member']
            })

        team_list.append({
            'manager': {
                'name': str(redmine_manager),
                'id': manager['manager']
            },
            'members': member_list
        })

    return team_list


@login_required
@user_passes_test(lambda u: u.is_superuser)
def get_teams(request):
    return HttpResponse(json.dumps(get_team_list()))


def get_specific_team(manager_id):
    redmine_manager = RedmineUser.objects.get(id=manager_id)
    members = TeamMember.objects.filter(manager=manager_id).values('member').distinct()

    member_list = []
    for member in members:
        redmine_user = RedmineUser.objects.get(id=member['member'])
        member_list.append({
            'name': str(redmine_user),
            'id': member['member']
        })

    return json.dumps({
        'manager': {
            'name': str(redmine_manager),
            'id': manager_id
        },
        'members': member_list
    })

@login_required
@user_passes_test(lambda u: u.is_superuser)
def get_team(request):
    return HttpResponse(get_specific_team(manager_id=request.GET['manager']))


@login_required
@user_passes_test(lambda u: u.is_superuser)
def save_manager(request):
    manager_obj = RedmineUser.objects.get(id=request.GET['manager'])
    for member in request.GET.getlist('members[]'):
        team_member = TeamMember.objects.get(member=member)
        team_member.manager = manager_obj
        team_member.save()

    return HttpResponse(get_specific_team(manager_id=request.GET['manager']))