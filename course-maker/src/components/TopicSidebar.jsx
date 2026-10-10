import React, { useState, useMemo } from "react";
import { 
  Search, 
  Filter, 
  MapPin, 
  BookMarked, 
  CheckCircle2, 
  Clock, 
  CircleDashed,
  ChevronRight,
  Layers
} from "lucide-react";

export default function TopicSidebar({ 
  topics, 
  selectedTopic, 
  onSelectTopic, 
  lessonsMap 
}) {
  const [search, setSearch] = useState("");
  const [selectedDomain, setSelectedDomain] = useState("All");
  const [assamOnly, setAssamOnly] = useState(false);
  const [statusFilter, setStatusFilter] = useState("All");

  // Extract unique domains
  const domains = useMemo(() => {
    const set = new Set();
    topics.forEach((t) => t.domain && set.add(t.domain));
    return ["All", ...Array.from(set)];
  }, [topics]);

  // Filter topics
  const filteredTopics = useMemo(() => {
    return topics.filter((t) => {
      // Domain filter
      if (selectedDomain !== "All" && t.domain !== selectedDomain) {
        return false;
      }
      // Assam filter
      if (assamOnly && !t.assamSpecific) {
        return false;
      }
      // Status filter
      const lesson = lessonsMap[t.id];
      const status = lesson?.status || "not_started";
      if (statusFilter !== "All" && status !== statusFilter) {
        return false;
      }
      // Search
      if (search.trim()) {
        const query = search.toLowerCase();
        return t.searchKey.includes(query) || t.id.toLowerCase().includes(query);
      }
      return true;
    });
  }, [topics, selectedDomain, assamOnly, statusFilter, search, lessonsMap]);

  return (
    <aside className="w-full lg:w-80 xl:w-96 flex flex-col bg-white border-r border-slate-200 h-[calc(100vh-61px)] shrink-0">
      {/* Search & Filter Header */}
      <div className="p-3.5 border-b border-slate-200 space-y-2.5 bg-slate-50/50">
        <div className="relative">
          <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search 840+ topics, eras, dynasties..."
            className="w-full pl-9 pr-3 py-2 bg-white text-xs border border-slate-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-red-600 focus:border-red-600 shadow-sm"
          />
          {search && (
            <button
              onClick={() => setSearch("")}
              className="absolute right-2.5 top-1/2 -translate-y-1/2 text-xs text-slate-400 hover:text-slate-600"
            >
              Clear
            </button>
          )}
        </div>

        {/* Domain horizontal pills */}
        <div className="flex gap-1.5 overflow-x-auto no-scrollbar py-0.5 text-xs">
          {domains.map((dom) => (
            <button
              key={dom}
              onClick={() => setSelectedDomain(dom)}
              className={`px-2.5 py-1 rounded-lg shrink-0 font-medium transition text-[11px] ${
                selectedDomain === dom
                  ? "bg-red-600 text-white shadow-sm"
                  : "bg-white text-slate-600 border border-slate-200 hover:bg-slate-100"
              }`}
            >
              {dom}
            </button>
          ))}
        </div>

        {/* Quick toggles */}
        <div className="flex items-center justify-between gap-2 pt-0.5 text-[11px]">
          <button
            onClick={() => setAssamOnly(!assamOnly)}
            className={`px-2.5 py-1 rounded-lg border flex items-center gap-1 font-medium transition ${
              assamOnly
                ? "bg-amber-100 border-amber-300 text-amber-900"
                : "bg-white border-slate-200 text-slate-600 hover:bg-slate-100"
            }`}
          >
            <MapPin className="w-3 h-3 text-red-600" />
            Assam Specific
          </button>

          <select
            value={statusFilter}
            onChange={(e) => setStatusFilter(e.target.value)}
            className="bg-white border border-slate-200 text-slate-700 rounded-lg px-2 py-1 text-[11px] focus:outline-none focus:ring-1 focus:ring-red-600"
          >
            <option value="All">All Status</option>
            <option value="ready">Ready (Done)</option>
            <option value="drafting">Drafting</option>
            <option value="not_started">Not Started</option>
          </select>
        </div>
      </div>

      {/* Topics Count info */}
      <div className="px-4 py-2 bg-slate-100/70 border-b border-slate-200/80 flex items-center justify-between text-[11px] text-slate-500 font-medium">
        <span>Showing {filteredTopics.length} topics</span>
        {selectedDomain !== "All" && (
          <span className="text-red-700 font-semibold">{selectedDomain}</span>
        )}
      </div>

      {/* Topics List */}
      <div className="flex-1 overflow-y-auto divide-y divide-slate-100">
        {filteredTopics.length === 0 ? (
          <div className="p-8 text-center text-slate-400 space-y-2">
            <Layers className="w-8 h-8 mx-auto opacity-40" />
            <p className="text-xs">No matching topics found.</p>
          </div>
        ) : (
          filteredTopics.map((topic) => {
            const isSelected = selectedTopic?.id === topic.id;
            const lesson = lessonsMap[topic.id];
            const status = lesson?.status || "not_started";

            return (
              <div
                key={topic.id}
                onClick={() => onSelectTopic(topic)}
                className={`p-3.5 cursor-pointer transition text-left relative group ${
                  isSelected
                    ? "bg-red-50/80 border-l-4 border-red-600"
                    : "hover:bg-slate-50"
                }`}
              >
                <div className="flex items-start justify-between gap-2">
                  <div className="space-y-1 flex-1 min-w-0">
                    <div className="flex items-center gap-1.5 flex-wrap">
                      <span className="text-[10px] font-mono text-slate-400 font-medium">
                        #{topic.index}
                      </span>
                      <span className="text-[10px] px-1.5 py-0.2 rounded font-semibold bg-slate-100 text-slate-700">
                        {topic.domain}
                      </span>
                      {topic.assamSpecific && (
                        <span className="text-[9px] px-1 py-0.2 rounded font-bold bg-amber-100 text-amber-800">
                          Assam
                        </span>
                      )}
                    </div>

                    <h4 className="text-xs font-semibold text-slate-800 group-hover:text-red-600 transition leading-snug line-clamp-2">
                      {topic.subSubtopic || topic.subtopic || topic.topic}
                    </h4>

                    <p className="text-[11px] text-slate-400 truncate">
                      {topic.subject} • {topic.topic}
                    </p>
                  </div>

                  {/* Status Indicator */}
                  <div className="shrink-0 flex items-center pt-1">
                    {status === "ready" ? (
                      <span title="Ready" className="text-emerald-600">
                        <CheckCircle2 className="w-4 h-4 fill-emerald-50" />
                      </span>
                    ) : status === "drafting" ? (
                      <span title="Drafting" className="text-amber-500">
                        <Clock className="w-4 h-4" />
                      </span>
                    ) : (
                      <span title="Not started" className="text-slate-300">
                        <CircleDashed className="w-4 h-4" />
                      </span>
                    )}
                  </div>
                </div>
              </div>
            );
          })
        )}
      </div>
    </aside>
  );
}
