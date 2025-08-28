import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Main from "./pages/Main";
import AboutMe from "./pages/Aboutme";

function App() {
  return (
    <Router>
      <Routes>
        {/*메인 페이지*/}
        <Route path="/" element={<Main />} />
        {/*자기소개 페이지*/}
        <Route path="/about" element={<AboutMe />} />

      </Routes>
    </Router>
  );
}

export default App;