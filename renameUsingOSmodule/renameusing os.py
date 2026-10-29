import os
def change_dir(direct = r'D:\Code With Harry\Python\images'):  
    os.chdir(direct)
    print(os.getcwd())
while True:
    enter = input("Wanna enter a directory? (Y/N): ")
    if enter == "Y":
        direct = input("Enter your directory: ")
        change_dir(direct)
        break
    else:
        change_dir()
        print(f"Default directory: D:\Code With Harry\Python\images")
        break

def rename():
    directory = os.listdir()
    for i, file in enumerate(directory):
        try:
            os.rename(file, f"{i}.png")
        except Exception as e1:
            os.rename(file, f"{i}.jpg")
        except Exception as e2:
            os.rename(file, f"{i}.pdf")
        except Exception as e3:
            os.rename(file, f"{i}.docx")
        except Exception as e4:
            os.rename(file, f"{i}.py")
        except Exception as e5:
            os.rename(file, f"{i}.js")
        except Exception as e6:
            os.rename(file, f"{i}.html")
        except Exception as e7:
            os.rename(file, f"{i}.css")
        except Exception as e8:
            os.rename(file, f"{i}.mp4")
        except Exception as e9:
            os.rename(file, f"{i}.mov")

print("Supports renaming of :")
print('''
.jpg
.png
.pdf
.docx
.py
.js
.html
.css
.mp4
.mov''')
choices_market = input("Would you like to change the files name to 1, 2, 3..n: (Y/N): ")
if choices_market=="Y" or choices_market=="y":
    rename()
    print("Done")
else: 
    print("Exiting... File names remain the same")
    print("Thank you!")