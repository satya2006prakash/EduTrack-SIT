-- ============================================================
--  EduTrack SIT  –  Supabase student_data table migration
--  Run this in your Supabase project → SQL Editor
-- ============================================================

-- 1. Create the table if it doesn't exist yet
CREATE TABLE IF NOT EXISTS public.student_data (
  id            UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  full_name     TEXT,
  usn           TEXT,
  courses       JSONB        DEFAULT '[]'::jsonb,
  branch        TEXT,
  semester      TEXT,
  cgpa_prior    NUMERIC(4,2),
  cgpa_credits  INTEGER,
  updated_at    TIMESTAMPTZ  DEFAULT now()
);

-- 2. Add any missing columns to an existing table (safe to run multiple times)
ALTER TABLE public.student_data ADD COLUMN IF NOT EXISTS branch        TEXT;
ALTER TABLE public.student_data ADD COLUMN IF NOT EXISTS semester      TEXT;
ALTER TABLE public.student_data ADD COLUMN IF NOT EXISTS cgpa_prior    NUMERIC(4,2);
ALTER TABLE public.student_data ADD COLUMN IF NOT EXISTS cgpa_credits  INTEGER;
ALTER TABLE public.student_data ADD COLUMN IF NOT EXISTS full_name     TEXT;
ALTER TABLE public.student_data ADD COLUMN IF NOT EXISTS usn           TEXT;

-- 3. Enable Row-Level Security (RLS) so each user can only see their own row
ALTER TABLE public.student_data ENABLE ROW LEVEL SECURITY;

-- 4. Policy: users can read their own row
DROP POLICY IF EXISTS "Users can read own data" ON public.student_data;
CREATE POLICY "Users can read own data"
  ON public.student_data
  FOR SELECT
  USING (auth.uid() = id);

-- 5. Policy: users can insert/update their own row
DROP POLICY IF EXISTS "Users can upsert own data" ON public.student_data;
CREATE POLICY "Users can upsert own data"
  ON public.student_data
  FOR ALL
  USING (auth.uid() = id)
  WITH CHECK (auth.uid() = id);

-- Done! ✅
