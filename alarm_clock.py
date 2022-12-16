
class AlarmClock:
    current_time = ''
    alarm_set_for = ''
    def __init__(self, current_time, alarm_on_or_off, alarm_set_for):
        self.current_time = current_time
        self.alarm_on_or_off = alarm_on_or_off
        self.alarm_set_for = alarm_set_for
        if self.alarm_on_or_off == True:
                self.alarm_on_or_off = 'Alarm is on.'
        else:
                return 'Alarm is off.'
    
    def change_current_time(self, new_time):
        self.current_time = new_time
        print(self.current_time)
    
    #def set_alarm_clock(self, ):
jesses_alarm = AlarmClock('2:25PM',True, '6:00PM')
print()
print(jesses_alarm.current_time)
print()
jesses_alarm.change_current_time('3:30PM')
print()
print(jesses_alarm.alarm_on_or_off)
