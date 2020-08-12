import React from "react";
import { Link } from "react-router-dom";
import { Navbar, Nav, NavDropdown, NavItem } from "react-bootstrap";

const Navigation = () => {
  return (
    <Navbar bg="light" expand="lg" className="mb-3">
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <NavDropdown title="Imobiliária" id="basic-nav-dropdown">
            <NavItem>
              <Nav.Link as={Link} to="/estate_agencies/add">
                Criar Imobiliária
              </Nav.Link>
            </NavItem>
            <NavDropdown.Divider />
            <NavItem>
              <Nav.Link as={Link} to="/estate_agencies">
                Listar Imobiliárias
              </Nav.Link>
            </NavItem>
          </NavDropdown>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default Navigation;
