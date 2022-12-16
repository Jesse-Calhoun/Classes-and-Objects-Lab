from alarm_clock import AlarmClock

johns_alarm = AlarmClock('5:00', True, '6:00')

print(johns_alarm.current_time)
print()
johns_alarm.change_current_time('5:05')
print()
johns_alarm.toggle_alarm()
