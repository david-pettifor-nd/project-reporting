from django.core.management.base import BaseCommand, CommandError
import datetime
import psycopg2
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText
from django.shortcuts import render

class Command(BaseCommand):
    help = 'Checks for low hours of the previous week'

    def add_arguments(self, parser):
        parser.add_argument('--type', type=str)

    def handle(self, *args, **options):
        dateframe = get_last_date_range()

        # get a list of all users which have supervisors
        connection = psycopg2.connect(database='redmine_default', user='redmine_system', password='Lets go turbo!')
        cursor = connection.cursor()

        # get the custom field id for supervisor lists
        cursor.execute(
            "SELECT id FROM custom_fields WHERE name = 'Supervisor Notification Emails' AND type='UserCustomField';")
        custom_field_id = cursor.fetchone()
        if custom_field_id is None:
            self.stdout.write(
                self.style.ERROR('Failed to find custom field "Supervisor Notification Emails" for users.'))
        else:
            custom_field_id = custom_field_id[0]



        cursor.execute("SELECT distinct(customized_id) FROM custom_values WHERE custom_field_id = %(custom_field_id)s;" % {
            'custom_field_id': custom_field_id
        })

        user_list = cursor.fetchall()
        low_hours_count = 0
        for user in user_list:
            hours = get_hours(user_id=user[0],
                              start_date=dateframe['saturday'],
                              end_date=dateframe['friday'],
                              cursor=cursor)
            # check hours
            if hours is None or hours < 40:
                low_hours_count += 1
                print "Sending email to", user[0], "for low hours:", hours

                if options['type'] == 'monday_morning':
                    email_address = 'dpettifo@nd.edu'
                    message = open('templates/notification_emails/monday_morning.html', 'r').read()
                    send_notification(email_address, ['noctemowl@gmail.com'], message, 'Redmine: Low Hours Reminder')

        print low_hours_count, "/", len(user_list), "had low hours"


            # self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))

def get_last_date_range():
    today = datetime.date.today()
    idx = (today.weekday() + 2) % 7  # MON = 0, SUN = 6 -> SUN = 0 .. SAT = 6
    # print ("IDX: " + str(idx))
    sat = today - datetime.timedelta(idx + 7)
    fri = sat + datetime.timedelta(6)
    return {
        'saturday': sat,
        'friday': fri
    }

def get_hours(user_id, start_date, end_date, cursor):
    cursor.execute("SELECT SUM(hours) FROM time_entries "
                   "WHERE user_id=%(user)s AND spent_on >= '%(start)s' AND spent_on <= '%(end)s'" % {
        'user': user_id,
        'start': start_date,
        'end': end_date
    })

    return cursor.fetchone()[0]

def send_notification(to_email, cc_list, message_body, message_subject):
    msg = MIMEText(message_body, 'html')

    msg['Subject'] = message_subject
    msg['From'] = 'noreply@turbo.crc.nd.edu'
    msg['To'] = to_email
    if cc_list:
        msg['Cc'] = cc_list
        list_of_recipients = to_email + cc_list
    else:
        list_of_recipients = [to_email]

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('localhost')
    s.sendmail('noreply@turbo.crc.nd.edu', list_of_recipients, msg.as_string())
    s.quit()