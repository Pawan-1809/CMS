# College Management System (`CMS`)

Fresh Django rebuild of the Heritage College Management Portal inside `CMS`, preserving the original multi-role structure, AdminLTE UI, Chart.js dashboards, and role-based workflows.

## Stack

- Python 3.11
- Django 3.2.25
- SQLite by default, PostgreSQL-ready through `DATABASE_URL`
- Bootstrap + AdminLTE + Chart.js
- WhiteNoise for static files

## Project Structure

```text
CMS/
├── .venv/
├── manage.py
├── requirements.txt
├── .env.example
├── static/
├── staticfiles/
├── media/
├── student_management_system/
└── student_management_app/
```

## Run Locally

```powershell
cd D:\Desktop\PROJECTS\College_management_portal\CMS
.venv\Scripts\activate
python manage.py migrate
python manage.py populate_demo_portal
python manage.py runserver
```

## Demo Credentials

- Admin: `admin@college.edu` / `admin123`
- Staff: `staff@college.edu` / `staff123`
- Student: `student@college.edu` / `student123`

## Notes

- Static assets have already been collected successfully.
- Demo data creates one course, one subject, one staff, one student, attendance, leave, feedback, and result records so the charts render immediately.
- For Render, use `build.sh` as the build command and the `render.yaml` blueprint in this repo root.
- Render starts the site with Gunicorn against Django WSGI and uses the app's production static storage.
- `SECURE_PROXY_SSL_HEADER` is already configured for Render's proxy, so HTTPS redirects and secure cookies work correctly there.
- Render also sets a conservative HSTS value by default; you can raise it later after you are happy with the live domain setup.
- If you deploy on Render with the default `.onrender.com` URL, settings automatically trust `RENDER_EXTERNAL_HOSTNAME`.
- If you later attach a custom domain, add that domain to `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` in Render environment variables.
