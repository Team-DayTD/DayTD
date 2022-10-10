import React, { useState, memo } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHouse,faHeart,faUser, faArrowRightFromBracket  } from '@fortawesome/free-solid-svg-icons';
import SignIn from '../Pages/SignIn';

const Navbar = memo(() => {
  const navigate = useNavigate();
  const sessionStorage = window.sessionStorage;
  const [isSIModal, SetIsSIModal] = useState(JSON.stringify(sessionStorage.loginId)?false:true);
  const [session, SetSession] = useState(false);

  const handleSignInModal = () => {
    SetIsSIModal(!isSIModal);
  };

  const handleLogOut = ()=>{
      sessionStorage.removeItem("loginId");
      navigate('/');
      SetIsSIModal(true);
      SetSession(!session);
  }

  const isLogin = ()=>{
    if(!JSON.stringify(sessionStorage.loginId)){
      navigate('/');
      SetIsSIModal(true);
    }
  }

  return (
    <div className='navContainer'>
      <nav className='nav'>
        <Link to={`/Main`} onClick={isLogin}>
          <h1 className='logo'>DayTD</h1>
        </Link>
        <ul className='menu'>
          <Link to="/Main" onClick={isLogin}>
            <li className='item'><FontAwesomeIcon icon={faHouse}/></li>
          </Link>
          <Link to="/Like" onClick={isLogin}>
            <li className='item'><FontAwesomeIcon icon={faHeart}/></li>
          </Link>
          {JSON.stringify(sessionStorage.loginId)?
          <Link to="/MyPage" onClick={isLogin}>
            <li className='item'><FontAwesomeIcon icon={faUser}/></li>
          </Link>
          :<li className='item' onClick={handleSignInModal}>
            <FontAwesomeIcon icon={faUser} onClick={isLogin}/>
          </li>}
          {JSON.stringify(sessionStorage.loginId)?
          <li className='item' onClick={handleLogOut}> 
            <FontAwesomeIcon icon={faArrowRightFromBracket}/>
          </li>
          :null
          }
        </ul>
        <SignIn isModal={isSIModal} close={handleSignInModal}/>
      </nav>
    </div>
  );
})

export default Navbar;