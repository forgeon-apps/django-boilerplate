### The error

> ModuleNotFoundError: No module named 'django'


It’s your laptop politely screaming:

> “Bro… you never installed Django in this environment.” 😄

### What the error actually means

This line is the key:

```text
ModuleNotFoundError: No module named 'django'
```

Python is trying to run:

```python
from django.core.management import execute_from_command_line
```

inside `manage.py`, but there is **no Django package installed** in the Python environment you’re using for:

```bash
python3 manage.py runserver
```

So either:

1. Django isn’t installed at all, **or**
2. It’s installed in another virtual environment / Python version, and you’re not using that one.

---

### Fix it step by step (the “correct” way)

From your project folder:

```bash
cd ...forgeon-demo-project/django-example
```

#### 1. Create a virtual environment

```bash
python3 -m venv .venv
```

#### 2. Activate it

```bash
source .venv/bin/activate
```


#### 2.1. Dectivate it

```bash
deactivate
```

You should now see something like `(.venv)` at the start of your terminal prompt.

#### 3. Install dependencies

If the project has `requirements.txt` (most Django examples do):

```bash
pip install -r requirements.txt
```

If it doesn’t, just install Django directly to test:

```bash
pip install django
```

(Optionally also `djangorestframework` or whatever else the example needs.)

#### 4. Run the dev server again

```bash
python manage.py runserver
# or
python3 manage.py runserver
```

If everything’s good, you’ll see:

```text
Starting development server at http://127.0.0.1:8000/
```

---

### If it *still* complains

Quick checklist:

* Are you sure the venv is active? Prompt should start with `(.venv)`
* Run:

  ```bash
  which python
  which pip
  ```

  Both should point inside your project’s `.venv` folder.
* Check installed packages:

  ```bash
  pip show django
  ```

  If nothing shows up → Django really isn’t installed in that environment.

---

If you paste me your project tree (`tree -L 2` from the project folder) or `ls` output + `requirements.txt` content, I can tailor the exact commands for this specific example project.
