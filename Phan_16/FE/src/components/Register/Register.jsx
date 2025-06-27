import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import './Register.css'

function Register() {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [errorMessage, setErrorMessage] = useState("")
  const navigate = useNavigate()

  const handleRegister = async (e) => {
    e.preventDefault()

    const formData = new FormData()
    formData.append("username", username)
    formData.append("password", password)

    try {
      const response = await fetch("http://localhost:8000/users/", {
        method: "POST",
        body: formData
      })

      if (response.ok) {
        alert("Register success")
        navigate("/login")
      } else {
        const error = await response.json()
        setErrorMessage(error.detail || "Register error")
      }
    } catch (error) {
      console.error("Error:", error)
      setErrorMessage("Connect sever failed")
    }
  }

  return (
    <div className = "page">
      <div className="container">
        <h1>Register</h1>
        <form onSubmit={handleRegister}>
          <input type="text" placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} required />
          <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} required />
          <button type="submit">Register</button>
        </form>
        <p>Already have an account? <a href="/login">Login</a></p>
        <div className="error">{errorMessage}</div>
      </div>
    </div> 
  )
}

export default Register
