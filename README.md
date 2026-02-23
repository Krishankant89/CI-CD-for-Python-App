# 🚀 Flask CI/CD Pipeline Project

A complete DevOps project demonstrating CI/CD pipeline implementation with Flask, Docker, and GitHub Actions.

## 📋 Project Overview

This project showcases:
- **Flask** web application with RESTful API
- **Docker** containerization
- **GitHub Actions** CI/CD pipeline
- **Automated testing** with pytest
- **Code coverage** reporting
- **Docker image** building and publishing

## 🏗️ Architecture

```
Developer → Git Push → GitHub
                         ↓
                 GitHub Actions
                 ├── Run Tests (pytest)
                 ├── Lint Code (flake8, black)
                 ├── Build Docker Image
                 ├── Test Container
                 └── Push to Registry
```

## 🛠️ Technologies Used

- **Python 3.11**
- **Flask** - Web framework
- **pytest** - Testing framework
- **Docker** - Containerization
- **GitHub Actions** - CI/CD automation
- **Gunicorn** - Production WSGI server

## 📁 Project Structure

```
cicd-flask-project/
├── .github/
│   └── workflows/
│       └── cicd.yml           # GitHub Actions pipeline
├── app.py                     # Flask application
├── test_app.py                # Test suite
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Local development setup
├── .dockerignore             # Docker ignore file
├── .gitignore                # Git ignore file
└── README.md                 # This file
```

## 🚦 Getting Started

### Prerequisites

- Python 3.11+
- Docker & Docker Compose
- Git
- GitHub account

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Krishankant89/CI-CD-for-Python-App
   cd cicd-flask-project
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```
   Visit: http://localhost:5000

5. **Run tests**
   ```bash
   pytest -v
   pytest --cov=app  # With coverage
   ```

### Docker Development

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

2. **Build Docker image manually**
   ```bash
   docker build -t flask-cicd-app .
   ```

3. **Run Docker container**
   ```bash
   docker run -d -p 5000:5000 --name flask-app flask-cicd-app
   ```

4. **Test the container**
   ```bash
   curl http://localhost:5000/health
   ```

## 🔄 CI/CD Pipeline

The GitHub Actions pipeline automatically:

1. **Test Stage**
   - Runs pytest with coverage
   - Uploads coverage reports

2. **Lint Stage**
   - Checks code with flake8
   - Verifies formatting with black

3. **Build Stage**
   - Builds Docker image
   - Tests container health
   - Saves image as artifact

4. **Deploy Stage** (on main branch)
   - Pushes to Docker Hub
   - Sends deployment notifications

### Setting Up GitHub Actions

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Flask CI/CD project"
   git branch -M main
   git remote add origin https://github.com/Krishankant89/CI-CD-for-Python-App
   git push -u origin main
   ```

2. **Configure Docker Hub** (Optional)
   - Go to Settings → Secrets and variables → Actions
   - Add secrets:
     - `DOCKERHUB_USERNAME`: Your Docker Hub username
     - `DOCKERHUB_TOKEN`: Docker Hub access token

3. **Watch the pipeline run**
   - Go to Actions tab in your GitHub repository
   - See the pipeline execute automatically

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Welcome message |
| `/health` | GET | Health check |
| `/api/info` | GET | Application info |

### Example Requests

```bash
# Home endpoint
curl http://localhost:5000/

# Health check
curl http://localhost:5000/health

# App info
curl http://localhost:5000/api/info
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test
pytest test_app.py::test_home_endpoint
```

## 🐳 Docker Commands

```bash
# Build image
docker build -t flask-cicd-app .

# Run container
docker run -d -p 5000:5000 --name myapp flask-cicd-app

# View logs
docker logs myapp

# Stop container
docker stop myapp

# Remove container
docker rm myapp

# Using docker-compose
docker-compose up -d      # Start in background
docker-compose logs -f    # Follow logs
docker-compose down       # Stop and remove
```


- GitHub: [@yourusername](https://github.com/Krishankant89)
'''
