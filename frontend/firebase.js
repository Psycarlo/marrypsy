import { firebase } from "@firebase/app";
import "@firebase/auth";
import "@firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyCNTnTNHz4ZMG4y55P7-C4ch1gJyUj6EwM",
  authDomain: "marrypsy-34678.firebaseapp.com",
  projectId: "marrypsy-34678",
  storageBucket: "marrypsy-34678.appspot.com",
  messagingSenderId: "1052120316456",
  appId: "1:1052120316456:web:62b13bd2dd0e56f028d31d",
  measurementId: "G-27J44BFYVN"
};
firebase.initializeApp(firebaseConfig);

const db = firebase.firestore();
const auth = firebase.auth();

export { db, auth };
