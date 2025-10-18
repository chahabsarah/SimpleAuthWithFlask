
## 📘 SimpleAuthWithFlask

A secure **Flask** authentication application, including:

* Registration and login forms using Flask-WTF
* JWT-based authentication
* Protected dashboard
* Token storage in `localStorage`
* User roles: `admin`, `client`

---

### 🛠️ Technologies Used

* Python 3.12
* Flask
* Flask-WTF
* Flask-JWT-Extended
* Flask-Login
* HTML5 / CSS3
* SQLite
* JavaScript (for `localStorage`)

---

### 🚀 Getting Started

1. **Clone the project**

```bash
git clone https://github.com/chahabsarah/SimpleAuthWithFlask.git
cd SimpleAuthWithFlask
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate      # on Unix/macOS
venv\Scripts\activate         # on Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
flask run
```

---

### 🔐 Features

| Endpoint          | Description                      |
| ----------------- | -------------------------------- |
| `/register`       | Registration page with form      |
| `/login`          | Login page with form             |
| `/api/login`      | JWT authentication via JSON POST |
| `/dashboard`      | JWT-protected dashboard          |
| `/api/protected`  | JWT-protected API route          |
| `/api/admin-only` | Accessible only by `admin` role  |
| `localStorage`    | Stores JWT token client-side     |

---

### 📂 Project Structure

```
flask-auth-app/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   └── templates/
│       ├── base.html
│       ├── login.html
│       ├── register.html
│       └── dashboard.html
│
├── requirements.txt
└── README.md
```

---
### 🖼️ Screenshots
```
![Home page](../SimpleAuthWithFlask/app/static/home.jpg)
![Login page](../SimpleAuthWithFlask/app/static/login.jpg)
![Sign up page](../SimpleAuthWithFlask/app/static/signup.jpg)
```
---
### 👩‍💻 Developed By

**Sarra Chahab**


