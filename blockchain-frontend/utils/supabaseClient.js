import { createClient } from '@supabase/supabase-js'; //this is the library that we will use to interact with Supabase

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL; // this is the URL that we will use to connect to Supabase
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

export const supabase = createClient(supabaseUrl, supabaseAnonKey); //this is the client that we will use to interact with Supabase
// it also allows us to interact with the database and the storage