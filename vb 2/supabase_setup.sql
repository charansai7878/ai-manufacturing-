-- Run this SQL in your Supabase SQL Editor to set up the database

-- Create the 'users' table
CREATE TABLE IF NOT EXISTS users (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    fullname TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Enable RLS (Optional but recommended)
-- ALTER TABLE users ENABLE ROW LEVEL SECURITY;

-- Note: Since this app uses a Service Key or Anon Key with full access to 'users' for simplicity,
-- you might want to adjust policies if you plan to scale.
