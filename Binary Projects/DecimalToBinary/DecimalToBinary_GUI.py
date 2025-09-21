import customtkinter as ctk
from tkinter import messagebox

def decimal_to_binary(decimal_number: str) -> str:
    """
    Convert a decimal integer to its binary string equivalent.
    """
    decimal_number = decimal_number.strip()
    if not decimal_number:
        raise ValueError("Empty string was passed to the function")
    
    if not (decimal_number.lstrip("-").isdigit()):
        raise ValueError("Non-decimal value was passed to the function")
    
    num = int(decimal_number)
    if num == 0:
        return "0"
    
    is_negative = num < 0
    num = abs(num)

    binary_string = ""
    while num > 0:
        binary_string = str(num % 2) + binary_string
        num //= 2
    
    return "-" + binary_string if is_negative else binary_string

def convert():
    decimal_value = entry.get()
    try:
        result = decimal_to_binary(decimal_value)
        result_label.configure(text=f"Binary Value: {result}", text_color="#000000")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
        result_label.configure(text="")

ctk.set_appearance_mode("light")  
ctk.set_default_color_theme("dark-blue") 

root = ctk.CTk()
root.title("Decimal To Binary Converter")
root.geometry("500x450")
root.configure(fg_color="white") 

title_label = ctk.CTkLabel(root,
                           text="Decimal  →  Binary Converter",
                           font=("Poppins", 32, "bold"),
                           text_color="black") 
title_label.pack(pady=15)

subtitle_label = ctk.CTkLabel(root,
                           text="Only input Decimal Numbers\n( 0-9 )",
                           font=("Segoe UI", 20),
                           text_color="#555555")  
subtitle_label.pack(pady=20)

entry = ctk.CTkEntry(root,
                     placeholder_text="Enter Decimal Number",
                     font=("Consolas", 30, "bold"),
                     width=380,
                     height=70,
                     justify="center",
                     fg_color="white",
                     border_color="black",
                     border_width=2,
                     text_color="black")
entry.pack(pady=10)

convert_btn = ctk.CTkButton(root,
                            text="Convert",
                            command=convert,
                            font=("Montserrat", 20, "bold"),
                            width=140,
                            height=55,
                            corner_radius=20,
                            fg_color="black",
                            hover_color="#333333", 
                            text_color="white")
convert_btn.pack(pady=25)

result_label = ctk.CTkLabel(root,
                            text="...",
                            font=("Century Gothic", 23, "bold"),
                            text_color="black")
result_label.pack(pady=25)

root.mainloop()
