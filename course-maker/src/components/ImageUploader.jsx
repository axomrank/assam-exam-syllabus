import React, { useState, useRef } from "react";
import { UploadCloud, Image as ImageIcon, X, Loader2, Link2, Check } from "lucide-react";
import { uploadToImgBB } from "../services/imgbb";

export default function ImageUploader({ value, onChange, label = "Card Visual / Image" }) {
  const [isUploading, setIsUploading] = useState(false);
  const [error, setError] = useState("");
  const [showUrlInput, setShowUrlInput] = useState(false);
  const [urlInput, setUrlInput] = useState("");
  const [copied, setCopied] = useState(false);
  const fileInputRef = useRef(null);

  const handleFileChange = async (e) => {
    const file = e.target.files?.[0];
    if (!file) return;

    if (!file.type.startsWith("image/")) {
      setError("Please select a valid image file (PNG, JPG, WEBP)");
      return;
    }

    try {
      setIsUploading(true);
      setError("");
      const result = await uploadToImgBB(file);
      onChange(result.url);
    } catch (err) {
      setError(err.message || "Failed to upload to ImgBB");
    } finally {
      setIsUploading(false);
      if (fileInputRef.current) fileInputRef.current.value = "";
    }
  };

  const handleUrlSubmit = (e) => {
    e.preventDefault();
    if (urlInput.trim()) {
      onChange(urlInput.trim());
      setUrlInput("");
      setShowUrlInput(false);
    }
  };

  const handleCopy = () => {
    if (!value) return;
    navigator.clipboard.writeText(value);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="w-full space-y-2">
      <div className="flex items-center justify-between text-xs font-semibold text-slate-700">
        <span>{label}</span>
        <button
          type="button"
          onClick={() => setShowUrlInput(!showUrlInput)}
          className="text-red-700 hover:text-red-800 flex items-center gap-1 font-medium transition"
        >
          <Link2 className="w-3.5 h-3.5" />
          {showUrlInput ? "Cancel URL" : "Paste URL"}
        </button>
      </div>

      {showUrlInput && (
        <form onSubmit={handleUrlSubmit} className="flex gap-2">
          <input
            type="url"
            value={urlInput}
            onChange={(e) => setUrlInput(e.target.value)}
            placeholder="https://i.ibb.co/..."
            className="flex-1 text-xs px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-600 focus:border-red-600 bg-white"
          />
          <button
            type="submit"
            className="px-3 py-2 bg-red-600 text-white rounded-lg text-xs font-semibold hover:bg-red-700 transition"
          >
            Apply
          </button>
        </form>
      )}

      {value ? (
        <div className="relative group rounded-xl overflow-hidden border border-slate-200 bg-slate-50 shadow-sm aspect-video max-h-48 flex items-center justify-center">
          <img
            src={value}
            alt="Uploaded preview"
            className="w-full h-full object-cover transition group-hover:scale-105 duration-300"
          />
          <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center gap-3">
            <button
              type="button"
              onClick={handleCopy}
              className="p-2 bg-white/90 hover:bg-white text-slate-800 rounded-full shadow-md text-xs flex items-center gap-1 transition"
              title="Copy image URL"
            >
              {copied ? <Check className="w-4 h-4 text-emerald-600" /> : <Link2 className="w-4 h-4" />}
            </button>
            <button
              type="button"
              onClick={() => onChange("")}
              className="p-2 bg-red-600/90 hover:bg-red-700 text-white rounded-full shadow-md transition"
              title="Remove image"
            >
              <X className="w-4 h-4" />
            </button>
          </div>
          <span className="absolute bottom-2 left-2 px-2 py-0.5 rounded bg-black/60 backdrop-blur-sm text-white text-[10px] font-mono">
            ImgBB Hosted
          </span>
        </div>
      ) : (
        <div
          onClick={() => !isUploading && fileInputRef.current?.click()}
          className={`border-2 border-dashed rounded-xl p-4 text-center cursor-pointer transition flex flex-col items-center justify-center gap-2 bg-slate-50/70 hover:bg-red-50/40 hover:border-red-400 ${
            isUploading ? "opacity-60 pointer-events-none border-red-300" : "border-slate-300"
          }`}
        >
          <input
            type="file"
            ref={fileInputRef}
            onChange={handleFileChange}
            accept="image/*"
            className="hidden"
          />
          {isUploading ? (
            <div className="flex flex-col items-center gap-2 py-3">
              <Loader2 className="w-6 h-6 text-red-600 animate-spin" />
              <p className="text-xs font-medium text-slate-600">Uploading to ImgBB...</p>
            </div>
          ) : (
            <div className="py-2 flex flex-col items-center gap-1">
              <div className="w-10 h-10 rounded-full bg-red-100 flex items-center justify-center text-red-600 mb-1">
                <UploadCloud className="w-5 h-5" />
              </div>
              <p className="text-xs font-semibold text-slate-700">
                Click to upload image to <span className="text-red-600">ImgBB</span>
              </p>
              <p className="text-[11px] text-slate-500">PNG, JPG, WEBP up to 32MB</p>
            </div>
          )}
        </div>
      )}

      {error && (
        <p className="text-xs text-rose-600 font-medium bg-rose-50 p-2 rounded-lg border border-rose-200">
          ⚠️ {error}
        </p>
      )}
    </div>
  );
}
