import './css/App.css'
import { Routes,Route } from 'react-router-dom'
import Home from "./pages/Home"
import Login from './pages/Login'
import Register from './pages/Register'
import ProtectedRoute from './components/ProtectedRoute'
import { AuthProvider } from './context/AuthContext'

function App() {
  return (
    <AuthProvider>
      <main className="main-content">
        <Routes>
          <Route path="/" element={<Home/>} />
    
          <Route path="/register" element={<Register/>}/>
          
          <Route path="/login" element={<Login/>}/>
        </Routes>
      </main>
    </AuthProvider>
  )
}

export default App
