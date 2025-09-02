import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Button from "../components/Button";

export default function Gallery() {
  const [images, setImages] = useState([]);
  const navigate = useNavigate();


  useEffect(() => {
    // FastAPI에서 DB 이미지 목록 가져오기
    axios.get("http://127.0.0.1:8000/upload/")
      .then(res => setImages(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <Button onClick={() => navigate("/home")}>HOME</Button>
      <h1>여기는 갤러리 페이지</h1>
      <div className="gallery-container" style={{ display: "flex", flexWrap: "wrap", gap: "10px" }}>
        {images.map(img => (
          <div key={img.id} style={{ width: "150px", height: "150px" }}>
            <img
              src={`http://127.0.0.1:8000/${img.file_path}`}
              alt={img.file_name}
              style={{ width: "100%", height: "100%", objectFit: "cover" }}
            />
          </div>
        ))}
      </div>
    </div>
  );
}
