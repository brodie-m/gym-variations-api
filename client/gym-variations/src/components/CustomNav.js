import React from 'react'
import {Nav, Navbar, NavbarBrand, NavLink} from 'react-bootstrap'
export default function CustomNav() {
    return (
        <div>
            <Navbar className = 'p-2 m-2 bg-light'>
                <NavbarBrand >gym variations</NavbarBrand>
                <NavLink>Home</NavLink>
                <NavLink>About</NavLink>
            </Navbar>
            
        </div>
    )
}
