# 🕑 Remind-Me-Later

**Remind-Me-Later** is a simple yet effective Django-based web application that allows users to create reminders with messages for specific dates and times. Users can receive these reminders through browser notifications. The app includes a custom login system, a sleek Bootstrap 5 UI, and logical categorization for upcoming and past reminders.

---

## 🚀 Features

- ✅ Custom user authentication system (not using Django's default admin auth)
- ✅ Secure login/logout mechanism
- ✅ Add, view, and manage reminders
- ✅ Separate views for:
  - **My Reminders** – Upcoming reminders
  - **My Old Reminders** – Past reminders
- ✅ In-built Django forms for adding new reminders
- ✅ Uses SQLite as backend DB
- ✅ Bootstrap 5 based responsive frontend UI
- ✅ Browser notification support via JavaScript

## 📽️ Project Demo

[![Watch Demo](https://img.shields.io/badge/Watch-Demo-blue?style=for-the-badge)](https://drive.google.com/file/d/1hrsbfK7LNqyEpbCAb8AmCqU8rYb1apuR/view?usp=sharing)


## 🗂️ Project Structure

```bash
Remind-Me-Later/
│
├── login/  # App for custom user authentication
├── Project/    # Django project configuration folder
├── Reminder_App/   # Core app handling reminders
├── static/ # Static files (CSS/JS)
├── templates/  # HTML templates
├── manage.py   # Django management script
├── requirements.txt    # Project dependencies
└── README.md   # Project overview (you’re here)
```

## 💡 How It Works

### 🔐 Login System

- Custom user authentication (no default Django admin login)
- After login, user is redirected to the main dashboard with:
- Navigation bar: `My Reminders`, `My Old Reminders`, Username & Logout button.

### ⏰ Reminder Functionality

- **Add Reminder**: Through Django’s built-in form UI
- **View Reminders**: Displayed as Bootstrap and custom CSS widgets
- **Upcoming Reminders**: Listed under "My Reminders"
- **Past Reminders**: Automatically moved to "My Old Reminders" based on date/time

### 🔔 Notifications

- Browser notifications are triggered for upcoming reminders using JavaScript.

---

## 🛠 Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, Bootstrap 5, CSS3, JavaScript
- **Database**: SQLite (default in Django)
- **Authentication**: Custom user auth
- **Notifications**: JavaScript browser notifications

---

## 🛠️ Future Enhancements

- Add Email or SMS API for notification
- Deploy on AWS or Azure Server

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/TejasVarute/Remind-Me-Later
```

### 2. Create & activate Virtual Environment

```bash
env\Scripts\activate
```

### 3. Install Requirements

```bash
    pip install -r requirements.txt
```

### 4. Apply Migations

```bash
    python manage.py makemigrations
    python manage.py migrate
```

### 5. Run Server

```bash
    python manage.py runserver
```

visit ```localhost:8000``` in your browser or ```https://127.0.0.1:8000/```

## 👨‍💻 Author

- **Tejas Varute**
- GitHub: [@TejasVarute](https://github.com/TejasVarute)
