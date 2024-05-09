#!/usr/bin/yarn dev

import { createClient, print } from 'redis';

const rsClient = createClient();

rsClient.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

rsClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
  rsClient.SET(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
  rsClient.GET(schoolName, (_err, reply) => {
    console.log(reply);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
