import customtkinter as ctk

ctk.set_appearance_mode("default")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("To-Do List")
app.geometry("400x600")


def add_task():
    pass


frame = ctk.CTkFrame(master=app, border_width=20)
frame.pack(expand=True, fill="both")

entry = ctk.CTkEntry(
    frame, placeholder_text="Add new task", font=("Helvetica", 25), width=170
)
entry.grid(pady=40, padx=20)

bt1 = ctk.CTkButton(frame, text="✔", command=add_task, font=("Helvetica", 40))
bt1.grid(pady=40)

app.mainloop()
