# from django_celery_beat.models import CrontabSchedule, PeriodicTask
# import pytz

# schedule, created = CrontabSchedule.objects.get_or_create(
#     minute='1',
#     hour='*',
#     day_of_week='*',
#     day_of_month='*',
#     month_of_year='*',
#     timezone=pytz.timezone('Asia/Baku')
# )

# PeriodicTask.objects.create(
#     interval=schedule,                  # we created this above.
#     name='Importing contacts',          # simply describes this periodic task.
#     task='account_create',  # name of task.
# )