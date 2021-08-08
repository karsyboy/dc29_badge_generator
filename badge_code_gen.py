# PySerial is required to run this script make sure to install it with python3 and as sudo
import serial,io,random,bisect

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) # Make sure the serial device is set to the proper port
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
badge_str_1 = "362F" # First for characters of a badge response for your badge
badge_str_2 = "505800CE40911357017C7FBC" # Characters 9 through 32 from the same badge response used for badge_str_1

# Generates a list of all hex combinations to test with
def gen_all_hex():
    i = 0
    while i < 16**4:
        yield "{:04X}".format(i)
        i += 1

badge_id = []
for s in gen_all_hex():
    badge_id.append(s)

# Starts session with defcon badge 
sio.write(str("\n\r"))
sio.flush() 
badge_count = input("Enter current badge count: ")
badge_count = int(badge_count)

# While loop to run through all possible badge combinations
while badge_count <= 65500:
    sio.write(str("5"))
    badge_full_id = badge_str_1 + badge_id[badge_count] + badge_str_2
    print(badge_full_id)
    sio.write(str(badge_full_id))
    sio.write("\n\r")
    sio.write("\n\r")
    sio.flush()
    badge_count += 1
    print(badge_count)

print("Job Done!!!")
ser.close()

