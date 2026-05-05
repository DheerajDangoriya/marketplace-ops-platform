const Order = require('../models/Order');
const Product = require('../models/Product');
const Vendor = require('../models/Vendor');

// Mock data for when MongoDB is not available
const mockAnalytics = {
  totalRevenue: 128430,
  totalOrders: 456,
  inStock: 1240,
  totalVendors: 82,
  pendingOrders: 23,
  shippedOrders: 189,
  chartData: [
    { name: 'Jan', revenue: 4200, orders: 120 },
    { name: 'Feb', revenue: 5300, orders: 180 },
    { name: 'Mar', revenue: 4700, orders: 150 },
    { name: 'Apr', revenue: 6100, orders: 210 },
    { name: 'May', revenue: 7000, orders: 230 },
  ],
};

const getAnalytics = async (req, res, next) => {
  try {
    // Check if we have database connection
    if (!global.dbConnected) {
      return res.json(mockAnalytics);
    }

    const totalRevenueData = await Order.aggregate([
      { $group: { _id: null, revenue: { $sum: '$amount' }, orders: { $sum: 1 } } },
    ]);

    const stockData = await Product.aggregate([
      { $group: { _id: null, inStock: { $sum: '$stock' } } },
    ]);

    const activeVendors = await Vendor.countDocuments();

    const pendingOrders = await Order.countDocuments({ status: 'Pending' });
    const shippedOrders = await Order.countDocuments({ status: 'Shipped' });

    const metrics = {
      totalRevenue: totalRevenueData[0]?.revenue || 0,
      totalOrders: totalRevenueData[0]?.orders || 0,
      inStock: stockData[0]?.inStock || 0,
      totalVendors: activeVendors,
      pendingOrders,
      shippedOrders,
      chartData: [
        { name: 'Jan', revenue: 4200, orders: 120 },
        { name: 'Feb', revenue: 5300, orders: 180 },
        { name: 'Mar', revenue: 4700, orders: 150 },
        { name: 'Apr', revenue: 6100, orders: 210 },
        { name: 'May', revenue: 7000, orders: 230 },
      ],
    };

    res.json(metrics);
  } catch (error) {
    next(error);
  }
};

module.exports = { getAnalytics };
