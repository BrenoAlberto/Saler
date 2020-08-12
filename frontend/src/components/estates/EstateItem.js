import React from "react";
import { Card } from "react-bootstrap";

const EstateItem = ({ item }) => {
  return (
    <Card style={{ width: "18rem" }}>
      <Card.Body>
        <Card.Title>{item.name}</Card.Title>
        <Card.Subtitle className="mb-2 text-muted">
          {item.address}
        </Card.Subtitle>
      </Card.Body>
    </Card>
  );
};

export default EstateItem;
