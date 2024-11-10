import { initializeApp } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js";
import { getFirestore, doc, updateDoc, getDoc, query, where, collection, getDocs } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-firestore.js";
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

document.getElementById('submitTransfer').addEventListener('click', async () => {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const receiverEmail = document.getElementById('receiverEmail').value.trim(); // Trim spaces
    const transferAmount = parseFloat(document.getElementById('transferAmount').value);

    console.log('Button clicked');
    console.log('Email:', email);
    console.log('Password:', password);
    console.log('Receiver Email:', receiverEmail);
    console.log('Transfer Amount:', transferAmount);

    if (email && password && receiverEmail && !isNaN(transferAmount) && transferAmount > 0) {
        try {
            // Authenticate user
            console.log('Attempting to authenticate user...');
            const userCredential = await signInWithEmailAndPassword(auth, email, password);
            const user = userCredential.user;
            console.log('User authenticated:', user);

            // Retrieve sender's document
            const senderRef = doc(db, "users", user.uid);
            console.log('Retrieving sender document...');
            const senderDoc = await getDoc(senderRef);

            if (senderDoc.exists()) {
                const senderData = senderDoc.data();
                console.log('Sender Data:', senderData);

                // Check if sender has sufficient balance
                if ((senderData.balance || 0) >= transferAmount) {
                    // Retrieve receiver's document
                    console.log('Retrieving receiver document with email:', receiverEmail);
                    const receiverQuery = query(collection(db, "users"), where("email", "==", receiverEmail));
                    const receiverSnapshot = await getDocs(receiverQuery);

                    if (!receiverSnapshot.empty) {
                        const receiverDoc = receiverSnapshot.docs[0];
                        const receiverData = receiverDoc.data();
                        console.log('Receiver Data:', receiverData);

                        // Proceed with balance update
                        const newSenderBalance = (senderData.balance || 0) - transferAmount;
                        const newReceiverBalance = (receiverData.balance || 0) + transferAmount;

                        // Update both sender's and receiver's documents
                        console.log('Updating sender balance...');
                        await updateDoc(senderRef, { balance: newSenderBalance });
                        console.log('Updating receiver balance...');
                        await updateDoc(receiverDoc.ref, { balance: newReceiverBalance });

                        alert('Transfer successful!');
                    } else {
                        console.log('Receiver email not found.');
                        alert('Receiver email not found.');
                    }
                } else {
                    console.log('Insufficient balance.');
                    alert('Insufficient balance.');
                }
            } else {
                console.log('Sender account not found.');
                alert('Sender account not found.');
            }
        } catch (error) {
            console.error('Error processing transfer:', error);
            alert('Failed to process transfer. Please check your credentials and try again.');
        }
    } else {
        alert('Please fill out all fields with valid information.');
    }
});
    