# NetraPulse AI

## Progress Log – Day 0 & Day 1

### Project Information

**Project Name:** NetraPulse AI

**Tagline:** Observe. Analyze. Protect.

**Full Name:** NetraPulse AI: Enterprise Real-Time Banking Fraud Intelligence Platform

**Owner:** Kalpesh Patil

**Current Phase:** Phase 1 – Authentication Service

---

# Project Vision

NetraPulse AI is an enterprise-grade banking fraud intelligence platform designed to monitor transaction streams in real time and determine whether transactions should be:

* Approved
* Verified
* Blocked

Target Users:

* Fraud Analysts
* Risk Teams
* Security Teams
* Compliance Teams
* Banking Administrators

---
# Additional Notes (End of Day 1)

## Current Project Structure

NetraPulseAI/

backend/
└── auth_service/
├── api/
├── core/
├── db/
├── models/
├── schemas/
├── repositories/
├── services/
└── tests/

frontend/
docs/
research/
docker/

README.md

---

## Architecture Decisions

### Decision 1: Layered Architecture

Flow:

Client
↓
API Route
↓
Service Layer
↓
Repository Layer
↓
Database

Reason:

* Separation of concerns
* Easier testing
* Easier maintenance
* Enterprise scalability

---

### Decision 2: FastAPI

Reason:

* High performance
* Automatic Swagger documentation
* Strong typing support
* Excellent for microservices

---

### Decision 3: PostgreSQL + SQLAlchemy

Reason:

* Industry-standard database
* ORM support
* Strong relational capabilities
* Suitable for future fraud analytics

---

## Progress Summary

Completed:

* Project planning
* Technology stack finalization
* Git repository initialization
* First commit
* Enterprise folder structure
* Virtual environment creation
* Dependency installation

Pending:

* main.py
* config.py
* session.py
* PostgreSQL setup
* SQLAlchemy integration
* User model
* JWT authentication
* Register API
* Login API
* RBAC

---

## Day 2 Objectives

1. Create main.py
2. Create config.py
3. Create session.py
4. Run first FastAPI application
5. Open Swagger UI
6. Understand FastAPI request lifecycle

Current Progress Estimate:
5% Complete

# Technology Stack

## Backend

* Python 3.12.10
* FastAPI
* SQLAlchemy
* Alembic

## Database

* PostgreSQL

## Authentication

* JWT
* Role-Based Access Control (RBAC)

## Frontend

* React
* Vite
* Tailwind CSS

## Deployment

* Docker
* Microsoft Azure

---

# Day 0 Activities

## Architecture Planning

Selected enterprise layered architecture:

Client
↓
API Route
↓
Service Layer
↓
Repository Layer
↓
Database

This architecture was chosen to ensure:

* Scalability
* Maintainability
* Testability
* Enterprise readiness

---

## Repository Creation

Created project repository:

NetraPulseAI/

Initialized Git repository.

Created first commit.

---

## Project Structure

Created root project structure:

NetraPulseAI/

backend/
frontend/
docs/
research/
docker/

README.md

---

## Environment Decisions

Operating System:

Windows 11

Python Version:

3.12.10

Git Version:

2.45.1

Virtual Environment:

venv

Decision:

Development will use Python virtual environments.

Docker will be introduced during deployment phases.

---

# Day 1 Activities

## Authentication Service Structure

Created Authentication Service module:

backend/auth_service/

Created enterprise folder structure:

auth_service/

api/
core/
db/
models/
schemas/
repositories/
services/
tests/

---

## Folder Responsibilities

### api/

Contains FastAPI route definitions.

Examples:

* Register User
* Login User
* User Profile

---

### services/

Contains business logic.

Examples:

* Authentication Logic
* JWT Generation
* Password Validation

---

### repositories/

Contains database interaction logic.

Examples:

* Create User
* Fetch User
* Update User

---

### models/

Contains SQLAlchemy database models.

Examples:

* User Model
* Role Model

---

### schemas/

Contains Pydantic request/response schemas.

Examples:

* UserCreate
* UserLogin
* UserResponse

---

### core/

Contains application configuration and security.

Examples:

* JWT Configuration
* Application Settings
* Security Utilities

---

### db/

Contains database connectivity layer.

Examples:

* SQLAlchemy Session
* Database Engine

---

### tests/

Contains automated test cases.

---

## Virtual Environment Setup

Created Python Virtual Environment:

venv

Verified activation.

---

## Installed Dependencies

FastAPI

Uvicorn

SQLAlchemy

PostgreSQL Driver

Alembic

Python-JOSE

Passlib (bcrypt)

Python Multipart

Pydantic Settings

Email Validator

---

# Current Status

Phase:

Phase 1 – Authentication Service

Status:

In Progress

Completed:

* Git Setup
* Repository Initialization
* Project Structure
* Authentication Service Structure
* Virtual Environment
* Dependency Installation

Pending:

* main.py
* config.py
* session.py
* PostgreSQL Setup
* SQLAlchemy Integration
* User Model
* JWT Authentication
* Register API
* Login API
* RBAC

---

# Next Session Goals

1. Create main.py
2. Create config.py
3. Create session.py
4. Understand FastAPI application startup
5. Design PostgreSQL integration
6. Design User model

---

# Learning Outcomes So Far

Learned:

* Git initialization
* Project organization
* Virtual environments
* Dependency management
* Enterprise folder structure
* Layered backend architecture

Prepared For:

* FastAPI development
* SQLAlchemy ORM
* PostgreSQL integration
* JWT authentication
* Enterprise backend engineering

---

Document Version: 1.0

Last Updated: Day 1
Project: NetraPulse AI
