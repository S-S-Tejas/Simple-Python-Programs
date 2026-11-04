import time
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

print("24 Hour - Drink Water Remainder: ")

with open("water.txt", "a") as f:
    print(f.write("Drink Water Remainder:\n"))

with open("water.txt", "r") as f:
    print("Previous Activity: ")
    print(f.read())

count = 0
while count<=24:
    a = "Drink Water" 
    b = time.strftime("%a, %d %b %Y %H:%M:%S")
    time.sleep(3600)
    count = count + 1
    print(f"{a}, {b}")
    speaker.Speak(f"{a}, {b}")
    with open("water.txt", "a") as f:
        print(f.write(f"{a}, {b}\n"))

with open("water.txt", "a") as f:
        print(f.write("\n24 Hour report generated!\n"))
print("Thank you")
