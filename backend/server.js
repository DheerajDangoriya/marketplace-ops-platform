const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const apiRoutes = require('./routes/api');
const { errorHandler, notFound } = require('./middleware/errorMiddleware');

dotenv.config();

// Try to connect to MongoDB, but don't fail if it's not available
let dbConnected = false;
connectDB().then((connected) => {
  dbConnected = connected;
  global.dbConnected = connected;
}).catch((err) => {
  console.warn('⚠️  MongoDB not available, running with mock data:', err.message);
  dbConnected = false;
  global.dbConnected = false;
});

const app = express();
app.use(cors());
app.use(express.json());

app.use('/api', apiRoutes);

app.use(notFound);
app.use(errorHandler);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
  console.log(`📊 Database: ${dbConnected ? 'Connected' : 'Mock Data Mode'}`);
});
