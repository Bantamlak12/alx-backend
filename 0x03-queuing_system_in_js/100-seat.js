const redis = require('redis');
const kue = require('kue');
const { promisify } = require('util');
const express = require('express');

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const queue = kue.createQueue();

// REDIS
let reservationEnabled = true;
let INITIAL_AVAILABLE_SEAT = 50;

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Functions
const reserveSeat = (number) => {
  setAsync('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const availableSeats = await getAsync('available_seats');
  return availableSeats;
};

// Set the number of available to 50
reserveSeat(INITIAL_AVAILABLE_SEAT);

// SERVER
const app = express();
const PORT = 1245;

app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  return res.json({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled)
    return res.json({ status: 'Reservation are blocked' });

  const job = queue.create('reserve_seat').save((err) => {
    if (err) return res.json({ status: 'Reservation failed' });
    return res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', () => {
    console.log(`Seat reservation job ${job.id} failed: ${job.id}`);
  });
});

app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    let availableSeats = await getCurrentAvailableSeats();
    availableSeats -= 1;

    if (+availableSeats < 0) {
      return done(new Error('Not enough seats available'));
    }
    reserveSeat(availableSeats);

    if (+availableSeats === 0) reservationEnabled = false;

    done();
  });
});

app.listen(PORT, () => {
  console.log(`The app is running on port: ${PORT}`);
});
