from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print ("")
print ("")
print("""processing.......""")

APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")
while True:
  try:
   with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
      print("")
      session = client.session.save()
      client.send_message("me", f"Here is your TELEGRAM STRING SESSION\n(tap to copy)👇 \n\n `{session}`")
      print("You telegramString session successfully stored in your telegram, please check your Telegram Saved Messages ")
      print("Store it safe !!")
  except:
   print ("")
   print ("Wrong phone number \n make sure its with correct  country code")
   print ("")
   continue
  break
