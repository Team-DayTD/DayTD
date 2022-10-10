import React, { useState, useEffect } from 'react';
import Weather from './Section/weather';
import RecoCody from './Section/RecoCody';
import axios from 'axios';

const MainPage = ()=>{
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const [GPS, setGPS] = useState();
  const [lat, setLat] = useState(60.0);
  const [lon, setLon] = useState(127.0);
  const [loc, setLoc] = useState({
    si: "",
    gu: "",
    dong: "",
  });
  
  const fetchGPS = async()=>{
    try{
      setLoading(true);
      const url = `${process.env.REACT_APP_URL}/our_weather/`
      const response = await axios.get(url, {params:{ lat:lat ,lon:lon}},
      {withCredentials:true});
      setGPS(response.data);
    } catch(e){
      setError(e);
      console.log(e);
    }
    mapApi();
    setLoading(false);
  }

  const getLocation = () => {
    if (navigator.geolocation) { // GPS를 지원하면
      navigator.geolocation.getCurrentPosition(function(position) {
        setLat(position.coords.latitude);
        setLon(position.coords.longitude);
      }, function(error) {
        console.error(error);
      }, {
        maximumAge: 0,
        enableHighAccuracy: false,
        timeout: Infinity
      });
    } else {
      alert('GPS를 지원하지 않습니다');
      return;
    }
  }

const mapApi = async () => {
  try {
    let response = await axios
      .get(
        `https://dapi.kakao.com/v2/local/geo/coord2address.json?input_coord=WGS84&x=${lon}&y=${lat}`,
        {
          headers: {
            Authorization: `KakaoAK ${process.env.REACT_APP_KAKAO_KEY}`,  
          },
        },
      )
      .then(response => {
        const location = response.data.documents[0];
        setLoc({si: location.address.region_1depth_name,
          gu: location.address.region_2depth_name,
          dong: location.address.region_3depth_name});
      });
  } catch (error) {
    // console.log(error.message);
  }
};

  useEffect(()=>{
    setError(false);
    setLoading(true);
    getLocation();
    fetchGPS();
  },[lat])
  
  return (
    <div>
      <Weather GPS={GPS} loading={loading} loc={loc}/>
      <RecoCody/>
    </div>
  );
}

export default MainPage;