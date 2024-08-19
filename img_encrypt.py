from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.geometry("300x200")
root.config(padx=20, pady=20)
root.title('Image Encryptor')

def get_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('Image file', '*.jpg')])
    if file is not None:
        file_name = file.name
        encrypt_file(file_name)

def encrypt_file(file_name):
    passw = file_text.get()
    
    # Input validation
    try:
        passw = int(passw)
        if not (0 <= passw <= 255):
            raise ValueError("Password must be between 0 and 255")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
        return

    try:
        with open(file_name, 'rb') as fi:
            image = bytearray(fi.read())
        
        for index, value in enumerate(image):
            image[index] = value ^ passw

        with open(file_name, 'wb') as fi1:
            fi1.write(image)

        encrypt_button.config(text='Saved!!')
        file_text.delete(0, END)
        your_password.config(text=f'Your Password:\n{passw}')
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

encrypt_button = Button(root, text='Encrypt/Decrypt', command=get_file, bg='green', fg='white')
encrypt_button.grid(row=0, column=1, padx=10)

password = Label(text='Enter Password (0-255):', fg='Red')
password.grid(row=1, column=0, columnspan=2, pady=10)

file_text = Entry(root)
file_text.grid(row=2, column=0, columnspan=2)

your_password = Label(text='', fg='Green')
your_password.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
