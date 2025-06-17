import Content from '../Content/Content';
import {datacontent}  from '../Content/db';
import './Main-content.css';

function MainContent() {
    return(
        <div className='main-content'>
            <h2>danh sách gợi ý</h2>
            <ul className='content-list'>
                {datacontent.map((item, index) => (
                    <Content key={index} {...item} />
                ))}
            </ul>
        </div>
    )
}

export default MainContent;