# ALX Travel App (0x00)

This is a backend project for the **ALX Travel App**, designed using Django. It provides core functionality for travel listings, bookings, and user reviews, forming the foundation of a booking system similar to Airbnb.

## 🚀 Features

- 🔖 Users can browse travel listings (hotels, apartments, experiences)
- 📅 Users can create bookings for available listings
- ⭐ Users can leave reviews on completed bookings

## 🏗️ Tech Stack

- **Python 3**
- **Django 4.x**
- **Django REST Framework**
- **SQLite / PostgreSQL** (Switchable)
- **Docker** (optional)

## 📁 Project Structure

```bash
alx_travel_app_0x00/
├── alx_travel_app/           # Django project folder
│   └── settings.py, urls.py
├── listings/                 # Core app: listings, bookings, reviews
│   ├── models.py             # Listing, Booking, Review models
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── manage.py
└── README.md
