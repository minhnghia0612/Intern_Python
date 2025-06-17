import logo from '../../assets/tenomad.png';
import './Header.css';

function Header() {
  return (
    <header className="header">
        <ul className="header-menu-left">
            <li><img src={logo} alt="logo-menu" /></li>
            <li><a href='/'>Nhà đất bán</a></li>
            <li><a href='/'>Tin tức</a></li>
            <li><a href='/'>Dự án</a></li>
        </ul>
        <ul className="header-menu-right">
            <li><a href="/">Đăng nhập</a></li>
            <li><a href="/">Đăng ký</a></li>
        </ul>
    </header>
  );
}
export default Header;