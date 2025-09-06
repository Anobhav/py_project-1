import customtkinter as ctk
import login
import signup
import json
from Operations import Operations
from tkinter import messagebox, simpledialog
import builtins

# ---------- App setup ----------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Banking Management System")
app.geometry("500x450")

# ---------- Frames ----------
login_frame = ctk.CTkFrame(app)
signup_frame = ctk.CTkFrame(app)
dashboard_frame = ctk.CTkFrame(app)

for frame in (login_frame, signup_frame, dashboard_frame):
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

# ---------- Helper functions ----------
def ask_input(prompt):
    return simpledialog.askstring("Input Required", prompt, parent=app)

def run_with_input(func, *args):
    """
    Temporarily override input() and print() to work with popups.
    """
    old_input = builtins.input
    old_print = builtins.print

    def popup_print(*args, **kwargs):
        message = " ".join(str(a) for a in args)
        messagebox.showinfo("Info", message)

    builtins.input = ask_input
    builtins.print = popup_print

    try:
        func(*args)
    finally:
        builtins.input = old_input
        builtins.print = old_print

# ---------- Frame Switching ----------
def show_login():
    signup_frame.pack_forget()
    dashboard_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

def show_signup():
    login_frame.pack_forget()
    signup_frame.pack(fill="both", expand=True)

def show_dashboard(username):
    login_frame.pack_forget()
    signup_frame.pack_forget()
    dashboard_frame.pack(fill="both", expand=True)

    for widget in dashboard_frame.winfo_children():
        widget.destroy()

    # Create a single Operations instance per session
    ops = Operations(username)

    container = ctk.CTkFrame(dashboard_frame, corner_radius=10)
    container.grid(row=0, column=0, pady=20)

    ctk.CTkLabel(container, text=f"Welcome {username} 👋", font=("Arial", 20, "bold")).pack(pady=15)

    ctk.CTkButton(container, text="💰 Deposit Money", width=250,
                  command=lambda: run_with_input(ops.deposit)).pack(pady=10)

    ctk.CTkButton(container, text="💸 Withdraw Money", width=250,
                  command=lambda: run_with_input(ops.withdraw)).pack(pady=10)

    ctk.CTkButton(container, text="📊 Check Balance", width=250,
                  command=lambda: run_with_input(ops.check_balance)).pack(pady=10)

    ctk.CTkButton(container, text="⚙️ Change Account Details", width=250,
                  command=lambda: run_with_input(ops.change_details)).pack(pady=10)

    ctk.CTkButton(container, text="🚪 Logout", width=250,
                  command=show_login).pack(pady=20)

# ---------- Login ----------
login_container = ctk.CTkFrame(login_frame, corner_radius=10)
login_container.grid(row=0, column=0)

ctk.CTkLabel(login_container, text="Banking System", font=("Arial", 22, "bold")).pack(pady=15)

entry_user = ctk.CTkEntry(login_container, placeholder_text="Username", width=250)
entry_user.pack(pady=5)

entry_pass = ctk.CTkEntry(login_container, placeholder_text="Password", show="*", width=250)
entry_pass.pack(pady=5)

def handle_login():
    username = entry_user.get().strip()
    password = entry_pass.get().strip()
    if login.lg(username, password):
        show_dashboard(username)
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

ctk.CTkButton(login_container, text="Login", width=200, command=handle_login).pack(pady=15)
ctk.CTkButton(login_container, text="Sign Up", width=200, fg_color="gray30",
              command=show_signup).pack(pady=5)

# ---------- Signup ----------
signup_container = ctk.CTkFrame(signup_frame, corner_radius=10)
signup_container.grid(row=0, column=0)

ctk.CTkLabel(signup_container, text="Create Account", font=("Arial", 22, "bold")).pack(pady=15)

entry_signup_user = ctk.CTkEntry(signup_container, placeholder_text="New Username", width=250)
entry_signup_user.pack(pady=5)

entry_signup_pass = ctk.CTkEntry(signup_container, placeholder_text="New Password", show="*", width=250)
entry_signup_pass.pack(pady=5)

def handle_signup():
    username = entry_signup_user.get().strip()
    password = entry_signup_pass.get().strip()

    with open("Bank_Data.json", "r") as f:
        data = json.load(f)

    if username in data["users"]:
        messagebox.showerror("Error", "Username already exists")
        return

    try:
        signup.add_user(username, password)
        messagebox.showinfo("Success", "Account created! Please login.")
        show_login()
    except ValueError as e:
        messagebox.showerror("Error", str(e))

ctk.CTkButton(signup_container, text="Register", width=200, command=handle_signup).pack(pady=15)
ctk.CTkButton(signup_container, text="Back to Login", width=200, fg_color="gray30",
              command=show_login).pack(pady=5)

# ---------- Start App ----------
show_login()
app.mainloop()
