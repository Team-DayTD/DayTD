import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Popup from '../components/popup';

const SignUp = () => {
  const navigate = useNavigate();
  const [popup, setPopup] = useState({open: false, title: "", message: "", callback: false});

  const [id, setUserId] = useState("");
  const [idCheck, setUserIdCheck] = useState(false);
  const [password, setPassword] = useState("");
  const [passwordConfirm, setConfirmPassword] = useState("");
  const [gender, setGender] = useState("M");
  const [email, setEmail] = useState("");
  const [users, setUsers] = useState("");
  const [idError, setUserIdError] = useState(false);
  const [passwordError, setPasswordError] = useState(false);
  const [passwordConfirmError, setConfirmPasswordError] = useState(false);
  const [emailError, setEmailError] = useState(false);

  const now = new Date();
  let years = [];
  let month = [];
  let days = [];  
  const [birth, setBirth] = useState({
    year: "",
    month: "01",
    day: "01",
  });
  let date = new Date(birth.year, birth.month, 0).getDate();

  const onChangeUserId = (e) => {
    const userIdRegex = /^[A-Za-z0-9+]{5,}$/;
    if ((!e.target.value || (userIdRegex.test(e.target.value)))) setUserIdError(false);
    else setUserIdError(true);
    setUserId(e.target.value);
  };

  const onChangeEmail = (e) => {
    const emailRegex = /^(([^<>()\[\].,;:\s@"]+(\.[^<>()\[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/i;
    if (!e.target.value || emailRegex.test(e.target.value)) setEmailError(false);
    else setEmailError(true);
    setEmail(e.target.value);
  };
  
  const onChangePassword = (e) => {
    const passwordRegex =/^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,25}$/
    if ((!e.target.value || (passwordRegex.test(e.target.value)))) setPasswordError(false);
    else setPasswordError(true);

    if (!passwordConfirm || e.target.value === passwordConfirm) setConfirmPasswordError(false);
    else setConfirmPasswordError(true);
    setPassword(e.target.value);
  };
  const onChangeConfirmPassword = (e) => {
    if (password === e.target.value) setConfirmPasswordError(false);
    else setConfirmPasswordError(true);
    setConfirmPassword(e.target.value);
  };

  const onChangeGender = (e) => {
      setGender(e.target.value);
  };

  for (let y = now.getFullYear(); y >= 1930; y -= 1) {
    years.push(y);
  }
    
  for (let m = 1; m <= 12; m += 1) {
    if (m < 10) {
      month.push("0" + m.toString());
    } else {month.push(m.toString());}
  }
    
  for (let d = 1; d <= date; d += 1) {
    if (d < 10) {
      days.push("0" + d.toString());
    } else {days.push(d.toString());}
  }
  
  const validation = () => {
    if(!id) setUserIdError(true);
    if(!email) setEmailError(true);
    if(!password) setPasswordError(true);
    if(!passwordConfirm) setConfirmPasswordError(true);

    if(id && idCheck && password && passwordConfirm && gender && email && birth.year && birth.month && birth.day ) return true;
    else return false;
  }

  const idCheckHandler = () => {
    let check = true;
    if(idError||!id){
      alert("아이디를 제대로 입력해 주세요.");
      setUserIdCheck(false);
      return
    }
    users.forEach((user)=>{
      if(user.use===id)
        check=false;
    })
    if(check)
      alert("사용하실 수 있는 아이디입니다.");
    else
      alert("이미 존재하는 아이디입니다.");
    setUserIdCheck(check);
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

  const onSubmit = (e) => {
    const birthFormat = `${birth.year}-${birth.month}-${birth.day}`;
    console.log(id, email, password, gender, birthFormat);
    if(!validation()){
      alert('중복 확인 및 빈칸을 채워주세요');
    }
    else{
    const url = `${process.env.REACT_APP_URL}/account/api/register/`
    const header = {"Content-type":"application/json"}
    const data= {
      user: id,
      password: password,
      gender: gender,
      birth: birthFormat,
      email: email,
    }
    console.log(data);
    axios.post(url, data, header,{ withCredentials: true })
    .then(function (response) {
    console.log(response);
    if(response.status == 201){
      alert('회원가입 성공!')
      navigate('/Main');
      } else {
      let message = response.data.message;
      alert(message);
      }
      }).catch(function (error) {
        console.log(error);
      });
    }
  }

  useEffect(()=>{
    fetchUser();
  },[])


  return (
    <div className='backContainer'>
      <Popup open = {popup.open} setPopup = {setPopup} message = {popup.message} title = {popup.title} callback = {popup.callback}/>
      <section id="signUp" className='signUpContainer'>
        <h1 className='title'>회원 가입</h1>

        <form>
        <div id="signUpId" className='signUpBox'>
          <label className='subTitle' for='id'>아이디 <span className='star'>*</span></label><br/>
          <input type="text" name="id" id="id" maxlength="20" value={id}
            placeholder="ID" className='input' onChange={onChangeUserId}/>
          <button type='button' className={`idCheckBtn ${idCheck?'idCheck':'idCheckBtn'}`} onClick={()=>idCheck?null:idCheckHandler()}>중복 확인</button>
          <div className={`noti ${idError?'active':'none'}`}>최소 5자 이상, 영어와 숫자만 포함해주세요.</div>
        </div>
        <div id="signUpEmail" className='signUpBox'>
          <label className='subTitle' for='email'>이메일 <span className='star'>*</span></label><br/>
          <input type="text" name=""email id="email" maxlength="50" value={email}
            placeholder="Email" className='input' onChange={onChangeEmail}/>
          <div className={`noti ${emailError?'active':'none'}`}>이메일 형식이 맞지 않습니다.</div>
        </div>
        <div id="pwBox" className='signUpBox'>
          <label className='subTitle' for='password'>비밀번호 <span className='star'>*</span></label><br/>
          <input type="Password" name="password" id="password" maxlength="20" value={password}
            placeholder="비밀번호" className='input' onChange={onChangePassword}/>
          <div className={`noti ${passwordError?'active':'none'}`}>최소 8자 이상, 영어와 숫자, 특수문자를 포함해주세요. </div>
          <input type="Password" name="password" id="passwordConfirm" maxlength="20" value={passwordConfirm}
            placeholder="비밀번호 재확인" className='input' onChange={onChangeConfirmPassword}/>
          <div className={`noti ${passwordConfirmError?'active':'none'}`}>비밀번호가 일치하지 않습니다.</div>
        </div>
        </form>
        <div id="signUpGender" className='signUpBox'>
          <p className='subTitle' >성별 <span className='star'>*</span></p>
          <label for='male'>남성</label>
          <input type="radio" name="gender" id="M" value="M"
            className='radio' checked={gender === 'M'}
            onChange={onChangeGender}/>
          <label for='female'>여성</label>
          <input type="radio" name="gender" id="W" value="W" 
            className='radio' checked={gender === 'W'}
            onChange={onChangeGender}/>
        </div>
        <div id="signUpBirthday" className='signUpBox'>
          <label className='subTitle' for='yy'>생년월일 <span className='star'>*</span></label><br/>
          <select id='yy' className='select'
            value={birth.year} onChange={e =>setBirth({ ...birth, year: e.target.value })}>
            <option>년</option>
            {years.map(item => (
              <option value={item} key={item}>
                {item}
              </option>
            ))}
          </select>
          <select id='mm' className='select'
            value={birth.month} onChange={e =>setBirth({ ...birth, month: e.target.value })}>
            <option>월</option>
            {month.map(item => (
              <option value={item} key={item}>
                {item}
              </option>
            ))}
          </select>
          <select id='dd' className='select'
            value={birth.day} onChange={e =>setBirth({ ...birth, day: e.target.value })}>
            <option>일</option>
            {days.map(item => (
              <option value={item} key={item}>
                {item}
              </option>
            ))}
          </select>
        </div>
        
        <button className={`singUpSubmit ${onSubmit? 'btnAction' : 'btnInaction'}`}
          onClick={onSubmit}>가입하기</button>             
      </section>
    </div>
  );
};

export default SignUp;