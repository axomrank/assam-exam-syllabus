import React, { useState } from "react";
import { 
  BookOpen, 
  HelpCircle, 
  Shuffle, 
  Layers, 
  Plus, 
  Trash2, 
  Save, 
  CheckCircle, 
  Clock, 
  AlertCircle,
  Sparkles,
  ArrowRight,
  MoveUp,
  MoveDown
} from "lucide-react";
import ImageUploader from "./ImageUploader";

export default function StageEditor({ 
  lesson, 
  onChangeLesson, 
  onSaveLesson, 
  isSaving,
  syncStatus 
}) {
  const [activeTab, setActiveTab] = useState("learning"); // learning | flashcards | quizzes | match

  if (!lesson) {
    return (
      <div className="flex-1 flex flex-col items-center justify-center p-8 text-center text-slate-400">
        <Layers className="w-12 h-12 mb-3 text-slate-300 animate-pulse" />
        <h3 className="text-base font-semibold text-slate-700">No Topic Selected</h3>
        <p className="text-xs text-slate-500 max-w-sm mt-1">
          Pick any topic from the left sidebar to start drafting learning cards, flashcards, quizzes, and match exercises.
        </p>
      </div>
    );
  }

  // --- Handlers for Learning Cards ---
  const handleAddLearningCard = () => {
    const newCards = [
      ...lesson.learningCards,
      {
        id: `lc_${Date.now()}`,
        title: "",
        conceptText: "",
        highlights: [""],
        keyAreas: [""],
        imageUrl: "",
      },
    ];
    onChangeLesson({ ...lesson, learningCards: newCards });
  };

  const handleUpdateLearningCard = (index, field, value) => {
    const updated = [...lesson.learningCards];
    updated[index] = { ...updated[index], [field]: value };
    onChangeLesson({ ...lesson, learningCards: updated });
  };

  const handleRemoveLearningCard = (index) => {
    if (lesson.learningCards.length <= 1) return;
    const updated = lesson.learningCards.filter((_, i) => i !== index);
    onChangeLesson({ ...lesson, learningCards: updated });
  };

  // --- Handlers for Flashcards ---
  const handleAddFlashcard = () => {
    const newCards = [
      ...lesson.flashcards,
      {
        id: `fc_${Date.now()}`,
        coreStatement: "",
        keyPoints: [""],
        imageUrl: "",
      },
    ];
    onChangeLesson({ ...lesson, flashcards: newCards });
  };

  const handleUpdateFlashcard = (index, field, value) => {
    const updated = [...lesson.flashcards];
    updated[index] = { ...updated[index], [field]: value };
    onChangeLesson({ ...lesson, flashcards: updated });
  };

  const handleRemoveFlashcard = (index) => {
    if (lesson.flashcards.length <= 1) return;
    const updated = lesson.flashcards.filter((_, i) => i !== index);
    onChangeLesson({ ...lesson, flashcards: updated });
  };

  // --- Handlers for Quizzes ---
  const handleAddQuiz = () => {
    const newQuizzes = [
      ...lesson.quizzes,
      {
        id: `qz_${Date.now()}`,
        question: "",
        options: ["", "", "", ""],
        correctIndex: 0,
        explanation: "",
        imageUrl: "",
      },
    ];
    onChangeLesson({ ...lesson, quizzes: newQuizzes });
  };

  const handleUpdateQuiz = (index, field, value) => {
    const updated = [...lesson.quizzes];
    updated[index] = { ...updated[index], [field]: value };
    onChangeLesson({ ...lesson, quizzes: updated });
  };

  const handleRemoveQuiz = (index) => {
    if (lesson.quizzes.length <= 1) return;
    const updated = lesson.quizzes.filter((_, i) => i !== index);
    onChangeLesson({ ...lesson, quizzes: updated });
  };

  // --- Handlers for Matches ---
  const handleAddMatchPair = () => {
    const newMatches = [
      ...lesson.matches,
      { id: `m_${Date.now()}`, leftText: "", rightText: "" },
    ];
    onChangeLesson({ ...lesson, matches: newMatches });
  };

  const handleUpdateMatchPair = (index, field, value) => {
    const updated = [...lesson.matches];
    updated[index] = { ...updated[index], [field]: value };
    onChangeLesson({ ...lesson, matches: updated });
  };

  const handleRemoveMatchPair = (index) => {
    if (lesson.matches.length <= 2) return;
    const updated = lesson.matches.filter((_, i) => i !== index);
    onChangeLesson({ ...lesson, matches: updated });
  };

  return (
    <div className="flex-1 flex flex-col h-[calc(100vh-61px)] overflow-hidden bg-slate-50/50">
      {/* Lesson Meta Header */}
      <div className="bg-white border-b border-slate-200 px-6 py-4 shadow-sm">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="space-y-1">
            <div className="flex items-center gap-2 flex-wrap text-xs">
              <span className="px-2 py-0.5 rounded font-bold bg-red-100 text-red-700">
                {lesson.domain}
              </span>
              <span className="text-slate-400">•</span>
              <span className="text-slate-600 font-medium">{lesson.subject}</span>
              <span className="text-slate-400">•</span>
              <span className="text-slate-500">{lesson.topic}</span>
            </div>
            <h2 className="text-lg font-bold text-slate-900 leading-snug">
              {lesson.topicTitle}
            </h2>
            <div className="text-[11px] text-slate-500 flex items-center gap-2">
              <span>Last edited by: <strong className="text-slate-700">{lesson.updatedBy || "Anonymous"}</strong></span>
              {syncStatus?.synced === false && (
                <span className="text-amber-600 font-medium bg-amber-50 px-1.5 py-0.5 rounded">
                  Local draft (Firestore offline)
                </span>
              )}
            </div>
          </div>

          <div className="flex items-center gap-3">
            {/* Status Selector */}
            <select
              value={lesson.status}
              onChange={(e) => onChangeLesson({ ...lesson, status: e.target.value })}
              className={`text-xs font-semibold px-3 py-2 rounded-xl border transition ${
                lesson.status === "ready"
                  ? "bg-emerald-50 border-emerald-300 text-emerald-800"
                  : lesson.status === "drafting"
                  ? "bg-amber-50 border-amber-300 text-amber-800"
                  : "bg-slate-50 border-slate-300 text-slate-700"
              }`}
            >
              <option value="not_started">⚪ Not Started</option>
              <option value="drafting">🟡 Drafting</option>
              <option value="ready">🟢 Ready (Publishable)</option>
            </select>

            {/* Save Button */}
            <button
              onClick={onSaveLesson}
              disabled={isSaving}
              className="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-xl text-xs font-bold shadow-md shadow-red-600/20 transition flex items-center gap-1.5"
            >
              <Save className="w-3.5 h-3.5" />
              {isSaving ? "Saving..." : "Save Lesson"}
            </button>
          </div>
        </div>

        {/* 4 Stage Tabs */}
        <div className="flex gap-2 mt-4 overflow-x-auto no-scrollbar pt-1">
          <button
            onClick={() => setActiveTab("learning")}
            className={`px-3.5 py-2 rounded-xl text-xs font-bold flex items-center gap-2 transition ${
              activeTab === "learning"
                ? "bg-red-600 text-white shadow-sm"
                : "bg-slate-100 text-slate-600 hover:bg-slate-200"
            }`}
          >
            <BookOpen className="w-4 h-4" />
            <span>1. Learning Cards</span>
            <span className={`px-1.5 py-0.2 rounded-full text-[10px] ${
              activeTab === "learning" ? "bg-red-700 text-white" : "bg-slate-200 text-slate-700"
            }`}>
              {lesson.learningCards.length}
            </span>
          </button>

          <button
            onClick={() => setActiveTab("flashcards")}
            className={`px-3.5 py-2 rounded-xl text-xs font-bold flex items-center gap-2 transition ${
              activeTab === "flashcards"
                ? "bg-red-600 text-white shadow-sm"
                : "bg-slate-100 text-slate-600 hover:bg-slate-200"
            }`}
          >
            <Layers className="w-4 h-4" />
            <span>2. Flashcards</span>
            <span className={`px-1.5 py-0.2 rounded-full text-[10px] ${
              activeTab === "flashcards" ? "bg-red-700 text-white" : "bg-slate-200 text-slate-700"
            }`}>
              {lesson.flashcards.length}
            </span>
          </button>

          <button
            onClick={() => setActiveTab("quizzes")}
            className={`px-3.5 py-2 rounded-xl text-xs font-bold flex items-center gap-2 transition ${
              activeTab === "quizzes"
                ? "bg-red-600 text-white shadow-sm"
                : "bg-slate-100 text-slate-600 hover:bg-slate-200"
            }`}
          >
            <HelpCircle className="w-4 h-4" />
            <span>3. Quiz MCQs</span>
            <span className={`px-1.5 py-0.2 rounded-full text-[10px] ${
              activeTab === "quizzes" ? "bg-red-700 text-white" : "bg-slate-200 text-slate-700"
            }`}>
              {lesson.quizzes.length}
            </span>
          </button>

          <button
            onClick={() => setActiveTab("match")}
            className={`px-3.5 py-2 rounded-xl text-xs font-bold flex items-center gap-2 transition ${
              activeTab === "match"
                ? "bg-red-600 text-white shadow-sm"
                : "bg-slate-100 text-slate-600 hover:bg-slate-200"
            }`}
          >
            <Shuffle className="w-4 h-4" />
            <span>4. Match the Following</span>
            <span className={`px-1.5 py-0.2 rounded-full text-[10px] ${
              activeTab === "match" ? "bg-red-700 text-white" : "bg-slate-200 text-slate-700"
            }`}>
              {lesson.matches.length}
            </span>
          </button>
        </div>
      </div>

      {/* Stage Editor Content Area */}
      <div className="flex-1 overflow-y-auto p-6 space-y-6">
        {/* ==============================================================
            STAGE 1: LEARNING CARDS
            ============================================================== */}
        {activeTab === "learning" && (
          <div className="space-y-6 max-w-4xl mx-auto">
            <div className="bg-red-50/70 border border-red-200 rounded-xl p-4 text-xs text-red-900 flex items-start justify-between gap-4">
              <p>
                <strong>📱 Social-Media Style Learning Feed:</strong> One focused concept per card, striking Assam-relevant image/visual, short punchy explanation, and highlighted takeaways.
              </p>
              <button
                type="button"
                onClick={handleAddLearningCard}
                className="shrink-0 px-3 py-1.5 bg-red-600 text-white rounded-lg font-semibold hover:bg-red-700 flex items-center gap-1 shadow-sm transition"
              >
                <Plus className="w-3.5 h-3.5" />
                Add Card
              </button>
            </div>

            {lesson.learningCards.map((card, idx) => (
              <div
                key={card.id || idx}
                className="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 space-y-5 transition hover:border-slate-300"
              >
                <div className="flex items-center justify-between border-b border-slate-100 pb-3">
                  <div className="flex items-center gap-2">
                    <span className="w-6 h-6 rounded-full bg-red-100 text-red-700 font-bold text-xs flex items-center justify-center">
                      {idx + 1}
                    </span>
                    <h3 className="text-sm font-bold text-slate-800">
                      Learning Card #{idx + 1}
                    </h3>
                  </div>
                  {lesson.learningCards.length > 1 && (
                    <button
                      type="button"
                      onClick={() => handleRemoveLearningCard(idx)}
                      className="text-xs text-rose-600 hover:text-rose-700 flex items-center gap-1 font-medium transition"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                      Remove
                    </button>
                  )}
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
                  {/* Left Column: Text & Concepts */}
                  <div className="space-y-4">
                    <div>
                      <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">
                        Card Title / Subtopic
                      </label>
                      <input
                        type="text"
                        value={card.title}
                        onChange={(e) => handleUpdateLearningCard(idx, "title", e.target.value)}
                        placeholder="e.g. The Ahom Dynasty: An Overview"
                        className="w-full px-3 py-2 text-xs border border-slate-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-red-600 focus:border-red-600"
                      />
                    </div>

                    <div>
                      <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">
                        Concept Explanation (Bite-sized micro-copy)
                      </label>
                      <textarea
                        rows={5}
                        value={card.conceptText}
                        onChange={(e) => handleUpdateLearningCard(idx, "conceptText", e.target.value)}
                        placeholder="The Ahom dynasty ruled Assam for nearly 600 years (1228-1826) and played a key role in shaping the region's political, cultural and social identity..."
                        className="w-full px-3 py-2 text-xs border border-slate-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-red-600 focus:border-red-600 leading-relaxed"
                      />
                    </div>

                    {/* Key Area Tags */}
                    <div>
                      <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">
                        Key Areas Explored in Next Cards (Comma-separated chips)
                      </label>
                      <input
                        type="text"
                        value={Array.isArray(card.keyAreas) ? card.keyAreas.join(", ") : card.keyAreas || ""}
                        onChange={(e) => handleUpdateLearningCard(idx, "keyAreas", e.target.value.split(",").map(s => s.trim()))}
                        placeholder="e.g. Origins, Administration, Mughal Conflicts"
                        className="w-full px-3 py-2 text-xs border border-slate-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-red-600 focus:border-red-600"
                      />
                    </div>
                  </div>

                  {/* Right Column: Visual Upload via ImgBB */}
                  <div>
                    <ImageUploader
                      value={card.imageUrl}
                      onChange={(url) => handleUpdateLearningCard(idx, "imageUrl", url)}
                      label="Visual / Monument / Map Background"
                    />
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* ==============================================================
            STAGE 2: FLASHCARDS
            ============================================================== */}
        {activeTab === "flashcards" && (
          <div className="space-y-6 max-w-4xl mx-auto">
            <div className="bg-red-50/70 border border-red-200 rounded-xl p-4 text-xs text-red-900 flex items-start justify-between gap-4">
              <p>
                <strong>🗂️ Square Active Recall Flashcards:</strong> Bold core statement, concise bullet points, and high-contrast image. Tested with <em>"I Know This"</em> and <em>"Revise Again"</em>.
              </p>
              <button
                type="button"
                onClick={handleAddFlashcard}
                className="shrink-0 px-3 py-1.5 bg-red-600 text-white rounded-lg font-semibold hover:bg-red-700 flex items-center gap-1 shadow-sm transition"
              >
                <Plus className="w-3.5 h-3.5" />
                Add Flashcard
              </button>
            </div>

            {lesson.flashcards.map((card, idx) => (
              <div
                key={card.id || idx}
                className="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 space-y-5"
              >
                <div className="flex items-center justify-between border-b border-slate-100 pb-3">
                  <div className="flex items-center gap-2">
                    <span className="w-6 h-6 rounded-full bg-red-100 text-red-700 font-bold text-xs flex items-center justify-center">
                      {idx + 1}
                    </span>
                    <h3 className="text-sm font-bold text-slate-800">
                      Flashcard #{idx + 1}
                    </h3>
                  </div>
                  {lesson.flashcards.length > 1 && (
                    <button
                      type="button"
                      onClick={() => handleRemoveFlashcard(idx)}
                      className="text-xs text-rose-600 hover:text-rose-700 flex items-center gap-1 font-medium transition"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                      Remove
                    </button>
                  )}
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
                  <div className="space-y-4">
                    <div>
                      <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">
                        Core Important Fact / Statement
                      </label>
                      <textarea
                        rows={3}
                        value={card.coreStatement}
                        onChange={(e) => handleUpdateFlashcard(idx, "coreStatement", e.target.value)}
                        placeholder="The Ahom dynasty ruled Assam for nearly 600 years (1228 – 1826)."
                        className="w-full px-3 py-2 text-xs border border-slate-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-red-600 focus:border-red-600 font-semibold"
                      />
                    </div>

                    <div>
                      <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">
                        Key Points (One point per line)
                      </label>
                      <textarea
                        rows={4}
                        value={Array.isArray(card.keyPoints) ? card.keyPoints.join("\n") : card.keyPoints || ""}
                        onChange={(e) => handleUpdateFlashcard(idx, "keyPoints", e.target.value.split("\n"))}
                        placeholder="Founded by Sukapha in 1228&#10;Ruled for almost 6 centuries&#10;Known for administrative brilliance&#10;Resisted Mughal expansion"
                        className="w-full px-3 py-2 text-xs border border-slate-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-red-600 focus:border-red-600 leading-relaxed font-mono"
                      />
                    </div>
                  </div>

                  <div>
                    <ImageUploader
                      value={card.imageUrl}
                      onChange={(url) => handleUpdateFlashcard(idx, "imageUrl", url)}
                      label="Flashcard Visual"
                    />
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* ==============================================================
            STAGE 3: QUIZZES
            ============================================================== */}
        {activeTab === "quizzes" && (
          <div className="space-y-6 max-w-4xl mx-auto">
            <div className="bg-red-50/70 border border-red-200 rounded-xl p-4 text-xs text-red-900 flex items-start justify-between gap-4">
              <p>
                <strong>❓ Quiz MCQs:</strong> Single-choice question with instant feedback styling and a 2-line explanation.
              </p>
              <button
                type="button"
                onClick={handleAddQuiz}
                className="shrink-0 px-3 py-1.5 bg-red-600 text-white rounded-lg font-semibold hover:bg-red-700 flex items-center gap-1 shadow-sm transition"
              >
                <Plus className="w-3.5 h-3.5" />
                Add Question
              </button>
            </div>

            {lesson.quizzes.map((quiz, idx) => (
              <div
                key={quiz.id || idx}
                className="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 space-y-5"
              >
                <div className="flex items-center justify-between border-b border-slate-100 pb-3">
                  <div className="flex items-center gap-2">
                    <span className="w-6 h-6 rounded-full bg-red-100 text-red-700 font-bold text-xs flex items-center justify-center">
                      {idx + 1}
                    </span>
                    <h3 className="text-sm font-bold text-slate-800">
                      Quiz Question #{idx + 1}
                    </h3>
                  </div>
                  {lesson.quizzes.length > 1 && (
                    <button
                      type="button"
                      onClick={() => handleRemoveQuiz(idx)}
                      className="text-xs text-rose-600 hover:text-rose-700 flex items-center gap-1 font-medium transition"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                      Remove
                    </button>
                  )}
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
                  <div className="space-y-4">
                    <div>
                      <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">
                        Question Text
                      </label>
                      <input
                        type="text"
                        value={quiz.question}
                        onChange={(e) => handleUpdateQuiz(idx, "question", e.target.value)}
                        placeholder="Which of the following rivers flows through Majuli island in Assam?"
                        className="w-full px-3 py-2 text-xs border border-slate-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-red-600 focus:border-red-600 font-semibold"
                      />
                    </div>

                    {/* 4 Options */}
                    <div className="space-y-2">
                      <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider">
                        Options (Select the correct answer radio button)
                      </label>
                      {["A", "B", "C", "D"].map((letter, optIdx) => (
                        <div key={letter} className="flex items-center gap-2">
                          <label className="flex items-center justify-center w-7 h-7 rounded-lg border font-bold text-xs cursor-pointer transition shrink-0 bg-slate-50 border-slate-300 hover:bg-slate-100">
                            <input
                              type="radio"
                              name={`correct_${idx}`}
                              checked={quiz.correctIndex === optIdx}
                              onChange={() => handleUpdateQuiz(idx, "correctIndex", optIdx)}
                              className="hidden"
                            />
                            <span className={quiz.correctIndex === optIdx ? "text-emerald-700 font-extrabold" : "text-slate-600"}>
                              {letter}
                            </span>
                          </label>
                          <input
                            type="text"
                            value={quiz.options[optIdx] || ""}
                            onChange={(e) => {
                              const newOpts = [...quiz.options];
                              newOpts[optIdx] = e.target.value;
                              handleUpdateQuiz(idx, "options", newOpts);
                            }}
                            placeholder={`Option ${letter}...`}
                            className={`flex-1 px-3 py-1.5 text-xs border rounded-xl focus:outline-none transition ${
                              quiz.correctIndex === optIdx
                                ? "border-emerald-500 bg-emerald-50/30 ring-1 ring-emerald-500 font-medium"
                                : "border-slate-300 focus:ring-2 focus:ring-red-600"
                            }`}
                          />
                          {quiz.correctIndex === optIdx && (
                            <span className="text-[10px] text-emerald-700 font-bold px-2 py-0.5 rounded bg-emerald-100 shrink-0">
                              Correct ✓
                            </span>
                          )}
                        </div>
                      ))}
                    </div>

                    {/* Explanation */}
                    <div>
                      <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">
                        Answer Explanation (Shown immediately upon answering)
                      </label>
                      <textarea
                        rows={3}
                        value={quiz.explanation}
                        onChange={(e) => handleUpdateQuiz(idx, "explanation", e.target.value)}
                        placeholder="Correct! Majuli, the world's largest river island, is formed by the Brahmaputra River in Assam."
                        className="w-full px-3 py-2 text-xs border border-slate-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-red-600 focus:border-red-600 leading-relaxed"
                      />
                    </div>
                  </div>

                  <div>
                    <ImageUploader
                      value={quiz.imageUrl}
                      onChange={(url) => handleUpdateQuiz(idx, "imageUrl", url)}
                      label="Scenic / Contextual Question Visual"
                    />
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* ==============================================================
            STAGE 4: MATCH THE FOLLOWING
            ============================================================== */}
        {activeTab === "match" && (
          <div className="space-y-6 max-w-4xl mx-auto">
            <div className="bg-red-50/70 border border-red-200 rounded-xl p-4 text-xs text-red-900 flex items-start justify-between gap-4">
              <p>
                <strong>🧩 Topic Capstone Matching:</strong> Connect matching items between Column A and Column B. Once completed, the topic completion modal triggers!
              </p>
              <button
                type="button"
                onClick={handleAddMatchPair}
                className="shrink-0 px-3 py-1.5 bg-red-600 text-white rounded-lg font-semibold hover:bg-red-700 flex items-center gap-1 shadow-sm transition"
              >
                <Plus className="w-3.5 h-3.5" />
                Add Pair
              </button>
            </div>

            <div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 space-y-4">
              <div className="flex items-center justify-between border-b border-slate-100 pb-3">
                <h3 className="text-sm font-bold text-slate-800">
                  Matching Pairs ({lesson.matches.length} pairs)
                </h3>
              </div>

              <div className="grid grid-cols-12 gap-3 text-xs font-bold uppercase tracking-wider text-slate-500 px-1">
                <span className="col-span-1">#</span>
                <span className="col-span-5">Column A (e.g. Ruler / Dynasty / Site)</span>
                <span className="col-span-5">Column B (e.g. Contribution / Location / Fact)</span>
                <span className="col-span-1 text-center">Action</span>
              </div>

              <div className="space-y-2.5">
                {lesson.matches.map((match, idx) => (
                  <div key={match.id || idx} className="grid grid-cols-12 gap-3 items-center">
                    <span className="col-span-1 text-xs font-bold text-slate-400 pl-1">
                      {idx + 1}.
                    </span>
                    <div className="col-span-5">
                      <input
                        type="text"
                        value={match.leftText}
                        onChange={(e) => handleUpdateMatchPair(idx, "leftText", e.target.value)}
                        placeholder="e.g. Sukapha"
                        className="w-full px-3 py-2 text-xs border border-slate-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-red-600 font-medium"
                      />
                    </div>
                    <div className="col-span-5">
                      <input
                        type="text"
                        value={match.rightText}
                        onChange={(e) => handleUpdateMatchPair(idx, "rightText", e.target.value)}
                        placeholder="e.g. Established the Ahom kingdom in 1228"
                        className="w-full px-3 py-2 text-xs border border-slate-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-red-600"
                      />
                    </div>
                    <div className="col-span-1 flex justify-center">
                      {lesson.matches.length > 2 && (
                        <button
                          type="button"
                          onClick={() => handleRemoveMatchPair(idx)}
                          className="p-1.5 text-slate-400 hover:text-rose-600 rounded-lg hover:bg-rose-50 transition"
                          title="Remove pair"
                        >
                          <Trash2 className="w-3.5 h-3.5" />
                        </button>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
