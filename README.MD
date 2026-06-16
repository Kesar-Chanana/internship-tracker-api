# Internship Tracker API

## Project Overview

Internship Tracker API is a backend project built with Python and FastAPI to manage job applications.


---

## Problem Statement

Students applying for internships often apply to many companies at the same time. It becomes difficult to track:

* Company name
* Job role
* Location
* Application status
* Date applied
* Notes
* Follow-up requirements

This project solves that problem by providing a backend API to store, update, search, and manage job applications.

---

## Tech Stack

### Backend

* Python
* FastAPI
* Pydantic
* SQLAlchemy
* Alembic

### Database

* PostgreSQL
* SQL

### Tools

* Git
* GitHub
* Docker
* Linux basics
* GitHub Actions

### Testing

* pytest

---

## Project Architecture



```text
Client / Frontend
        ↓
FastAPI Backend
        ↓
PostgreSQL Database
```


## Example Job Application Data

```json
{
  "company": "Delivery Hero",
  "role": "Backend Intern",
  "location": "Berlin",
  "status": "Applied",
  "notes": "Python, FastAPI, PostgreSQL role"
}
```
