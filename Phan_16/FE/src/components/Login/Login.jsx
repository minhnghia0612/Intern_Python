import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import '../Register/Register.css'
function Login({ onLogin }) {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [errorMessage, setErrorMessage] = useState("")
  const navigate = useNavigate()

  const handleLogin = async (e) => {
    e.preventDefault()

    const formData = new FormData()
    formData.append("username", username)
    formData.append("password", password)

    try {
      const response = await fetch("http://localhost:8000/token", {
        method: "POST",
        body: formData
      })

      if (response.ok) {
        const data = await response.json()
        localStorage.setItem("token", data.access_token)
        onLogin()
        navigate("/") // chuyển về trang chính
      } else {
        const error = await response.json()
        setErrorMessage(error.detail || "Incorrect username or password")
      }
    } catch (error) {
      console.error("Error:", error)
      setErrorMessage("Connect sever failed")
    }
  }

  return (
    <div className = "page">
      <div className="container">
        <h1>Login</h1>
        <form onSubmit={handleLogin}>
          <input type="text" placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} required />
          <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} required />
          <button type="submit">Login</button>
        </form>
        <p>Don't have an account? <a href="/register">Register</a></p>
        <div className="error">{errorMessage}</div>
      </div>
    </div>
  )
}

export default Login
