// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.7.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.7.0/firebase-analytics.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDjgSZ63OUKKOlG0NO2FqIFq1hGuTlvNco",
  authDomain: "cardenas-reports-backend.firebaseapp.com",
  databaseURL: "https://cardenas-reports-backend-default-rtdb.firebaseio.com",
  projectId: "cardenas-reports-backend",
  storageBucket: "cardenas-reports-backend.appspot.com",
  messagingSenderId: "671598383327",
  appId: "1:671598383327:web:9969ca7a9936a50220996a",
  measurementId: "G-LSYSGVNW6J"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);