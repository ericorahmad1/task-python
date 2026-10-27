import tkinter as tk
from tkinter import messagebox

def calculate_discount():
    try:
        # Mengambil nilai dari input
        original_price = float(entry_price.get())
        discount_percent = float(entry_discount.get())
        
        # Menghitung jumlah diskon dan harga akhir
        discount_amount = original_price * (discount_percent / 100)
        final_price = original_price - discount_amount
        
        # Memperbarui label dengan hasil kalkulasi
        label_result.config(text=f"Final Price: Rp. {final_price:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan angka yang valid.")

# Membuat window utama
root = tk.Tk()
root.title("Discount Calculator")
root.geometry("300x250")

# Membuat elemen-elemen UI
label_price = tk.Label(root, text="Original Price:")
label_price.pack(pady=(20, 5))

entry_price = tk.Entry(root, justify="center")
entry_price.pack(pady=5)

label_discount = tk.Label(root, text="Discount (%):")
label_discount.pack(pady=(10, 5))

entry_discount = tk.Entry(root, justify="center")
entry_discount.pack(pady=5)

btn_calculate = tk.Button(root, text="Calculate", command=calculate_discount)
btn_calculate.pack(pady=15)

label_result = tk.Label(root, text="Final Price: Rp. 0.00")
label_result.pack()

# Menjalankan loop aplikasi
if __name__ == "__main__":
    root.mainloop()
