import { faChevronDown } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import axios from 'axios';
import React, { memo, useEffect, useState } from 'react';
import location from "../../../data/location.json";

const CodyMyFilter = memo((props)=>{
  const [style, setStyle] = useState("전체");
  const [loc, setLoc] = useState({
    si:'서울특별시',
    gu:'전체',
    dong:'전체'
  });
  const [locSave, setLocSave] = useState();
  const [styleSave, setStyleSave] = useState();
  const [error, setError] = useState(false);
  const [isOpen, setToggle] = useState(false); 
  const id = JSON.stringify(sessionStorage.loginId).replace(/\"/gi, "");
  const styleList = ["캐주얼","러블리","심플베이직","섹시글램","유니크", "유니섹스","빈티지","기타"]

  const toggleBtn = () => {
    setToggle(isOpen => !isOpen); // on,off 개념 boolean
  }

  const fetchLocSave = async()=>{
    try{
      const url = `${process.env.REACT_APP_URL}/clothes/api/my_location/post/`
      const header = {"Content-type":"application/json"}
      const data= {
        user_id: id,
        si:loc.si,
        dong: loc.dong,
        gu: loc.gu,
        num_list: props.cate
      }
      const response = await axios.post(url, data, header,{ withCredentials: true })
      setLocSave(response);
      if(response.status == 201){
        alert('저장 성공!')
        props.fetchCody()
      } else {
        let message = locSave.data.message;
        alert(message);
      }
    } catch(e){
      setError(e);
      console.log(e);
    }
  }

  const fetchStyleSave = async()=>{
    try{
      const url = `${process.env.REACT_APP_URL}/clothes/api/my_style/post/`
      const header = {"Content-type":"application/json"}
      const data= {
        user_id: id,
        user_style: style,
        num_list: props.cate
      }
      const response = await axios.post(url, data, header,{ withCredentials: true })
      setStyleSave(response);
    } catch(e){
      setError(e);
      console.log(e);
    }
  }

  const onSave = () => {
    fetchLocSave();
    fetchStyleSave()
  }
  useEffect(()=>{
    setLoc({si:props.locOpt.si, 
      gu:props.locOpt.gu, 
      dong:props.locOpt.dong});
    setStyle(props.styleOpt);
  },[props.locOpt])

  return (
    <div className='filterContainer'>
        <div className='showFilter'>
        <ul className='filter'>
            <li className='clotheItem active'>#{style}룩</li>
            <li className='clotheItem active locActive'>#{`${loc.si} ${loc.gu} ${loc.dong}`}</li>
        </ul>
        <FontAwesomeIcon className={`option ${isOpen ?'option':'turn'}`} onClick={()=>toggleBtn()} icon={faChevronDown} />
        </div>
        <div className={`Hidefilter ${isOpen ?'showFilterBox':'hideFilterBox'}`}>
        <ul className='style'>
          {styleList.map(s=>
          (<li onClick={()=>setStyle(s)} className='styleItem'>#{s}</li>))}
        </ul>
        <div className='loc'>
        <select id='location' className='select'
          value={loc.si} onChange={e =>setLoc({si:e.target.value, gu:"전체",dong:"전체"})}>
          {Object.keys(location).map(si => (
            <option value={si} key={si}>
              {si}
            </option>
          ))}
        </select>
        <select id='location' className='select'
          value={loc.gu} onChange={e =>setLoc({...loc, gu:e.target.value, dong:"전체"})}>
          {Object.keys(location[loc.si]).map(gu => (
            <option value={gu} key={gu}>
              {gu}
            </option>
          ))}
        </select>
        <select id='location' className='select'
          value={loc.dong} onChange={e =>setLoc({...loc, dong:e.target.value})}>
          {location[loc.si][loc.gu].map(dong => (
            <option value={dong} key={dong}>
              {dong}
            </option>
          ))}
        </select>
        </div>
        <button className={`saveBtn ${isOpen ?'showSaveBtn':'hideSaveBtn'}`} onClick={onSave}>저장</button>
        </div>
    </div>
  );
});

export default CodyMyFilter;