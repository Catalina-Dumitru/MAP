
#pyautogui
import pyautogui
import time
import keyboard
def cautare_google():
    if pyautogui.locateOnScreen(r"C:\Users\catal\Pictures\Screenshots\Screenshotgoogle.png", confidence=0.3) !=None:
      print("da")
      camp_google=pyautogui.locateOnScreen(r"C:\Users\catal\Pictures\Screenshots\Screenshotgoogle.png", confidence=0.3)
      pyautogui.click(camp_google)
      pyautogui.write("https://www.youtube.com/@DanCadar")
      pyautogui.press('enter')
      time.sleep(2)
    else:
      print("nu")

res = pyautogui.confirm("daca doriti sa incepeti rularea programului?","Confirmare")
if (res =="OK"):
    cautare_google()
else:
    pyautogui.alert("ati ales anulare","Anulare")