import React from "react";
import EstateItem from "./EstateItem";
import Spinner from "../ui/Spinner";
import { CardDeck } from "react-bootstrap";

const EstateGrid = ({ items, isLoading }) => {
  return isLoading ? (
    <Spinner />
  ) : (
    <CardDeck>
      {items.map((item) => (
        <EstateItem key={item.id} item={item} />
      ))}
    </CardDeck>
  );
};

export default EstateGrid;
