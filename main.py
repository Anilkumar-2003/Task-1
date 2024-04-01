import tkinter as tk
from tkinter import messagebox
import re
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def submit_data():
    # Get data from entry fields
    name = name_entry.get().strip()
    aicte_id = aicte_id_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    college_name = college_entry.get().strip()
    
    # Perform data validation
    if not name:
        messagebox.showerror("Error", "Please enter a name.")
        return
    if not aicte_id:
        messagebox.showerror("Error", "Please enter an AICTE ID.")
        return
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email) or not email.endswith("@gmail.com"):
        messagebox.showerror("Error", "Please enter a valid Gmail email address.")
        return
    if not phone.isdigit() or len(phone) != 10:
        messagebox.showerror("Error", "Please enter a valid 10-digit phone number.")
        return
    if not college_name:
        messagebox.showerror("Error", "Please enter a college name.")
        return
    
    # Data is valid, generate PDF
    generate_pdf(name, aicte_id, email, phone, college_name)
    messagebox.showinfo("Success", "Successfully Registered\nPDF Generated")

def generate_pdf(name, aicte_id, email, phone, college_name):
    # Create PDF document
    pdf_filename = "user_data.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    
    # Write data to PDF
    c.drawString(100, 680, "STUDENT DETAILS:")
    c.drawString(100, 650, f"Name: {name}")
    c.drawString(100, 630, f"AICTE ID: {aicte_id}")
    c.drawString(100, 610, f"Email: {email}")
    c.drawString(100, 590, f"Phone: {phone}")
    c.drawString(100, 570, f"College Name: {college_name}")
    
    # Save PDF
    c.save()

# Create main application window
root = tk.Tk()
root.title("Systecks Solutions")
root.geometry("4600x5000")
root.resizable(False, False)

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set geometry dimensions
window_width = 400
window_height = 300
x_coordinate = (screen_width - window_width) / 2
y_coordinate = (screen_height - window_height) / 2
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# Create and place widgets
main_heading = tk.Label(root, text="Student Registration Form", font=("Arial", 20, "bold"), fg="red")
main_heading.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Name:" ) .grid(row=1, column=0, padx=10, pady=5, sticky="e" )
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=5 )

tk.Label(root, text="AICTE ID:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
aicte_id_entry = tk.Entry(root)
aicte_id_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Email (Gmail):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(root)
email_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
phone_entry = tk.Entry(root)
phone_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="College Name:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
college_entry = tk.Entry(root)
college_entry.grid(row=5, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=6, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()