import React, { useState, useEffect, useMemo, useCallback } from "react";
import Navbar from "./components/Navbar";
import TopicSidebar from "./components/TopicSidebar";
import StageEditor from "./components/StageEditor";
import MobileSimulator from "./components/MobileSimulator";
import NameModal from "./components/NameModal";
import SettingsModal from "./components/SettingsModal";
import { 
  getAllTopics, 
  getCollaboratorName, 
  createEmptyLesson, 
  saveLesson, 
  subscribeToAllLessons 
} from "./services/courseService";
import { Check, AlertCircle } from "lucide-react";

export default function App() {
  const [topics] = useState(() => getAllTopics());
  const [selectedTopic, setSelectedTopic] = useState(() => topics[0] || null);
  const [lessonsMap, setLessonsMap] = useState({});
  const [activeLesson, setActiveLesson] = useState(null);
  const [isSaving, setIsSaving] = useState(false);
  const [syncStatus, setSyncStatus] = useState(null);
  const [toast, setToast] = useState(null);

  // Layout View mode: "split" | "editor" | "preview"
  const [previewMode, setPreviewMode] = useState("split");

  // Collaborator & Modals
  const [collaboratorName, setCollaboratorNameState] = useState(() => getCollaboratorName());
  const [isNameModalOpen, setIsNameModalOpen] = useState(() => !getCollaboratorName());
  const [isSettingsModalOpen, setIsSettingsModalOpen] = useState(false);

  // Show toast notification
  const showToast = useCallback((msg, type = "success") => {
    setToast({ msg, type });
    setTimeout(() => setToast(null), 3000);
  }, []);

  // Subscribe to real-time lessons
  useEffect(() => {
    const unsub = subscribeToAllLessons(
      (updatedMap) => {
        setLessonsMap(updatedMap);
      },
      (err) => {
        console.warn("Real-time listener warning:", err);
      }
    );
    return () => unsub();
  }, []);

  // When selectedTopic or lessonsMap changes, load or initialize the active lesson
  useEffect(() => {
    if (!selectedTopic) return;
    const existing = lessonsMap[selectedTopic.id];
    if (existing) {
      setActiveLesson(JSON.parse(JSON.stringify(existing)));
    } else {
      setActiveLesson(createEmptyLesson(selectedTopic));
    }
  }, [selectedTopic?.id]);

  // Handle Save
  const handleSaveLesson = async () => {
    if (!activeLesson || !selectedTopic) return;
    setIsSaving(true);
    try {
      const res = await saveLesson(selectedTopic.id, activeLesson);
      setSyncStatus(res);
      setLessonsMap((prev) => ({
        ...prev,
        [selectedTopic.id]: activeLesson,
      }));
      showToast(
        res.synced ? "Lesson saved & synced to cloud!" : "Lesson saved locally! (Cloud offline)",
        res.synced ? "success" : "warning"
      );
    } catch (err) {
      showToast("Failed to save lesson: " + err.message, "error");
    } finally {
      setIsSaving(false);
    }
  };

  // Move to next topic in syllabus
  const handleNextTopic = () => {
    if (!selectedTopic) return;
    const currentIndex = topics.findIndex((t) => t.id === selectedTopic.id);
    if (currentIndex !== -1 && currentIndex < topics.length - 1) {
      setSelectedTopic(topics[currentIndex + 1]);
      showToast(`Loaded Topic #${currentIndex + 2}: ${topics[currentIndex + 1].subSubtopic || topics[currentIndex + 1].topic}`);
    } else {
      showToast("🎉 You've reached the end of the syllabus checklist!");
    }
  };

  // Syllabus stats
  const stats = useMemo(() => {
    let drafting = 0;
    let ready = 0;
    Object.values(lessonsMap).forEach((les) => {
      if (les.status === "ready") ready++;
      else if (les.status === "drafting") drafting++;
    });
    return {
      total: topics.length,
      drafting,
      ready,
    };
  }, [topics, lessonsMap]);

  return (
    <div className="min-h-screen bg-slate-100 flex flex-col font-sans text-slate-800">
      {/* Top Navbar */}
      <Navbar
        collaboratorName={collaboratorName}
        onEditName={() => setIsNameModalOpen(true)}
        onOpenSettings={() => setIsSettingsModalOpen(true)}
        previewMode={previewMode}
        setPreviewMode={setPreviewMode}
        stats={stats}
      />

      {/* Main Workspace Layout */}
      <div className="flex-1 flex overflow-hidden">
        {/* Left: Syllabus Topics Sidebar */}
        <TopicSidebar
          topics={topics}
          selectedTopic={selectedTopic}
          onSelectTopic={(topic) => setSelectedTopic(topic)}
          lessonsMap={lessonsMap}
        />

        {/* Center: Stage Content Editor */}
        {(previewMode === "split" || previewMode === "editor") && (
          <StageEditor
            lesson={activeLesson}
            onChangeLesson={setActiveLesson}
            onSaveLesson={handleSaveLesson}
            isSaving={isSaving}
            syncStatus={syncStatus}
          />
        )}

        {/* Right: Live Interactive Mobile Phone Simulator */}
        {(previewMode === "split" || previewMode === "preview") && (
          <div
            className={`bg-slate-200/50 p-6 flex flex-col items-center justify-start overflow-y-auto ${
              previewMode === "split"
                ? "hidden xl:flex w-[430px] border-l border-slate-200 shrink-0"
                : "flex-1"
            }`}
          >
            <div className="text-center mb-3">
              <h3 className="text-xs font-bold uppercase tracking-wider text-slate-600">
                Live AxomRank Journey Preview
              </h3>
              <p className="text-[11px] text-slate-400">
                Test the 4-step micro-learning flow live as you build
              </p>
            </div>

            <MobileSimulator
              lesson={activeLesson}
              onNextTopic={handleNextTopic}
            />
          </div>
        )}
      </div>

      {/* Floating Toast notification */}
      {toast && (
        <div
          className={`fixed bottom-6 right-6 z-50 px-4 py-3 rounded-2xl shadow-xl border text-xs font-semibold flex items-center gap-2 animate-in slide-in-from-bottom duration-200 ${
            toast.type === "success"
              ? "bg-slate-900 text-white border-slate-800 shadow-slate-900/30"
              : toast.type === "warning"
              ? "bg-amber-50 text-amber-900 border-amber-300"
              : "bg-rose-50 text-rose-900 border-rose-300"
          }`}
        >
          {toast.type === "success" ? (
            <Check className="w-4 h-4 text-emerald-400" />
          ) : (
            <AlertCircle className="w-4 h-4 text-amber-500" />
          )}
          <span>{toast.msg}</span>
        </div>
      )}

      {/* Modals */}
      <NameModal
        isOpen={isNameModalOpen}
        onClose={() => setIsNameModalOpen(false)}
        currentName={collaboratorName}
        onNameSaved={(name) => {
          setCollaboratorNameState(name);
          showToast(`Welcome, ${name}!`);
        }}
      />

      <SettingsModal
        isOpen={isSettingsModalOpen}
        onClose={() => setIsSettingsModalOpen(false)}
        onLessonsReloaded={() => {
          showToast("Lessons reloaded from backup!");
        }}
      />
    </div>
  );
}
