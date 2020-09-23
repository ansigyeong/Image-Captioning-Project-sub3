import axios from 'axios';

const rest_api_key = "4b1318b8f31e1675d1e5e72a4638636f"

// axios 객체 생성
export default axios.create({
    baseURL:"https://kakaoi-newtone-openapi.kakao.com/v1/recognize", 
    headers: {
        "Access-Control-Allow-Origin": "http://localhost:8080/",
        "Content-Type": "application/octet-stream",
        "Authorization": "KakaoAK " + rest_api_key,
    },
  });