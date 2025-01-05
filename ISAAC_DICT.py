import tkinter as tk
from tkinter import messagebox
Igbo = {"lion":"agu",
 "war":"agha",
 "name":"aha",
 "bag":"akpa",
 "night":"abali",
 "fish":"azu",
 "dog":"nkita",
 "child":"nwa",
 "father":"nna",
 "spoon":"ngazi",
 "town":"obodo",
 "bedroom":"obu",
 "black":"oji",
 "boss":"onye isi",
 "rice":"osikapa",
 "tree":"osisi",
 "cold":"oyi",
 "hawk":"egbe",
 "cow":"ehi",
 "goat":"ewu",
 }
def search_translation():
    word = entry.get().lower().strip()  # Get the word from the search bar
    if word in Igbo:
        result_var.set(f"Translation: {Igbo[word]}")
    else:
       messagebox.showerror("Error",  "Word not found in dictionary")
root = tk.Tk()
root.title("English to Igbo dictinary")
root.geometry("600x250")
label = tk.Label(root, text="Enter an English word:")
label.pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)
search_button =tk.Button(root, text="Search", command=search_translation)
search_button.pack(pady=10)
result_var = tk.StringVar()
result_label = tk.Label(root,     textvariable=result_var, font=("Arial", 14))
result_label.pack(pady=10)
root.mainloop()

