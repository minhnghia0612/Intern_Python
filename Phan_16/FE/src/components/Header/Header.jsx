import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import logo from '../../assets/tenomad.png'
import './Header.css'

function Header() {
  const [username, setUsername] = useState("")
  const navigate = useNavigate()

  const handleLogout = () => {
    localStorage.removeItem("token")
    navigate("/login")
    window.location.reload() // ép tải lại để mất Header và MainContent
  }

  useEffect(() => {
    const token = localStorage.getItem("token")
    if (token) {
      fetch("http://localhost:8000/me", {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
        .then(res => {
          if (!res.ok) throw new Error("Unauthorized")
          return res.json()
        })
        .then(data => {
          setUsername(data.username || data.user_name || "")
        })
        .catch(() => {
          handleLogout()
        })
    }
  }, [])

  return (
    <header className="header">
        <ul className="header-menu-left">
            <li><img src={logo} alt="logo-menu" /></li>
            <li><a href='/'>Nhà đất bán</a></li>
            <li><a href='/'>Tin tức</a></li>
            <li><a href='/'>Dự án</a></li>
            
        </ul>
        <ul className="header-menu-right">
          {username && (
          <>
            <li>{username}</li>
            <li><button onClick={handleLogout}>Logout</button></li>
          </>
        )}
        </ul>
    </header>
  );
}
export default Header;