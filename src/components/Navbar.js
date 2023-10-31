import React from 'react';
import { NavLink } from "react-router-dom";

function Navbar() {
  return (
    <div>
      <nav>
        <NavLink exact to="/"> Home </NavLink>
        <NavLink exact to="/"> Games </NavLink>
        <NavLink exact to="/"> Watch </NavLink>
        <NavLink exact to="/"> News </NavLink>
        <NavLink exact to="/"> Teams </NavLink>
        <NavLink exact to="/"> Stats </NavLink>
        <NavLink exact to="/"> Standings </NavLink>
        <NavLink to="/player"> Player </NavLink>
        <NavLink to="/player-list"> PlayerList </NavLink>
      </nav>
    </div>
  );
}

export default Navbar;
