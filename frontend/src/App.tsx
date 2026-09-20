import { Navigate, Route, Routes } from "react-router-dom";
import { api } from "./api/client";
import { ErrorBox, Loading, TitleBlock } from "./components/Layout";
import { useAsync } from "./hooks/useAsync";
import { AuditPage } from "./pages/AuditPage";
import { Dashboard } from "./pages/Dashboard";
import { GraphPage } from "./pages/GraphPage";
import { ProjectsPage } from "./pages/ProjectsPage";
import { ResourcesPage } from "./pages/ResourcesPage";
import { SubjectPage } from "./pages/SubjectPage";
import { TopicPage } from "./pages/TopicPage";

export function App() {
  const { data: subjects, loading, error, reload } = useAsync(() => api.subjects(), []);

  return (
    <>
      <TitleBlock subjects={subjects ?? []} />
      <main className="wrap">
        {loading && <Loading what="Platforma yuklanmoqda" />}
        {error && <ErrorBox message={error} onRetry={reload} />}
        {subjects && (
          <Routes>
            <Route path="/" element={<Dashboard subjects={subjects} />} />
            <Route path="/fan/:subjectId" element={<SubjectPage />} />
            <Route path="/mavzu/:topicId" element={<TopicPage />} />
            <Route path="/xarita" element={<GraphPage subjects={subjects} />} />
            <Route path="/loyihalar" element={<ProjectsPage subjects={subjects} />} />
            <Route path="/manbalar" element={<ResourcesPage subjects={subjects} />} />
            <Route path="/audit" element={<AuditPage />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        )}
      </main>
      <footer style={{
        borderTop: "1px solid var(--rule-faint)", marginTop: "2rem",
        padding: "1rem 0", background: "var(--paper)",
      }}>
        <div className="wrap" style={{ display: "flex", gap: "1rem",
             justifyContent: "space-between", flexWrap: "wrap" }}>
          <span className="tiny muted">
            5 fan · 150 mavzu · o'zbek tilida
          </span>
          <a href="/audit" className="tiny muted">Akademik audit</a>
        </div>
      </footer>
    </>
  );
}
