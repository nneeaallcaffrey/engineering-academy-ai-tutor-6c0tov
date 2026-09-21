/** Backend javoblarining turlari — app/schemas.py ning aksi. */

export interface SubjectBrief {
  id: string;
  code: string;
  order: number;
  title: string;
  tagline: string;
  topic_count: number;
  accent: string;
}

export interface TopicBrief {
  id: string;
  subject_id: string;
  module_id: string;
  order: number;
  global_order: number;
  title: string;
  description: string;
  learning_objective: string;
  difficulty: string;
  estimated_minutes: number;
  prerequisites: string[];
  tags: string[];
  next_topic: string | null;
  has_lab: boolean;
}

export interface ModuleOut {
  id: string;
  order: number;
  title: string;
  summary: string;
  outcome: string;
}

export interface SubjectDetail extends SubjectBrief {
  description: string;
  goal: string;
  modules: ModuleOut[];
  assessments: Assessment[];
  topics: TopicBrief[];
}

export interface Assessment {
  kind: string;
  title: string;
  covers: string;
  weight: number;
  format: string;
}

export interface Concept { term: string; definition: string; }
export interface DerivationStep { title: string; latex: string; explanation: string; }
export interface EquationOut { latex: string; description: string; name: string; }
export interface SolutionStep { latex: string; text: string; }

export interface WorkedExample {
  statement: string;
  given: string[];
  steps: SolutionStep[];
  answer: string;
  engineering_note: string;
}

export interface QuizItem {
  question: string;
  answer: string;
  options: string[];
  correct_index: number;
  kind: string;
}

export interface LabParameter {
  key: string;
  label: string;
  minimum: number;
  maximum: number;
  default: number;
  step: number;
  unit: string;
}

export interface Computation {
  caption: string;
  code: string;
  parameters: LabParameter[];
  expected_output: string;
}

export interface VisualizationOut {
  kind: string;
  tool: string;
  description: string;
  how_to_draw: string;
}

export interface ManimRef {
  scene: string;
  module: string;
  title: string;
  summary: string;
}

export interface FigureParam {
  key: string; label: string; minimum: number; maximum: number;
  default: number; step: number; unit: string;
}
export interface FigureCurve {
  label: string; expr: string;
  color: "tension" | "compress" | "mark" | "rule" | "ink";
  dashed: boolean; when: string;
}
export interface FigureReadout {
  label: string; expr: string; unit: string;
  color: "tension" | "compress" | "mark" | "rule" | "ink"; text: string;
}
export interface FigureSpec {
  kind: "plot" | "element" | "mohr" | "beam" | "field" | "shape" | "polar" | "bars" | "section";
  title: string;
  caption: string;
  params: FigureParam[];
  curves: FigureCurve[];
  readouts: FigureReadout[];
  x_label: string;
  y_label: string;
  x_min: string;
  x_max: string;
  options: Record<string, string>;
  note: string;
}

export interface Lesson {
  physical_problem: string;
  concepts: Concept[];
  derivation: DerivationStep[];
  formula_meaning: string;
  equations: EquationOut[];
  conditions: string;
  worked_example: WorkedExample;
  computation: Computation;
  visualization: VisualizationOut;
  interpretation: string;
  common_mistakes: string[];
  quiz: QuizItem[];
  bridge_to_next: string;
  research_extension: string;
  manim: ManimRef | null;
  figures: FigureSpec[];
}

export interface TopicDetail extends TopicBrief {
  lesson: Lesson;
  mathematical_core: string;
  engineering_application: string;
  computational_component: string;
  visualization_component: string;
  research_extension: string;
  previous_link: string;
  subject_title: string;
  prev_topic: string | null;
}

export interface RunValue { label: string; value: number; unit: string; }
export interface RunSeries { label: string; x: number[]; y: number[]; xlabel: string; ylabel: string; }
export interface RunTable { title: string; headers: string[]; rows: string[][]; }

export interface RunResponse {
  ok: boolean;
  values: RunValue[];
  notes: string[];
  series: RunSeries[];
  tables: RunTable[];
  stdout: string;
  error: string;
  error_type: string;
  duration_ms: number;
}

export interface GraphNode {
  id: string; title: string; subject_id: string;
  module_id: string; order: number; difficulty: string;
}
export interface GraphEdge { source: string; target: string; kind: string; }
export interface GraphResponse { nodes: GraphNode[]; edges: GraphEdge[]; }

export interface AuditCheck {
  key: string; question: string; passed: boolean;
  detail: string; offenders: string[];
}
export interface AuditResponse {
  passed: boolean;
  checks: AuditCheck[];
  counts: Record<string, number>;
}

export interface ProjectStage { name: string; detail: string; }
export interface FinalProject {
  id: string;
  subject_id: string;
  title: string;
  problem_statement: string;
  stages: ProjectStage[];
  deliverables: string[];
  starter_code: string;
  evaluation: string[];
  parameters: LabParameter[];
}

export interface ResourceOut {
  id: number; subject_id: string; title: string;
  author: string; year: string; kind: string; note: string;
}
