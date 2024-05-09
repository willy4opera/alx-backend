#!/usr/bin/yarn dev

import { promisify } from 'util';
import { createClient, print } from 'redis';

const rsClient = createClient();

rsClient.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const setNewSchool = (schoolName, value) => {
  rsClient.SET(schoolName, value, print);
};

const displaySchoolValue = async (schoolName) => {
  console.log(await promisify(client.GET).bind(rsClient)(schoolName));
};

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

rsClient.on('connect', async () => {
  console.log('Redis client connected to the server');
  await main();
});
