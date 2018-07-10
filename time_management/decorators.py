from django.http import HttpResponseRedirect
from django.db import connection
from pr.settings.base import LOGIN_URL

def user_is_in_manager_group(function):
    def wrap(request, *args, **kwargs):
        username = request.user.username
        cursor = connection.cursor()

        cursor.execute("select lastname "
                       "from users "
                       "where id in "
                       "(select group_id "
                       "from groups_users "
                       "where user_id in "
                       "(select id from users where login = '%s'));" % (username))

        groups = cursor.fetchall()
        group_list = []
        for g in groups:
            group_list.append(g[0])

        if "Managers" in group_list:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(LOGIN_URL)

        # return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap