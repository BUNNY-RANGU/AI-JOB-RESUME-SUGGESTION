# Vercel Deployment Guide

## Quick Deploy

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel:**
   ```bash
   vercel login
   ```

3. **Deploy:**
   ```bash
   vercel --prod
   ```

## Configuration

- **Runtime:** Python 3.11
- **Framework:** Streamlit
- **Entry Point:** frontend/app.py

## Environment Variables

No environment variables required for basic deployment.

## Troubleshooting

### Common Issues:

1. **Build fails:** Check requirements.txt is in root directory
2. **App doesn't load:** Verify frontend/app.py exists
3. **Static files missing:** Check .vercelignore configuration

### Local Testing:

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run frontend/app.py
```

## Post-Deployment

Your app will be available at: `https://your-project-name.vercel.app`
