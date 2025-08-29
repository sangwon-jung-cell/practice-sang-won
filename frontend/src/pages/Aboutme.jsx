import { motion } from "framer-motion";
import { useNavigate } from "react-router-dom";
import Button from "../components/Button";

export default function Main() {
  const navigate = useNavigate();

  return (
    <main className="min-h-screen flex items-center justify-center bg-gradient-to-br from-purple-100 to-blue-100 p-6">
      <motion.div
        className="max-w-lg w-full bg-white rounded-2xl shadow-lg p-8"
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
      >
        {/* 프로필 이미지 */}
        <div className="flex justify-center">
          <img
            src="https://via.placeholder.com/120"
            alt="profile"
            className="w-32 h-32 rounded-full border-4 border-purple-200 shadow-md"
          />
        </div>

        <Button onClick={() => navigate("/home")}>HOME</Button>

        {/* 이름 + 소개 */}
        <h1 className="text-2xl font-bold text-center mt-4 text-gray-800">
          정상원
        </h1>
        <p className="text-center text-gray-500 mt-2">
          풀스택 개발자 지망생 🚀 | React & FastAPI 공부중
        </p>

        {/* 자기소개 문단 */}
        <p className="mt-6 text-gray-700 leading-relaxed text-center">
          안녕하세요! 새로운 기술을 배우고 프로젝트로 적용하는 걸 좋아합니다.
          요즘은 <span className="font-semibold text-purple-600">React</span>와{" "}
          <span className="font-semibold text-blue-600">FastAPI</span>를 활용해
          웹 애플리케이션을 개발하고 있어요. 앞으로 더 멋진 서비스를 만들고 싶습니다!
        </p>

        {/* 소셜 링크 */}
        <div className="flex justify-center gap-6 mt-6">
          <a
            href="https://github.com/sangwon-jung-cell/practice-sang-won"
            className="text-gray-600 hover:text-black"
            target="_blank"
          >
            GitHub
          </a>
          <a
            href="https://linkedin.com/in/yourusername"
            className="text-gray-600 hover:text-blue-700"
            target="_blank"
          >
            LinkedIn
          </a>
        </div>
      </motion.div>
    </main>
  );
}
