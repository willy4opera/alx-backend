#!/usr/bin/yarn dev

import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setNewSch = (schoolID, value) => {
  client.SET(schoolID, value, print);
};

const printScholVal = (schoolID) => {
  client.GET(schoolID, (_err, reply) => {
    console.log(reply);
  });
};

printScholVal('Holberton');
setNewSch('HolbertonSanFrancisco', '100');
printScholVal('HolbertonSanFrancisco');
