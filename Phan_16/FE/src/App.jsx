import './App.css'
import Header from './components/Header/Header'
import MainContent from './components/Main-content/Main-content'
import Login from './components/Login/Login'
import Register from './components/Register/Register'
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import { useState, useEffect } from 'react'

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false)

  // Kiểm tra token khi load app
  useEffect(() => {
    const token = localStorage.getItem("token")
    setIsAuthenticated(!!token)
  }, [])

  return (
    <Router>
      {/* Header luôn hiển thị nếu đã đăng nhập */}
      {isAuthenticated && <Header />}
      
      <Routes>
        <Route path="/" element={isAuthenticated ? <MainContent /> : <Navigate to="/login" />} />
        
        {/* Trang đăng nhập */}
        <Route path="/login" element={<Login onLogin={() => setIsAuthenticated(true)} />} />
        
        {/* Trang đăng ký */}
        <Route path="/register" element={<Register />} />

      </Routes>
    </Router>
  )
}

export default App
