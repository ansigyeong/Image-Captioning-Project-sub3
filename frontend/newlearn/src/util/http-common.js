import axios from 'axios';

// axios 객체 생성
export default axios.create({
    // 배포용
     baseURL: "http://j3d107.p.ssafy.io:8005",
    // 로컬용
    // baseURL:"http://localhost:8000", 
         headers: {
         'Content-Type': 'application/json',
         },
 });
