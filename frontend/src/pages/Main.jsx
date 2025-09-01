import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import Button from "../components/Button";
import "./Main.css"
import { useNavigate } from "react-router-dom";


export default function Main() {
  const navigate = useNavigate();
  const [posts, setPosts] = useState([]);        // 글 목록 상태
  const [page, setPage] = useState(1)
  const postPerPage = 10;
  const [title, setTitle] = useState("");        // 글 제목 입력 상태
  const [content, setContent] = useState("");    // 글 내용 입력 상태
  const fileInputRef = useRef(null);   // 숨겨진 파일 input 참조



  const handleButtonClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);      // 서버에서 받을 필드 이름

    axios.post("http://127.0.0.1:8000/upload/", formData)
    .then((data) => console.log("업로드 완료:", data))
    .catch((err) => console.error("업로드 실패:", err));
  };

  
  // 백엔드에서 글 목록 가져오기
  const fetchPosts = () => {
    const skip = (page - 1) * postPerPage;
    axios.get(`http://127.0.0.1:8000/posts/?skip=${skip}&limit=${postPerPage}`)
      .then(res => setPosts(res.data))
      .catch(err => console.error(err));
  };

  useEffect(() => {
    fetchPosts();
  }, [page]);

  // 글 작성
  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post("http://127.0.0.1:8000/posts/", { title, content })
      .then(res => {
        console.log(res.data);
        setTitle("");       // 입력 초기화
        setContent("");     
        fetchPosts();       // 글 목록 갱신
      })
      .catch(err => console.error(err));
  };

  return (
    <>
    <div className="container">
      {/* 상단 버튼 영역*/}
      <div className="button-group">
        <Button onClick={() => navigate("/about")}>About Me</Button>
        <Button onClick={() => navigate("/gallery")}>Gallery</Button>
      </div>
      <h1>wellcome to Kevin's board</h1>
      <h2>write whatever you want!</h2>

      {/* 글 작성 폼 */}
      <form onSubmit={handleSubmit} className="post-form">
        <input
          type="text"
          placeholder="제목"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="내용"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          required
        />
        <Button type="submit">작성</Button>
        <div>
          <Button onClick={handleButtonClick}>이미지 첨부</Button>
          {/* 숨겨진 파일 input */}
          <input
            type="file"
            accept="image/*"
            ref={fileInputRef}
            style={{ display: "none" }}
            onChange={handleFileChange}
          />
        </div>
      </form>

      {/* 글 목록 */}
      <ul className="post-list">
        {posts.map(post => (
          <li key={post.id}>
            <strong>{post.title}</strong>: {post.content}
          </li>
        ))}
      </ul>
    </div>

    <div className="pagination">
      {[1, 2, 3, 4, 5].map(num => (
        <button key={num} onClick={() => setPage(num)}>{num}</button>
      ))}
    </div>
    </>
  );
}