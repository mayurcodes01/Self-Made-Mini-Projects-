import customtkinter as ctk
import requests
import random
from style_utils import funny_style, motivational_style, poetic_style

def fetch_quote() -> str:
    """Fetch a random quote from API (ignores SSL verification for testing)."""
    url = "https://zenquotes.io/api/random" 
    try:
        response = requests.get(url, verify=False, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f"{data[0]['q']} — {data[0]['a']}"
    except Exception as e:
        return f"⚠️ Could not fetch quote (Error: {e})"
    
    return "Life is like code: messy but beautiful."

def personalize_quote(quote: str) -> str:
    """Randomly choose a style and return personalized quote."""
    styles = [funny_style, motivational_style, poetic_style]
    style_func = random.choice(styles)
    return style_func(quote)

def generate_quote():
    original = fetch_quote()
    personalized = personalize_quote(original)
    original_textbox.configure(state="normal")
    personalized_textbox.configure(state="normal")

    original_textbox.delete("1.0", "end")
    personalized_textbox.delete("1.0", "end")

    original_textbox.insert("1.0", original)
    personalized_textbox.insert("1.0", personalized)

    original_textbox.configure(state="disabled")
    personalized_textbox.configure(state="disabled")

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Personalized Quote Generator")
app.geometry("700x500")

title_label = ctk.CTkLabel(app, text="✨ Personalized Quote Generator", font=("Arial", 22, "bold"))
title_label.pack(pady=20)

btn = ctk.CTkButton(app, text="🔄 Generate Quote", font=("Arial", 16, "bold"), command=generate_quote)
btn.pack(pady=15)

frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(padx=20, pady=20, fill="both", expand=True)

original_label = ctk.CTkLabel(frame, text="- Original Quote:", font=("Arial", 16, "bold"))
original_label.pack(anchor="w", padx=10, pady=5)

original_textbox = ctk.CTkTextbox(frame, height=100, font=("Arial", 14), wrap="word")
original_textbox.pack(padx=10, pady=5, fill="x")
original_textbox.configure(state="disabled")

personalized_label = ctk.CTkLabel(frame, text="- Personalized Quote:", font=("Arial", 16, "bold"))
personalized_label.pack(anchor="w", padx=10, pady=5)

personalized_textbox = ctk.CTkTextbox(frame, height=120, font=("Arial", 14), wrap="word")
personalized_textbox.pack(padx=10, pady=5, fill="x")
personalized_textbox.configure(state="disabled")

app.mainloop()
