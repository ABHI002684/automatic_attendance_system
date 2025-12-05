# Automatic Face Attendance System 🚀  
_Ongoing Project_

A lightweight, offline face-recognition-based attendance system built using **Python**, **OpenCV**, and **dlib**.  
The project focuses on automating attendance marking, generating course-wise XLS reports, extracting face features, and emailing attendance summaries — without relying on cloud services.

> 🔧 **Status:** Core backend modules completed (attendance, file creation, voice feedback, email). Further enhancements (GUI, dashboards, optimizations) are in progress.

---

## ✨ Features (Current Scope)

### ✅ Attendance Marking & XLS File Creation
- Detects recognized faces and marks students as **present**.
- Records attendance with **timestamps**.
- Creates and updates **course-wise `.xlsx` files** automatically.
- Ensures clean, structured attendance data for each session.

### ✅ Voice Feedback
- Announces the **registration number** of each student when marked present.
- Avoids duplicate announcements for the same student.
- Helps in **manual cross-verification** of attendance in real time.

### ✅ Face Feature Extraction
- Uses **dlib** to generate **128D facial embeddings**.
- Stores all extracted features in `features_all.csv`.
- Supports **multiple face samples per student** for better accuracy.

### ✅ Email Sending with Attendance Attachment
- Sends attendance `.xlsx` files as email attachments.
- Uses **SMTP** with app-password-based authentication.
- Designed for quick sharing of daily attendance reports.

---

## 🧩 Project Structure

```bash
automatic_attendance_system/
│
├── attendance_taker.py               # Detect faces & mark attendance
├── features_extraction_to_csv.py     # Extract 128D features & save to CSV
├── marking_attendance_in_xls.py      # Create/update XLS attendance files
├── voice_call_of_name.py                 # Voice announcement for marked students
├── mailing_xls_attendence_file.py          # Email attendance XLS as attachment
│
├── data/
│   ├── data_faces/                   # Captured face images
│   ├── features_all.csv              # Extracted 128D face features
│
├── attendance_files/                 # Course-wise attendance sheets
│   ├── cs101.xlsx
│   ├── cs201.xlsx
│
├── .env                              # Email config (not committed)
├── requirements.txt
└── README.md

## 🛠️ Tech Stack

**📝 Language**
- **Python**

**📚 Libraries & Frameworks**
- **OpenCV** – Face detection & image processing  
- **dlib** – 128D facial feature extraction  
- **numpy** – Numerical operations  
- **pandas** – Data handling & transformations  
- **xlrd / xlwt / openpyxl** – XLS/XLSX attendance file operations  
- **smtplib** – Email sending (SMTP)

**💾 Data Storage**
- `.csv` – Face feature embeddings  
- `.xlsx` – Course-wise attendance records  

**⚙️ Other Tools**
- `.env` – Environment-based email and config management  


## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/ABHI002684/automatic_attendance_system.git
   cd automatic_attendance_system
   ```

2. Install the dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables
   - Copy `.env.sample` to `.env`
   - Fill in your email credentials and basic configurations.


## Environment Variables (.env)

| Variable            | Description                          |
|---------------------|--------------------------------------|
| EMAIL_SENDER         | Your Gmail/SMTP email address        |
| EMAIL_PASSWORD       | App-specific password for Gmail     |
| SMTP_SERVER          | SMTP server (e.g., smtp.gmail.com)   |
| SMTP_PORT            | SMTP port (e.g., 587)                |


## Contributing

Contributions, ideas, and feedback are welcome.  
Feel free to open an Issue or submit a Pull Request.

## License

This project is licensed under the MIT License.

---

