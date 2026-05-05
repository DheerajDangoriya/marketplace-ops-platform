const Order = require('../models/Order');

// Mock data for when MongoDB is not available
const mockOrders = [
  {
    _id: '1',
    orderId: 'ORD-001',
    customer: 'John Doe',
    date: new Date('2024-01-15'),
    amount: 1250.00,
    status: 'Delivered',
  },
  {
    _id: '2',
    orderId: 'ORD-002',
    customer: 'Jane Smith',
    date: new Date('2024-01-16'),
    amount: 890.50,
    status: 'Shipped',
  },
  {
    _id: '3',
    orderId: 'ORD-003',
    customer: 'Bob Johnson',
    date: new Date('2024-01-17'),
    amount: 2100.75,
    status: 'Pending',
  },
];

const getOrders = async (req, res, next) => {
  try {
    if (!global.dbConnected) {
      return res.json(mockOrders);
    }

    const orders = await Order.find().sort({ date: -1 });
    res.json(orders);
  } catch (error) {
    next(error);
  }
};

const createOrder = async (req, res, next) => {
  try {
    const { orderId, customer, amount, status } = req.body;

    if (!global.dbConnected) {
      const newOrder = {
        _id: Date.now().toString(),
        orderId,
        customer,
        amount,
        status: status || 'Pending',
        date: new Date(),
      };
      return res.status(201).json(newOrder);
    }

    const order = await Order.create({ orderId, customer, amount, status });
    res.status(201).json(order);
  } catch (error) {
    next(error);
  }
};

const updateOrderStatus = async (req, res, next) => {
  try {
    const { order_id } = req.params;
    const { status } = req.body;

    if (!global.dbConnected) {
      const order = mockOrders.find(o => o._id === order_id);
      if (!order) {
        res.status(404);
        throw new Error('Order not found');
      }
      order.status = status;
      return res.json(order);
    }

    const order = await Order.findByIdAndUpdate(
      order_id,
      { status },
      { new: true }
    );

    if (!order) {
      res.status(404);
      throw new Error('Order not found');
    }

    res.json(order);
  } catch (error) {
    next(error);
  }
};

module.exports = { getOrders, createOrder, updateOrderStatus };
