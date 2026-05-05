const mongoose = require('mongoose');

const vendorSchema = new mongoose.Schema({
  name: { type: String, required: true, unique: true },
  email: { type: String, required: true, unique: true },
  phone: { type: String },
  rating: { type: Number, default: 4.5 },
});

module.exports = mongoose.model('Vendor', vendorSchema);
