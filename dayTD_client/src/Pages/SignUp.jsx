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
      alert("???????????? ????????? ????????? ?????????.");
      setUserIdCheck(false);
      return
    }
    users.forEach((user)=>{
      if(user.use===id)
        check=false;
    })
    if(check)
      alert("???????????? ??? ?????? ??????????????????.");
    else
      alert("?????? ???????????? ??????????????????.");
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
      alert('?????? ?????? ??? ????????? ???????????????');
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
      alert('???????????? ??????!')
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
        <h1 className='title'>?????? ??????</h1>

        <form>
        <div id="signUpId" className='signUpBox'>
          <label className='subTitle' for='id'>????????? <span className='star'>*</span></label><br/>
          <input type="text" name="id" id="id" maxlength="20" value={id}
            placeholder="ID" className='input' onChange={onChangeUserId}/>
          <button type='button' className={`idCheckBtn ${idCheck?'idCheck':'idCheckBtn'}`} onClick={()=>idCheck?null:idCheckHandler()}>?????? ??????</button>
          <div className={`noti ${idError?'active':'none'}`}>?????? 5??? ??????, ????????? ????????? ??????????????????.</div>
        </div>
        <div id="signUpEmail" className='signUpBox'>
          <label className='subTitle' for='email'>????????? <span className='star'>*</span></label><br/>
          <input type="text" name=""email id="email" maxlength="50" value={email}
            placeholder="Email" className='input' onChange={onChangeEmail}/>
          <div className={`noti ${emailError?'active':'none'}`}>????????? ????????? ?????? ????????????.</div>
        </div>
        <div id="pwBox" className='signUpBox'>
          <label className='subTitle' for='password'>???????????? <span className='star'>*</span></label><br/>
          <input type="Password" name="password" id="password" maxlength="20" value={password}
            placeholder="????????????" className='input' onChange={onChangePassword}/>
          <div className={`noti ${passwordError?'active':'none'}`}>?????? 8??? ??????, ????????? ??????, ??????????????? ??????????????????. </div>
          <input type="Password" name="password" id="passwordConfirm" maxlength="20" value={passwordConfirm}
            placeholder="???????????? ?????????" className='input' onChange={onChangeConfirmPassword}/>
          <div className={`noti ${passwordConfirmError?'active':'none'}`}>??????????????? ???????????? ????????????.</div>
        </div>
        </form>
        <div id="signUpGender" className='signUpBox'>
          <p className='subTitle' >?????? <span className='star'>*</span></p>
          <label for='male'>??????</label>
          <input type="radio" name="gender" id="M" value="M"
            className='radio' checked={gender === 'M'}
            onChange={onChangeGender}/>
          <label for='female'>??????</label>
          <input type="radio" name="gender" id="W" value="W" 
            className='radio' checked={gender === 'W'}
            onChange={onChangeGender}/>
        </div>
        <div id="signUpBirthday" className='signUpBox'>
          <label className='subTitle' for='yy'>???????????? <span className='star'>*</span></label><br/>
          <select id='yy' className='select'
            value={birth.year} onChange={e =>setBirth({ ...birth, year: e.target.value })}>
            <option>???</option>
            {years.map(item => (
              <option value={item} key={item}>
                {item}
              </option>
            ))}
          </select>
          <select id='mm' className='select'
            value={birth.month} onChange={e =>setBirth({ ...birth, month: e.target.value })}>
            <option>???</option>
            {month.map(item => (
              <option value={item} key={item}>
                {item}
              </option>
            ))}
          </select>
          <select id='dd' className='select'
            value={birth.day} onChange={e =>setBirth({ ...birth, day: e.target.value })}>
            <option>???</option>
            {days.map(item => (
              <option value={item} key={item}>
                {item}
              </option>
            ))}
          </select>
        </div>
        
        <button className={`singUpSubmit ${onSubmit? 'btnAction' : 'btnInaction'}`}
          onClick={onSubmit}>????????????</button>             
      </section>
    </div>
  );
};

export default SignUp;