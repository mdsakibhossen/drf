
# How to Create `requirements.txt` and Install Dependencies

## 1. Create a `requirements.txt` File

### Automatically
- Use `pip freeze` to capture all currently installed packages in your virtual environment:
  ```bash
  pip freeze > requirements.txt
  ```
- This will create a `requirements.txt` file containing lines like:
  ```
  Django==4.2.3
  djangorestframework==3.14.0
  requests==2.31.0
  ```

### Manually
- If you know the specific dependencies and versions, write them manually:
  ```
  Django==4.2.3
  djangorestframework
  requests>=2.30
  ```

---

## 2. Install Dependencies from `requirements.txt`
- Use `pip install` to install all dependencies listed in the `requirements.txt` file:
  ```bash
  pip install -r requirements.txt
  ```

---

## Best Practices
- Always generate the `requirements.txt` file from within your project's virtual environment to avoid unnecessary or global packages.
- Specify exact versions for compatibility, especially in production environments.

---

## Example

### Generate:
```bash
pip freeze > requirements.txt
```

### Install:
```bash
pip install -r requirements.txt
```
