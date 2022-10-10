import React from 'react';

const CateBtn = (props) => {
  return (
    <button title="CateBtn" onClick={()=>{props.btnSetting(props.nav)}}
      className='cateBtn'>
      {props.content}</button>
  );
};

export default CateBtn;