import { initializeApp } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js";
import { getFirestore, doc, updateDoc, getDoc } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-firestore.js";
import { getAuth, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-auth.js";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyDEAPy9N1ELyfUj2v2_-hGFdlrsM96mqow",
    authDomain: "internet-bank-v2.firebaseapp.com",
    projectId: "internet-bank-v2",
    storageBucket: "internet-bank-v2.appspot.com",
    messagingSenderId: "745458432351",
    appId: "1:745458432351:web:1fb4ce86a9af7624269eea"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore();
const auth = getAuth();

document.getElementById('submitLoan').addEventListener('click', async () => {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const cardNumber = document.getElementById('card').value;
    const loanAmount = parseFloat(document.getElementById('loanAmount').value);

    console.log('Button clicked');
    console.log('Email:', email);
    console.log('Password:', password);
    console.log('Card Number:', cardNumber);
    console.log('Loan Amount:', loanAmount);

    if (email && password && cardNumber && !isNaN(loanAmount) && loanAmount > 0) {
        try {
            // Authenticate user
            const userCredential = await signInWithEmailAndPassword(auth, email, password);
            const user = userCredential.user;
            console.log('User authenticated:', user);

            // Retrieve user document
            const usersRef = doc(db, "users", user.uid);
            const userDoc = await getDoc(usersRef);

            if (userDoc.exists()) {
                const userData = userDoc.data();
                console.log('User Data:', userData);
                if (userData.cardNumber === cardNumber) {
                    const newBalance = (userData.balance || 0) + loanAmount;
                    await updateDoc(usersRef, { balance: newBalance });
                    alert('Loan amount added to your balance.');
                } else {
                    alert('Card number does not match.');
                }
            } else {
                alert('User document not found.');
            }
        } catch (error) {
            console.error('Error updating balance:', error);
            alert('Failed to update balance. Please check your email and password, and try again.');
        }
    } else {
        alert('Please fill out all fields with valid information.');
    }
});
