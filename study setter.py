import time

mood_map = {
    'physics': {'mood': range(8, 11), 'time':40},
    'chemistry': {'mood': [5], 'time': 45},
    'biology': {'mood': range(6, 8), 'time': 90},
    'maths': {'mood': range(3, 5), 'time': 60},
    'english': {'mood': [2], 'time': 30}
}

user = int(input('Enter your mood on the scale 2-10: '))

selected = None

for subject, values in mood_map.items():
    if user in values['mood']:
        selected = subject
        break

def timer():
    if selected:
        x = mood_map[selected]['time']
        print(f'You have to study {selected} for {x} minutes')

        start = input('Enter s to run timer: ').lower()

        if start == 's':
            total_seconds = x * 60
            if x<60:
                for t in range(total_seconds, 0, -1):
                    seconds = t % 60
                    minutes = t // 60
                    print(f'00:{minutes:02d}:{seconds:02d}')
                    time.sleep(1)
                print("time's up")
            elif x>60:
                for t in range(total_seconds, 0, -1):
                    hours = t // 3600
                    minutes = (t % 3600) // 60
                    seconds = t % 60
                    print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
                    time.sleep(1)
                print("time's up")
        else:
            print('Type s to start studying')
            timer()
    else:
        print("No subject matches your mood")

timer()








