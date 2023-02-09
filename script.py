import os
import json
import time
import socket
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Entry
import openai

# Defines the main menu
class MainMenu:
    def __init__(self, master):
        self.master = master
        master.title("DocGPT v1.0")

        self.api_key = self.get_api_key()
        if not self.api_key:
            self.enter_api_key()

        self.upload_button = tk.Button(
            master, text="Upload a document", command=self.upload_document)
        self.upload_button.pack()

        self.ask_question_button = tk.Button(
            master, text="Ask a question", command=self.ask_question)
        self.ask_question_button.pack()

        self.view_results_button = tk.Button(
            master, text="View results", command=self.view_results)
        self.view_results_button.pack()

        self.view_api_key_button = tk.Button(
            master, text="View API Key", command=self.view_api_key)
        self.view_api_key_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

    # Defines the api key
    def get_api_key(self):
        if os.path.exists("api_key.gpt"):
            with open("api_key.gpt", "r") as f:
                api_key = f.read()
                return api_key.strip()
        return None

    def enter_api_key(self):
        api_key = tk.simpledialog.askstring(
            "API Key", "Enter your OpenAI API Key:")
        with open("api_key.gpt", "w") as f:
            f.write(api_key)
        self.api_key = api_key

    # Defines the upload document function
    def upload_document(self):
        openai.api_key = self.api_key
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"),
                                                          ("Word files", "*.doc"),
                                                          ("Excel files", "*.xls")])
        if file_path:
            prompt = "What would you like to ask about the uploaded document?"
            question = tk.simpledialog.askstring("Question", prompt)
            if question:
                response = openai.Completion.create(
                    engine="text-davinci-002",
                    prompt=prompt,
                    max_tokens=1024,
                    n=1,
                    stop=None,
                    temperature=0.5,
                ).choices[0].text
                result = {"timestamp": time.time(), "ip": socket.gethostbyname(socket.gethostname()),
                          "document": file_path, "question": question, "answer": response}
                self.store_result(result)
                self.ask_another_question(result)

    # Defines the ask a question function
    def ask_question(self):
        openai.api_key = self.api_key
        question = tk.simpledialog.askstring(
            "Question", "What would you like to ask ChatGPT?")
        if question:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=question,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            ).choices[0].text
            result = {"timestamp": time.time(), "ip": socket.gethostbyname(socket.gethostname()),
                      "document": None, "question": question, "answer": response}
            self.store_result(result)
            self.ask_another_question(result)

    # Defines the view results function
    def view_results(self):
        if os.path.exists("results.json"):
            with open("results.json", "r") as f:
                results = json.load(f)
                message = "Results:\n"
                for result in results:
                    message += "Timestamp: {}\n".format(result["timestamp"])
                    message += "IP Address: {}\n".format(result["ip"])
                    message += "Document: {}\n".format(result["document"])
                    message += "Question: {}\n".format(result["question"])
                    message += "Answer: {}\n\n".format(result["answer"])
                messagebox.showinfo("Results", message)
        else:
            messagebox.showwarning("Warning", "No results found.")

    # Defines the view api key function
    def view_api_key(self):
        messagebox.showinfo("API Key", self.api_key)

    # Defines the ask another question function
    def ask_another_question(self, result):
        answer = messagebox.askyesno(
            "Another Question", "Would you like to ask another question about the same document?")
        if answer:
            self.ask_question()
        else:
            self.view_results()

    # Defines the results storage function
    def store_result(self, result):
        if os.path.exists("results.json"):
            with open("results.json", "r") as f:
                results = json.load(f)
            results.append(result)
        else:
            results = [result]
        with open("results.json", "w") as f:
            json.dump(results, f)


if __name__ == "__main__":
    root = tk.Tk()
    my_gui = MainMenu(root)
    root.mainloop()
