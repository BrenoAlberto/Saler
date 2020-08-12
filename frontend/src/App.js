import React from "react";
import Pages from "./pages";
import "./App.css";

const App = () => {
  return (
    <div className="container">
      <Pages />
    </div>
  );
};

// api.estate              DELETE, GET, PUT  /api/v1/estates/<id>
// api.estate_agency       DELETE, GET, PUT  /api/v1/estate_agencies/<id>
// api.estate_agency_list  GET, POST         /api/v1/estate_agencies
// api.estate_list         GET, POST         /api/v1/estates

export default App;
