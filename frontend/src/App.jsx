import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Main from "./pages/Main";
import Aboutme from "./pages/Aboutme";
import Gallery from "./pages/Gallery";

function App() {
  return (
    <Router>
      <Routes>
        {/*기본 루트*/}
        <Route path="/" element={<Main />} />
        {/*메인 페이지*/}
        <Route path="/home" element={<Main />} />
        {/*자기소개 페이지*/}
        <Route path="/about" element={<Aboutme />} />
        {/*갤러리 페이지*/}
        <Route path="/gallery" element={<Gallery />} />

      </Routes>
    </Router>
  );
}

export default App;