const mongoose = require('mongoose');

const connectDB = async () => {
  try {
    const mongoUri = process.env.MONGO_URI || 'mongodb://localhost:27017/marketplace_ops';
    await mongoose.connect(mongoUri, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });

    console.log('✅ MongoDB connected');
    return true;
  } catch (error) {
    console.warn('⚠️  MongoDB connection failed, using mock data:', error.message);
    return false;
  }
};

module.exports = connectDB;
