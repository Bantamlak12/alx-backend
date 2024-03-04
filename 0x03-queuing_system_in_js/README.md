# Project: 0x03. Queuing System in JS

## Resources

#### Read or watch:

- [Redis quick start](https://redis.io/docs/install/install-redis/)
- [Redis client interface](https://redis.io/docs/connect/cli/)
- [Redis client for Node JS](https://github.com/redis/node-redis)
- [Kue](https://github.com/Automattic/kue) deprecated but still use in the industry

## Learning Objectives

- How to run a Redis server on your machine
- How to run simple operations with the Redis client
- How to use a Redis client with Node JS for basic operations
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to the build a basic Express app interacting with a Redis server and queue

## How to install redis

Download, extract, and compile the latest stable Redis version (higher than 5.0.7) - [https://redis.io/download/]()

```
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
```

- Start Redis in the background with `src/redis-server`

```
$ src/redis-server &
```

- Make sure that the server is working with a ping `src/redis-cli ping`

```
PONG
```

```
$ src/redis-cli ping -p [PID_OF_Redis_Server]
```

Using the Redis client again, set the value `School` for the key `Holberton`

```
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"
```

- Kill the server with the process id of the redis-server (hint: use `ps` and `grep`)

```
$ lsof -i:[PID_OF_Redis_Server]
```

```
$ kill [PID_OF_Redis_Server]
```

## Tasks

| Task                                                            | File                                                                     |
| --------------------------------------------------------------- | ------------------------------------------------------------------------ |
| 0. Install a redis instance                                     | [README.md](./README.md), [dump.rdb](./dump.rdb)                         |
| 1. Node Redis Client                                            | [0-redis_client.js](./0-redis_client.js)                                 |
| 2. Node Redis client and basic operations                       | [1-redis_op.js](./1-redis_op.js)                                         |
| 3. Node Redis client and async operations                       | [2-redis_op_async.js](./2-redis_op_async.js)                             |
| 4. Node Redis client and advanced operations                    | [4-redis_advanced_op.js](./4-redis_advanced_op.js)                       |
| 5. Node Redis client publisher and subscriber                   | [5-subscriber.js](./5-subscriber.js), [5-publisher.js](./5-publisher.js) |
| 6. Create the Job creator                                       | [6-job_creator.js](./6-job_creator.js)                                   |
| 7. Create the Job processor                                     | [6-job_processor.js](./6-job_processor.js)                               |
| 8. Track progress and errors with Kue: Create the Job creator   | [7-job_creator.js](./7-job_creator.js)                                   |
| 9. Track progress and errors with Kue: Create the Job processor | [7-job_processor.js](./7-job_processor.js)                               |
| 10. Writing the job creation function                           | [8-job.js](./8-job.js)                                                   |
| 11. Writing the test for job creation                           | [8-job.test.js](./8-job.test.js)                                         |
| 12. In stock?                                                   | [9-stock.js](./9-stock.js)                                               |
