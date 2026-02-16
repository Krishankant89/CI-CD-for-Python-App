# 🚀 CI/CD Pipeline Quick Reference

## Project Structure
```
cicd-flask-project/
├── app.py                    # Flask application
├── test_app.py               # Test suite (pytest)
├── requirements.txt          # Python dependencies
├── Dockerfile               # Container definition
├── docker-compose.yml       # Local dev orchestration
├── .github/workflows/
│   └── cicd.yml            # GitHub Actions pipeline
└── README.md               # Documentation
```

## Local Development Commands

### Python Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate          # Linux/Mac
venv\Scripts\activate             # Windows

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py                     # Dev mode
gunicorn --bind 0.0.0.0:5000 app:app  # Production mode
```

### Testing
```bash
# Run all tests
pytest

# Verbose output
pytest -v

# With coverage
pytest --cov=app

# Coverage report (HTML)
pytest --cov=app --cov-report=html

# Run specific test
pytest test_app.py::test_home_endpoint
```

### API Testing
```bash
# Test endpoints
curl http://localhost:5000/
curl http://localhost:5000/health
curl http://localhost:5000/api/info

# Pretty print JSON
curl http://localhost:5000/ | jq

# Test with headers
curl -H "Content-Type: application/json" http://localhost:5000/
```

## Docker Commands

### Building
```bash
# Build image
docker build -t flask-cicd-app .

# Build with tag
docker build -t flask-cicd-app:v1.0 .

# Build without cache
docker build --no-cache -t flask-cicd-app .
```

### Running
```bash
# Run container
docker run -d -p 5000:5000 --name myapp flask-cicd-app

# Run with environment variables
docker run -d -p 5000:5000 \
  -e ENVIRONMENT=production \
  --name myapp flask-cicd-app

# Run interactively
docker run -it -p 5000:5000 flask-cicd-app

# Run with volume mount (live reload)
docker run -d -p 5000:5000 \
  -v $(pwd)/app.py:/app/app.py \
  --name myapp flask-cicd-app
```

### Management
```bash
# List containers
docker ps                    # Running
docker ps -a                # All

# View logs
docker logs myapp           # All logs
docker logs -f myapp        # Follow logs
docker logs --tail 50 myapp # Last 50 lines

# Execute command in container
docker exec -it myapp bash
docker exec myapp curl http://localhost:5000/health

# Stop and remove
docker stop myapp
docker rm myapp

# Remove image
docker rmi flask-cicd-app
```

### Docker Compose
```bash
# Start services
docker-compose up            # Foreground
docker-compose up -d         # Background
docker-compose up --build    # Rebuild images

# Stop services
docker-compose stop          # Stop containers
docker-compose down          # Stop and remove

# View logs
docker-compose logs          # All logs
docker-compose logs -f       # Follow
docker-compose logs flask-app # Specific service

# Rebuild
docker-compose build
docker-compose build --no-cache
```

## Git & GitHub

### Initial Setup
```bash
# Initialize repository
git init
git add .
git commit -m "Initial commit: CI/CD Flask project"
git branch -M main

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/cicd-flask-project.git

# Push to GitHub
git push -u origin main
```

### Regular Workflow
```bash
# Check status
git status

# Add changes
git add .                    # All files
git add app.py              # Specific file

# Commit
git commit -m "Add feature X"

# Push
git push                     # To current branch
git push origin main        # To main branch

# Pull latest changes
git pull

# View history
git log
git log --oneline
```

### Branch Workflow
```bash
# Create and switch to branch
git checkout -b feature/new-endpoint

# List branches
git branch

# Switch branch
git checkout main

# Merge branch
git checkout main
git merge feature/new-endpoint

# Delete branch
git branch -d feature/new-endpoint
```

## GitHub Actions

### Viewing Pipeline
1. Go to your repository on GitHub
2. Click "Actions" tab
3. See workflow runs
4. Click on a run to see details

### Pipeline Triggers
- Push to `main` or `develop` branch
- Pull request to `main` branch
- Manual trigger (workflow_dispatch)

### Pipeline Jobs
1. **Test** - Run pytest with coverage
2. **Lint** - Check code quality (flake8, black)
3. **Build** - Build Docker image
4. **Push** - Push to Docker Hub (optional)

### Adding Secrets
1. Go to Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Add:
   - `DOCKERHUB_USERNAME`
   - `DOCKERHUB_TOKEN`

## Troubleshooting

### Application Issues
```bash
# Check if port is in use
lsof -i :5000                # Mac/Linux
netstat -ano | findstr :5000 # Windows

# Kill process on port
kill -9 $(lsof -t -i:5000)   # Mac/Linux

# View application logs
python app.py  # Check output
```

### Docker Issues
```bash
# Check Docker is running
docker --version
docker ps

# Clean up Docker
docker system prune          # Remove unused data
docker system prune -a       # Remove all unused images

# Rebuild from scratch
docker-compose down -v
docker-compose up --build

# Check container health
docker inspect myapp | grep -A 10 Health
```

### Test Failures
```bash
# Run tests with verbose output
pytest -v -s

# Run specific test
pytest test_app.py::test_home_endpoint -v

# Check test coverage
pytest --cov=app --cov-report=term-missing
```

### GitHub Actions Failures
- Check the Actions tab for error messages
- Review job logs for specific failures
- Ensure secrets are configured correctly
- Test locally before pushing:
  ```bash
  pytest
  docker build -t test-image .
  docker run test-image
  ```

## Common Modifications

### Adding New Endpoint
```python
# In app.py
@app.route('/api/users')
def get_users():
    return jsonify({"users": ["Alice", "Bob"]})

# In test_app.py
def test_users_endpoint(client):
    response = client.get('/api/users')
    assert response.status_code == 200
    assert 'users' in response.get_json()
```

### Adding Environment Variables
```python
# In app.py
import os
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///default.db')

# In Dockerfile
ENV DATABASE_URL=postgresql://user:pass@db:5432/mydb

# In docker-compose.yml
environment:
  - DATABASE_URL=postgresql://user:pass@db:5432/mydb
```

### Adding Dependencies
```bash
# Install package
pip install requests

# Update requirements
pip freeze > requirements.txt

# Or manually edit requirements.txt
# requests==2.31.0
```

## Performance Tips

### Docker Optimization
```dockerfile
# Use specific Python version
FROM python:3.11-slim

# Combine RUN commands
RUN apt-get update && apt-get install -y package1 package2 \
    && rm -rf /var/lib/apt/lists/*

# Use .dockerignore
# Add unnecessary files to .dockerignore
```

### Application Optimization
```python
# Use production WSGI server
gunicorn --workers 4 --threads 2 app:app

# Enable caching
from flask import Flask
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
```

## Useful Resources

- Flask Docs: https://flask.palletsprojects.com/
- Docker Docs: https://docs.docker.com/
- GitHub Actions: https://docs.github.com/actions
- pytest Docs: https://docs.pytest.org/

## Resume Points Template

**DevOps Engineer - CI/CD Pipeline Project**
- Developed automated CI/CD pipeline using GitHub Actions reducing deployment time by 80%
- Implemented Docker containerization with multi-stage builds, reducing image size by 40%
- Achieved 95% test coverage using pytest with automated coverage reporting
- Orchestrated microservices using Docker Compose for local development
- Configured automated Docker image building and publishing to container registry
- Implemented health checks and graceful shutdown for production reliability

## Next Level Features

1. **Database Integration**
   - Add PostgreSQL/MongoDB
   - Database migrations with Alembic

2. **Kubernetes Deployment**
   - Write K8s manifests
   - Deploy to minikube/cloud

3. **Monitoring & Logging**
   - Add Prometheus metrics
   - Grafana dashboards
   - ELK stack integration

4. **Security**
   - Add security scanning
   - Implement secrets management
   - HTTPS/SSL configuration

5. **Advanced CI/CD**
   - Staging environment
   - Blue-green deployment
   - Canary releases
