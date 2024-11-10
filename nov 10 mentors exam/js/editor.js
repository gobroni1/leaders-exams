// Import the functions you need from the SDKs you need
import { getFirestore, doc, updataDoc, getDocs, collection } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js";
import { getAuth, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-auth.js";
import { initializeApp} from "https://www.gstatic.com/firebasejs/10.13.0/firebase-firestore-app.js";

//  SDK  = software development kit ()

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
const auth = getAuth(app);
const db = getFirestore(app);


onAuthStateChanged(auth, (user) => {
    if (user) {
        if (user.email === "admin@gmail.com" || user.email === "gobronitsitlauri12@gmail.com"){
            console.log("welcome in admin!");
            loadUserData();
        }else {
            alert("nah, you ain't admin");
            window.location.href="../html/stats.html";
        }
    }else {
        window.location.href = "./index.html"
    }
});