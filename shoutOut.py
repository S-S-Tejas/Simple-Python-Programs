import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
choice = "Y"
listPeople = ["Tejas"]
while True:
    a = input("Enter a name: ")
    listPeople.append(a)
    choice = input("Wanna enter another name (Y/N): ").upper()
    if choice == "N":
        break
while True:
    for People in listPeople:
        print(f"Shoutout to {People}")
        speaker.Speak(f"Shoutout to {People}")
    break
print("Thank you!")
speaker.Speak(f"Thank you!")