import { db } from "../firebase/config";
import { 
  collection, 
  doc, 
  setDoc, 
  getDoc, 
  onSnapshot, 
  serverTimestamp 
} from "firebase/firestore";
import topicsData from "../data/topics.json";

const LOCAL_STORAGE_LESSONS_KEY = "axomrank_cached_lessons";
const LOCAL_STORAGE_USER_KEY = "axomrank_collaborator_name";

/**
 * Gets collaborator name
 */
export function getCollaboratorName() {
  return localStorage.getItem(LOCAL_STORAGE_USER_KEY) || "";
}

export function setCollaboratorName(name) {
  if (name) {
    localStorage.setItem(LOCAL_STORAGE_USER_KEY, name.trim());
  }
}

/**
 * Get all topics from the static checklist
 */
export function getAllTopics() {
  return topicsData;
}

/**
 * Local cache helpers
 */
function getLocalLessons() {
  try {
    const raw = localStorage.getItem(LOCAL_STORAGE_LESSONS_KEY);
    return raw ? JSON.parse(raw) : {};
  } catch (e) {
    console.warn("Failed to read local lessons:", e);
    return {};
  }
}

function saveLocalLesson(topicId, lessonData) {
  try {
    const local = getLocalLessons();
    local[topicId] = {
      ...lessonData,
      _localUpdated: Date.now(),
    };
    localStorage.setItem(LOCAL_STORAGE_LESSONS_KEY, JSON.stringify(local));
  } catch (e) {
    console.warn("Failed to write to local lessons cache:", e);
  }
}

/**
 * Creates default lesson structure for a topic
 */
export function createEmptyLesson(topic) {
  return {
    topicId: topic.id,
    topicTitle: topic.subSubtopic || topic.subtopic || topic.topic,
    domain: topic.domain,
    subject: topic.subject,
    topic: topic.topic,
    subtopic: topic.subtopic,
    subSubtopic: topic.subSubtopic,
    status: "not_started", // not_started | drafting | ready
    updatedBy: getCollaboratorName() || "Anonymous",
    updatedAt: new Date().toISOString(),
    learningCards: [
      {
        id: "lc_1",
        title: topic.subSubtopic || topic.subtopic || topic.topic,
        conceptText: "",
        highlights: [""],
        keyAreas: [""],
        imageUrl: "",
      }
    ],
    flashcards: [
      {
        id: "fc_1",
        coreStatement: "",
        keyPoints: [""],
        imageUrl: "",
      }
    ],
    quizzes: [
      {
        id: "qz_1",
        question: "",
        options: ["", "", "", ""],
        correctIndex: 0,
        explanation: "",
        imageUrl: "",
      }
    ],
    matches: [
      { id: "m_1", leftText: "", rightText: "" },
      { id: "m_2", leftText: "", rightText: "" },
      { id: "m_3", leftText: "", rightText: "" },
      { id: "m_4", leftText: "", rightText: "" },
    ],
  };
}

/**
 * Subscribes to all lessons from Firestore with local fallback
 */
export function subscribeToAllLessons(onUpdate, onError) {
  const localCache = getLocalLessons();
  onUpdate(localCache);

  try {
    const lessonsCol = collection(db, "lessons");
    const unsubscribe = onSnapshot(
      lessonsCol,
      (snapshot) => {
        const remoteLessons = { ...getLocalLessons() };
        snapshot.forEach((docSnap) => {
          remoteLessons[docSnap.id] = docSnap.data();
        });
        localStorage.setItem(LOCAL_STORAGE_LESSONS_KEY, JSON.stringify(remoteLessons));
        onUpdate(remoteLessons);
      },
      (err) => {
        console.warn("Firestore real-time sync warning (fallback to local):", err.message);
        if (onError) onError(err);
      }
    );
    return unsubscribe;
  } catch (err) {
    console.warn("Firestore not available yet, using local store:", err);
    return () => {};
  }
}

/**
 * Saves a lesson to Firestore & local cache
 */
export async function saveLesson(topicId, lessonData) {
  const author = getCollaboratorName() || "Collaborator";
  const updatedData = {
    ...lessonData,
    topicId,
    updatedBy: author,
    updatedAt: new Date().toISOString(),
  };

  // Always save locally first
  saveLocalLesson(topicId, updatedData);

  // Then sync with Firestore
  try {
    const docRef = doc(db, "lessons", topicId);
    await setDoc(docRef, {
      ...updatedData,
      serverTime: serverTimestamp(),
    }, { merge: true });
    return { success: true, synced: true };
  } catch (err) {
    console.warn("Firestore save failed, stored in local cache:", err.message);
    return { success: true, synced: false, error: err.message };
  }
}

/**
 * Export all lessons as JSON file
 */
export function exportAllLessonsJSON() {
  const lessons = getLocalLessons();
  const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(lessons, null, 2));
  const downloadAnchor = document.createElement("a");
  downloadAnchor.setAttribute("href", dataStr);
  downloadAnchor.setAttribute("download", `axomrank_lessons_backup_${new Date().toISOString().split("T")[0]}.json`);
  document.body.appendChild(downloadAnchor);
  downloadAnchor.click();
  downloadAnchor.remove();
}

/**
 * Import lessons from JSON
 */
export async function importLessonsJSON(jsonString) {
  try {
    const parsed = JSON.parse(jsonString);
    const existing = getLocalLessons();
    const merged = { ...existing, ...parsed };
    localStorage.setItem(LOCAL_STORAGE_LESSONS_KEY, JSON.stringify(merged));

    // Try batch pushing to Firestore if available
    for (const [topicId, data] of Object.entries(parsed)) {
      try {
        const docRef = doc(db, "lessons", topicId);
        await setDoc(docRef, data, { merge: true });
      } catch (e) {
        // Continue silently on error
      }
    }
    return { success: true, count: Object.keys(parsed).length };
  } catch (err) {
    throw new Error("Invalid JSON file: " + err.message);
  }
}
