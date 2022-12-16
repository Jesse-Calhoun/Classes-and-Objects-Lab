class AlarmClock:

    def __init__(self, current_time, alarm_on_or_off, alarm_set_for):
        self.current_time = current_time
        self.alarm_is_on = alarm_on_or_off
        self.alarm_set_for = alarm_set_for
    def change_current_time(self, new_time):
        self.current_time = new_time
        print(self.current_time)
    def toggle_alarm(self):
        self.alarm_is_on = not self.alarm_is_on
        if self.alarm_is_on:
                print('Alarm has been turned on.')
        else:
                print('Alarm has been turned off.')
    def set_alarm_time(self, alarm_time):
        self.alarm_set_for = alarm_time
        print(self.alarm_set_for)
    
jesses_alarm = AlarmClock('2:25PM',True, '6:00PM')
print(jesses_alarm.current_time)
print()
jesses_alarm.change_current_time('4:30PM')
print()
print(jesses_alarm.alarm_is_on)
jesses_alarm.toggle_alarm()
print()
print(jesses_alarm.alarm_is_on)
print()
print(jesses_alarm.alarm_set_for)
jesses_alarm.set_alarm_time('6:30PM')
