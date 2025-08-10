# FastAPI Project Setup with Firebase Environment Variables

This project uses **FastAPI** as the backend framework and integrates with **Firebase** for authentication and other services. The Firebase credentials and configuration are managed through environment variables stored in a `.env.development` file.

---

## Prerequisites

- Python 3.8 or higher installed
- `pip` package manager
- (Optional) `virtualenv` or `venv` for virtual environment management

---

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-project-directory>
```
### 2. Create and activate a virtual environment (recommended)
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Environment Variables Setup
1. .env.development file <br/>
Create a .env.development file in the root of the project (or use the one already provided) to store Firebase environment variables securely. This file should include your Firebase credentials and configuration like this:
```bash
FIREBASE_API_KEY=your_api_key_here
FIREBASE_AUTH_DOMAIN=your_project_id.firebaseapp.com
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_STORAGE_BUCKET=your_project_id.appspot.com
FIREBASE_MESSAGING_SENDER_ID=your_sender_id
FIREBASE_APP_ID=your_app_id
FIREBASE_MEASUREMENT_ID=your_measurement_id
```

