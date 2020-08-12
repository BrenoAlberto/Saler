import React, { useState } from "react";
import axios from "axios";
import { Form, Button } from "react-bootstrap";
import querystring from "querystring";

const EstateAgencyForm = () => {
  const [formEstateAgency, setFormEstateAgency] = useState({});
  const [validated, setValidated] = useState(false);

  const submitEstateAgencyForm = async (event) => {
    const form = event.currentTarget;
    if (form.checkValidity() === false) {
      event.preventDefault();
      event.stopPropagation();
    } else {
      const result = await axios.post(
        `http://localhost:5000/api/v1/estate_agencies`,
        querystring.stringify(formEstateAgency)
      );

      console.log(result);
    }

    setValidated(true);
  };

  return (
    <Form noValidate validated={validated}>
      <Form.Group
        onChange={(e) =>
          setFormEstateAgency({ ...formEstateAgency, name: e.target.value })
        }
      >
        <Form.Label>Nome do Imobiliária *</Form.Label>
        <Form.Control required type="input" placeholder="Insira um nome." />
        <Form.Control.Feedback type="invalid">
          Por favor, informe o nome da imobiliária.
        </Form.Control.Feedback>
      </Form.Group>
      <Form.Group
        onChange={(e) =>
          setFormEstateAgency({ ...formEstateAgency, address: e.target.value })
        }
      >
        <Form.Label>Endereço *</Form.Label>
        <Form.Control required type="input" placeholder="Insira o endereço." />
        <Form.Control.Feedback type="invalid">
          Por favor, informe o endereço da imobiliária.
        </Form.Control.Feedback>
      </Form.Group>
      <Button variant="primary" onClick={submitEstateAgencyForm} type="button">
        Registrar Imobiliária
      </Button>
    </Form>
  );
};

export default EstateAgencyForm;
