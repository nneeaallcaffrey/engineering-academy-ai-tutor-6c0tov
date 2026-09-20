/** Backend bilan ishlash. Dev rejimda Vite proxy, Docker'da nginx. */

import type {
  AuditResponse, FinalProject, GraphResponse, ResourceOut, RunResponse,
  SubjectBrief, SubjectDetail, TopicBrief, TopicDetail,
} from "./types";

const BASE = import.meta.env.VITE_API_BASE ?? "";

export class ApiError extends Error {
  constructor(message: string, readonly status: number) {
    super(message);
    this.name = "ApiError";
  }
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  let res: Response;
  try {
    res = await fetch(`${BASE}${path}`, {
      headers: { "Content-Type": "application/json" },
      ...init,
    });
  } catch {
    throw new ApiError(
      "Serverga ulanib bo'lmadi. Backend ishga tushganini tekshiring.", 0);
  }
  if (!res.ok) {
    let detail = `So'rov bajarilmadi (${res.status})`;
    try {
      const body = await res.json();
      if (typeof body?.detail === "string") detail = body.detail;
    } catch { /* javob JSON emas — standart xabar qoladi */ }
    throw new ApiError(detail, res.status);
  }
  return res.json() as Promise<T>;
}

export const api = {
  subjects: () => request<SubjectBrief[]>("/api/subjects"),
  subject: (id: string) => request<SubjectDetail>(`/api/subjects/${id}`),

  topics: (params: Record<string, string | number | undefined> = {}) => {
    const q = new URLSearchParams();
    for (const [k, v] of Object.entries(params)) {
      if (v !== undefined && v !== "") q.set(k, String(v));
    }
    const s = q.toString();
    return request<TopicBrief[]>(`/api/topics${s ? `?${s}` : ""}`);
  },
  topic: (id: string) => request<TopicDetail>(`/api/topics/${id}`),

  run: (id: string, body: { code?: string; params?: Record<string, number> }) =>
    request<RunResponse>(`/api/topics/${id}/run`, {
      method: "POST",
      body: JSON.stringify(body),
    }),

  projects: () => request<FinalProject[]>("/api/projects"),
  resources: () => request<ResourceOut[]>("/api/resources"),
  graph: (subjectId?: string) =>
    request<GraphResponse>(
      `/api/curriculum/graph${subjectId ? `?subject_id=${subjectId}` : ""}`),
  audit: () => request<AuditResponse>("/api/curriculum/audit"),
};
