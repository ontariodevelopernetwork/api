from fastapi import FastAPI
import  os
app = FastAPI()

@app.get("/status")
def status():
    return "ACTIVE"

@app.get("/create")
def create(username = "", password = ""):
    if os.path.exists(username + ".txt") == True:
        return "ERROR: 1 -- ACCOUNT ALREADY EXISTS"
    
    if os.path.exists(username + ".txt") == False:
        
        with open(username + ".txt", "w") as f:
            f.write(password)
        with open(username + ".messages", "w") as f:
            f.write("")
        return "SUCCESS"
    
@app.get("/delete")
def delete(username = "", password = ""):
    if os.path.exists(username + ".txt") == True:
        if open(username + ".txt", "r").read() == password:
            os.remove(username + ".txt")
            os.remove(username + ".messages")
        return "SUCCESS"
    if os.path.exists(username + ".txt") == False:
        return "ERROR: 2 -- ACCOUNT DOES NOT EXIST"
    
@app.get("/view")
def view(username = "", password = ""):
    if os.path.exists(username + ".txt") == True:
        if open(username + ".txt", "r").read() == password:
            return open(username + ".messages", "r").read()
    if os.path.exists(username + ".txt") == False:
        return "ERROR: 2 -- ACCOUNT DOES NOT EXIST"

@app.get("/send")
def send(username = "", password = "", to = "", message = ""):
    if open(username + ".txt", "r").read() == password:
        if os.path.exists(to + ".messages") == True:
            with open(to + ".messages", "a") as f:
                f.write(username + ": " + message + "|[SPLIT]|")
            with open(username + ".messages", "a") as f:
                f.write("You: " + message  + "|[SPLIT]|")
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
