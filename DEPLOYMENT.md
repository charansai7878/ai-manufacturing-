# Deployment Guide: Vercel + Supabase

Follow these steps to deploy your Industrial Nexus application.

## 1. Supabase Setup
1.  Create a new project on [Supabase](https://supabase.com/).
2.  In your project dashboard, go to the **SQL Editor**.
3.  Paste the contents of `supabase_setup.sql` (found in this folder) and run it. This creates the `users` table.
4.  Go to **Project Settings** > **API**.
5.  Copy your **Project URL** and **anon public Key**.

## 2. Vercel Deployment
1.  Push your code to a GitHub/GitLab/Bitbucket repository.
2.  Import the project to [Vercel](https://vercel.com/).
3.  In the **Environment Variables** section during configuration, add the following:
    *   `GROQ_API_KEY`: Your Groq API key.
    *   `SUPABASE_URL`: Your Supabase Project URL.
    *   `SUPABASE_KEY`: Your Supabase anon Key.
    *   `FLASK_SECRET_KEY`: A random secret string for sessions.
4.  Click **Deploy**.

## 3. Local Testing
If you want to test locally with Supabase:
1.  Update your local `.env` file with the Supabase credentials.
2.  Install the new dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the app:
    ```bash
    python src/app.py
    ```

Note: The `users.db` file is no longer used and can be deleted.
