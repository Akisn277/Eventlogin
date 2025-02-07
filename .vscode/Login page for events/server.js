const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

// Handle form submission
app.post('/register', (req, res) => {
    const formData = req.body;
    console.log('Received form data:', formData);
    res.json({ message: 'Registration successful!', data: formData });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});