import React, { useState } from 'react';
import CateBtn from '../../../components/cateBtn';
import CodyBest from './codyBest';
import CodyMy from './codyMy';

const RecoCody = () => {
  const [codyContent, setCodyContent] = useState('best');

  const codyComponent = {
    best: <CodyBest/>,
    cody1: <CodyMy nav='cody1'/>,
    cody2: <CodyMy nav='cody2'/>,
    cody3: <CodyMy nav='cody3'/>,
  }

  const btnSetting = content =>{
    setCodyContent(content);
  }

  return (
    <div className='recoContainer'>
      <div className='btnContainer'>
        <CateBtn content='Best!' nav='best' btnSetting={btnSetting}/>
        <CateBtn content='출근룩' nav='cody1' btnSetting={btnSetting}/>
        <CateBtn content='일상룩' nav='cody2' btnSetting={btnSetting}/>
        <CateBtn content='데이트룩' nav='cody3' btnSetting={btnSetting}/>
      </div>
      {codyContent && <div className='content_container'>{codyComponent[codyContent]}</div>}
    </div>
  );
};

export default RecoCody;