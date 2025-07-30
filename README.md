
# 🚀 Flask App Auto Deployment to AWS EC2 using GitHub Actions

This project demonstrates how to **automatically deploy a Flask app** to an AWS EC2 instance using **GitHub Actions**, **Docker**, and **Gunicorn**.

---

## ⭐ Project Goal

> ✅ Auto-deploy a Flask web app to EC2 every time you push to the `main` branch.

---

## ⭐ Tech Stack

| Layer         | Tool / Service        |
|---------------|------------------------|
| App Framework | Flask (Python)         |
| Web Server    | Gunicorn               |
| OS & Infra    | Ubuntu EC2 Instance    |
| CI/CD         | GitHub Actions         |
| SSH Copy      | `appleboy/scp-action`  |
| SSH Run       | `appleboy/ssh-action`  |

---⭐ How to Use
Push any code to the main branch.

GitHub Action will:

Copy files to EC2

Install requirements

Restart the app using gunicorn
