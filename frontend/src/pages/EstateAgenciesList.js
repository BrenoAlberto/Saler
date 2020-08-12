import React, { useState, useEffect } from "react";
import axios from "axios";
import EstateGrid from "../components/estates/EstateGrid";

const EstateAgenciesList = () => {
  const [items, setItems] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchItems = async () => {
      const result = await axios(
        `http://localhost:5000/api/v1/estate_agencies`
      );

      setItems(result.data.items);
      setIsLoading(false);
    };
    fetchItems();
  }, []);

  return <EstateGrid isLoading={isLoading} items={items} />;
};

export default EstateAgenciesList;
