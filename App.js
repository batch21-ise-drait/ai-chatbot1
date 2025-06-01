import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from './components/Home'
import About from './components/About'
import Help from './components/Help'
import Welcome from "./components/Welcome"; // ✅ Import SlidingPage
import Contact from './components/Contact' // ✅ Add Contact Page
import Results from './components/Results'

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/help" element={<Help />} />
        <Route path="/welcome" element={<Welcome />} /> {/* ✅ Route for Slider */}
        <Route path="/contact" element={<Contact />} /> {/* ✅ Contact Page */}
        <Route path="/results" element={<Results />} /> {/* ✅ Results Page */}
      </Routes>
    </Router>
  );
};

export default App;
