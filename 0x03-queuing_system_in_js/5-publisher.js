#!/usr/bin/yarn dev

// Node Redis client publisher and subscriber.

import { createClient } from 'redis';

const rsClient = createClient();

rsClient.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    rsClient.publish('holberton school channel', message);
  }, time);
};

rsClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
