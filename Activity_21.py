import time

def convert_sec_to_ymdhms(sec):
    temp, seconds = divmod(sec, 60)
    temp, minutes = divmod(temp, 60)
    temp, hours = divmod(temp, 24)
    temp, days = divmod(temp, 30)
    months = temp % 12
    years = sec // (365*24*60*60) #coz if we just consider temp after doing temp %12 then it would be w.r.t 360 days and not 365 so this
    return {'years': int(years), 'months': int(months), 'days': int(days),
            'hours': int(hours), 'minutes': int(minutes), 'seconds':seconds}

def get_todays_date(passed_time):
    day = 1 + passed_time['days']
    month = 1 + passed_time['months'] #the month is 4 months back???
    year = 1970 + passed_time['years']
    return f"{day}-{month}-{year}"

def main():
    sec = time.time()
    passed_time = convert_sec_to_ymdhms(sec)
    print(passed_time)
    today = get_todays_date(passed_time)
    print(today)

main()
