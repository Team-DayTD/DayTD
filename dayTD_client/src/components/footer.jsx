import React from 'react';
import { FaGithub } from "react-icons/fa"

const Footer = () => {
  return (
    <footer className='footer'>
      <div className='discription'>
      <h2 className='title'>Lets talk 
      <FaGithub className='githubIcon'
      onClick={()=> window.open('https://github.com/Team-DayTD','_blank')}/>
      </h2>
      <h4></h4>
      <h5>
      Copyright ⓒ2022 <b className='blue'>DayTD</b> - All Rights Reserved
      </h5>
      </div>
    </footer>
  );
};

export default Footer;