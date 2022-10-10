import React, { useState, useEffect } from 'react';
import { IoIosHeart } from 'react-icons/io'
import CodyMyFilter from './codyMyFilter';
import axios from 'axios'
import Loader from '../../../components/Loader';

const CodyMy = (props) => {
    const [loading, setLoading] = useState(true);
    const [locFilterLoading, setLocFilterLoading] = useState(true);
    const [styleFilterLoading, setStyleFilterLoading] = useState(true);
    const [error, setError] = useState(false);
    const [cody, setCody] = useState();
    const [locFilterOpt, setLocFilterOpt] = useState();
    const [styleFilterOpt, setStyleFilterOpt] = useState('전체');
    const [isHeart, setIsHeart] = useState(false);
    const [likeCody, setLikeClothes] = useState();
    const [likeCodyLoading, setLikeCodyLoading] = useState(true);
    const userId = JSON.stringify(sessionStorage.loginId).replace(/\"/gi, "");
    
    const codyName = {
      cody1: "출근룩",
      cody2: "일상룩",
      cody3: "데이트룩",
    }

    // 코디 불러오기
    const fetchCody = async(style)=>{
      try{
        setLoading(true);
        const url = `${process.env.REACT_APP_URL}/clothes/api/clothes/`
        const response = await axios.get(url,{params:{user: userId, style: style}},{withCredentials:true});
        setCody(response.data);
        setIsHeart(false);
        likeCody&&likeCody.forEach((cody)=>{
          if(cody.user === userId){
            if(cody.clothes === response.data.id){
              setIsHeart(true);
            }
          }
        });
      } catch(e){
        setError(e);
        console.log(e);
      }
      setLoading(false);
    }

    // 위치 불러오기
    const fetchFilterLocOpt = async()=>{
      try{
        fetchFilterStyleOpt();
        setLocFilterLoading(true);
        const url = `${process.env.REACT_APP_URL}/clothes/api/my_location/`
        const response = await axios.get(url, {params:{user_id: userId,num_list: props.nav}},{withCredentials:true});
        setLocFilterOpt(response.data);
      } catch(e){
        setError(e);
        console.log(e);
      }
      setLocFilterLoading(false);
    }

    // 스타일 불러오기
    const fetchFilterStyleOpt = async()=>{
      try{
        setStyleFilterLoading(true);
        const url = `${process.env.REACT_APP_URL}/clothes/api/my_style/`
        const response = await axios.get(url, {params:{user_id: userId,num_list: props.nav}},{withCredentials:true});
        setStyleFilterOpt(response.data.user_style);
        fetchCody(response.data.user_style);
      } catch(e){
        setError(e);
        console.log(e);
      }
      setStyleFilterLoading(false);
    }

    
    // 찜 목록 
    const fetchLikeClothes = async()=>{
      try{
        setLikeCodyLoading(true);
        const url = `${process.env.REACT_APP_URL}/clothes/api/likes/`
        const response = await axios.get(url,{withCredentials:true});
        setLikeClothes(response.data);
        fetchFilterLocOpt(styleFilterOpt);
      } catch(e){
        setError(e);
        console.log(e);
      }
      setLikeCodyLoading(false);
    }
    
    // 찜 선택
    const fetchLike = async()=>{
      console.log('선택');
      try{
        const url = `${process.env.REACT_APP_URL}/clothes/api/likes/post/`
        const header = {"Content-type":"application/json"}
        const data= {
          like_select: true,
          user: userId,
          clothes: Number(cody.id),
          style: cody.style,
        }
        const response = await axios.post(url, data, header,{ withCredentials: true })
        setIsHeart(true);
      } catch(e){
        setError(e);
        console.log(e);
      }
    }
    
    // 찜취소
    const fetchUnlike = async()=>{
      try{
        const url = `${process.env.REACT_APP_URL}/clothes/api/likes/put/`
        const header = {"Content-type":"application/json"}
        const data= {
          like_select: false,
          user: userId,
          clothes: Number(cody.id),
          style: cody.style,
        }
        const response = await axios.put(url, data, header,{ withCredentials: true })
        setIsHeart(false);
      } catch(e){
        setError(e);
        console.log(e);
      }
    }
    
    const nextImgHandler=()=>{
      fetchCody(styleFilterOpt)
      setIsHeart(false)
    }

    useEffect(()=>{
      fetchLikeClothes();
    },[props.nav])
    
    return (
        <div className='codyMy'>
          <h3 className='title'>오늘의 {codyName[props.nav]}</h3>
          {locFilterLoading?
            <Loader type="spin" spinColor="#175A97" fontColor="#175A97"/>
            :<CodyMyFilter locOpt={locFilterOpt} styleOpt={styleFilterOpt} fetchCody={fetchCody} cate={props.nav}/>}
          <div className='btnBox'>
            <button className='nextBtn'
              onClick={nextImgHandler}>다음 코디</button>                 
          </div>
          {loading?
          <div className='codyBox codyBoxLoading'>
            <Loader type="spin" spinColor="#175A97" fontColor="#175A97" 
            minHeight="500px" message="AI가 코디를 추천하고 있어요!"/>
          </div>
          :<div className='codyBox'>
            <IoIosHeart
              onClick={isHeart?(e)=>{fetchUnlike(e.target.id)}:(e)=>{fetchLike(e.target.id)}}
              className={`heart ${isHeart?'heartActive':null}`} />
            <img className='codyImg' src={`${process.env.REACT_APP_URL}/media/clothes/${cody.style}/${cody.id}.jpg`} alt="" />
          </div>
          }
        </div>
    );
};

export default CodyMy;