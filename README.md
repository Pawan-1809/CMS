<div align="center">

# 🎓 Heritage College Management Portal

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=00D4AA&center=true&vCenter=true&width=435&lines=Student+Management+System;Built+with+Django+%F0%9F%90%8D;Heritage+Institute+of+Technology" alt="Typing SVG" />

[![Django](https://img.shields.io/badge/Django-3.2.25-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-live-demo">Live Demo</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-contributors">Contributors</a>
</p>

---

🌟 **A comprehensive college management system for Heritage Institute of Technology** 🌟

</div>

## 🚀 Live Demo

<div align="center">

### 🌐 **[college-management-portal.onrender.com](https://college-management-portal.onrender.com)**

![Dashboard Preview](https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge)

**Test Credentials:**

- 👑 **Admin**: `admin@college.edu` / `admin123`
- 👨‍🏫 **Staff**: `staff@college.edu` / `staff123`
- 👨‍🎓 **Student**: `student@college.edu` / `student123`

</div>

## ✨ Features

<table>
<tr>
<td width="33%">

### 👑 **Admin/HOD Panel**

- 📈 **Dashboard Analytics** - Performance charts & insights
- 👥 **Staff Management** - Add, update, delete staff
- 👨‍🎓 **Student Management** - Complete student lifecycle
- 📚 **Course Management** - Academic program control
- 📖 **Subject Management** - Curriculum organization
- 📅 **Session Management** - Academic year planning
- 📊 **Attendance Overview** - Monitor all classes
- 💬 **Feedback System** - Review & respond
- 🏖️ **Leave Management** - Approve/reject requests

</td>
<td width="33%">

### 👨‍🏫 **Staff/Teacher Portal**

- 📉 **Personal Dashboard** - Teaching insights
- ✅ **Attendance Tracking** - Mark & update attendance
- 📝 **Result Management** - Grade & assess students
- 📊 **Performance Reports** - Student progress
- 🏖️ **Leave Application** - Request time off
- 💬 **Feedback Channel** - Communicate with HOD
- 📚 **Subject Overview** - Teaching assignments
- 📅 **Schedule View** - Class timetables

</td>
<td width="33%">

### 👨‍🎓 **Student Dashboard**

- 📈 **Academic Dashboard** - Personal progress
- 📊 **Attendance View** - Track your presence
- 🏆 **Results Portal** - Grades & assessments
- 📚 **Subject Details** - Course information
- 📅 **Academic Calendar** - Important dates
- 🏖️ **Leave Request** - Apply for absence
- 💬 **Feedback System** - Share concerns
- 📝 **Profile Management** - Update personal info

</td>
</tr>
</table>

## 🚀 Quick Start

### 💻 **Local Development**

```bash
# 1. Clone the repository
git clone https://github.com/Pawan-1809/College_management_portal.git
cd College_management_portal

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Environment setup
cp .env.example .env
# Edit .env file with your configuration

# 5. Run migrations
python manage.py migrate

# 6. Create superuser (optional)
python manage.py createsuperuser

# 7. Start development server
python manage.py runserver
```

## 🛠️ Tech Stack

<div align="center">

| Category       | Technology                                                                                                                                                                                                                                                                                                        | Purpose        |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| **Backend**    | ![Django](https://img.shields.io/badge/-Django-092E20?style=flat-square&logo=django&logoColor=white)                                                                                                                                                                                                              | Web Framework  |
| **Database**   | ![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white) ![SQLite](https://img.shields.io/badge/-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)                                                                                             | Data Storage   |
| **Frontend**   | ![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/-CSS3-1572B6?style=flat-square&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) | User Interface |
| **Styling**    | ![Bootstrap](https://img.shields.io/badge/-Bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white)                                                                                                                                                                                                     | UI Components  |
| **Deployment** | ![Render](https://img.shields.io/badge/-Render-46E3B7?style=flat-square&logo=render&logoColor=white)                                                                                                                                                                                                              | Cloud Hosting  |
| **Storage**    | ![WhiteNoise](https://img.shields.io/badge/-WhiteNoise-9146FF?style=flat-square)                                                                                                                                                                                                                                  | Static Files   |

</div>

## 📁 Project Structure

```
College-management-portal/
├── 📁 student_management_app/
│   ├── 👑 management/commands/     # Custom Django commands
│   ├── 📋 templates/           # HTML templates
│   ├── 🔄 migrations/          # Database migrations
│   └── 📝 models.py            # Database models
├── 🎨 static/                  # Static files (CSS, JS, Images)
├── 🗺️ media/                   # User uploaded files
├── ⚙️ student_management_system/ # Main project settings
└── 📦 requirements.txt         # Python dependencies
```

## 🔧 Configuration

<details>
<summary><b>🔍 Click to expand environment variables</b></summary>

```env
# Django Configuration
SECRET_KEY=your-secret-key-here
DEBUG=True  # Set to False in production
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Database (SQLite for development)
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

# Security Settings
SECURE_SSL_REDIRECT=False  # Set to True in production
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False
```

</details>

## 🛡️ Security Features

- 🔐 **Email-based Authentication** - Secure login system
- 👥 **Role-based Access Control** - Admin, Staff, Student roles
- 🌐 **CSRF Protection** - Cross-site request forgery prevention
- 📜 **Input Validation** - SQL injection protection
- 🔒 **Session Management** - Secure session handling
- 🏆 **Production Ready** - SSL/HTTPS support

### 💖 **Support the Project**

If you find this project helpful, please consider:

[![GitHub Stars](https://img.shields.io/github/stars/Pawan-1809/College_management_portal?style=social)](https://github.com/Pawan-1809/College_management_portal/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Pawan-1809/College_management_portal?style=social)](https://github.com/Pawan-1809/College_management_portal/network/members)

</div>

<p align="center">
  <b>🎆 Made with Efforts </b><br>
  <i>for Heritage Institute of Technology</i>
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=16&duration=2000&pause=1000&color=00D4AA&center=true&vCenter=true&width=600&lines=Thank+you+for+visiting+our+project!;%E2%AD%90+Star+us+on+GitHub+if+you+found+it+helpful!;Built+with+Django+and+%E2%9D%A4%EF%B8%8F+by+Heritage+Team" alt="Footer Typing SVG" />
</p>

</div>
