import React from 'react';
import { NavLink } from "react-router-dom";

function Navbar() {
  return (
    <div>
      <nav>
        <NavLink exact to="/"> Home </NavLink>
        <NavLink to="/player"> Player </NavLink>
        <NavLink to="/player-list"> PlayerList </NavLink>
      </nav>
    </div>
  );
}

export default Navbar;
