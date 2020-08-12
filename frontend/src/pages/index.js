import React from "react";
import { Route, Switch } from "react-router-dom";
import EstateAgenciesList from "./EstateAgenciesList";
import Layout from "../components/ui/Layout";
import EstateAgencyForm from "../components/estates/EstateAgencyForm";

const Pages = () => {
  return (
    <React.Fragment>
      <Layout />
      <Switch>
        <Route exact path="/" component={EstateAgenciesList} />
        <Route
          exact
          path="/estate_agencies/add/"
          component={EstateAgencyForm}
        />
        <Route exact path="/estate_agencies" component={EstateAgenciesList} />
      </Switch>
    </React.Fragment>
  );
};

export default Pages;
