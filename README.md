# DocGPT
A script that empowers a user to upload a document and ask questions of ChatGPT for document analysis. Download the script and add your own api key.

## Step-by-Step Instructions for Creating and Adding a Your Own API Key

1. Go to OpenAI's website (https://beta.openai.com/docs/guides/how-to-use-openai) and sign up for an account.

2. After you have signed up, go to the API Key section and generate an API Key.

3. Copy the API Key to your clipboard.

4. Open the Python script in your preferred code editor.

5. In the script, find line 14:
```
openai.api_key = "INSERT-CHATGPT-API-KEY-HERE"
```

6. Replace "INSERT-CHATGPT-API-KEY-HERE" with the API Key you copied in step 3, between the quotation marks.

## Step-by-Step Instructions for Running the Script

1. Pre-requisites:
 - Install Python 3 on your computer.
 - Install the required libraries (openai, time, socket, os, and tkinter).
 - Ensure that the document you want to upload (if you choose to upload a document) is in the same directory as the script.

2. Run the script by executing the following command in your terminal or command prompt:
```
python3 script.py
```

3. You will be prompted with a dialog asking whether you want to upload a document or ask a question directly. Choose your option by typing 1 or 2 and pressing Enter.
```
+---------------------------------------------------+
|                                                   |
|  Choose an option:                                |
|  1. Upload a document                             |
|  2. Ask a question directly                       |
|                                                   |
+---------------------------------------------------+
```

4. If you choose option 1, a file dialog will appear, allowing you to select the document you want to ask questions about.

5. If you choose option 2, you will be prompted to enter your question directly.
```
+---------------------------------------------------+
|                                                   |
|  Enter your question:                             |
|                                                   |
+---------------------------------------------------+
```

6. After entering your question, the answer will be displayed on the screen.
```
+---------------------------------------------------+
|                                                   |
|  Answer:                                          |
|  [Your answer will be displayed here]             |
|                                                   |
+---------------------------------------------------+
```

7. You will be prompted to ask another question or display all the results before saving to a file. Choose your option by typing 1 or 2 and pressing Enter.
```
+---------------------------------------------------+
|                                                   |
|  What would you like to do next?                  |
|  1. Ask another question                          |
|  2. Display all results and save to a file        |
|                                                   |
+---------------------------------------------------+
```

8. If you choose option 1, you will be taken back to step 5.

9. If you choose option 2, the results will be displayed on the screen, including the timestamp and the IP address of the source of the request. Then, you will be prompted to enter a filename to save the results.
```
+---------------------------------------------------+
|                                                   |
|  Saving the results to a file                     |
|                                                   |
+---------------------------------------------------+
```

10. Enter a filename and press Enter to save the results to a file. The file will be saved in the same directory as the script.

11. The script will display a message confirming that the results have been saved successfully.
```
Results saved successfully!
```
