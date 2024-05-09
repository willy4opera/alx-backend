#!/usr/bin/yarn dev

// Node Redis client publisher and subscriber 
import { createClient } from 'redis';

const rsClient = createClient();
const EXIT_MSG = 'KILL_SERVER';

rsClient.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

rsClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

rsClient.subscribe('holberton school channel');

rsClient.on('message', (_err, msg) => {
  console.log(msg);
  if (msg === EXIT_MSG) {
    rsClient.unsubscribe();
    rsClient.quit();
  }
});
