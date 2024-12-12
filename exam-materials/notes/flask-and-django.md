### Basic Notes on Flask and Django

---

#### **What is Flask, and how is it used in Python programming?**

- **Flask** is a lightweight and flexible web framework for Python.
- Known as a **micro-framework** because it does not come with built-in tools or features like authentication or database management (these can be added as extensions).
- Designed for simplicity, making it ideal for small to medium-sized applications or APIs.
- Flask applications are written in Python, using the `flask` module.

**Key Features of Flask**:

- Minimalist and modular.
- Built-in development server and debugger.
- Support for URL routing and RESTful request handling.
- Extensible with many libraries and plugins.

**Installation**:

```bash
pip install flask
```

---

#### **What is Django, and how does it differ from Flask?**

- **Django** is a full-stack web framework for Python designed for building robust and scalable web applications.
- Comes with a lot of built-in features like authentication, database ORM, and an admin interface.
- Follows the **"batteries-included"** philosophy, providing everything needed for web development.

**Key Features of Django**:

- ORM for database interaction.
- Built-in user authentication system.
- Admin dashboard for managing models.
- Middleware support and templating system.

**Differences Between Flask and Django**:

| **Aspect**          | **Flask**                           | **Django**                        |
|---------------------|-------------------------------------|-----------------------------------|
| **Type**            | Micro-framework                    | Full-stack framework             |
| **Flexibility**     | Highly customizable, minimal setup | Includes most features out-of-box|
| **Learning Curve**  | Easy for beginners                 | Steeper, especially for small apps|
| **Use Case**        | Small/medium apps, APIs            | Large, complex, and scalable apps|

---

#### **How do you create a simple Flask web application?**

**Step 1: Install Flask**

```bash
pip install flask
```

**Step 2: Create a Python Script (e.g., `app.py`)**

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run()
```

**Step 3: Run the Application**

```bash
python app.py
```

- Open your browser and navigate to `http://localhost:5000` to see the message.
