import { useEffect, useState } from 'react';
import { supabase } from '../utils/supabaseClient';
import { useRouter } from 'next/router';

export default function Dashboard(){
    const [user, setUser] = useState(null); // this is the user that we will use to store the user data
    const router = useRouter(); // this is the router that we will use to navigate between pages

    useEffect(() => {
        const fetchUser = async () => {
            const { data } = await supabase.auth.getUser(); // this is the function that we will use to get the user data
            if (!data){
                router.push('/auth'); // if there is no user data, we will navigate the user to the auth page
            }
            else{
                setUser(data.user);
            }
        };
        fetchUser(); // this is the function that we will use to fetch the user data
    }, []);

    const handleLogout = async () => {
        await supabase.auth.signOut(); // this is the function that we will use to sign out the user
        router.push('/auth'); // this is the function that we will use to navigate the user to the auth page
    };

    return user ? (
        <div>
            <h2>Welcome, {user.email}!</h2>
            <button onClick={handleLogout}>Logout</button>
        </div>
    ) : (
        <p>Loading...</p> // if the user is not loaded, we will display a loading message
    );
}