const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

// DATA
const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

// IN STOKE REDIS
const client = redis.createClient();
// Promisify getCurrentReservedStockById function to work with async/await
const getAsync = promisify(client.get).bind(client);

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// DATA ACCESS
const getItemById = (itemId) => {
  return listProducts.filter((item) => item.itemId === itemId)[0];
};

const reserveStockById = (itemId, stoke) => {
  client.set(`item.${itemId}`, stoke);
};

const getCurrentReservedStockById = async (itemId) => {
  const reservedStoke = await getAsync(`item.${itemId}`);
  return reservedStoke;
};

// SERVER
// PRODUCT DETAIL
const app = express();
const PORT = 1245;

app.listen(PORT, () => {
  console.log(`App is runnning on port: ${PORT}`);
});

// PRODUCTS
app.get('/list_products', (req, res) => {
  return res.status(200).json(listProducts);
});
app.get('/list_products/:itemId', async (req, res) => {
  const currentProduct = getItemById(req.params.itemId * 1);

  if (!currentProduct)
    return res.status(404).json({ status: 'Product not found' });

  const currentAvailableStoke = await getCurrentReservedStockById(
    req.params.itemId * 1
  );

  const stoke =
    currentAvailableStoke !== null
      ? currentAvailableStoke
      : currentProduct.initialAvailableQuantity;

  currentProduct.currentQuantity = stoke;

  return res.status(200).json(currentProduct);
});
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = req.params.itemId * 1;
  const item = getItemById(itemId);

  if (!item) return res.status(404).json({ status: 'Product not found' });

  let stokeAvailable = await getCurrentReservedStockById(itemId);
  if (stokeAvailable === null) stokeAvailable = item.initialAvailableQuantity;

  if (+stokeAvailable < 1) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  reserveStockById(itemId, +stokeAvailable - 1);
  return res.json({ status: 'Reservation confirmed', itemId });
});
