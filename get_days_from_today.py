import datetime


def get_days_from_today(date): #data format: "yyyy-mm-dd"
    try:
        now=datetime.date.today()
        try:
            date_parameter=datetime.date.fromisoformat(date)#, "%Y-%m-%d")
        except:
            print("Date format error in get_days_from_today(date)")
            return None

        day_now=now.toordinal()
        day_parameter=date_parameter.toordinal()
        return day_now-day_parameter
    except:
        print("Unknown error in get_days_from_today(date)")   
        return None 
#test
print(get_days_from_today("2025-01-01"))