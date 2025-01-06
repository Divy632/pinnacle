import tkinter as tk
import sqlite3
import calendar
from tkinter import messagebox
from datetime import datetime
from plyer import notification

# CREATING DATABASE
def createdatabase():
    conn = sqlite3.connect('reminder.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reminder
                 (date TEXT, reminder_text TEXT)''')
    conn.commit()
    conn.close()

def add_reminder(date, reminder_text):
    conn = sqlite3.connect('reminder.db')
    c = conn.cursor()
    c.execute('INSERT INTO reminder (date, reminder_text) VALUES(?, ?)', (date, reminder_text))
    conn.commit()
    conn.close()

def show_notification(reminder_text):
    notification.notify(
        title="Reminder!",
        message=reminder_text,
        timeout=10  # Show for 10 seconds
    )

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CALENDAR AND REMINDER APP")
        self.selected_date = None
        self.create_calendar()
        self.reminder_section()
    
    def create_calendar(self):
        self.cal_frame = tk.Frame(self.root)
        self.cal_frame.pack()
        self.display_month()
    
    def display_month(self):
        year = datetime.now().year
        month = datetime.now().month
        month_days = calendar.monthcalendar(year, month)
        
        # Clear existing widgets
        for widgets in self.cal_frame.winfo_children():
            widgets.destroy()
        
        mon_label = tk.Label(self.cal_frame, text=f"{calendar.month_name[month]} {year}", font=("Times New Roman", 18), fg="blue")
        mon_label.grid(row=0, column=1, columnspan=5, pady=10)

        weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat","Sun"]
        for col, day in enumerate(weekdays):
            tk.Label(self.cal_frame, text=day, font=('Helvetica', 12),fg="Red").grid(row=1, column=col)
        
        for row, week in enumerate(month_days):
            for col, day in enumerate(week):
                if day != 0:
                    day_button = tk.Button(self.cal_frame, text=str(day), width=5, command=lambda d=day: self.select_date(d))
                    day_button.grid(row=row + 2, column=col, padx=10, pady=5)
    
    def select_date(self, day):
        self.selected_date = day
        messagebox.showinfo("Selected Date", f"Selected date is: {self.selected_date}")
    
    def reminder_section(self):
        self.reminder_frame = tk.Frame(self.root)
        self.reminder_frame.pack(pady=20)
        
        tk.Label(self.reminder_frame, text="Set a Reminder", font=('Helvetica', 14)).pack()
        
        self.reminder_entry = tk.Entry(self.reminder_frame, width=50)
        self.reminder_entry.pack(pady=10)
        
        self.set_reminder_button = tk.Button(self.reminder_frame, text="Set Reminder", command=self.set_reminder)
        self.set_reminder_button.pack()
    
    def set_reminder(self):
        if not self.selected_date:
            messagebox.showerror("Error", "Please select a date first")
            return
        
        reminder_text = self.reminder_entry.get()
        if reminder_text == "":
            messagebox.showerror("Error", "Please enter a reminder text")
            return
        
        date = f"{datetime.now().year}-{datetime.now().month:02d}-{self.selected_date:02d}"
        add_reminder(date, reminder_text)
        
        messagebox.showinfo("Reminder Set", f"Reminder for {date}: {reminder_text}")
       
        show_notification(f"Reminder for {date}: {reminder_text}")

    def check_for_reminders(self):
        # Check for reminders for the current date
        date = datetime.now().strftime("%Y-%m-%d")
        conn = sqlite3.connect('reminder.db')
        c = conn.cursor()
        c.execute("SELECT reminder_text FROM reminder WHERE date = ?", (date,))
        reminders = c.fetchall()
        conn.close()

        if reminders:
            for reminder in reminders:
                show_notification(reminder[0])

def run_app():
    createdatabase()  # Initialize the database
    root = tk.Tk()
    app = CalendarApp(root)

    # Check for reminders periodically (e.g., every minute)
    def periodic_check():
        app.check_for_reminders()
        root.after(60000, periodic_check)  # 60,000 ms = 1 minute

    periodic_check()  # Start checking for reminders

    root.mainloop()

run_app()
