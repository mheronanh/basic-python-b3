import smtplib, ssl, email
import tkinter as tk

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from tkinter import filedialog
from tkinter import messagebox

window = tk.Tk()
window.title("Email Sender")

def upload_receiver():
    # Prosedur ini berguna untuk membuka dialog box untuk memasukkan file receiver list
    global filename
    filename = filedialog.askopenfilename(title="Choose receiver_list.txt file")

def attach_file():
    # Prosedur ini digunakan untuk menambahkan attachments
    global attach_files
    attach_files = filedialog.askopenfilenames(title="Choose file(s)")
    global frame4
    frame4 = tk.Frame(master=window, border=5)
    lbl_attachment = tk.Label(master=frame4, text=f"{len(attach_files)} file(s) attached")
    lbl_attachment.pack()
    frame4.pack()


def kirim_email():
    # Keseluruhan prosedur ini untuk mengirim email
    # Opening receiver list 
    with open(filename, "r") as receiver_file:
        receiver_list = (receiver_file.read()).split("\n")
        receiver_file.close()

    # Preparation for sending the email
    port = 587
    smtp_server = "smtp.gmail.com" #Spesifikasi pada program ini hanya mneggunakan Gmail 
    sender_email = entry_sender.get()
    recipients = receiver_list
    password = entry_password.get()

    # Create a multipart message and set headers
    global message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ", ".join(receiver_list)
    message['Subject'] = entry_subject.get()

    # Membuat body email
    body = txt_body.get("1.0", tk.END)
    message.attach(MIMEText(body, "plain"))

    # Menambahkan attachment
    global attach_files
    for file in attach_files:
        with open(file, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename = {file}"
        )
        message.attach(part)
    
    # Sending email dengan menggunakan protokol keamanan TLS
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipients, message.as_string())

    messagebox.showinfo("Information", "Email has been sent.")
    #reset gui after send an email
    attach_files = tuple()
    frame4.destroy()

# GUI
# Pembuatan frame1
frame1 = tk.Frame(master=window, border=5)
# Part pengirim
lbl_sender = tk.Label(master=frame1, text="Sender:")
entry_sender = tk.Entry(master=frame1)
lbl_password = tk.Label(master=frame1, text="Password:")
entry_password = tk.Entry(master=frame1, show="*")
# Part receiver
lbl_receiverlist = tk.Label(master=frame1, text="Receiver List")
btn_add_receiver = tk.Button(master=frame1, text="Open", command=upload_receiver)
# Component dari frame1
lbl_sender.pack(fill=tk.X, side=tk.LEFT, expand=True)
entry_sender.pack(fill=tk.X, side=tk.LEFT, expand=True, padx=5, pady=5)
lbl_password.pack(fill=tk.X, side=tk.LEFT, expand=True)
entry_password.pack(fill=tk.X, side=tk.LEFT, expand=True, padx=5, pady=5)
lbl_receiverlist.pack(fill=tk.X, side=tk.LEFT, expand=True)
btn_add_receiver.pack(fill=tk.X, side=tk.LEFT, expand=False, padx=5, pady=5)
# Packing frame1
frame1.pack(fill=tk.BOTH, expand=True)

# Pembuatan frame2
frame2 = tk.Frame(master=window)
frame2.rowconfigure(1, minsize=100)
frame2.columnconfigure(1, minsize=50)
# Pembuatan subject
lbl_subject = tk.Label(master=frame2, text="Subject:", width=10)
entry_subject = tk.Entry(master=frame2, width=100)
# Component dari subject
lbl_subject.grid(row=0, column=0, sticky="w")
entry_subject.grid(row=0, column=1, padx=5, pady=5, sticky="w")
# Pembuatan body email
lbl_body = tk.Label(master=frame2, text="Body:", width=10)
txt_body = tk.Text(master=frame2, width=75)
# Component dari frame3
lbl_body.grid(row=1, column=0, sticky="nw")
txt_body.grid(row=1, column=1, padx=5, pady=5, sticky="W")
# Packing frame2
frame2.pack(fill=tk.BOTH, expand=True)

# Pembuatan frame3
frame3 = tk.Frame(master=window)
btn_attachment = tk.Button(master=frame3, text="Add Attachment(s)", command=attach_file)
btn_send = tk.Button(master=frame3, text="Send", command=kirim_email)
btn_attachment.pack(padx=5, pady=5)
btn_send.pack(padx=5, pady=5)
frame3.pack(fill=tk.BOTH, expand=True)

window.mainloop()