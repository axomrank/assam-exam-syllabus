import React, { useState } from "react";
import { UserCheck, Sparkles } from "lucide-react";
import { setCollaboratorName } from "../services/courseService";
import { auth, signInAnonymously } from "../firebase/config";

export default function NameModal({ isOpen, onClose, onNameSaved, currentName = "" }) {
  const [name, setName] = useState(currentName);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  if (!isOpen) return null;

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!name.trim()) {
      setError("Please enter your name or nickname to proceed.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      // Anonymous Firebase Auth
      await signInAnonymously(auth).catch((err) => {
        console.warn("Anonymous auth warning (offline mode enabled):", err.message);
      });

      setCollaboratorName(name.trim());
      onNameSaved(name.trim());
      onClose();
    } catch (err) {
      setError(err.message || "Failed to sign in");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4 animate-in fade-in duration-200">
      <div className="bg-white rounded-2xl max-w-md w-full shadow-2xl border border-slate-100 overflow-hidden transform scale-100 transition-all">
        <div className="bg-gradient-to-r from-red-600 to-rose-700 p-6 text-white text-center relative">
          <div className="w-14 h-14 bg-white/20 rounded-2xl mx-auto flex items-center justify-center backdrop-blur-md mb-3 shadow-inner">
            <Sparkles className="w-8 h-8 text-amber-200" />
          </div>
          <h2 className="text-xl font-bold tracking-tight">Welcome to AxomRank Studio</h2>
          <p className="text-xs text-red-100 mt-1">
            Collaborative course creation platform for Assam Gov Exam Aspirants
          </p>
        </div>

        <form onSubmit={handleSubmit} className="p-6 space-y-4">
          <div>
            <label className="block text-xs font-semibold text-slate-700 uppercase tracking-wider mb-2">
              Who is editing today?
            </label>
            <input
              type="text"
              autoFocus
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="e.g. Angsuman, Ronit, Nilav..."
              className="w-full px-4 py-3 border border-slate-300 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-red-600 focus:border-red-600 shadow-sm"
            />
            <p className="text-[11px] text-slate-500 mt-1.5">
              Your edits, learning cards, and questions will be tagged with this name.
            </p>
          </div>

          {error && (
            <p className="text-xs text-rose-600 bg-rose-50 p-2.5 rounded-lg border border-rose-200">
              {error}
            </p>
          )}

          <div className="pt-2">
            <button
              type="submit"
              disabled={loading}
              className="w-full py-3 bg-red-600 hover:bg-red-700 text-white rounded-xl font-semibold text-sm shadow-md shadow-red-600/20 transition flex items-center justify-center gap-2"
            >
              <UserCheck className="w-4 h-4" />
              {loading ? "Entering Studio..." : "Start Creating Content"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
