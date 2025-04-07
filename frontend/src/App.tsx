// import { useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'
import NavbarSignedIn from './components/NavbarSignedIn';
import NavbarSignedOut from './components/NavbarSignedOut';
import About from './pages/About';
import Browse from './pages/Browse';
import HomeSignedIn from './pages/HomeSignedIn';
import HomeSignedOut from './pages/HomeSignedOut';
import Login from './pages/Login';
import Profile from './pages/Profile';
import Register from './pages/Register';
import Strategy from "./pages/Strategy";
import Trade from './pages/Trade';

function App() {
  // const [user, setUser] = useState<User | null>(null)
  const user = true;

  return (
    <>

    <Router>
    {user ? <NavbarSignedIn/> : <NavbarSignedOut/>} 
      <Routes>
      <Route path="/" element={user? <HomeSignedIn/> : <HomeSignedOut/>} />
        <Route path="/browse" element={<Browse />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/trade" element={<Trade />} />
        <Route path="/strategy" element={<Strategy />} />
        <Route path="/about" element={<About />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="*" element={user? <HomeSignedIn/> : <HomeSignedOut/>} />

      </Routes>
    </Router>
    
    </>
  )
}

export default App
