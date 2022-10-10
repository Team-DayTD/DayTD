import React, {memo} from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faLocationDot  } from '@fortawesome/free-solid-svg-icons';
import Loader from '../../../components/Loader';

const Weather = memo((props) => {
    let today = new Date();
    const dayArray = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"];
    const weather = {
        1: 'sun.png',
        3: 'cloudyDay.png',
        4: 'clouds.png',
    }
    
    return (
        <div className='weather'>
            {props.GPS?
            props.loading?<Loader type="spin" spinColor="white" fontColor="white"/>
            :<section className='weatherContainer'>
                <h3 className='todayTxt'>오늘은?</h3>
                <h2 className='today'>{today.getMonth() + 1}월 {today.getDate()}일 <span className='day'>{dayArray[today.getDay()-1]}</span></h2>
                <div className='weatherBox'>
                    <img className='weatherImg' src={`${process.env.PUBLIC_URL}/images/${weather[props.GPS.sky]}`} alt=""/>
                    <ul className='temperature'>
                        <li className='TMPRT'>{props.GPS.temperture}º</li>
                        <li className='TMPRT_MinMax'>습기 : {props.GPS.humid} <p></p> 강수량 : {props.GPS.rain}</li>
                        <li className='location'><FontAwesomeIcon className='locIcon' icon={faLocationDot} />{props.loc.gu}</li>
                    </ul>
                </div>
            </section>
            :<Loader type="spin" spinColor="white" fontColor="white"/>}
        </div>
    );
})

export default Weather;