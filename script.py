import openai
import tkinter as tk
from tkinter import filedialog
import time
import socket

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

# Initialize the API key for OpenAI
openai.api_key = "INSERT-CHATGPT-API-KEY-HERE"

# Define a function to ask a question about a document
def ask_question(prompt, document):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        frequency_penalty=0,
        presence_penalty=0,
    )

    message = completions.choices[0].text
    return message

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

print("+" + "-"*50 + "+")
print("|" + " "*50 + "|")
print("|  Upload a document or ask a question to DocGPT  |")
print("|" + " "*50 + "|")
print("+" + "-"*50 + "+")

# Choose between uploading a document or asking a question
choice = input("Enter '1' to upload a document or '2' to ask a question: ")

# Upload the document or ask the question
if choice == "1":
    file_path = open_file_dialog()
    with open(file_path, encoding='utf8') as file:
        document = file.read()
else:
    document = ""

results = []
while True:
    prompt = input("Enter your question: ")
    answer = ask_question(prompt, document)
    results.append((time.time(), get_ip(), prompt, answer))

    continue_asking = input("Do you want to ask another question (yes/no)? ")
    if continue_asking.lower() != "yes":
        break

print("\n+" + "-"*50 + "+")
print("|" + " "*50 + "|")
print("|  Displaying all the results  |")
print("|" + " "*50 + "|")
print("+" + "-"*50 + "+")

for result in results:
    print("Time:", time.ctime(result[0]))
    print("IP:", result[1])
    print("Question:", result[2])
    print("Answer:", result[3], "\n")

print("\n+" + "-"*50 + "+")
print("|" + " "*50 + "|")
print("| Saving the results to a file |")
print("|" + " "*50 + "|")
print("+" + "-"*50 + "+")

filename = input("Enter a filename to save the results: ")
with open(filename, "w") as file:
    for result in results:
        file.write("Time: " + time.ctime(result[0]) + "\n")
        file.write("IP: " + result[1] + "\n")
        file.write("Question: " + result[2] + "\n")
        file.write("Answer: " + result[3] + "\n\n")

print("Results saved successfully!")
