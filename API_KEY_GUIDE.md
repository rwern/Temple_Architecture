# 🔑 API Key Configuration Guide

This guide explains how to configure Google Gemini API keys for your Tamil Temple Architecture AI app.

## 📖 Overview

Your app now supports **flexible API key management**:

1. **Default API Key** (via Streamlit secrets) - Users can use the app immediately
2. **User-provided API Key** - Users can override with their own key
3. **No Default Key** - Users must provide their own key

---

## 🌐 For Streamlit Cloud Deployment

### Setting Up a Default API Key

1. **Deploy your app** to Streamlit Cloud first
2. **Go to your app** in the Streamlit Cloud dashboard
3. **Click the hamburger menu** (⋮) → **Settings**
4. **Click "Secrets"** in the left sidebar
5. **Add the following** in TOML format:

```toml
GOOGLE_API_KEY = "your-actual-gemini-api-key-here"
```

6. **Click "Save"**
7. **Wait for the app to restart** (automatic)

### Getting a Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the key (keep it secure!)
5. Use it in your secrets configuration

### How Users Will See It

**With Default API Key:**
```
✅ Default API Key Available
☐ Use my own API key instead
🔑 Using default API key
```

**When User Checks "Use my own API key":**
```
✅ Default API Key Available
☑ Use my own API key instead
[Enter Your Gemini API Key: ___________]
```

**Without Default API Key:**
```
⚠️ Please enter your Gemini API Key to use AI features
[Enter Gemini API Key: ___________]
```

---

## 💻 For Local Development

### Option 1: Using Secrets (Recommended)

1. **Navigate to** `.streamlit/` folder in your project
2. **Copy** `secrets.toml.example` to `secrets.toml`:
   ```bash
   # In PowerShell
   Copy-Item .streamlit\secrets.toml.example .streamlit\secrets.toml
   ```
3. **Edit** `.streamlit/secrets.toml`:
   ```toml
   GOOGLE_API_KEY = "your-actual-api-key-here"
   ```
4. **Run the app**:
   ```bash
   streamlit run Temple_App.py
   ```
5. **Note**: `secrets.toml` is in `.gitignore` and won't be committed

### Option 2: Enter Key in the App

1. **Run the app** without configuring secrets:
   ```bash
   streamlit run Temple_App.py
   ```
2. **Enter your API key** in the sidebar when prompted
3. **Note**: You'll need to re-enter it each time you restart the app

---

## 🔒 Security Best Practices

### ✅ DO:
- Store API keys in Streamlit secrets (cloud) or `secrets.toml` (local)
- Keep `secrets.toml` in `.gitignore`
- Use environment-specific keys (dev vs production)
- Rotate keys periodically
- Monitor API usage in Google AI Studio

### ❌ DON'T:
- Commit API keys to Git
- Share API keys publicly
- Hardcode keys in your Python files
- Use production keys for testing
- Share your `secrets.toml` file

---

## 🧪 Testing API Key Configuration

### Test Locally with Secrets

1. Configure `.streamlit/secrets.toml` as shown above
2. Run: `streamlit run Temple_App.py`
3. Check sidebar - should show "✅ Default API Key Available"
4. Select a temple and click "Analyze Architecture with AI"
5. Should work without entering a key

### Test User Override

1. With secrets configured, run the app
2. Check "Use my own API key instead"
3. Enter a different API key
4. Should show "🔑 Using your custom API key"
5. Test the AI analysis feature

### Test Without Secrets

1. Rename or remove `.streamlit/secrets.toml`
2. Run the app
3. Should prompt for API key
4. Enter your key
5. Test the AI analysis feature

---

## 🐛 Troubleshooting

### Issue: "Default API Key Available" not showing

**Possible causes:**
- Secrets not configured in Streamlit Cloud
- Typo in secret key name (must be `GOOGLE_API_KEY`)
- App hasn't restarted after saving secrets

**Solution:**
1. Check secrets configuration in Streamlit Cloud
2. Ensure key name is exactly `GOOGLE_API_KEY`
3. Manually reboot the app

### Issue: "API Key Configured!" but AI analysis fails

**Possible causes:**
- Invalid API key
- API key quota exceeded
- Network issues
- Gemini API service down

**Solution:**
1. Verify API key is correct
2. Check quota in [Google AI Studio](https://aistudio.google.com/app/apikey)
3. Try a different API key
4. Check error message in the app

### Issue: Local secrets not working

**Possible causes:**
- File named incorrectly (must be `secrets.toml`, not `secrets.toml.example`)
- File not in `.streamlit/` folder
- TOML syntax error

**Solution:**
1. Verify file path: `.streamlit/secrets.toml`
2. Check TOML syntax (no quotes around key name, quotes around value)
3. Restart Streamlit app

---

## 📊 API Key Usage Patterns

### Pattern 1: Public Demo App
- **Setup**: Configure default API key in Streamlit Cloud
- **User Experience**: Works immediately, no setup needed
- **Use Case**: Demos, portfolios, public showcases
- **Cost**: You pay for all API usage

### Pattern 2: User-Provided Keys
- **Setup**: Don't configure default key
- **User Experience**: Users must get their own key
- **Use Case**: Apps with many users, cost-sensitive projects
- **Cost**: Users pay for their own usage

### Pattern 3: Hybrid (Current Implementation)
- **Setup**: Configure default key + allow override
- **User Experience**: Works immediately, but users can use their own
- **Use Case**: Best of both worlds
- **Cost**: You pay for default usage, users can opt to use their own

---

## 🎯 Recommended Setup

For your Tamil Temple Architecture AI app, we recommend **Pattern 3 (Hybrid)**:

1. **Configure a default API key** in Streamlit Cloud secrets
2. **Users can use the app immediately** without setup
3. **Power users can use their own keys** if they prefer
4. **Monitor your API usage** in Google AI Studio
5. **Set usage alerts** to avoid unexpected costs

---

## 📚 Additional Resources

- [Streamlit Secrets Documentation](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management)
- [Google AI Studio](https://aistudio.google.com/app/apikey)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Streamlit Security Best Practices](https://docs.streamlit.io/knowledge-base/deploy/authentication-without-sso)

---

## ✅ Quick Reference

### Streamlit Cloud Secrets Format
```toml
GOOGLE_API_KEY = "AIzaSy..."
```

### Local Secrets File Location
```
.streamlit/secrets.toml
```

### Check if Secrets Work
```python
# In your app or Python console
import streamlit as st
print(st.secrets["GOOGLE_API_KEY"])  # Should print your key
```

### Get Your API Key
[Google AI Studio → Create API Key](https://aistudio.google.com/app/apikey)

---

**Need help?** Check the troubleshooting section above or refer to the deployment workflow.
