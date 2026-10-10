import React, { useState } from "react";
import { 
  X, 
  Key, 
  Database, 
  Download, 
  Upload, 
  ExternalLink, 
  Check, 
  Sparkles,
  RefreshCw
} from "lucide-react";
import { 
  getImgbbApiKey, 
  setImgbbApiKey, 
  DEFAULT_IMGBB_API_KEY 
} from "../services/imgbb";
import { 
  exportAllLessonsJSON, 
  importLessonsJSON 
} from "../services/courseService";

export default function SettingsModal({ isOpen, onClose, onLessonsReloaded }) {
  const [apiKey, setApiKey] = useState(getImgbbApiKey());
  const [savedKey, setSavedKey] = useState(false);
  const [importing, setImporting] = useState(false);
  const [importStatus, setImportStatus] = useState("");

  if (!isOpen) return null;

  const handleSaveKey = (e) => {
    e.preventDefault();
    setImgbbApiKey(apiKey);
    setSavedKey(true);
    setTimeout(() => setSavedKey(false), 2000);
  };

  const handleResetDefault = () => {
    setApiKey(DEFAULT_IMGBB_API_KEY);
    setImgbbApiKey(DEFAULT_IMGBB_API_KEY);
    setSavedKey(true);
    setTimeout(() => setSavedKey(false), 2000);
  };

  const handleFileImport = (e) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setImporting(true);
    setImportStatus("");

    const reader = new FileReader();
    reader.onload = async (event) => {
      try {
        const text = event.target?.result;
        const res = await importLessonsJSON(text);
        setImportStatus(`✅ Successfully imported ${res.count} lessons!`);
        if (onLessonsReloaded) onLessonsReloaded();
      } catch (err) {
        setImportStatus(`❌ Import failed: ${err.message}`);
      } finally {
        setImporting(false);
      }
    };
    reader.readAsText(file);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4 animate-in fade-in duration-200">
      <div className="bg-white rounded-2xl max-w-lg w-full shadow-2xl border border-slate-100 overflow-hidden max-h-[90vh] flex flex-col">
        {/* Header */}
        <div className="p-5 border-b border-slate-100 flex items-center justify-between bg-slate-50/70">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-lg bg-red-100 flex items-center justify-center text-red-600">
              <Sparkles className="w-4 h-4" />
            </div>
            <div>
              <h2 className="text-base font-bold text-slate-800">Studio Settings & Cloud</h2>
              <p className="text-xs text-slate-500">Configure ImgBB, Firebase & Local Backup</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 text-slate-400 hover:text-slate-700 rounded-lg hover:bg-slate-100 transition"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6 space-y-6 overflow-y-auto">
          {/* ImgBB API Section */}
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <label className="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                <Key className="w-3.5 h-3.5 text-red-600" />
                ImgBB API Key
              </label>
              <button
                type="button"
                onClick={handleResetDefault}
                className="text-[11px] text-red-600 hover:underline flex items-center gap-1 font-medium"
              >
                Reset to default
              </button>
            </div>
            <p className="text-xs text-slate-500 leading-relaxed">
              Images uploaded to cards will be hosted via this ImgBB key.
            </p>
            <form onSubmit={handleSaveKey} className="flex gap-2">
              <input
                type="text"
                value={apiKey}
                onChange={(e) => setApiKey(e.target.value)}
                placeholder="Enter ImgBB API key..."
                className="flex-1 px-3 py-2 text-xs border border-slate-300 rounded-xl font-mono focus:outline-none focus:ring-2 focus:ring-red-600 focus:border-red-600 bg-slate-50/50"
              />
              <button
                type="submit"
                className="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-xl text-xs font-semibold shadow-sm transition flex items-center gap-1"
              >
                {savedKey ? <Check className="w-3.5 h-3.5" /> : null}
                {savedKey ? "Saved" : "Save"}
              </button>
            </form>
          </div>

          <hr className="border-slate-100" />

          {/* Firebase Cloud Firestore Info */}
          <div className="space-y-2">
            <div className="flex items-center justify-between">
              <label className="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                <Database className="w-3.5 h-3.5 text-red-600" />
                Firebase Real-time Sync
              </label>
              <span className="text-[10px] px-2 py-0.5 rounded-full font-medium bg-emerald-100 text-emerald-800">
                Project: axomrank-bf44f
              </span>
            </div>
            <p className="text-xs text-slate-600 leading-relaxed">
              When enabled in Firebase Console, all lesson updates instantly sync between you and your collaborators in real-time.
            </p>
            <div className="bg-amber-50 border border-amber-200 rounded-xl p-3 text-xs text-amber-900 space-y-1.5">
              <div className="font-semibold flex items-center gap-1">
                <span>⚡ Two quick 1-click console toggles:</span>
              </div>
              <ul className="list-disc list-inside space-y-1 text-amber-800">
                <li>
                  <a
                    href="https://console.firebase.google.com/project/axomrank-bf44f/firestore"
                    target="_blank"
                    rel="noreferrer"
                    className="underline text-red-700 font-semibold inline-flex items-center gap-0.5 ml-1"
                  >
                    Enable Cloud Firestore <ExternalLink className="w-2.5 h-2.5" />
                  </a>
                </li>
                <li>
                  <a
                    href="https://console.firebase.google.com/project/axomrank-bf44f/authentication/providers"
                    target="_blank"
                    rel="noreferrer"
                    className="underline text-red-700 font-semibold inline-flex items-center gap-0.5 ml-1"
                  >
                    Enable Anonymous Auth <ExternalLink className="w-2.5 h-2.5" />
                  </a>
                </li>
              </ul>
            </div>
          </div>

          <hr className="border-slate-100" />

          {/* Backup / Export / Import */}
          <div className="space-y-3">
            <label className="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
              <Download className="w-3.5 h-3.5 text-red-600" />
              Backup & Migration
            </label>
            <p className="text-xs text-slate-500">
              Download all created lessons as a master JSON file, or restore from a backup.
            </p>
            <div className="grid grid-cols-2 gap-3">
              <button
                type="button"
                onClick={exportAllLessonsJSON}
                className="px-3 py-2.5 border border-slate-200 hover:border-slate-300 bg-white hover:bg-slate-50 text-slate-700 rounded-xl text-xs font-semibold flex items-center justify-center gap-1.5 shadow-sm transition"
              >
                <Download className="w-3.5 h-3.5 text-slate-500" />
                Export JSON Backup
              </button>

              <label className="px-3 py-2.5 border border-slate-200 hover:border-slate-300 bg-white hover:bg-slate-50 text-slate-700 rounded-xl text-xs font-semibold flex items-center justify-center gap-1.5 shadow-sm transition cursor-pointer">
                <Upload className="w-3.5 h-3.5 text-slate-500" />
                {importing ? "Importing..." : "Import JSON"}
                <input
                  type="file"
                  accept=".json"
                  onChange={handleFileImport}
                  className="hidden"
                />
              </label>
            </div>

            {importStatus && (
              <p className="text-xs font-medium p-2.5 rounded-lg bg-slate-100 text-slate-700">
                {importStatus}
              </p>
            )}
          </div>
        </div>

        {/* Footer */}
        <div className="p-4 border-t border-slate-100 bg-slate-50 flex justify-end">
          <button
            onClick={onClose}
            className="px-5 py-2 bg-slate-800 hover:bg-slate-900 text-white rounded-xl text-xs font-semibold transition"
          >
            Done
          </button>
        </div>
      </div>
    </div>
  );
}
