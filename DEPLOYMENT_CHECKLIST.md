# 🚀 Streamlit Cloud Deployment Checklist

Quick reference guide for deploying your Tamil Temple Architecture AI app.

## ✅ Pre-Deployment Checklist

- [ ] App runs locally without errors (`streamlit run Temple_App.py`)
- [ ] All dependencies are in `requirements.txt`
- [ ] Code is committed to Git
- [ ] Repository is pushed to GitHub
- [ ] Repository is **PUBLIC** (required for free tier)
- [ ] You have a GitHub account
- [ ] You have signed up for Streamlit Community Cloud

## 📋 Deployment Steps (Quick Version)

1. **Go to**: [share.streamlit.io](https://share.streamlit.io)
2. **Sign in** with GitHub
3. **Click** "New app"
4. **Select**:
   - Your repository
   - Branch: `main`
   - Main file: `Temple_App.py`
5. **Click** "Deploy!"
6. **Wait** 2-5 minutes for deployment
7. **Configure Secrets** (Recommended):
   - Go to app settings → Secrets
   - Add: `GOOGLE_API_KEY = "your-api-key"`
   - Click Save
8. **Get** your public URL (e.g., `your-app.streamlit.app`)

## 🔑 API Key Options

Your app now supports **flexible API key usage**:

### ✅ With Default API Key (Recommended)
- Configure `GOOGLE_API_KEY` in Streamlit Cloud secrets
- Users can use the app immediately
- Users can still override with their own key if desired

### 🔓 Without Default API Key
- Users must enter their own Gemini API key
- They can get one free from [Google AI Studio](https://aistudio.google.com/app/apikey)


## 🔗 Important Links

- **Streamlit Cloud**: https://share.streamlit.io
- **Full Workflow**: See `.agent/workflows/deploy-streamlit-cloud.md`
- **Documentation**: https://docs.streamlit.io/streamlit-community-cloud

## 📝 Current Project Status

### Files Ready for Deployment:
- ✅ `Temple_App.py` - Main application
- ✅ `temple_data.py` - Temple data
- ✅ `requirements.txt` - Dependencies
- ✅ `README.md` - Project documentation
- ✅ `.gitignore` - Git ignore rules

### Required Dependencies:
```
streamlit
google-generativeai
python-dotenv
```

## 🎯 Next Steps

1. **Open GitHub Desktop**
2. **Ensure all changes are committed**
3. **Push to GitHub** (click "Push origin")
4. **Verify repository is public** on GitHub.com
5. **Follow deployment steps** above

## 💡 Tips

- Users will enter their own Gemini API key in the app
- App will auto-update when you push to GitHub
- Check logs in Streamlit Cloud if issues occur
- Free tier includes unlimited public apps!

## 🆘 Need Help?

Run the command: `/deploy-streamlit-cloud` to see the full detailed workflow.
