import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import simpledialog, messagebox
from attendance_taker import attendance_taker
from get_faces_from_camera_tkinter import registerStudent
from mailing_xls_attendance_file import send_email_with_attachment
from xls_attendance.xls_file_creator import xls_file_creator

# Load environment variables
load_dotenv()
PASSWORD = os.getenv("APP_PASSWORD")
SECRET_KEY = os.getenv("SECRET_KEY")

def start_attendance_system(root_login):
    root_login.destroy()
    root = tk.Tk()
    root.title("Attendance System")
    root.attributes("-fullscreen", True)
    root.configure(bg="#1e1e1e")

    registration_number = ""
    course_id = ""
    send_name = ""
    send_course = ""
    send_email = ""
    course_students = []
    student_entries = []

    def switch_frame(target):
        for frame in [main_menu, register_frame, attendance_frame, send_frame, create_course_frame]:
            frame.pack_forget()
        target.pack(expand=True, fill="both")

    def reset_all_entries():
        reg_entry.delete(0, tk.END)
        course_entry.delete(0, tk.END)
        send_name_entry.delete(0, tk.END)
        send_course_entry.delete(0, tk.END)
        send_email_entry.delete(0, tk.END)
        course_id_entry.delete(0, tk.END)
        for entry in student_entries:
            entry.destroy()
        student_entries.clear()
        create_new_student_entry()

    def on_register_click():
        nonlocal registration_number
        name = reg_entry.get().strip()
        if name:
            register_error.config(text="")
            registration_number = name.lower()
            registerStudent(registration_number)
            reset_all_entries()
        else:
            register_error.config(text="Please enter registration number.")

    def on_attendance_click():
        nonlocal course_id
        cid = course_entry.get().strip()
        if cid:
            attendance_error.config(text="")
            course_id = cid.strip().lower()
            attendance_taker(course_id)
            reset_all_entries()
        else:
            attendance_error.config(text="Please enter Course ID.")

    def on_send_click():
        nonlocal send_name, send_course, send_email
        name = send_name_entry.get().strip()
        course = send_course_entry.get().strip()
        email = send_email_entry.get().strip()
        if name and course and email:
            send_error.config(text="")
            send_email_with_attachment(name, course, email)
            send_name, send_course, send_email = name, course, email
            reset_all_entries()
        else:
            send_error.config(text="All fields are required.")

    def on_create_course():
        nonlocal course_students
        cid = course_id_entry.get().strip().lower()
        students = [e.get().strip().lower() for e in student_entries if e.get().strip().lower()]
        if cid and students:
            create_error.config(text="")
            course_students = students
            sorted_students = sorted(course_students, key=lambda x: x.lower())
            xls_file_creator(cid, sorted_students)
            reset_all_entries()
        else:
            create_error.config(text="Course ID and at least one student required.")

    def on_enter_pressed(event):
        if event.widget.get().strip():
            create_new_student_entry()
            root.after(100, lambda: scroll_to_widget(student_entries[-1]))

    def create_new_student_entry():
        entry = tk.Entry(student_inner_frame, font=("Arial", 14), width=40, justify="center")
        entry.pack(pady=5)
        entry.bind("<Return>", on_enter_pressed)
        student_entries.append(entry)
        entry.focus_set()

    def scroll_to_widget(widget):
        canvas.update_idletasks()
        canvas.yview_moveto(widget.winfo_y() / max(1, student_inner_frame.winfo_height()))

    