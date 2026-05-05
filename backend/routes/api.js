const express = require('express');
const {
  getOrders,
  createOrder,
  updateOrderStatus,
} = require('../controllers/orderController');
const { getProducts, createProduct } = require('../controllers/productController');
const { getVendors, createVendor } = require('../controllers/vendorController');
const { getAnalytics } = require('../controllers/analyticsController');

const router = express.Router();

router.get('/analytics', getAnalytics);

router.get('/orders', getOrders);
router.post('/orders', createOrder);
router.put('/orders/:order_id/status', updateOrderStatus);

router.get('/products', getProducts);
router.post('/products', createProduct);

router.get('/vendors', getVendors);
router.post('/vendors', createVendor);

module.exports = router;
