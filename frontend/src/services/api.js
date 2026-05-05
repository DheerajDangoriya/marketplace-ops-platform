import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:5000/api',
  timeout: 5000,
});

export const fetchAnalytics = () => API.get('/analytics').catch(() => ({
  data: {
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
  },
}));

export const fetchOrders = () => API.get('/orders').catch(() => ({
  data: [
    { _id: '1', orderId: 'ORD-001', customer: 'John Doe', date: new Date('2024-01-15'), amount: 1250.00, status: 'Delivered' },
    { _id: '2', orderId: 'ORD-002', customer: 'Jane Smith', date: new Date('2024-01-16'), amount: 890.50, status: 'Shipped' },
    { _id: '3', orderId: 'ORD-003', customer: 'Bob Johnson', date: new Date('2024-01-17'), amount: 2100.75, status: 'Pending' },
  ],
}));

export const fetchProducts = () => API.get('/products').catch(() => ({
  data: [
    { _id: '1', sku: 'PROD-001', name: 'Wireless Headphones', price: 199.99, stock: 45, vendor: 'TechCorp' },
    { _id: '2', sku: 'PROD-002', name: 'Smart Watch', price: 299.99, stock: 23, vendor: 'GadgetWorld' },
    { _id: '3', sku: 'PROD-003', name: 'Bluetooth Speaker', price: 79.99, stock: 67, vendor: 'AudioTech' },
  ],
}));

export const fetchVendors = () => API.get('/vendors').catch(() => ({
  data: [
    { _id: '1', name: 'TechCorp', email: 'contact@techcorp.com', phone: '+1-555-0101', rating: 4.8 },
    { _id: '2', name: 'GadgetWorld', email: 'sales@gadgetworld.com', phone: '+1-555-0102', rating: 4.6 },
    { _id: '3', name: 'AudioTech', email: 'support@audiotech.com', phone: '+1-555-0103', rating: 4.9 },
  ],
}));

export default API;
