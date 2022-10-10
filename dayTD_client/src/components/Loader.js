import React from 'react';
import ReactLoading from 'react-loading';
function Loader({type, spinColor, fontColor, minHeight="0px", message="loading"}) {
  return (
    <div className="contentWrap" style={{
      height: "100%",   
      minHeight:`${minHeight}`,
      display:"flex",
      alignItems:"center",
      justifyContent:"center"}}> 
      <div style={{
        width:"100%",
        height:"100%",
        margin:"auto",
        display: "flex",
        flexDirection:"column",
        justifyContent:"center",
        alignItems:"center",
        }}>
        <ReactLoading
          type={type}
          color={spinColor}
          width={'10%'} />
        <p style={{color:`${fontColor}`}}>{message}</p>
      </div>
    </div>
  );
}
export default Loader;