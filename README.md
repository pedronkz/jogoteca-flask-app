# 🎮 Jogoteca

A full-stack web application built with **Python** and **Flask** to manage a curated library of video games.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

## 🚀 Features

* **User Authentication:** Secure Login and Logout system.
* **User Registration:** New users can sign up to access the system.
* **Route Protection:** Only authenticated users can add new games.
* **Dynamic Routing:** Uses Flask's `url_for` to build flexible URLs.
* **Modern UI:** Responsive design using **Bootstrap 4** with custom cards and shadow effects.
* **Flash Messages:** Visual feedback for user actions (e.g., "Logged in successfully").

## 🛠️ Tech Stack

* **Backend:** Python 3, Flask.
* **Frontend:** HTML5, CSS3, Bootstrap 4.
* **Template Engine:** Jinja2.

## 📦 How to Run

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/jogoteca.git](https://github.com/YOUR_USERNAME/jogoteca.git)
    cd jogoteca
    ```

2.  **Create a Virtual Environment** (Optional but recommended)
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install flask
    ```

4.  **Run the Application**
    ```bash
    python jogoteca.py
    ```

5.  **Access the App**
    Open your browser and go to `http://127.0.0.1:5000`

## 🔐 Default Credentials

Since the database is currently volatile (in-memory dictionary), use these credentials to test or create a new user:

| User (Nickname) | Password |
| :--- | :--- |
| **PF** | `teste01` |
| **BADCHAGAS** | `fisica` |
| **GOAT** | `bode` |

## 📝 Future Improvements (Roadmap)

* [ ] Integration with **MySQL Database** for data persistence.
* [ ] Implementation of **Password Hashing** for security.
* [ ] Edit and Delete game functionality.

---

Made with 💙 by **Pedro Ferreira**
