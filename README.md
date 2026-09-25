python# Heart Disease Prediction System

A Django-based web application that uses machine learning to predict heart disease risk based on patient data.

## Features

- Heart disease risk prediction using machine learning
- User authentication (Patient, Doctor, Admin)
- Patient management
- Doctor management
- Feedback system
- Real-time notifications
- Search history tracking
- Interactive dashboard

## Requirements

- Python 3.8+
- Django 5.1.5
- Other dependencies listed in requirements.txt

## Installation


2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Setup

1. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

2. Create a superuser (admin):
```bash
python manage.py createsuperuser
```
Follow the prompts to enter:
- Username
- Email address
- Password

3. Start the development server:
```bash
python manage.py runserver
```

4. Access the application:
- Main site: http://127.0.0.1:8000/
- Admin interface: http://127.0.0.1:8000/admin/
- Admin login: http://127.0.0.1:8000/login_admin

## User Types

1. **Admin**
   - Access via /login_admin
   - Manage doctors and patients
   - View feedback
   - Monitor system usage

2. **Doctor**
   - Register/Login via main page
   - View patient predictions
   - Receive notifications about new predictions
   - Update profile

3. **Patient**
   - Register/Login via main page
   - Get heart disease predictions
   - View prediction history
   - Send feedback
   - Receive notifications

## Required Packages

```
django>=5.1.5
djangorestframework>=3.14.0
numpy>=1.24.0
pandas>=2.0.0
scikit-learn>=1.2.0
matplotlib>=3.7.0
python-dateutil>=2.8.2
pytz>=2023.3
scipy>=1.10.0
joblib>=1.2.0
threadpoolctl>=3.1.0
pillow>=9.5.0
```

## Usage

1. **For Patients:**
   - Register a new account
   - Log in
   - Enter health parameters
   - Get prediction results
   - View prediction history
   - Send feedback

2. **For Doctors:**
   - Register (requires admin approval)
   - Log in
   - View assigned patients
   - Monitor predictions
   - Update profile

3. **For Administrators:**
   - Log in through /login_admin
   - Approve/manage doctors
   - View all patients
   - Monitor system usage
   - View feedback

## Troubleshooting

1. If you encounter database errors:
```bash
python manage.py makemigrations
python manage.py migrate
```

2. If you need to reset your admin password:
```bash
python manage.py changepassword admin_username
```

3. For permission errors during package installation:
```bash
pip install --user package_name
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
