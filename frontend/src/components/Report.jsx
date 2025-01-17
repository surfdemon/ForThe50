import React, { useState } from "react";
import axios from "axios";
import { Container, Row, Col, Form, Button } from "react-bootstrap";
import Datetime from "react-datetime";
import "react-datetime/css/react-datetime.css";
import styles from "../styles/Report.module.css";
import ChainImg from "../assets/images/chain.svg";

function Report() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    location: "",
    description: "",
    date_and_time: "",
    category: "",
    country: "",
    authority: "",
  });

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleDateChange = (date) => {
    setFormData((prev) => ({
      ...prev,
      date_and_time: date.format("YYYY-MM-DD HH:mm"),
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("Submitting data:", formData);
    try {
      const response = await axios.post("/api/report/create/", formData);
      alert("Report successfully submitted!");
    } catch (error) {
      console.error("Error submitting report:", error);
      alert("Failed to submit the report.");
    }
  };

  return (
    <div className="main-content d-flex justify-content-center align-items-center">
      <img
        src={ChainImg}
        alt="Map Background"
        className={`${styles.chainImage}`}
      />
      <Container>
        <h1 className={`${styles.pageHeader} text-center mt-5`}>
          Be the Voice for the Voiceless.
        </h1>
        <Row className="justify-content-center">
          <Col xs={12} md={8} lg={8}>
            <div
              className={`${styles.reportContainer} mt-5 mb-5 p-4 rounded shadow`}
            >
              <h2 className="text-center mb-4">Report a Crime</h2>
              <Form onSubmit={handleSubmit}>
                <Form.Group className="mb-3" controlId="name">
                  <Form.Label className={`${styles.formLabel}`}>
                    Name (optional)
                  </Form.Label>
                  <Form.Control
                    className={`${styles.formInput}`}
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                  />
                </Form.Group>

                <Form.Group className="mb-3" controlId="email">
                  <Form.Label className={`${styles.formLabel}`}>
                    Email (optional)
                  </Form.Label>
                  <Form.Control
                    className={`${styles.formInput}`}
                    type="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                  />
                </Form.Group>

                <Form.Group className="mb-3" controlId="location">
                  <Form.Label className={`${styles.formLabel}`}>
                    Location*
                  </Form.Label>
                  <Form.Control
                    className={`${styles.formInput}`}
                    type="text"
                    name="location"
                    required
                    value={formData.location}
                    onChange={handleChange}
                  />
                </Form.Group>

                <Form.Group className="mb-3" controlId="description">
                  <Form.Label className={`${styles.formLabel}`}>
                    Description*
                  </Form.Label>
                  <Form.Control
                    className={`${styles.formInput}`}
                    as="textarea"
                    name="description"
                    rows={3}
                    required
                    value={formData.description}
                    onChange={handleChange}
                  />
                </Form.Group>

                <Form.Group className="mb-3" controlId="date_and_time">
                  <Form.Label className={`${styles.formLabel}`}>
                    Date and Time*
                  </Form.Label>
                  <Datetime
                    onChange={handleDateChange}
                    inputProps={{ placeholder: "Select date and time" }}
                  />
                </Form.Group>

                <Form.Group className="mb-3" controlId="category">
                  <Form.Label className={`${styles.formLabel}`}>
                    Category*
                  </Form.Label>
                  <Form.Control
                    className={`${styles.formInput}`}
                    as="select"
                    name="category"
                    required
                    value={formData.category}
                    onChange={handleChange}
                  >
                    <option value="">- Select Category -</option>
                    <option value="Sexual Exploitation">
                      Sexual Exploitation
                    </option>
                    <option value="Labor Exploitation">
                      Labor Exploitation
                    </option>
                    <option value="Child Exploitation">
                      Child Exploitation
                    </option>
                    <option value="Organ Harvesting">Organ Harvesting</option>
                    <option value="Forced Begging">Forced Begging</option>
                    <option value="Forced Crime">Forced Crime</option>
                  </Form.Control>
                </Form.Group>

                <Form.Group className="mb-3" controlId="country">
                  <Form.Label className={`${styles.formLabel}`}>
                    Country*
                  </Form.Label>
                  <Form.Control
                    className={`${styles.formInput}`}
                    as="select"
                    name="country"
                    required
                    value={formData.country}
                    onChange={handleChange}
                  >
                    <option value="">- Select Country -</option>
                    <option value="United Kingdom">United Kingdom</option>
                    <option value="Ireland">Ireland</option>
                  </Form.Control>
                </Form.Group>

                <Form.Group className="mb-3" controlId="authority">
                  <Form.Label className={`${styles.formLabel}`}>
                    Authority*
                  </Form.Label>
                  <Form.Control
                    className={`${styles.formInput}`}
                    as="select"
                    name="authority"
                    required
                    value={formData.authority}
                    onChange={handleChange}
                  >
                    <option value="">- Select Authority -</option>
                    <option value="Modern Slavery & Exploitation Helpline">
                      Modern Slavery & Exploitation Helpline
                    </option>
                    <option value="Crimestoppers">Crimestoppers</option>
                    <option value="An Garda Síochána (HTICU)">
                      An Garda Síochána (HTICU)
                    </option>
                    <option value="Department of Justice and Equality (AHTU)">
                      Department of Justice and Equality (AHTU)
                    </option>
                    <option value="Testing Authority">Testing Authority</option>
                  </Form.Control>
                </Form.Group>

                <Button
                  type="submit"
                  className={`${styles.submitBtn} w-100 mt-4`}
                  variant="primary"
                >
                  Submit Report
                </Button>
              </Form>
            </div>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default Report;
