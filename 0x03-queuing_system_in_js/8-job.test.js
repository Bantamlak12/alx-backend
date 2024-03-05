const kue = require('kue');
const expect = require('chai').expect;
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(function () {
    // Create a new queue
    queue = kue.createQueue();
    // Enter test mode
    queue.testMode.enter();
  });

  afterEach(function (done) {
    // Crear the queue
    queue.testMode.clear();
    // Exit the test mode
    queue.testMode.exit();
    done();
  });

  it('display an error message if jobs is not an array', () => {
    expect(() => {
      createPushNotificationsJobs('string', queue);
    }).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', () => {
    const jobs = [{ data: 'job1' }, { data: 'job2' }];
    queue.create('push_notification_code_3', jobs).save();
    expect(queue.testMode.jobs.length).to.equal(1);
  });
});
