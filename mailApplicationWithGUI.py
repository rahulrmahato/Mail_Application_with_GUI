import tkinter as tk
from tkinter import messagebox
import smtplib

def send_email():
    sender_email = sender_email_entry.get()
    sender_password = sender_password_entry.get()
    recipient_email = recipient_email_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", "end-1c")

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        email_text = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, recipient_email, email_text)

        server.quit()
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

app = tk.Tk()
app.title("Mail Application")

sender_email_label = tk.Label(app, text="Sender Email:")
sender_email_label.pack()
sender_email_entry = tk.Entry(app)
sender_email_entry.pack()

sender_password_label = tk.Label(app, text="Sender Password:")
sender_password_label.pack()
sender_password_entry = tk.Entry(app, show="*")
sender_password_entry.pack()

recipient_email_label = tk.Label(app, text="Recipient Email:")
recipient_email_label.pack()
recipient_email_entry = tk.Entry(app)
recipient_email_entry.pack()

subject_label = tk.Label(app, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(app)
subject_entry.pack()

message_label = tk.Label(app, text="Message:")
message_label.pack()
message_text = tk.Text(app, height=10, width=40)
message_text.pack()

send_button = tk.Button(app, text="Send Email", command=send_email)
send_button.pack()

app.mainloop()
