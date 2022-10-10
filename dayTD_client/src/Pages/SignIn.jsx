import axios from 'axios';
import React, { memo, useEffect, useState } from "react";
import { Link, useNavigate } from 'react-router-dom';

const SignIn = memo((props) => {
  const navigate = useNavigate();
  const sessionStorage = window.sessionStorage;
  const [users, setUsers] = useState("");
  const [id, setUserId] = useState("");
  const [password, setPassword] = useState("");
  const [noti, setNoti] = useState(false);

  const onChangeUserId = (e) => {
    setUserId(e.target.value);
  };

  const onChangePassword = (e) => {
    setPassword(e.target.value);
  };

  const fetchUser = async()=>{
    try{
      const url = `${process.env.REACT_APP_URL}/account/api/user/`
      const response = await axios.get(url,{withCredentials:true});
      setUsers(response.data);
    } catch(e){
      console.log(e);
    }
  }

  useEffect(()=>{
    fetchUser();
  },[])

  const close = ()=>{
    props.close();
    setNoti(false);
    setUserId("");
    setPassword("");
  }
  const loginClickHandler = () => {
    users.forEach((user)=>{
      if(user.user===id && user.password ===password){
        sessionStorage.setItem("loginId", id);
        alert(`${JSON.stringify(sessionStorage.loginId)}님 로그인 성공`)
        navigate('/');
        close();
      }
    })
    if(!JSON.stringify(sessionStorage.loginId)){
      setNoti(true);
    }
  };

  const onCheckEnter = (e) => {
    if(e.key === 'Enter') {
      loginClickHandler()
    }
  }

  return (
    <> 
    {props.isModal?(
    <div className='modal'>
      <section id="login" className='loginContainer'>
        <h1 className='logo'>DayTD</h1>
        
        <form type="text" id="idForm" className='formBox'>
          <h4>아이디</h4>
          <input type="text" name="id" id="id" maxLength="20" value={id}
          placeholder="ID" className='input' onChange={onChangeUserId}/>
        </form>
        <form type="Password" id="pwForm" className='formBox' onKeyPress={onCheckEnter}>
          <h4>Password</h4>
          <input type="Password" name="password" id="password" maxLength="20" value={password}
          placeholder="비밀번호" className='input' onChange={onChangePassword}/>
        </form>
        <div className={`noti ${noti?'active':'none'}`}>아이디 혹은 비밀번호가 잘못됐습니다.</div>
        <div className='option'>
          <Link to="/SignUp" onClick={close}>
            <button className='signUp'>회원가입하기</button>
          </Link>
        </div>
        <div className='submit' onClick={loginClickHandler}>
          <button>로그인하기</button>
        </div>   
      </section>
    </div>):null}
  </>
  );
});

export default SignIn;