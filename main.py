from fastapi import FastAPI
import  os
import glob
import openai
import requests
app = FastAPI()

# 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
openai.api_key = ""
model_engine = "text-davinci-003"
def chatgpt(prompt):
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    return response

@app.get("/status")
def status():
    return "ACTIVE"

@app.get("/create")
def create(username = "", password = "", phone = ""):
    if os.path.exists(username + ".txt") == True:
        return "ERROR: 1 -- ACCOUNT ALREADY EXISTS"
    
    if os.path.exists(username + ".txt") == False:
        
        with open(username + ".txt", "w") as f:
            f.write(password)
        with open(username + ".phone", "w") as f:
            f.write(phone)
        with open(username + ".messages", "w") as f:
            f.write("")
        return "SUCCESS"
    
@app.get("/delete")
def delete(username = "", password = ""):
    if os.path.exists(username + ".txt") == True:
        if open(username + ".txt", "r").read() == password:
            os.remove(username + ".txt")
            os.remove(username + ".messages")
            os.remove(username + ".phone")
        return "SUCCESS"
    if os.path.exists(username + ".txt") == False:
        return "ERROR: 2 -- ACCOUNT DOES NOT EXIST"
    
@app.get("/view")
def view(username = "", password = ""):
    if os.path.exists(username + ".txt") == True:
        if open(username + ".txt", "r").read() == password:
            return open(username + ".messages", "r").read()
        if open(username + ".txt", "r").read() != password:
            return "ERROR: 2 -- ACCOUNT DOES NOT EXIST"
    if os.path.exists(username + ".txt") == False:
        return "ERROR: 2 -- ACCOUNT DOES NOT EXIST"

@app.get("/send")
def send(username = "", password = "", to = "", message = ""):
    if open(username + ".txt", "r").read() == password:
        if os.path.exists(to + ".messages") == True:
            with open(to + ".messages", "a") as f:
                f.write("|[NAME]|" + username + "|[NAME]|: " + message + "|[SPLIT]|")
            with open(username + ".messages", "a") as f:
                f.write("You: " + message  + "|[SPLIT]|")
                requests.get("https://voip.ms/api/v1/rest.php^api_username=nevtech@nevtech.ca&api_password=30212178Skyler&method=SendSMS&did=2894820253&dst=" + to + ".phone" + "&message=" + "You have a message from: " + username + ".  open on your computer to view it.")
                return "SUCCESS"
                
        if os.path.exists(to + ".messages") == False:
            return "ERROR: 3 -- PERSON DOES NOT EXIST"
    if open(username + ".txt", "r").read() != password:
        return "ERROR: 4 -- AUTHENTICATION FAILED"
    
@app.get("/clear")
def clear(username = "", password = ""):
    if open(username + ".txt", "r").read() == password:
        if os.path.exists(username + ".messages") == True:
            with open(username + ".messages", "w") as f:
                f.write("")
                return "SUCCESS"

@app.get("/admin")
def admin(username = "", password = ""):
    if os.path.exists(username + ".admin") == True:
        if open(username + ".admin", "r").read() == password:
            return "SUCCESS"
    if os.path.exists(username + ".admin") == False:
        return "INVALID CREDENTIALS"
    
@app.get("/admin-view")
def adminview(username = "", password = ""):
    if os.path.exists(username + ".admin") == True:
        if open(username + ".admin", "r").read() == password:
            return glob.glob("/var/www/html/api/*.txt")
        
@app.get("/admin-reset")
def adminreset(username = "", password = "", targetuser = "", newpassword = ""):
    if os.path.exists(username + ".admin") == True:
        if open(username + ".admin", "r").read() == password:
            if os.path.exists(targetuser + ".txt"):
                with open(targetuser + ".txt", "w") as f:
                    f.write(newpassword)
                    return "SUCCESS"

@app.get("/admin-delete")
def adminview(username = "", password = "", targetuser = ""):
    if os.path.exists(username + ".admin") == True:
        if open(username + ".admin", "r").read() == password:
            if os.path.exists(targetuser + ".txt"):
                os.remove(targetuser + ".txt")
                return "SUCCESS"
            
@app.get("/admin-messages")
def adminmessages(username = "", password = "", targetuser = ""):
    if os.path.exists(username + ".admin") == True:
        if open(username + ".admin", "r").read() == password:
            output = open(targetuser + ".messages", "r").read
            return output
        
@app.get("/admin-delete-messages")
def adminmessages(username = "", password = "", targetuser = ""):
    if os.path.exists(username + ".admin") == True:
        if open(username + ".admin", "r").read() == password:
            with open(targetuser + ".messages", "w") as f:
                f.write("")
            return "SUCCESS"

@app.get("/chatgpt")
def chatgptanswer(username = "", password = "", message = ""):
    if os.path.exists(username + ".txt") == True:
        if open(username + ".txt", "r").read() == password:
            return chatgpt(message)
        if open(username + ".txt", "r").read() != password:
            return "ERROR: 2 -- ACCOUNT DOES NOT EXIST"
    if os.path.exists(username + ".txt") == False:
        return "ERROR: 2 -- ACCOUNT DOES NOT EXIST"