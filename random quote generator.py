import tkinter as tk
import requests
from threading import Thread

#API 
api = "https://zenquotes.io/api/random"
quotes = []
quote_number = 0

#main window
window = tk.Tk()
window.geometry("900x350")
window.title("Quote Generator")
window.grid_columnconfigure(0, weight=1)
window.resizable(True, True)
window.configure(bg="light yellow")

def preload_quote():
    """Fetch and store 10 random quotes from API."""
    global quotes
    print("****Loading Quotes...****")
    for _ in range(10):
        try:
            response = requests.get(api, timeout=5)
            random_quote = response.json()  
            
            content = random_quote[0]["q"]
            author = random_quote[0]["a"]
            
            quote = f"{content}\n\nBy {author}"
            quotes.append(quote)
        except requests.exceptions.RequestException as e:
            print(f"Error: Unable to fetch quote. {e}")
            break  
    print("Finished Loading!")

Thread(target=preload_quote, daemon=True).start()

def get_random_quote():
    """Display a new quote from the list and fetch more if needed."""
    global quote_label, quotes, quote_number
    
    if quotes:
        quote_label.configure(text=quotes[quote_number])  
        quote_number += 1  

        if quote_number >= len(quotes) - 3:
            thread = Thread(target=preload_quote, daemon=True)
            thread.start()
    else:
        quote_label.configure(text="Loading quotes... Please wait.")

#UI 
quote_label = tk.Label(
    window, text="Click on the button to generate a random quote!",
    height=6, pady=10, wraplength=800,
    font=("Times New Roman", 24), bg="light yellow"
)
quote_label.grid(row=0, column=0, sticky="WE", padx=20, pady=10)

button = tk.Button(
    window, text="Generate", command=get_random_quote,
    bg="dark blue", fg="#ffffff", activebackground="light yellow",
    font=("Helvetica", 14)
)
button.grid(row=1, column=0, sticky="WE", padx=20, pady=10)

if __name__ == "__main__":
    window.mainloop()
