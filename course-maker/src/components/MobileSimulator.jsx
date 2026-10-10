import React, { useState, useEffect } from "react";
import { 
  Wifi, 
  Battery, 
  ChevronLeft, 
  ChevronRight, 
  Check, 
  RotateCcw, 
  Sparkles, 
  Award, 
  Layers,
  ArrowRight,
  ExternalLink,
  BookOpen,
  HelpCircle,
  Shuffle
} from "lucide-react";
import confetti from "canvas-confetti";

export default function MobileSimulator({ lesson, onNextTopic }) {
  const [screen, setScreen] = useState("feed"); // feed | flashcards | quiz | match | completed
  
  // Flashcard carousel state
  const [currentFcIndex, setCurrentFcIndex] = useState(0);
  const [fcKnownCount, setFcKnownCount] = useState(0);

  // Quiz state
  const [currentQzIndex, setCurrentQzIndex] = useState(0);
  const [selectedOption, setSelectedOption] = useState(null);
  const [quizScore, setQuizScore] = useState(0);

  // Match state
  const [selectedLeft, setSelectedLeft] = useState(null);
  const [matchedPairs, setMatchedPairs] = useState({}); // { leftIdx: rightIdx }
  const [matchError, setMatchError] = useState(null);

  // Reset internal states when lesson changes
  useEffect(() => {
    setScreen("feed");
    setCurrentFcIndex(0);
    setCurrentQzIndex(0);
    setSelectedOption(null);
    setMatchedPairs({});
    setSelectedLeft(null);
    setMatchError(null);
  }, [lesson?.topicId]);

  if (!lesson) {
    return (
      <div className="w-[380px] h-[720px] rounded-[48px] border-[12px] border-slate-900 bg-slate-100 flex items-center justify-center p-8 text-center text-slate-400">
        <p className="text-xs">Select a topic to preview mobile experience</p>
      </div>
    );
  }

  const learningCards = lesson.learningCards || [];
  const flashcards = lesson.flashcards || [];
  const quizzes = lesson.quizzes || [];
  const matches = lesson.matches || [];

  // Current flashcard
  const activeFc = flashcards[currentFcIndex] || flashcards[0];
  // Current quiz
  const activeQz = quizzes[currentQzIndex] || quizzes[0];

  // Confetti trigger
  const triggerConfetti = () => {
    confetti({
      particleCount: 80,
      spread: 60,
      origin: { y: 0.6 }
    });
  };

  // Match handler
  const handleSelectLeft = (idx) => {
    if (matchedPairs[idx] !== undefined) return;
    setSelectedLeft(idx);
    setMatchError(null);
  };

  const handleSelectRight = (rightIdx) => {
    if (selectedLeft === null) return;
    // Check if right item is already matched
    if (Object.values(matchedPairs).includes(rightIdx)) return;

    // Check if left and right match (by original array index)
    if (selectedLeft === rightIdx) {
      const nextMatched = { ...matchedPairs, [selectedLeft]: rightIdx };
      setMatchedPairs(nextMatched);
      setSelectedLeft(null);
      setMatchError(null);

      // Check if all matched
      if (Object.keys(nextMatched).length === matches.length) {
        triggerConfetti();
        setScreen("completed");
      }
    } else {
      setMatchError(rightIdx);
      setTimeout(() => setMatchError(null), 800);
      setSelectedLeft(null);
    }
  };

  return (
    <div className="flex flex-col items-center">
      {/* Simulation Mode Bar */}
      <div className="mb-3 flex items-center gap-1.5 bg-slate-200/80 p-1 rounded-xl text-[11px] font-semibold text-slate-700 shadow-inner">
        <button
          onClick={() => setScreen("feed")}
          className={`px-2.5 py-1 rounded-lg transition ${
            screen === "feed" ? "bg-white text-red-600 shadow-sm" : "hover:text-slate-900"
          }`}
        >
          1. Feed
        </button>
        <button
          onClick={() => setScreen("flashcards")}
          className={`px-2.5 py-1 rounded-lg transition ${
            screen === "flashcards" ? "bg-white text-red-600 shadow-sm" : "hover:text-slate-900"
          }`}
        >
          2. Flashcards
        </button>
        <button
          onClick={() => setScreen("quiz")}
          className={`px-2.5 py-1 rounded-lg transition ${
            screen === "quiz" ? "bg-white text-red-600 shadow-sm" : "hover:text-slate-900"
          }`}
        >
          3. Quiz
        </button>
        <button
          onClick={() => setScreen("match")}
          className={`px-2.5 py-1 rounded-lg transition ${
            screen === "match" || screen === "completed" ? "bg-white text-red-600 shadow-sm" : "hover:text-slate-900"
          }`}
        >
          4. Match
        </button>
      </div>

      {/* iPhone Device Frame */}
      <div className="w-[370px] h-[740px] bg-black rounded-[52px] p-3 shadow-2xl ring-1 ring-slate-800/60 relative flex flex-col justify-between shrink-0 select-none">
        {/* Dynamic Island / Speaker */}
        <div className="absolute top-5 left-1/2 -translate-x-1/2 w-28 h-6 bg-black rounded-full z-50 flex items-center justify-end px-2">
          <div className="w-2.5 h-2.5 rounded-full bg-slate-900 ring-1 ring-slate-800/80"></div>
        </div>

        {/* Screen Container */}
        <div className="w-full h-full bg-[#FCFBF8] rounded-[42px] overflow-hidden flex flex-col relative text-slate-800 font-sans">
          {/* iOS Top Bar */}
          <div className="h-10 px-6 pt-3 flex items-center justify-between text-[11px] font-semibold text-slate-800 z-40 bg-white/70 backdrop-blur-sm">
            <span>9:41</span>
            <div className="flex items-center gap-1.5">
              <Wifi className="w-3.5 h-3.5" />
              <Battery className="w-4 h-4 fill-slate-800" />
            </div>
          </div>

          {/* ==========================================================
              SCREEN 1: LEARNING CARDS FEED
              ========================================================== */}
          {screen === "feed" && (
            <div className="flex-1 overflow-y-auto no-scrollbar pb-6">
              {/* App Feed Header */}
              <div className="px-4 py-2 flex items-center justify-between border-b border-slate-100 bg-white sticky top-0 z-30">
                <div className="flex items-center gap-2">
                  <div className="w-6 h-6 rounded-lg bg-red-600 flex items-center justify-center text-white text-[10px] font-bold">
                    🏛️
                  </div>
                  <div>
                    <h4 className="text-xs font-bold text-slate-900 leading-tight">
                      {lesson.subject || "Assam History"}
                    </h4>
                    <p className="text-[10px] text-slate-400">Continuous feed</p>
                  </div>
                </div>
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-100 text-slate-600">
                  Topic #{lesson.topicId?.split("_")[1] || "1"}
                </span>
              </div>

              {/* Feed Content */}
              <div className="p-4 space-y-4">
                {learningCards.map((card, idx) => (
                  <div
                    key={card.id || idx}
                    className="bg-white rounded-3xl overflow-hidden shadow-sm border border-slate-200/80 space-y-3 pb-4"
                  >
                    {/* Visual Banner */}
                    <div className="h-44 w-full bg-gradient-to-tr from-amber-100 to-red-100 relative overflow-hidden flex items-center justify-center">
                      {card.imageUrl ? (
                        <img
                          src={card.imageUrl}
                          alt="Card visual"
                          className="w-full h-full object-cover"
                        />
                      ) : (
                        <div className="text-center p-4 text-red-700/60">
                          <BookOpen className="w-10 h-10 mx-auto mb-1 opacity-40" />
                          <span className="text-[11px] font-semibold">Visual placeholder</span>
                        </div>
                      )}
                      <div className="absolute top-3 left-3 bg-red-600/90 backdrop-blur-md text-white px-2.5 py-0.5 rounded-full text-[10px] font-bold shadow-sm">
                        {lesson.domain || "Assam"}
                      </div>
                    </div>

                    {/* Card Content */}
                    <div className="px-4 space-y-2">
                      <h3 className="text-base font-bold text-slate-900 leading-snug">
                        {card.title || "The Ahom Dynasty: An Overview"}
                      </h3>

                      <p className="text-xs text-slate-600 leading-relaxed">
                        {card.conceptText ||
                          "The Ahom dynasty ruled Assam for nearly 600 years (1228 - 1826) and played a key role in shaping the region's political, cultural and social identity..."}
                      </p>

                      {/* Key areas chips */}
                      {card.keyAreas && card.keyAreas.length > 0 && card.keyAreas[0] && (
                        <div className="pt-2 border-t border-slate-100">
                          <p className="text-[10px] font-semibold text-slate-500 mb-1.5 flex items-center gap-1">
                            <Sparkles className="w-3 h-3 text-amber-500" /> Key areas explored:
                          </p>
                          <div className="flex flex-wrap gap-1">
                            {card.keyAreas.map((chip, cIdx) => (
                              <span
                                key={cIdx}
                                className="px-2 py-0.5 rounded-lg bg-red-50 text-red-700 text-[10px] font-medium border border-red-100"
                              >
                                {chip}
                              </span>
                            ))}
                          </div>
                        </div>
                      )}
                    </div>
                  </div>
                ))}

                {/* Transition to Flashcards */}
                <button
                  onClick={() => setScreen("flashcards")}
                  className="w-full py-3.5 px-4 bg-gradient-to-r from-red-600 to-rose-600 text-white rounded-2xl font-bold text-xs shadow-lg shadow-red-600/25 flex items-center justify-center gap-2 hover:opacity-95 transition"
                >
                  <span>Almost done — flashcards next!</span>
                  <ArrowRight className="w-4 h-4" />
                </button>
              </div>
            </div>
          )}

          {/* ==========================================================
              SCREEN 2: FLASHCARDS CAROUSEL
              ========================================================== */}
          {screen === "flashcards" && (
            <div className="flex-1 flex flex-col justify-between p-4 bg-[#FBF9F5]">
              {/* Header */}
              <div className="flex items-center justify-between">
                <button
                  onClick={() => setScreen("feed")}
                  className="text-xs text-slate-500 flex items-center gap-1 font-semibold"
                >
                  <ChevronLeft className="w-4 h-4" /> Feed
                </button>
                <div className="text-center">
                  <h4 className="text-xs font-bold text-slate-800">Flashcards</h4>
                  <p className="text-[10px] text-slate-400">{lesson.domain}</p>
                </div>
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-red-100 text-red-700">
                  {currentFcIndex + 1}/{flashcards.length}
                </span>
              </div>

              {/* Progress target bubble */}
              <div className="bg-white rounded-2xl p-2.5 shadow-sm border border-slate-200/80 flex items-center gap-3">
                <div className="w-10 h-10 rounded-full bg-emerald-50 border-2 border-emerald-500 flex flex-col items-center justify-center text-emerald-700 font-bold text-[10px]">
                  <span>{currentFcIndex + 1}/{flashcards.length}</span>
                </div>
                <div>
                  <h5 className="text-[11px] font-bold text-slate-800">Keep going!</h5>
                  <p className="text-[10px] text-slate-500">
                    {flashcards.length - (currentFcIndex + 1)} more cards to complete today's target.
                  </p>
                </div>
              </div>

              {/* Square Active Recall Flashcard */}
              <div className="bg-white rounded-3xl overflow-hidden shadow-md border border-slate-200/80 flex-1 my-3 flex flex-col">
                <div className="h-36 bg-slate-100 relative overflow-hidden shrink-0">
                  {activeFc?.imageUrl ? (
                    <img
                      src={activeFc.imageUrl}
                      alt="Flashcard visual"
                      className="w-full h-full object-cover"
                    />
                  ) : (
                    <div className="w-full h-full flex items-center justify-center text-red-600/50 bg-red-50">
                      <Layers className="w-8 h-8 opacity-40" />
                    </div>
                  )}
                  <span className="absolute top-2.5 left-2.5 px-2 py-0.5 rounded-md bg-black/60 text-white text-[9px] font-semibold backdrop-blur-sm">
                    {lesson.topicTitle}
                  </span>
                </div>

                <div className="p-4 flex-1 flex flex-col justify-between space-y-3">
                  <h3 className="text-sm font-bold text-slate-900 leading-snug">
                    {activeFc?.coreStatement ||
                      "The Ahom dynasty ruled Assam for nearly 600 years (1228 – 1826)."}
                  </h3>

                  {activeFc?.keyPoints && (
                    <div className="space-y-1.5 bg-slate-50 p-3 rounded-xl border border-slate-100 flex-1 overflow-y-auto no-scrollbar">
                      <span className="text-[10px] font-bold text-red-700 flex items-center gap-1">
                        🎁 Key Points:
                      </span>
                      <ul className="text-[11px] text-slate-600 space-y-1 list-disc list-inside leading-snug">
                        {activeFc.keyPoints.map((pt, pIdx) => (
                          <li key={pIdx}>{pt}</li>
                        ))}
                      </ul>
                    </div>
                  )}

                  {/* Carousel pagination dots */}
                  <div className="flex justify-center gap-1.5 py-1">
                    {flashcards.map((_, dotIdx) => (
                      <span
                        key={dotIdx}
                        className={`h-1.5 rounded-full transition-all ${
                          dotIdx === currentFcIndex ? "w-5 bg-red-600" : "w-1.5 bg-slate-200"
                        }`}
                      />
                    ))}
                  </div>
                </div>
              </div>

              {/* Action Buttons: I Know This / Revise Again */}
              <div className="space-y-2">
                <div className="grid grid-cols-2 gap-2">
                  <button
                    onClick={() => {
                      setFcKnownCount(c => c + 1);
                      if (currentFcIndex < flashcards.length - 1) {
                        setCurrentFcIndex(c => c + 1);
                      } else {
                        setScreen("quiz");
                      }
                    }}
                    className="py-3 px-3 bg-emerald-600 hover:bg-emerald-700 text-white rounded-2xl font-bold text-xs flex items-center justify-center gap-1.5 shadow-md shadow-emerald-600/20 transition"
                  >
                    <Check className="w-4 h-4" />
                    <span>I Know This</span>
                  </button>

                  <button
                    onClick={() => {
                      if (currentFcIndex < flashcards.length - 1) {
                        setCurrentFcIndex(c => c + 1);
                      } else {
                        setScreen("quiz");
                      }
                    }}
                    className="py-3 px-3 border-2 border-red-500 text-red-600 hover:bg-red-50 bg-white rounded-2xl font-bold text-xs flex items-center justify-center gap-1.5 transition"
                  >
                    <RotateCcw className="w-3.5 h-3.5" />
                    <span>Revise Again</span>
                  </button>
                </div>

                <div className="flex items-center justify-between text-[11px] text-slate-400 px-1 pt-0.5">
                  <button
                    disabled={currentFcIndex === 0}
                    onClick={() => setCurrentFcIndex(c => Math.max(0, c - 1))}
                    className="disabled:opacity-30 hover:text-slate-600"
                  >
                    &lt; Prev
                  </button>
                  <span>Swipe or tap actions</span>
                  <button
                    onClick={() => {
                      if (currentFcIndex < flashcards.length - 1) {
                        setCurrentFcIndex(c => c + 1);
                      } else {
                        setScreen("quiz");
                      }
                    }}
                    className="hover:text-slate-600 font-semibold text-red-600"
                  >
                    {currentFcIndex < flashcards.length - 1 ? "Next >" : "Quizzes >"}
                  </button>
                </div>
              </div>
            </div>
          )}

          {/* ==========================================================
              SCREEN 3: QUIZ MCQs
              ========================================================== */}
          {screen === "quiz" && (
            <div className="flex-1 flex flex-col justify-between p-4 bg-[#FCFAF7] overflow-y-auto no-scrollbar">
              {/* Header */}
              <div>
                <div className="flex items-center justify-between mb-2">
                  <button
                    onClick={() => setScreen("flashcards")}
                    className="text-xs text-slate-500 flex items-center gap-1 font-semibold"
                  >
                    <ChevronLeft className="w-4 h-4" /> Flashcards
                  </button>
                  <span className="text-xs font-bold text-slate-800">Quiz</span>
                  <span className="text-[10px] font-bold text-red-700 bg-red-50 px-2 py-0.5 rounded-full">
                    {currentQzIndex + 1}/{quizzes.length}
                  </span>
                </div>

                {/* Progress Bar */}
                <div className="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden mb-3">
                  <div
                    className="bg-red-600 h-full transition-all duration-300"
                    style={{ width: `${((currentQzIndex + 1) / quizzes.length) * 100}%` }}
                  />
                </div>
              </div>

              {/* Question Card */}
              <div className="space-y-3 my-auto">
                {/* Visual */}
                <div className="h-32 w-full rounded-2xl bg-slate-100 overflow-hidden shadow-inner relative flex items-center justify-center">
                  {activeQz?.imageUrl ? (
                    <img
                      src={activeQz.imageUrl}
                      alt="Quiz visual"
                      className="w-full h-full object-cover"
                    />
                  ) : (
                    <HelpCircle className="w-8 h-8 text-slate-300" />
                  )}
                </div>

                <h3 className="text-xs font-bold text-slate-900 leading-snug">
                  {activeQz?.question || "Which of the following rivers flows through Majuli island in Assam?"}
                </h3>

                {/* Options List */}
                <div className="space-y-2">
                  {activeQz?.options?.map((opt, optIdx) => {
                    const isSelected = selectedOption === optIdx;
                    const isCorrect = activeQz.correctIndex === optIdx;
                    let btnStyle = "bg-white border-slate-200 text-slate-700 hover:border-slate-300";

                    if (selectedOption !== null) {
                      if (isCorrect) {
                        btnStyle = "bg-emerald-50 border-emerald-500 text-emerald-800 font-bold ring-1 ring-emerald-500";
                      } else if (isSelected) {
                        btnStyle = "bg-rose-50 border-rose-500 text-rose-800 font-bold ring-1 ring-rose-500";
                      }
                    }

                    return (
                      <button
                        key={optIdx}
                        onClick={() => {
                          if (selectedOption === null) {
                            setSelectedOption(optIdx);
                            if (optIdx === activeQz.correctIndex) {
                              setQuizScore(s => s + 1);
                            }
                          }
                        }}
                        className={`w-full p-2.5 rounded-xl border text-left text-xs transition flex items-center justify-between ${btnStyle}`}
                      >
                        <div className="flex items-center gap-2">
                          <span className="w-5 h-5 rounded-md bg-slate-100 text-slate-700 font-bold text-[10px] flex items-center justify-center">
                            {["A", "B", "C", "D"][optIdx]}
                          </span>
                          <span className="leading-snug">{opt || `Option ${optIdx + 1}`}</span>
                        </div>
                        {selectedOption !== null && isCorrect && (
                          <Check className="w-4 h-4 text-emerald-600 shrink-0" />
                        )}
                      </button>
                    );
                  })}
                </div>

                {/* Explanation Card when answered */}
                {selectedOption !== null && (
                  <div className="p-3 rounded-2xl bg-emerald-50/90 border border-emerald-200 text-xs text-emerald-900 animate-in fade-in duration-200 space-y-1">
                    <span className="font-bold flex items-center gap-1 text-[11px] text-emerald-800">
                      <Check className="w-3.5 h-3.5" />
                      {selectedOption === activeQz.correctIndex ? "Correct!" : "Explanation:"}
                    </span>
                    <p className="text-[11px] leading-relaxed text-emerald-800">
                      {activeQz.explanation ||
                        "Majuli, the world's largest river island, is formed by the Brahmaputra River in Assam."}
                    </p>
                  </div>
                )}
              </div>

              {/* Next Question CTA */}
              <div className="pt-2">
                <button
                  disabled={selectedOption === null}
                  onClick={() => {
                    setSelectedOption(null);
                    if (currentQzIndex < quizzes.length - 1) {
                      setCurrentQzIndex(c => c + 1);
                    } else {
                      setScreen("match");
                    }
                  }}
                  className="w-full py-3 bg-red-600 hover:bg-red-700 disabled:opacity-40 text-white rounded-2xl font-bold text-xs shadow-md shadow-red-600/20 transition flex items-center justify-center gap-1.5"
                >
                  <span>{currentQzIndex < quizzes.length - 1 ? "Next Question →" : "Final Match Activity →"}</span>
                </button>
              </div>
            </div>
          )}

          {/* ==========================================================
              SCREEN 4: MATCH THE FOLLOWING
              ========================================================== */}
          {screen === "match" && (
            <div className="flex-1 flex flex-col justify-between p-4 bg-[#FCFBF9] overflow-y-auto no-scrollbar">
              <div>
                <div className="flex items-center justify-between mb-2">
                  <button
                    onClick={() => setScreen("quiz")}
                    className="text-xs text-slate-500 flex items-center gap-1 font-semibold"
                  >
                    <ChevronLeft className="w-4 h-4" /> Quiz
                  </button>
                  <span className="text-xs font-bold text-slate-800">Match the Following</span>
                  <span className="text-[10px] font-bold text-red-700 bg-red-50 px-2 py-0.5 rounded-full">
                    {Object.keys(matchedPairs).length}/{matches.length}
                  </span>
                </div>

                <p className="text-[11px] text-slate-500 mb-3">
                  Tap an item on the left, then tap its matching pair on the right.
                </p>
              </div>

              {/* Interactive Match Columns */}
              <div className="grid grid-cols-2 gap-3 my-auto">
                {/* Left Column */}
                <div className="space-y-2">
                  <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block text-center">
                    Column A
                  </span>
                  {matches.map((item, idx) => {
                    const isMatched = matchedPairs[idx] !== undefined;
                    const isSelected = selectedLeft === idx;

                    return (
                      <button
                        key={idx}
                        disabled={isMatched}
                        onClick={() => handleSelectLeft(idx)}
                        className={`w-full p-2.5 rounded-xl border text-left text-[11px] font-medium transition ${
                          isMatched
                            ? "bg-slate-100 border-slate-200 text-slate-400 line-through"
                            : isSelected
                            ? "bg-red-50 border-red-600 text-red-700 ring-2 ring-red-600 font-bold"
                            : "bg-white border-slate-300 text-slate-700 hover:border-red-400"
                        }`}
                      >
                        {item.leftText || `Item ${idx + 1}`}
                      </button>
                    );
                  })}
                </div>

                {/* Right Column */}
                <div className="space-y-2">
                  <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block text-center">
                    Column B
                  </span>
                  {matches.map((item, rightIdx) => {
                    const isMatched = Object.values(matchedPairs).includes(rightIdx);
                    const isError = matchError === rightIdx;

                    return (
                      <button
                        key={rightIdx}
                        disabled={isMatched}
                        onClick={() => handleSelectRight(rightIdx)}
                        className={`w-full p-2.5 rounded-xl border text-left text-[11px] transition ${
                          isMatched
                            ? "bg-emerald-50 border-emerald-300 text-emerald-800 font-semibold"
                            : isError
                            ? "bg-rose-50 border-rose-500 text-rose-700 font-bold animate-shake"
                            : "bg-white border-slate-300 text-slate-700 hover:border-slate-400"
                        }`}
                      >
                        {item.rightText || `Match ${rightIdx + 1}`}
                      </button>
                    );
                  })}
                </div>
              </div>

              {/* Reset matching */}
              <div className="pt-4 text-center">
                <button
                  onClick={() => setMatchedPairs({})}
                  className="text-[11px] text-slate-400 hover:text-slate-600 flex items-center justify-center gap-1 mx-auto"
                >
                  <RotateCcw className="w-3 h-3" /> Reset pairs
                </button>
              </div>
            </div>
          )}

          {/* ==========================================================
              SCREEN 5: CELEBRATION / TOPIC COMPLETED
              ========================================================== */}
          {screen === "completed" && (
            <div className="flex-1 flex flex-col items-center justify-center p-6 text-center bg-gradient-to-b from-red-50/60 to-white space-y-4">
              <div className="w-20 h-20 rounded-full bg-red-100 flex items-center justify-center text-red-600 text-3xl shadow-lg shadow-red-600/10 animate-bounce">
                🎉
              </div>

              <div className="space-y-1.5">
                <span className="px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-xs font-bold">
                  Topic Completed!
                </span>
                <h3 className="text-base font-extrabold text-slate-900 pt-1">
                  {lesson.topicTitle}
                </h3>
                <p className="text-xs text-slate-500 max-w-xs">
                  You finished all visual cards, active recall flashcards, practice questions, and matching exercises!
                </p>
              </div>

              <div className="w-full space-y-2 pt-4">
                <button
                  onClick={() => {
                    triggerConfetti();
                    if (onNextTopic) onNextTopic();
                  }}
                  className="w-full py-3.5 bg-gradient-to-r from-red-600 to-rose-600 text-white rounded-2xl font-bold text-xs shadow-lg shadow-red-600/30 flex items-center justify-center gap-2 hover:opacity-95 transition"
                >
                  <span>Next Topic →</span>
                </button>

                <button
                  onClick={() => setScreen("feed")}
                  className="w-full py-2.5 text-xs text-slate-500 hover:text-slate-800 font-semibold"
                >
                  Review This Topic Again
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
