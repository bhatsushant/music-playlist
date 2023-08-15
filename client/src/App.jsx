import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LandingPage from './LandingPage';
import FindSong from './FindSong';
import React from 'react';
import './App.css';
import ParticlesBackground from './ParticlesBackground';
function App() {
  return (
    <>
      <div className='App'>
        <ParticlesBackground></ParticlesBackground>
        <Router>
          <Routes>
            <Route path='/' element={<LandingPage />}></Route>
            <Route path='/findSong' element={<FindSong />}></Route>
          </Routes>
        </Router>
      </div>
    </>
  );
}

export default App;
