import React from "react";
import { 
  Sparkles, 
  Settings, 
  Smartphone, 
  Layout, 
  User, 
  Download, 
  ExternalLink,
  BookOpen
} from "lucide-react";
import { exportAllLessonsJSON } from "../services/courseService";

export default function Navbar({ 
  collaboratorName, 
  onEditName, 
  onOpenSettings,
  previewMode,
  setPreviewMode,
  stats
}) {
  return (
    <header className="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200 px-4 lg:px-6 py-3 transition-all">
      <div className="flex items-center justify-between gap-4 max-w-7xl mx-auto">
        {/* Left: Brand & Title */}
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-red-700 to-rose-500 flex items-center justify-center text-white shadow-md shadow-red-600/20">
            <Sparkles className="w-5 h-5 text-amber-200" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-extrabold text-slate-900 tracking-tight text-lg">
                Axom<span className="text-red-600">Rank</span>
              </span>
              <span className="px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-700 border border-red-200">
                Course Studio
              </span>
            </div>
            <p className="text-[11px] text-slate-500 hidden sm:block">
              Visual Micro-Learning Lesson Plan Builder
            </p>
          </div>
        </div>

        {/* Center: Live Stats */}
        <div className="hidden md:flex items-center gap-4 bg-slate-50 px-3 py-1.5 rounded-xl border border-slate-200 text-xs text-slate-600">
          <div className="flex items-center gap-1.5">
            <BookOpen className="w-3.5 h-3.5 text-red-600" />
            <span>Syllabus: <strong className="text-slate-800">{stats.total}</strong></span>
          </div>
          <span className="text-slate-300">|</span>
          <div className="flex items-center gap-1.5">
            <span className="w-2 h-2 rounded-full bg-amber-500"></span>
            <span>Drafts: <strong className="text-slate-800">{stats.drafting}</strong></span>
          </div>
          <span className="text-slate-300">|</span>
          <div className="flex items-center gap-1.5">
            <span className="w-2 h-2 rounded-full bg-emerald-500"></span>
            <span>Ready: <strong className="text-slate-800">{stats.ready}</strong></span>
          </div>
        </div>

        {/* Right: Actions */}
        <div className="flex items-center gap-2 sm:gap-3">
          {/* View toggle button */}
          <div className="flex items-center bg-slate-100 p-1 rounded-xl border border-slate-200">
            <button
              onClick={() => setPreviewMode("split")}
              className={`px-2.5 py-1 rounded-lg text-xs font-medium flex items-center gap-1.5 transition ${
                previewMode === "split" 
                  ? "bg-white text-slate-900 shadow-sm" 
                  : "text-slate-600 hover:text-slate-900"
              }`}
              title="Split View (Editor + Mobile Phone)"
            >
              <Layout className="w-3.5 h-3.5" />
              <span className="hidden lg:inline">Split</span>
            </button>
            <button
              onClick={() => setPreviewMode("editor")}
              className={`px-2.5 py-1 rounded-lg text-xs font-medium flex items-center gap-1.5 transition ${
                previewMode === "editor" 
                  ? "bg-white text-slate-900 shadow-sm" 
                  : "text-slate-600 hover:text-slate-900"
              }`}
              title="Editor Focus"
            >
              <span className="hidden lg:inline">Editor</span>
              <span className="lg:hidden">Edit</span>
            </button>
            <button
              onClick={() => setPreviewMode("preview")}
              className={`px-2.5 py-1 rounded-lg text-xs font-medium flex items-center gap-1.5 transition ${
                previewMode === "preview" 
                  ? "bg-white text-slate-900 shadow-sm" 
                  : "text-slate-600 hover:text-slate-900"
              }`}
              title="Mobile Simulator Focus"
            >
              <Smartphone className="w-3.5 h-3.5 text-red-600" />
              <span className="hidden lg:inline">Preview</span>
            </button>
          </div>

          {/* Quick Export */}
          <button
            onClick={exportAllLessonsJSON}
            className="p-2 text-slate-600 hover:text-slate-900 hover:bg-slate-100 rounded-xl transition border border-transparent hover:border-slate-200"
            title="Export JSON Backup"
          >
            <Download className="w-4 h-4" />
          </button>

          {/* Settings */}
          <button
            onClick={onOpenSettings}
            className="p-2 text-slate-600 hover:text-slate-900 hover:bg-slate-100 rounded-xl transition border border-transparent hover:border-slate-200"
            title="Settings (ImgBB & Firebase)"
          >
            <Settings className="w-4 h-4" />
          </button>

          {/* Collaborator Profile */}
          <button
            onClick={onEditName}
            className="flex items-center gap-1.5 pl-2.5 pr-3 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-800 rounded-xl text-xs font-semibold border border-slate-200 transition"
            title="Click to change your editor name"
          >
            <div className="w-5 h-5 rounded-full bg-red-600 text-white flex items-center justify-center text-[10px] font-bold">
              {collaboratorName ? collaboratorName[0].toUpperCase() : <User className="w-3 h-3" />}
            </div>
            <span className="max-w-[80px] truncate">{collaboratorName || "Guest"}</span>
          </button>
        </div>
      </div>
    </header>
  );
}
