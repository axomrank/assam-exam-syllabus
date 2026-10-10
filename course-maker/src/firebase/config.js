import { initializeApp, getApps } from "firebase/app";
import { getAuth, signInAnonymously, onAuthStateChanged } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

export const firebaseConfig = {
  projectId: "axomrank-bf44f",
  appId: "1:165830985021:web:657ad33e1af91734feb154",
  storageBucket: "axomrank-bf44f.firebasestorage.app",
  apiKey: "AIzaSyBFh1K3n-gGvdCl53hzG1QdkH5QiNOCEL4",
  authDomain: "axomrank-bf44f.firebaseapp.com",
  messagingSenderId: "165830985021",
  measurementId: "G-C4ZX5DB1G3",
  projectNumber: "165830985021",
};

const app = getApps().length > 0 ? getApps()[0] : initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);

export { signInAnonymously, onAuthStateChanged };
export default app;
