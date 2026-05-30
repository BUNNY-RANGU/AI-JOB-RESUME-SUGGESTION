<div align="center">

# AI Career and Opportunity Navigator

AI-powered career intelligence platform for resume parsing, job matching, skill-gap analysis, and opportunity recommendations.

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-app-red)](https://streamlit.io)
[![FastAPI](https://img.shields.io/badge/FastAPI-backend-green)](https://fastapi.tiangolo.com)
[![Deploy](https://img.shields.io/badge/deploy-Vercel%20%7C%20Docker-black)](#deployment)

</div>

## Overview

AI Career and Opportunity Navigator is a career assistant that analyzes resumes, detects skills, suggests career paths, recommends improvements, and matches users with relevant job opportunities.

It is designed for students, freshers, and early-career developers who want a clear roadmap from current skills to better job opportunities.

## Features

| Feature | What It Does |
|---|---|
| Resume Parsing | Reads resumes and extracts skills, profile data, and experience signals |
| Career Intelligence | Scores AI readiness and suggests practical career paths |
| Job Matching | Filters opportunities by skills, experience, work mode, and role type |
| Skill Gap Analysis | Shows missing skills for target roles |
| Interview Practice | Includes interview simulation modules |
| Smart Alerts | Supports job alerts and notifications |
| Gamification | Adds progress and motivation features |

## Tech Stack

- Python
- Streamlit
- FastAPI
- PyPDF2
- Pandas and NumPy
- Docker
- Vercel configuration

## Project Structure

```text
AI-JOB-RESUME-SUGGESTION/
  backend/              AI matching, auth, parsing, alerts, interview modules
  frontend/             Streamlit UI
  feed_ui.py            Main feed experience
  gamification.py       Progress and engagement logic
  one_click_apply.py    Application workflow helper
  smart_notifications.py
  requirements.txt
```

## Run Locally

```bash
git clone https://github.com/BUNNY-RANGU/AI-JOB-RESUME-SUGGESTION.git
cd AI-JOB-RESUME-SUGGESTION
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run feed_ui.py
```

## Deployment

The repository includes Docker and Vercel configuration files. Choose the target based on how you want to host the app:

- Vercel for lightweight web deployment
- Docker for portable backend/app packaging
- Streamlit Community Cloud for Streamlit-first hosting

## Screenshots

Add updated screenshots here as the UI evolves:

```md
![Dashboard](docs/dashboard.png)
```

## Author

Built by [Rangu Suchandra](https://github.com/BUNNY-RANGU).
