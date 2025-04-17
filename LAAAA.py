import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def get_price(coin_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=inr"
    response = requests.get(url)
    data = response.json()
    return data.get(coin_id, {}).get("inr", "N/A")

def track_price():
    coin_id = entry_coin.get().lower().strip()
    try:
        price = get_price(coin_id)
        if price == "N/A":
            label_result.config(text="⚠️ Coin not found", foreground="#ff4d4d")
        else:
            label_result.config(text=f"💰 ₹{price:.2f}", foreground="#00e676")
    except Exception as e:
        label_result.config(text="⚠️ Unable to fetch data", foreground="#ff4d4d")

root = tk.Tk()
root.title("💹 Taraksh Coin Price Tracker")
root.geometry("900x600")
root.configure(bg="#000000")
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

try:
    image_path = r"C:\Users\Taraksh\Downloads\nanana.jpg"
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"Error loading background image: {e}")
frame = tk.Frame(root, bg='#000000', bd=0)
frame.place(relx=0.5, rely=0.5, anchor="center")

label_title = tk.Label(frame, text="💹 Live Coin Price in INR", font=("Segoe UI", 22, "bold"),
                       bg="#000000", fg="white")
label_title.pack(pady=(0, 20))

label_instructions = tk.Label(frame, text="Enter Coin ID (e.g., bitcoin, solana):",
                              font=("Segoe UI", 14), bg="#000000", fg="#dddddd")
label_instructions.pack(pady=(0, 10))

entry_coin = ttk.Entry(frame, width=25, font=("Segoe UI", 12))
entry_coin.pack(pady=(0, 15))

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 12, "bold"), foreground="white", background="#0078D7")
style.map("TButton", background=[("active", "#005A9E")])

button_track = ttk.Button(frame, text="🔍 Track Price", command=track_price)
button_track.pack(pady=(0, 20))

label_result = tk.Label(frame, text="", font=("Segoe UI", 16, "bold"), bg="#000000", fg="white")
label_result.pack()

footer = tk.Label(root, text="Powered by Taraksh", font=("Segoe UI", 10),
                  bg="#000000", fg="#aaaaaa")
footer.pack(side="bottom", pady=15)

root.mainloop()
