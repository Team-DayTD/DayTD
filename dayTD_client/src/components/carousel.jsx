import React from "react";
import Slider from "react-slick"; 

function Carousel (props,{ sliders }) {
  const settings = {
    dots: false,
    infinite: true,
    speed: 500,
    slidesToShow: 4,
    slidesToScroll: 1,
    centerPadding: '0px',
    speed: 500,
    autoplay: true, 
    autoplaySpeed: 4000, 
  }
  return(
      <div className='carouselContainer'>
				<link rel="stylesheet" type="text/css" charSet="UTF-8" href="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.6.0/slick.min.css" />
				<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.6.0/slick-theme.min.css" />
        <h3 className='title'><span className='color'>{props.title1}</span>{props.title2}{props.title3}</h3>
        <Slider {...settings}>
          {props.cody.map((cody) =>(
            <div className='codyBox' key={`box_${cody.id}`} >
              <div className='imgBox' key={`img_box_${cody.id}`} >
                <img className='codyImg' key={`img_${cody.id}`} src={`${process.env.REACT_APP_URL}/media/clothes/${cody.style}/${cody.id}.jpg`} alt="" />
              </div>
            </div>
          ))}
        </Slider>
      </div>
    );
}
export default Carousel;