const Vendor = require('../models/Vendor');

// Mock data for when MongoDB is not available
const mockVendors = [
  {
    _id: '1',
    name: 'TechCorp',
    email: 'contact@techcorp.com',
    phone: '+1-555-0101',
    rating: 4.8,
  },
  {
    _id: '2',
    name: 'GadgetWorld',
    email: 'sales@gadgetworld.com',
    phone: '+1-555-0102',
    rating: 4.6,
  },
  {
    _id: '3',
    name: 'AudioTech',
    email: 'support@audiotech.com',
    phone: '+1-555-0103',
    rating: 4.9,
  },
];

const getVendors = async (req, res, next) => {
  try {
    if (!global.dbConnected) {
      return res.json(mockVendors);
    }

    const vendors = await Vendor.find().sort({ name: 1 });
    res.json(vendors);
  } catch (error) {
    next(error);
  }
};

const createVendor = async (req, res, next) => {
  try {
    const { name, email, phone, rating } = req.body;

    if (!global.dbConnected) {
      const newVendor = {
        _id: Date.now().toString(),
        name,
        email,
        phone,
        rating: rating || 4.5,
      };
      return res.status(201).json(newVendor);
    }

    const vendor = await Vendor.create({ name, email, phone, rating });
    res.status(201).json(vendor);
  } catch (error) {
    next(error);
  }
};

module.exports = { getVendors, createVendor };
