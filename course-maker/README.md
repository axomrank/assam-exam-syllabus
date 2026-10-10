# AxomRank Studio — Course & Lesson Plan Creator

> **Live Deployment:** [https://axomrank-dev.web.app](https://axomrank-dev.web.app)  
> **Firebase Project:** `axomrank-bf44f`  
> **Preloaded Syllabus:** 842 topics from `MAster_topics_checklist.csv`

---

## 🚀 Key Features

1. **Anonymous Collaborator Entry:**
   - On first visit, simply type your name (e.g. *Angsuman*).
   - Edits are automatically tagged with the author's name (`updatedBy`).

2. **Master Syllabus Explorer:**
   - Search across all 842 topics, subtopics, eras, and dynasties.
   - Filter by Domain (History, Geography, Polity, Economy, Aptitude, English, Science) and toggle **Assam Specific Only**.
   - Track progress with `Not Started`, `Drafting`, and `Ready` status badges.

3. **4-Stage Micro-Learning Lesson Plan Editor:**
   - **Stage 1 (Learning Feed):** Title, bite-sized explanatory text, key areas explored tags, and ImgBB visual.
   - **Stage 2 (Flashcards):** Bold core statement, active recall key points list, and ImgBB visual.
   - **Stage 3 (Quiz MCQs):** Single-choice question, 4 options, radio selector for correct answer, instant explanation, and ImgBB visual.
   - **Stage 4 (Match the Following):** Column A $\leftrightarrow$ Column B pairs for the topic capstone activity.

4. **Live Interactive Mobile Simulator:**
   - Side-by-side or full-screen iPhone preview matching the AxomRank layout.
   - Interactive feeds, swipeable flashcards (*"I Know This"* vs *"Revise Again"*), clickable quiz with instant feedback, interactive matching columns, and confetti celebration upon topic completion.

5. **Direct ImgBB Cloud Hosting:**
   - Pre-configured with API Key: `783e3b5d9b1ee7702c93d32027671ae6`.
   - Drag & drop or file picker direct upload, or paste direct URLs.
   - Configurable anytime via the in-app **Settings** modal.

6. **Backup & Cloud Sync:**
   - Instant 1-click **Export JSON Backup** and **Import JSON**.
   - Offline-friendly local storage cache ensures 0 data loss.

---

## ⚡ Two 1-Click Firebase Console Steps for Real-Time Sync

To enable live real-time sync between devices:
1. **Enable Firestore Database:**
   👉 [Create Firestore Database](https://console.firebase.google.com/project/axomrank-bf44f/firestore) (Select location e.g. `asia-south1` or `us-central1` and start in Test Mode).
2. **Enable Anonymous Auth:**
   👉 [Enable Anonymous Authentication](https://console.firebase.google.com/project/axomrank-bf44f/authentication/providers) (Click "Anonymous" and turn the switch ON).

---

## 💻 Local Development & Deployment Commands

```bash
# Navigate to course-maker
cd course-maker

# Run local dev server
npm run dev

# Build for production
npm run build

# Deploy to axomrank-dev.web.app
firebase deploy --only hosting:axomrank-dev
```
