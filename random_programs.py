import time

#                       God----------------------------------------------------------------------------------

# try_out = ["In the beginning", "God created the heavens and the earth"]
# timed_try = 0
# holy_number = 3-0.333-0.333-0.333-0.333-0.333
# repeat = 0
# while True:
#     timed_try -= timed_try
#     time.sleep(holy_number)
#     print(try_out[timed_try])
#
#     timed_try += 1
#     time.sleep(holy_number)
#     print(try_out[timed_try])
#     repeat += 1
#     if repeat == 3:
#         while True:
#             print("Kneel before your king!")
#
#
#


#                       Counter---------------------------------------------------------------------------------



#counting_seconds = 2450
counting_seconds = 120
counting_minutes = 120
counting_hours = 0
while True:
    if counting_seconds >= 60:
        while counting_seconds >= 60:
            counting_seconds -= 60
            counting_minutes += 1
    if counting_minutes >= 60:
        while counting_minutes >= 60:
            counting_minutes -= 60
            counting_hours += 1
    print("\n secs:" + str(counting_seconds) + "\n minutes: " + str(counting_minutes) + "\n hours: " + str(counting_hours) + "\n")
    counting_seconds += 1
    time.sleep(1)


