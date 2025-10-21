import React from "react";
// import ReactDOM from "react-dom";
import { createRoot } from "react-dom/client";
import ChatInputWidget from "./ChatInputWidget";
 // Ensure the correct path to ChatInputWidget

const container = document.getElementById("root");
const root = createRoot(container!); // createRoot(container!) if you use TypeScript

root.render(
  <React.StrictMode>
    <ChatInputWidget />
  </React.StrictMode>,
);
