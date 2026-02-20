# Deploying Dash Applications to the Cloud

A comprehensive guide for students to publish their Dash dashboards online.

## Table of Contents
1. [Free Deployment Options](#free-deployment-options)
2. [Render.com (Recommended - Free)](#rendercom-recommended---free)
3. [Heroku (Paid)](#heroku-paid)
4. [PythonAnywhere (Free Tier)](#pythonanywhere-free-tier)
5. [Railway (Free Tier)](#railway-free-tier)
6. [Preparing Your Application](#preparing-your-application)

---

## Free Deployment Options

| Platform | Free Tier | Pros | Cons |
|----------|-----------|------|------|
| **Render.com** | ✅ Yes | Easy setup, auto-deploy from Git | App sleeps after inactivity |
| **Railway** | ✅ Limited | Simple, modern interface | $5 credit/month limit |
| **PythonAnywhere** | ✅ Yes | Python-specific, good docs | Limited resources |
| **Heroku** | ❌ No (Paid only) | Mature platform, excellent docs | No longer free |
| **Vercel** | ✅ Yes | Fast, free for personal | Limited Python support |

**Recommendation for Students**: Start with **Render.com** - it's free, easy to use, and has good documentation.

---

## Render.com (Recommended - Free)

### Step 1: Prepare Your Application

Create these files in your project directory:

#### `requirements.txt`
```txt
dash==2.18.1
dash-bootstrap-components==1.6.0
plotly==5.24.1
pandas==2.2.3
requests==2.32.3
gunicorn==23.0.0
```

Generate automatically:
```bash
pip freeze > requirements.txt
```

#### `render.yaml` (optional)
```yaml
services:
  - type: web
    name: my-dash-app
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:server
    envVars:
      - key: PYTHON_VERSION
        value: 3.12.0
```

#### Update your `app.py`
```python
# Add this near the top after creating the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
server = app.server  # ← Add this line for deployment

# At the bottom, change this:
if __name__ == "__main__":
    app.run(debug=True)  # Local development

# To this:
if __name__ == "__main__":
    app.run(debug=False)  # Production
```

### Step 2: Push to GitHub

```bash
# Initialize git repository
git init
git add .
git commit -m "Initial commit"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main
```

### Step 3: Deploy on Render

1. Go to [render.com](https://render.com/) and sign up (free)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure:
   - **Name**: `my-dash-app`
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:server`
   - **Instance Type**: `Free`
5. Click **"Create Web Service"**

Your app will be live at: `https://my-dash-app.onrender.com`

### Step 4: Auto-Deploy

Every time you push to GitHub, Render will automatically redeploy your app!

```bash
git add .
git commit -m "Updated dashboard"
git push
```

---

## Heroku (Paid)

**Note**: Heroku eliminated free tiers in November 2022. Plans start at $5/month.

### Step 1: Prepare Files

#### `requirements.txt`
```txt
dash==2.18.1
dash-bootstrap-components==1.6.0
plotly==5.24.1
pandas==2.2.3
requests==2.32.3
gunicorn==23.0.0
```

#### `Procfile` (no file extension)
```
web: gunicorn app:server
```

#### `runtime.txt`
```txt
python-3.12.0
```

#### Update `app.py`
```python
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
server = app.server  # ← Required for Heroku

if __name__ == "__main__":
    app.run(debug=False)
```

### Step 2: Deploy via Heroku CLI

```bash
# Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Create app
heroku create my-dash-app

# Push to Heroku
git push heroku main

# Open your app
heroku open
```

Your app will be at: `https://my-dash-app.herokuapp.com`

### Step 3: Monitor and Scale

```bash
# View logs
heroku logs --tail

# Scale dynos (requires payment)
heroku ps:scale web=1
```

---

## PythonAnywhere (Free Tier)

### Step 1: Sign Up
1. Go to [pythonanywhere.com](https://www.pythonanywhere.com/)
2. Create a free "Beginner" account

### Step 2: Upload Your Code
1. Go to **Files** tab
2. Upload your `app.py` and create `requirements.txt`

### Step 3: Install Dependencies
Open a **Bash console**:
```bash
pip install --user -r requirements.txt
```

### Step 4: Create Web App
1. Go to **Web** tab
2. Click **"Add a new web app"**
3. Choose **"Manual configuration"** → **Python 3.10**
4. In WSGI configuration file, replace contents with:

```python
import sys
path = '/home/yourusername/mysite'
if path not in sys.path:
    sys.path.append(path)

from app import server as application
```

5. Reload the web app

Your app will be at: `https://yourusername.pythonanywhere.com`

**Limitations**:
- Limited CPU time (100 seconds/day on free tier)
- Apps may be slow
- No custom domains on free tier

---

## Railway (Free Tier)

### Step 1: Prepare Files

Same as Render - need `requirements.txt` and update `app.py` with `server = app.server`.

### Step 2: Deploy

1. Go to [railway.app](https://railway.app/)
2. Sign up with GitHub
3. Click **"New Project"** → **"Deploy from GitHub repo"**
4. Select your repository
5. Railway auto-detects Python and deploys

**Note**: Free tier includes $5 credit/month. Monitor usage.

---

## Preparing Your Application

### Essential Files Checklist

```
my-dash-app/
├── app.py                 # Your main application
├── requirements.txt       # Python dependencies
├── Procfile              # For Heroku (optional for others)
├── runtime.txt           # Python version (optional)
├── .gitignore            # Ignore unnecessary files
└── README.md             # Project documentation
```

### `.gitignore` Template

Create this file to avoid pushing unnecessary files:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Environment variables
.env
.env.local

# Data files (if large)
*.csv
*.json
*.db
```

### Code Adjustments for Production

#### 1. Add Server Reference
```python
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
server = app.server  # ← Add this line
```

#### 2. Disable Debug Mode
```python
if __name__ == "__main__":
    app.run(debug=False)  # Change True to False
```

#### 3. Handle Large Data Files

If your app loads large CSV files, consider:

**Option A: Use URLs**
```python
# Instead of:
df = pd.read_csv('local_file.csv')

# Use:
url = 'https://raw.githubusercontent.com/yourusername/repo/main/data.csv'
df = pd.read_csv(url)
```

**Option B: Include in Repository**
```python
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, 'data', 'file.csv'))
```

#### 4. Environment Variables for Secrets

Never commit API keys! Use environment variables:

```python
import os

# Get API key from environment
API_KEY = os.environ.get('API_KEY', 'default-key-for-local')

# Use in your app
response = requests.get(f'https://api.example.com/data?key={API_KEY}')
```

Set on Render.com: Dashboard → Environment → Add Environment Variable

---

## Example: Deploying the COVID Dashboard

Let's deploy the COVID-19 dashboard from this repository.

### 1. Create `requirements.txt`

```bash
cd "08-Dashboards/1_Covid Dashboard"
cat > requirements.txt << EOF
dash==2.18.1
dash-bootstrap-components==1.6.0
plotly==5.24.1
pandas==2.2.3
requests==2.32.3
numpy==2.1.3
gunicorn==23.0.0
EOF
```

### 2. Update `app.py`

Add after line 15:
```python
server = app.server  # For deployment
```

### 3. Create `.gitignore`

```bash
cat > .gitignore << EOF
__pycache__/
*.pyc
.env
EOF
```

### 4. Push to GitHub

```bash
git init
git add .
git commit -m "COVID Dashboard ready for deployment"
git remote add origin https://github.com/yourusername/covid-dashboard.git
git push -u origin main
```

### 5. Deploy on Render

- Go to render.com → New Web Service
- Connect GitHub repo
- Build: `pip install -r requirements.txt`
- Start: `gunicorn app:server`
- Deploy!

**Live URL**: `https://covid-dashboard-xxxx.onrender.com`

---

## Common Deployment Issues

### 1. **Import Errors**
**Problem**: `ModuleNotFoundError: No module named 'dash'`

**Solution**: Check `requirements.txt` includes all dependencies
```bash
pip freeze > requirements.txt
```

### 2. **Port Issues**
**Problem**: App not accessible

**Solution**: Use environment port
```python
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8050))
    app.run(debug=False, host='0.0.0.0', port=port)
```

### 3. **Data Loading Fails**
**Problem**: CSV file not found

**Solution**: Use absolute paths or URLs
```python
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, 'data', 'file.csv')
```

### 4. **App Crashes on Startup**
**Problem**: Application errors in logs

**Solution**: Check logs
```bash
# Render: View logs in dashboard
# Heroku: heroku logs --tail
# Railway: View logs in project dashboard
```

### 5. **Slow Performance**
**Problem**: App takes long to load

**Solution**:
- Reduce data processing on startup
- Cache data using `@cache` decorator
- Use smaller datasets for demos

---

## Testing Before Deployment

Always test locally with production settings:

```bash
# Install gunicorn
pip install gunicorn

# Test production server locally
gunicorn app:server

# Visit http://localhost:8000
```

---

## Cost Comparison

| Platform | Free Tier | Paid Plans | Best For |
|----------|-----------|------------|----------|
| **Render** | ✅ 750 hrs/month | $7/month | Students, demos |
| **Railway** | ✅ $5 credit/month | $5+ usage | Small projects |
| **Heroku** | ❌ None | $5-$7/month | Production apps |
| **PythonAnywhere** | ✅ Limited | $5/month | Learning, simple apps |
| **AWS/GCP/Azure** | ✅ Generous | Pay-as-you-go | Advanced users |

---

## Best Practices

1. ✅ **Use version control** (Git/GitHub) for all projects
2. ✅ **Test locally** before deploying
3. ✅ **Use environment variables** for secrets
4. ✅ **Monitor usage** on free tiers
5. ✅ **Add README** explaining your project
6. ✅ **Include a demo screenshot** in your repository
7. ✅ **Set debug=False** in production
8. ✅ **Use `gunicorn`** as production server
9. ✅ **Cache data** when possible
10. ✅ **Keep dependencies minimal**

---

## Additional Resources

### Documentation
- [Dash Deployment](https://dash.plotly.com/deployment)
- [Render Docs](https://render.com/docs)
- [Heroku Python Guide](https://devcenter.heroku.com/articles/getting-started-with-python)

### Tutorials
- [Deploying Dash Apps - Plotly](https://dash.plotly.com/deployment)
- [Free Dash Deployment - Charming Data](https://www.youtube.com/watch?v=hSPmj7mK6ng)

### Community
- [Dash Community Forum](https://community.plotly.com/c/dash/16)
- [Stack Overflow - Dash Tag](https://stackoverflow.com/questions/tagged/plotly-dash)

---

## Quick Start Commands

### For Render (Recommended)

```bash
# 1. Create requirements.txt
pip freeze > requirements.txt

# 2. Add to app.py after creating app
server = app.server

# 3. Push to GitHub
git init
git add .
git commit -m "Ready for deployment"
git push origin main

# 4. Deploy on render.com
# - Connect GitHub
# - Build: pip install -r requirements.txt
# - Start: gunicorn app:server
```

**That's it! Your app is live! 🚀**

---

## Questions?

For specific help with your project:
1. Check the platform's documentation
2. Review deployment logs for errors
3. Ask on Dash Community Forum
4. Check this repository's Issues section

Happy deploying! 🎉
