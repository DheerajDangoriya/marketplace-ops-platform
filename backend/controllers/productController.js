const Product = require('../models/Product');

// Mock data for when MongoDB is not available
const mockProducts = [
  {
    _id: '1',
    sku: 'PROD-001',
    name: 'Wireless Headphones',
    price: 199.99,
    stock: 45,
    vendor: 'TechCorp',
  },
  {
    _id: '2',
    sku: 'PROD-002',
    name: 'Smart Watch',
    price: 299.99,
    stock: 23,
    vendor: 'GadgetWorld',
  },
  {
    _id: '3',
    sku: 'PROD-003',
    name: 'Bluetooth Speaker',
    price: 79.99,
    stock: 67,
    vendor: 'AudioTech',
  },
];

const getProducts = async (req, res, next) => {
  try {
    if (!global.dbConnected) {
      return res.json(mockProducts);
    }

    const products = await Product.find().sort({ name: 1 });
    res.json(products);
  } catch (error) {
    next(error);
  }
};

const createProduct = async (req, res, next) => {
  try {
    const { sku, name, price, stock, vendor } = req.body;

    if (!global.dbConnected) {
      const newProduct = {
        _id: Date.now().toString(),
        sku,
        name,
        price,
        stock,
        vendor,
      };
      return res.status(201).json(newProduct);
    }

    const product = await Product.create({ sku, name, price, stock, vendor });
    res.status(201).json(product);
  } catch (error) {
    next(error);
  }
};

module.exports = { getProducts, createProduct };
