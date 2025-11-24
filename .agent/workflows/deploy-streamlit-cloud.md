---
description: Deploy to Streamlit Community Cloud
---

# Deploy Tamil Temple Architecture AI to Streamlit Community Cloud

This workflow guides you through deploying your Streamlit application to Streamlit Community Cloud for free.

## Prerequisites

1. **GitHub Account**: You need a GitHub account (free)
2. **Public Repository**: Your code must be in a public GitHub repository
3. **Streamlit Cloud Account**: Sign up at [share.streamlit.io](https://share.streamlit.io)

---

## Step 1: Verify Your Local Setup

Before deploying, ensure your application works locally:

```bash
streamlit run Temple_App.py
```

Test the application in your browser and verify:
- ✅ Temple selection works
- ✅ Temple information displays correctly
- ✅ AI analysis works (with your API key)

---

## Step 2: Ensure All Files Are Committed to Git

Check the status of your Git repository:

```bash
git status
```

If you have uncommitted changes, commit them:

```bash
git add .
git commit -m "Prepare for Streamlit Cloud deployment"
```

---

## Step 3: Push to GitHub

If you haven't already pushed your repository to GitHub:

### Option A: Using GitHub Desktop (if installed)
1. Open GitHub Desktop
2. Select your repository
3. Click "Publish repository" or "Push origin"
4. Ensure the repository is **public** (required for free Streamlit Cloud)

### Option B: Using Command Line
```bash
git push origin main
```

If you haven't set up a remote repository yet:
1. Go to [github.com](https://github.com) and create a new repository
2. Name it something like `tamil-temple-ai`
3. Make it **public**
4. Follow GitHub's instructions to push your existing repository

---

## Step 4: Sign Up for Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"Sign up"** or **"Continue with GitHub"**
3. Authorize Streamlit to access your GitHub repositories
4. Complete the sign-up process

---

## Step 5: Deploy Your App

1. **Click "New app"** button in Streamlit Cloud dashboard
2. **Select your repository**:
   - Repository: `your-username/tamil-temple-ai` (or your repo name)
   - Branch: `main` (or your default branch)
   - Main file path: `Temple_App.py`
3. **Click "Deploy!"**

Streamlit Cloud will:
- Automatically detect `requirements.txt`
- Install dependencies
- Start your application
- Provide a public URL (e.g., `your-app.streamlit.app`)

---

## Step 6: Configure Secrets (API Key) - RECOMMENDED

Your app now supports **two ways** to use API keys:

### Option 1: Provide a Default API Key (Recommended)

This allows users to use the app immediately without needing their own API key, but they can still use their own if they prefer.

1. In Streamlit Cloud dashboard, go to your app settings (click the hamburger menu ⋮)
2. Click on **"Secrets"** in the left sidebar
3. Add your secrets in TOML format:

```toml
GOOGLE_API_KEY = "your-actual-api-key-here"
```

4. Click **"Save"**
5. The app will automatically restart

**How it works:**
- When a default key is configured, users see "✅ Default API Key Available"
- They can use the app immediately with the default key
- They can check "Use my own API key instead" to override with their own key

### Option 2: Let Users Provide Their Own Keys

If you don't configure a secret API key:
- Users will be prompted to enter their own Gemini API key
- They can get a free key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### Local Development with Secrets

To test secrets locally:

1. Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml`
2. Replace `"your-actual-api-key-here"` with your real API key
3. The file is already in `.gitignore`, so it won't be committed
4. Run the app locally: `streamlit run Temple_App.py`



---

## Step 7: Access Your Deployed App

Once deployment is complete (usually takes 2-5 minutes):

1. You'll receive a URL like: `https://your-app-name.streamlit.app`
2. Share this URL with anyone - it's publicly accessible!
3. The app will automatically update when you push changes to GitHub

---

## Step 8: Monitor and Manage

### View Logs
- Click on **"Manage app"** → **"Logs"** to see real-time logs
- Useful for debugging deployment issues

### Reboot App
- If the app crashes, click **"Reboot app"** in the menu

### Update App
- Simply push changes to your GitHub repository
- Streamlit Cloud will automatically detect and redeploy

---

## Troubleshooting

### Issue: "App is not deploying"
**Solution**: Check the logs for errors. Common issues:
- Missing dependencies in `requirements.txt`
- Python version incompatibility
- Syntax errors in code

### Issue: "Module not found"
**Solution**: Ensure all required packages are listed in `requirements.txt`:
```
streamlit
google-generativeai
python-dotenv
```

### Issue: "App keeps restarting"
**Solution**: 
- Check for infinite loops in your code
- Verify API key configuration
- Check memory usage (free tier has limits)

### Issue: "Repository not found"
**Solution**: 
- Ensure repository is **public**
- Re-authorize Streamlit Cloud to access your GitHub

---

## Optional: Custom Domain

If you want a custom domain (e.g., `temples.yourdomain.com`):

1. Go to app settings → **"General"**
2. Scroll to **"Custom subdomain"**
3. Enter your desired subdomain
4. For a full custom domain, you'll need to configure DNS settings

---

## App Management Best Practices

1. **Keep dependencies updated**: Regularly update `requirements.txt`
2. **Monitor usage**: Check analytics in Streamlit Cloud dashboard
3. **Handle errors gracefully**: Add try-catch blocks for API calls
4. **Add loading states**: Use `st.spinner()` for better UX
5. **Test locally first**: Always test changes before pushing

---

## Resources

- [Streamlit Cloud Documentation](https://docs.streamlit.io/streamlit-community-cloud)
- [Streamlit Forums](https://discuss.streamlit.io/)
- [Deployment Troubleshooting](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app/app-dependencies)

---

## Summary

✅ **Your app is now live!**
- Public URL: Check Streamlit Cloud dashboard
- Auto-deploys on GitHub push
- Free hosting with community support
- Share with the world! 🎉
