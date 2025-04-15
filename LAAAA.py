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
            label_result.config(text="⚠️ Coin not found", foreground="#cc0000")
        else:
            label_result.config(text=f"💰 ₹{price:.2f}", foreground="#007f00")
    except Exception as e:
        label_result.config(text="⚠️ Unable to fetch data", foreground="#cc0000")

root = tk.Tk()
root.title("💹 Taraksh Coin Price Tracker")
root.geometry("420x450")
root.configure(bg="#ffffff")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")
style.configure("TEntry", padding=5, font=("Segoe UI", 12))
style.configure("TButton", padding=6, font=("Segoe UI", 12, "bold"), foreground="#ffffff", background="#0052cc")
style.map("TButton", background=[("active", "#003d99")])

try:
    image_path = r"C:\Users\Taraksh\Downloads\nanana.jpg"
    img = Image.open(image_path)
    img = img.resize((120, 120), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    label_image = tk.Label(root, image=img, bg="#ffffff")
    label_image.image = img
    label_image.pack(pady=(20, 10))
except Exception as e:
    print(f"Error loading image: {e}")

label_title = tk.Label(root, text="Live Coin Price in INR", font=("Segoe UI", 18, "bold"), bg="#ffffff", fg="#333333")
label_title.pack(pady=(5, 20))

label_instructions = tk.Label(root, text="Enter Coin ID (e.g., bitcoin, solana):", font=("Segoe UI", 13), bg="#ffffff", fg="#555555")
label_instructions.pack()

entry_coin = ttk.Entry(root, width=24)
entry_coin.pack(pady=(8, 15))

button_track = ttk.Button(root, text="🔍 Track Price", command=track_price)
button_track.pack()

label_result = tk.Label(root, text="", font=("Segoe UI", 16, "bold"), bg="#ffffff", pady=10)
label_result.pack(pady=20)

footer = tk.Label(root, text="Powered by CoinGecko API", font=("Segoe UI", 9), bg="#ffffff", fg="#888888")
footer.pack(side="bottom", pady=10)

root.mainloop()