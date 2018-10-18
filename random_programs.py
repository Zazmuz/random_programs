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





#                       Counter---------------------------------------------------------------------------------



# counting_seconds = 2450
# counting_seconds = 0
# counting_minutes = 0
# counting_hours = 0
# while True:
#     if counting_seconds >= 60:
#         while counting_seconds >= 60:
#             counting_seconds -= 60
#             counting_minutes += 1
#     if counting_minutes >= 60:
#         while counting_minutes >= 60:
#             counting_minutes -= 60
#             counting_hours += 1
#     print("\n secs:" + str(counting_seconds) + "\n minutes: " + str(counting_minutes) + "\n hours: " + str(counting_hours) + "\n")
#     counting_seconds += 1
#     time.sleep(1)











def fibonacci_finder(repeats):
    fibonacci_sequence = None
    fibonacci_number_1 = 0
    fibonacci_number_2 = 1
    skipper = 0
    for i in range(repeats):
        if skipper == 1:
            fibonacci_sequence = fibonacci_number_1 + fibonacci_number_2
            fibonacci_number_2 = fibonacci_number_1
            fibonacci_number_1 = fibonacci_sequence
        else:
            skipper = 1
            fibonacci_sequence = 0
    print("The " + str(repeats) + "th number of the fibonacci seuence is: " + str(fibonacci_sequence))


def fibonacci_checker(number):
    fibonacci_sequence = None
    fibonacci_number_1 = 0
    fibonacci_number_2 = 1
    no_overly_large_numbers_are_ok = 0
    skipper = 0
    while True:
        if skipper == 1:
            fibonacci_sequence = fibonacci_number_1 + fibonacci_number_2
            fibonacci_number_2 = fibonacci_number_1
            fibonacci_number_1 = fibonacci_sequence
            if fibonacci_sequence == number:
                print("Your number is a fibonacci number!")
                break
            if no_overly_large_numbers_are_ok > 5000:
                print("Your number is not a fibonocci numbers! :(")
                break
            no_overly_large_numbers_are_ok += 1
        else:
            skipper = 1
            fibonacci_sequence = 0
fibonacci_checker(int(input()))

























