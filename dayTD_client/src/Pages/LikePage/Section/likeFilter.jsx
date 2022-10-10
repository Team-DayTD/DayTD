import React from 'react';

const LikeFilter = (props) => {
  const styleList = ["전체", "캐주얼","러블리","심플베이직","섹시글램","유니크","빈티지","유니섹스","기타"]

  return (
    <div className='likeFilterContainer'>
      <ul className='style'>
        {styleList.map(s=>
        (<li onClick={()=>props.changeStyle(s)} className={`styleItem ${props.style===s?'active':'default'}`}>#{s}</li>))}
      </ul>
    </div>
  );
};

export default LikeFilter;