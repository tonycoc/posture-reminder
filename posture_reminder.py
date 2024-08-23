try:
    import tkinter as tk
    import requests
    from win10toast import ToastNotifier as tn
    import json
    import threading
    import time
except:
    exit()

do_loop = False

def quote() -> str:
    try:
        r = requests.get("https://favqs.com/api/qotd")
        if r.status_code == 200:
            quote_text = json.loads(r.text)["quote"]

            return f'{quote_text["body"]} - {quote_text["author"]}'
        else:
            return "correct your posture or you'll be called 'guy who looks like C' - myMom"
    except:
        return "correct your posture or you'll be called 'guy who looks like C' - myMom"
def notifi():
    global do_loop
    print(do_loop)
    while do_loop:
        toast = tn()
        text = quote()
        toast.show_toast(title="Correct you posture!!!",msg=text,duration=15)

        user_input = entry.get()
        time.sleep(int(user_input)*60)



#Ui

root = tk.Tk()
root.title("Posture Reminder")
root.geometry("350x200")
label = tk.Label(root, text="be reminded in every:")
label.pack(pady=20)
entry = tk.Entry(root, width=20)
entry.pack(pady=0)

def btn_call():
    global do_loop
    if btn.cget("text") == "start":
    
        do_loop = True
        btn.config(text="stop")
        
        t1 = threading.Thread(target=notifi)
        t1.start()
        
    elif btn.cget("text")  == "stop":
        do_loop = False
        btn.config(text="start")

btn = tk.Button(root,command=btn_call,text="start")
btn.pack(pady=10)
root.mainloop()
    