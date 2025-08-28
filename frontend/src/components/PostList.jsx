import React, { useEffect, useState } from "react";
import axios from "axios";

export default function PostList() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/posts/")
      .then(res => setPosts(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>게시판 글 목록</h2>
      <ul>
        {posts.map(post => (
          <li key={post.id}>
            <strong>{post.title}</strong>: {post.content}
          </li>
        ))}
      </ul>
    </div>
  );
}