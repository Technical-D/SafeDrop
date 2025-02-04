# SafeDrop📩 - One-Time Secret Sharing API  
A secure API for sharing secrets using one-time encrypted links. Once accessed, the secret is permanently deleted.  

---

## 🚀 Features  
- **One-time secret sharing** – The secret is deleted after retrieval.  
- **AES-256 encryption (Fernet)** – Ensures data confidentiality.  
- **Expiration time** – Secrets expire after a set duration.  
- **REST API** – Built with Django Rest Framework (DRF).  

---

## 🛠 Installation  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/safedrop.git
   cd safedrop
   ```
2. **Install dependencies**
   ```bash
   pip install django djangorestframework cryptography
   ```
3. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. **Start the Django server**
   ```bash
   python manage.py runserver
   ```
---

## 📝 API Endpoints
1️⃣ Create a Secret
Endpoint: POST /api/create_secret/
Request Body:
```bash
{
    "message": "This is a secret message",
    "expires_in": 3600  # Expiration time in seconds (default: 1 hour)
}
```
Response:
```bash
{
    "secret_url": "http://127.0.0.1:8000/api/get_secret/<secret-key>/"
}
```

2️⃣ Retrieve a Secret (One-time Access)
Endpoint: GET /api/get_secret/<secret-key>/
Response (Success):
```bash
{
    "message": "This is a secret message"
}
```
Response (If expired or already accessed):
```bash
{
    "error": "Secret not found or expired"
}
```
---

## 🔒 Security Notes
  - The secret is encrypted using Fernet (AES-256) before storage.
  - Once retrieved, the secret is deleted permanently.
  - Secrets expire based on the expires_in value.

---

## 📌 Next Steps
  - Add authentication (API keys or tokens).
  - Enhance expiration handling (background cleanup tasks).
  - Deploy on a cloud platform (AWS, Heroku, etc.).

---

## 👨‍💻 Author
[Technical-D](https://github.com/Technical-D)
