import datetime
import calendar

def get_upcoming_birthdays(users, now_for_debug=None):
    upcoming_birthdays=[]
    for user in users:
        user_birthday=datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        if now_for_debug==None:                      #for debug and test
            today=datetime.date.today()
        else:
            today=now_for_debug

        if user_birthday.day==29 and user_birthday.month==2 and not calendar.isleap(today.year): #leap year
            user_birthday=user_birthday+datetime.timedelta(days=1)

        
        birthday_this_year=user_birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_actual=birthday_this_year.replace(year=birthday_this_year.year+1)
        else:
            birthday_actual=birthday_this_year
        delta_until_birthday=birthday_actual-today
        if delta_until_birthday.days<7:
            if birthday_actual.isoweekday()>5:
                birthday_actual=birthday_actual+datetime.timedelta(days=8-birthday_actual.isoweekday())
            d={'name': user["name"],
               'congratulation_date': birthday_actual.strftime("%Y.%m.%d")}
                #upcoming_birthdays.update({'name': "1",'congratulation_date': "2"})
            upcoming_birthdays=upcoming_birthdays+[d]


    upcoming_birthdays.sort(key=lambda d: d['congratulation_date'])

    return upcoming_birthdays



users = [
    {"name": "John Doe", "birthday": "1984.02.29"},
    {"name": "Jane Smith", "birthday": "1984.02.28"}
]

upcoming_birthdays = get_upcoming_birthdays(users,datetime.date(2025,2,28))
print("Список привітань на цьому тижні:", upcoming_birthdays)
