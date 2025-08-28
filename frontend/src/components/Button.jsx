import React from "react";

export default function Button({ children, onClick, type, style }) {
  return (
    <button
      type={type || "button"}   // 기본 버튼 타입은 "button"
      onClick={onClick}
      style={{
        padding: "5px 10px",
        marginTop: "10px",
        backgroundColor: "#6c63ff",
        color: "white",
        border: "none",
        borderRadius: "4px",
        cursor: "pointer",
        ...style
      }}
    >
      {children}
    </button>
  );
}