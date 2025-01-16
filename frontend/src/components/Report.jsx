import React, { useState } from "react";
import axios from "axios";

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
    <div className="container mt-4">
      <h2>Report to Authorities</h2>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="name" className="form-label">
            Name (optional)
          </label>
          <input
            type="text"
            className="form-control"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
          />
        </div>

        <div className="mb-3">
          <label htmlFor="email" className="form-label">
            Email (optional)
          </label>
          <input
            type="email"
            className="form-control"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
          />
        </div>

        <div className="mb-3">
          <label htmlFor="location" className="form-label">
            Location*
          </label>
          <input
            type="text"
            className="form-control"
            id="location"
            name="location"
            required
            value={formData.location}
            onChange={handleChange}
          />
        </div>

        <div className="mb-3">
          <label htmlFor="description" className="form-label">
            Description*
          </label>
          <textarea
            className="form-control"
            id="description"
            name="description"
            required
            value={formData.description}
            onChange={handleChange}
          />
        </div>

        <div className="mb-3">
          <label htmlFor="date_and_time" className="form-label">
            Date and Time*
          </label>
          <input
            type="text"
            className="form-control"
            id="date_and_time"
            name="date_and_time"
            required
            value={formData.date_and_time}
            onChange={handleChange}
          />
        </div>

        <div className="mb-3">
          <label htmlFor="category" className="form-label">
            Category*
          </label>
          <input
            type="text"
            className="form-control"
            id="category"
            name="category"
            required
            value={formData.category}
            onChange={handleChange}
          />
        </div>

        {/* Country & Authorithy */}
        <div className="mb-3">
          <label htmlFor="country" className="form-label">
            Country*
          </label>
          <select
            className="form-control"
            id="country"
            name="country"
            required
            value={formData.country}
            onChange={handleChange}
          >
            <option value="">- Select Country -</option>
            <option value="United Kingdom">United Kingdom</option>
            <option value="Ireland">Ireland</option>
          </select>
        </div>

        <div className="mb-3">
          <label htmlFor="authority" className="form-label">
            Authority*
          </label>
          <select
            className="form-control"
            id="authority"
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
          </select>
        </div>

        <button type="submit" className="btn btn-primary">
          Submit Report
        </button>
      </form>
    </div>
  );
}

export default Report;
