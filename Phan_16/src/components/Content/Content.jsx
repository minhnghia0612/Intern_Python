import "./Content.css";

function Content(props) {
    return(
        <>
        <li className ="content-item">
            <img src={props.image} alt={props.image} />
            <h3>{props.title}</h3>
            <div className="des">
                <p>{props.price}</p>
                <p>{props.area}</p>
            </div>
        </li>
        </>
    )
}
export default Content;