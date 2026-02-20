# COVID-19 Dashboard Deployment Instructions

This dashboard is **ready to deploy**! All configuration files are included.

## ✅ Pre-Deployment Checklist

This dashboard already has:
- ✅ `server = app.server` in app.py (line 16)
- ✅ `requirements.txt` with all dependencies
- ✅ `Procfile` for Heroku/Railway
- ✅ `runtime.txt` specifying Python version
- ✅ `.gitignore` to exclude unnecessary files

## 🚀 Deploy in 3 Steps

### Step 1: Push to GitHub (1 minute)

```bash
# Navigate to this directory
cd "08-Dashboards/1_Covid Dashboard"

# Initialize git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "COVID-19 Dashboard ready for deployment"

# Create new repo on github.com, then:
git remote add origin https://github.com/YOUR-USERNAME/covid-dashboard.git
git push -u origin main
```

### Step 2: Sign up on Render (30 seconds)

1. Go to [render.com](https://render.com)
2. Click "Get Started"
3. Sign up with GitHub (recommended)

### Step 3: Deploy (2 minutes)

1. Click **"New +"** → **"Web Service"**
2. Click **"Connect account"** to link GitHub
3. Select your **covid-dashboard** repository
4. Fill in these settings:

   ```
   Name:           covid-dashboard
   Environment:    Python 3
   Build Command:  pip install -r requirements.txt
   Start Command:  gunicorn app:server
   Instance Type:  Free
   ```

5. Click **"Create Web Service"**

6. Wait 2-3 minutes for deployment ⏱️

7. **Done!** Your app is live! 🎉

**Your URL**: `https://covid-dashboard.onrender.com`

## 📱 Access Your Dashboard

Share your live dashboard URL:
- Add to your resume/CV
- Share on LinkedIn
- Include in your portfolio
- Show to potential employers

## 🔄 Update Your Dashboard

Make changes and push:

```bash
# Make changes to app.py
# ...

# Push to GitHub
git add .
git commit -m "Updated dashboard features"
git push

# Render automatically redeploys in 1-2 minutes!
```

## ⚠️ Important Notes

### App Sleep Behavior (Free Tier)
- Apps **sleep after 15 minutes** of inactivity
- First visit after sleep takes **30-60 seconds** to wake up
- Subsequent visits are instant
- This is normal for free tier!

### To Keep It Always On
Upgrade to Render Starter ($7/month) in your dashboard settings.

### Free Tier Limits
- ✅ 750 hours per month (enough for most projects)
- ✅ 100 GB bandwidth per month
- ✅ 512 MB RAM
- ✅ 0.1 CPU

## 🐛 Troubleshooting

### Issue: "Application Error"

**Check logs**: Render Dashboard → Your Service → Logs

Common causes:
1. Missing dependency in `requirements.txt`
2. Import error in code
3. API connection issues

**Solution**: Check logs and fix the specific error

### Issue: Dashboard loads slowly

**Cause**: App was sleeping (normal on free tier)

**Solutions**:
1. Wait 30-60 seconds on first load
2. Upgrade to paid tier for always-on
3. Use [UptimeRobot](https://uptimerobot.com) to ping every 5 min

### Issue: Data not loading

**Cause**: disease.sh API might be temporarily down

**Solution**: The app will show errors in the UI. Wait and refresh.

### Issue: Can't find my app on Render

**Check**:
1. You're logged into the correct Render account
2. The deployment completed successfully (check email)
3. Try the exact URL from Render dashboard

## 📊 Monitor Your Dashboard

In Render dashboard you can see:
- 📈 Request metrics
- 📊 CPU/Memory usage
- 📋 Deployment logs
- ⚙️ Environment variables
- 🔄 Deploy history

## 🎨 Customize Your Deployment

### Change App Name

In Render dashboard → Settings → change the name

New URL will be: `https://your-new-name.onrender.com`

### Add Environment Variables

If you add API keys or secrets:

1. Render Dashboard → Environment
2. Click "Add Environment Variable"
3. Set `KEY` and `VALUE`
4. Click "Save Changes"

In your code:
```python
import os
API_KEY = os.environ.get('API_KEY')
```

### Custom Domain (Paid Tier)

1. Buy domain (e.g., from Namecheap)
2. Render Dashboard → Settings → Custom Domain
3. Add domain and configure DNS
4. Enable SSL (automatic)

## 📖 What Files Do What?

```
1_Covid Dashboard/
├── app.py              # Main Dash application
├── requirements.txt    # Python packages to install
├── Procfile           # Tells Heroku how to run app
├── runtime.txt        # Specifies Python version
├── .gitignore         # Files not to commit to git
└── README.md          # Project documentation
```

### requirements.txt
Lists all Python packages needed:
```txt
dash==2.18.1
dash-bootstrap-components==1.6.0
plotly==5.24.1
pandas==2.2.3
requests==2.32.3
numpy==2.1.3
gunicorn==23.0.0
```

### Procfile
Tells platform how to start your app:
```
web: gunicorn app:server
```

### runtime.txt
Specifies Python version:
```
python-3.12.0
```

## 🎓 Learn More

- 📖 [Full Deployment Guide](../DEPLOYMENT_GUIDE.md)
- 📊 [Platform Comparison](../DEPLOYMENT_COMPARISON.md)
- 🚀 [Quick Deploy Guide](../QUICK_DEPLOY.md)

## ✅ Deployment Complete!

Once deployed, your dashboard:
- ✅ Has a public URL anyone can access
- ✅ Updates automatically when you push to GitHub
- ✅ Has SSL/HTTPS enabled (secure)
- ✅ Works on desktop and mobile
- ✅ Can be shared on social media/portfolio

**Congratulations!** You've deployed your first web application! 🎉

---

## Quick Reference Card

```
┌─────────────────────────────────────────┐
│     COVID-19 DASHBOARD DEPLOYMENT       │
├─────────────────────────────────────────┤
│ Platform:  Render.com                   │
│ Cost:      $0 (Free)                    │
│ Time:      ~5 minutes                   │
│                                         │
│ STEPS:                                  │
│ 1. Push to GitHub                       │
│ 2. Connect repo to Render               │
│ 3. Deploy!                              │
│                                         │
│ BUILD COMMAND:                          │
│   pip install -r requirements.txt       │
│                                         │
│ START COMMAND:                          │
│   gunicorn app:server                   │
│                                         │
│ YOUR URL:                               │
│   https://yourapp.onrender.com          │
└─────────────────────────────────────────┘
```

Happy deploying! 🚀
