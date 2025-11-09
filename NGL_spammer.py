import requests
import uuid 
import random
import time
import os 

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)"
]

current_target = "placeholder"

def clear_screen():
    #clears the screen for all os's because linux is underappreciated, fuck this windowed world.
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def send_ngl(username):
    with open("messages.txt", "r") as fr:
        messages = [line.strip() for line in fr if line.strip()]
        question = random.choice(messages)
    data = {
        "username": username,
        "question": question,
        "deviceId": str(uuid.uuid4()),
        "referrer": "https://snapchat.com"
    }
    
    headers = {
    "User-Agent": random.choice(user_agents),
    "Content-Type": "application/x-www-form-urlencoded"
    }
    
    try:
        res = requests.post("https://ngl.link/api/submit", data=data, headers=headers, timeout=8)
        print(f"sent to {username} message: {question} | {res.status_code}")
    except Exception as e:
        print(f"error: {e}")
    if res.status_code == "404":
        print("404 User not found")

clear_screen()

print("""
         >==>    >=>    >===>    >=>                                                                                        
         >> >=>  >=>  >>    >=>  >=>                                                                                        
         >=> >=> >=> >=>         >=>              >===>  >=> >=>     >=> >=>  >===>>=>>==>  >===>>=>>==>    >==>    >> >==> 
         >=>  >=>>=> >=>         >=>             >=>     >>   >=>  >=>   >=>   >=>  >>  >=>  >=>  >>  >=> >>   >=>   >=>    
         >=>   > >=> >=>   >===> >=>               >==>  >>   >=> >=>    >=>   >=>  >>  >=>  >=>  >>  >=> >>===>>=>  >=>    
         >=>    >>=>  >=>    >>  >=>                 >=> >=> >=>   >=>   >=>   >=>  >>  >=>  >=>  >>  >=> >>         >=>    
         >=>     >=>   >====>    >=======>       >=> >=> >=>        >==>>>==> >==>  >>  >=> >==>  >>  >=>  >====>   >==>    
                                                         >=>                                                                      """)
print("WARNING: I am not responsible if you use this tool for any purposes that may be considered illegal.")

help = (''' 
99: Quit
01: Set target
02: send 1 message
03: Auto send messages
    ''')
print(help)
time.sleep(0.5)

while True:
    cmd = input("> ")
    if cmd == "01":
        new_target = input("Target's username on NGL (no @): ").strip()
        if new_target:
            current_target = new_target
            print(f"Target is set to {current_target} ")
        else:
            print("Invalid Target")    
    elif cmd == "99":
        print("Goodbye...")
        time.sleep(2)
        break
    elif cmd == "02":
        send_ngl(current_target)
    elif cmd == "03":
        print(f"Auto sending messages to {current_target} every 2s. CTRL + C to stop this madness.")
        try:
            while True:
                send_ngl(current_target)
                time.sleep(2)
        except KeyboardInterrupt:
            print("\n Auto Send has stopped.")
    else:
        print("Sorry! That command does not run around here.")
        time.sleep(0.3)
        print(help)
