
---

## 📘 SimpleAuthWithFlask

Une application d'authentification sécurisée en **Flask**, avec :

* Formulaire d’inscription et de connexion (Flask-WTF)
* Authentification avec JWT
* Dashboard protégé
* Stockage du token dans `localStorage`
* Rôles utilisateurs : `admin`, `client`.

---

### 🛠️ Technologies utilisées

* Python 3.12
* Flask
* Flask-WTF
* Flask-JWT-Extended
* Flask-Login
* HTML5 / CSS3
* SQLite
* JavaScript (pour `localStorage`)

---

### 🚀 Lancement du projet

1. **Cloner le projet**

```bash
git clone https://github.com/chahabsarah/SimpleAuthWithFlask.git
cd SimpleAuthWithFlask
```

2. **Créer un environnement virtuel**

```bash
python -m venv venv
source venv/bin/activate  # sous Unix/macOS
venv\Scripts\activate     # sous Windows
```

3. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

4. **Lancer l’application**

```bash
flask run
```


---

### 🔐 Fonctionnalités

| Fonctionnalité    | Description                           |
| ----------------- | ------------------------------------- |
| `/register`       | Page d'inscription via formulaire     |
| `/login`          | Page de connexion via formulaire      |
| `/api/login`      | Authentification avec JWT (POST JSON) |
| `/dashboard`      | Dashboard protégé par JWT             |
| `/api/protected`  | Route API protégée par JWT            |
| `/api/admin-only` | Accès réservé au rôle `admin`         |
| `localStorage`    | Stockage du token côté client         |

---

### 📂 Structure du projet

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
│
├── requirements.txt
└── README.md
```

---

### 👩‍💻 Développé par

**Sarra Chahab**

---

