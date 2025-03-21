import { useState } from 'react';
import { supabase } from '../utils/supabaseClient';
import { useRouter } from 'next/router';

export default function Auth() {
    const [email, setEmail] = useState(""); //this is the email that the user will use to sign in
    const [password, setPassword] = useState(""); //this is the password that the user will use to sign in
    const router = useRouter(); // this is the router that we will use to navigate between pages

    const handleSignup = async () => {
        const {error} = await supabase.auth.signUp({ email, password }); //this is the function that we will use to sign up the user
        if (error){
            alert(error.message); //if there is an error, we will alert the user
        }
        else{
            alert("Check your email for a confirmation link!"); //if there is no error, we will alert the user to check their email
        }
        
    };

    const handleLogin = async () => {
        const {error} = await supabase.auth.signInWithPassword({ email, password }); //this is the function that we will use to sign in the user
        if (error){
            alert(error.message); //if there is an error, we will alert the user
        }
        else{
            router.push("/dashboard"); //if there is no error, we will navigate the user to the dashboard
        }
    };

    return (
        <div>
            <h2> Sign-Up / Login</h2>
            <input type="email" placeholder="Email" onChange={(e) => setEmail(e.target.value)} /> 
            <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
            <button onClick={handleSignup}>Sign-Up</button>
            <button onClick={handleLogin}>Login</button>
        </div>
    );

}