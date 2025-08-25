import customtkinter as ctk
from tkinter import messagebox


def bin_to_decimal(bin_string: str) -> int:
    """
    Convert a binary value to its decimal equivalent
    """
    bin_string = str(bin_string).strip()
    if not bin_string:
        raise ValueError("Empty string was passed to the function")
    is_negative = bin_string[0] == "-"
    if is_negative:
        bin_string = bin_string[1:]
    if not all(char in "01" for char in bin_string):
        raise ValueError("Non-binary value was passed to the function")
    decimal_number = 0
    for char in bin_string:
        decimal_number = 2 * decimal_number + int(char)
    return -decimal_number if is_negative else decimal_number

def convert():
    binary_value = entry.get()
    try:
        result = bin_to_decimal(binary_value)
        result_label.configure(text=f"Decimal Value: {result}", text_color="#000000")  # 
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
        result_label.configure(text="")

ctk.set_appearance_mode("light")  
ctk.set_default_color_theme("dark-blue") 

root = ctk.CTk()
root.title("Binary To Decimal Converter")
root.geometry("500x450")
root.configure(fg_color="white") 

# Title
title_label = ctk.CTkLabel(root,
                           text="Binary  →  Decimal Converter",
                           font=("Poppins", 32, "bold"),
                           text_color="black") 
title_label.pack(pady=15)

subtitle_label = ctk.CTkLabel(root,
                           text="Only input Binary Numbers\n( 0's & 1's )",
                           font=("Segoe UI", 20),
                           text_color="#555555")  
subtitle_label.pack(pady=20)

entry = ctk.CTkEntry(root,
                     placeholder_text="Enter Binary Number",
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
