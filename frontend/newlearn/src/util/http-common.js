import axios from 'axios';

// axios 객체 생성
export default axios.create({
    // 배포용
    // baseURL: "https://13.125.110.84:8080",
    // 로컬용
    baseURL:"http://localhost:8000", 
        headers: {
        'Content-Type': 'application/json',
        },
  });