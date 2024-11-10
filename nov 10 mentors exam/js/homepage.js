// homepage.js
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js";
import { getAuth, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-auth.js";
import { getFirestore, getDoc, doc } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-firestore.js";

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

const auth = getAuth();
const db = getFirestore();

onAuthStateChanged(auth, (user) => {
    if (user) {
        const docRef = doc(db, "users", user.uid);
        getDoc(docRef)
            .then((docSpan) => {
                if (docSpan.exists()) {
                    const userData = docSpan.data();
                    document.getElementById('loggedUserFName').innerText = userData.firstName;
                    document.getElementById('loggedUserLName').innerText = userData.lastName;
                    document.getElementById('loggedUserEmail').innerText = userData.email;
                    document.getElementById('card').innerText = userData.cardNumber;
                    document.getElementById('balance').innerText = userData.balance;    
                } else {
                    console.log('No document found matching ID');
                }
            })
            .catch((error) => {
                console.log("Error getting document:", error);
            });
    } else {
        console.log("User not found");
    }
});

const logoutButton = document.getElementById('logout');
logoutButton.addEventListener('click', () => {
    signOut(auth)
        .then(() => {
            localStorage.removeItem('loggedInUserId');
            window.location.href = 'index.html';
        })
        .catch((error) => {
            console.error('Error signing out:', error);
        });

});

const deleteButton = document.getElementById('logout');
deleteButton.addEventListener('click', () => {
    signOut(auth)
        .then(() => {
            localStorage.deleteItem('loggedInUserId');
            window.location.href = 'index.html';
        })
        .catch((error) => {
            console.error('Error deleting Account:', error);
        });
});