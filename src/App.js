import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Player from './components/Player';
import PlayerList from './components/PlayerList';
import './App.css';

function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/player" element={<Player />} />
          <Route path="/player-list" element={<PlayerList />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
