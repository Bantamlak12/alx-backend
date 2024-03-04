const kue = require('kue');

// Create a queue
const queue = kue.createQueue();

// Job object
const obj = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

// Create a queue named 'push_notification_code' and create a job
const job = queue.create('push_notification_code', obj).save(() => {
  // Job successful creation
  console.log(`Notification job created: ${job.id}`);
});

// Job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Job failure
job.on('failed', () => {
  console.log('Notification job failed');
});
