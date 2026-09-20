import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import { App } from "./App";
import "katex/dist/katex.min.css";
import "@fontsource/ibm-plex-sans-condensed/400.css";
import "@fontsource/ibm-plex-sans-condensed/600.css";
import "@fontsource/ibm-plex-sans-condensed/700.css";
import "@fontsource/ibm-plex-mono/400.css";
import "@fontsource/ibm-plex-mono/500.css";
import "@fontsource/spectral/400.css";
import "@fontsource/spectral/500.css";
import "@fontsource/spectral/600.css";
import "@fontsource/spectral/400-italic.css";
import "./styles/base.css";

const el = document.getElementById("root");
if (!el) throw new Error("#root topilmadi");

createRoot(el).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
);
