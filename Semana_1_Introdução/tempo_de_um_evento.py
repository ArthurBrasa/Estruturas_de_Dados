def calculate_event_time(start, end):
    try:
        time = transform_time(end) - transform_time(start)
        if time<0:
            return 'Data inválida!'
    except:
        return 'Data inválida!'
        
    
    time = format_time(time)
    return f'{time[0]} dia(s)\n{time[1]} hora(s)\n{time[2]} minuto(s)\n{time[3]} segundo(s)'


def transform_time(time):
    hours = time[1].split(':')
    seconds = (int(time[0])*86400) + (int(hours[0])*3600) + int(hours[1])*60 + int(hours[2])
    return seconds

def format_time(time):
    day = time//86400
    time %= 86400
    hours = time//3600
    time %= 3600
    minutes = time//60
    time %= 60
    return (day, hours, minutes, time)

start = input().split()
end = input().split()
"""Exemplo de entrada
    5 08:12:23
    9 06:13:23
"""

print(calculate_event_time(start, end))
