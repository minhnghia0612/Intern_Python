import Content from '../Content/Content';
import {datacontent}  from '../Content/db';
import './Main-content.css';
import HousePricePredictor from '../HousePricePredictor/HousePricePredictor';

function MainContent() {
    return(
        <div className='main-content'>
            <h2>danh sách gợi ý</h2>
            <ul className='content-list'>
                {datacontent.map((item, index) => (
                    <Content key={index} {...item} />
                ))}
            </ul>
            <div className="predict-house-section">
                <h2>Dự đoán giá nhà</h2>
                <HousePricePredictor />
            </div>
        </div>
    )
}

export default MainContent;