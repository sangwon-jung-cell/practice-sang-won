import React from "react";
import { useNavigate } from "react-router-dom";
import Button from "../components/Button";

export default function Gallery() {
  const navigate = useNavigate();

  return (
    <div>
      <Button onClick={() => navigate("/home")}>HOME</Button>
      <h1>Gallery Page</h1>
      <p>여기는 갤러리 페이지입니다.</p>
    </div>
  );
}