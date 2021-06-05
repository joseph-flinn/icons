# Icons Service

## Architecture
I'm saving the architecture until after I have the business logic working.

### Celery
I think celery can be used here for a really fast implementation (delivery wise)

- https://docs.celeryproject.org/en/stable/getting-started/introduction.html
- https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html#first-steps
- https://docs.celeryproject.org/en/stable/getting-started/next-steps.html#next-steps
- https://docs.celeryproject.org/en/stable/userguide/concurrency/eventlet.html#introduction

After some thought, celery might come with too much bagage.


## Architecture from scratch
### Broker
The Broker takes in requests and pushes them onto the queue and then passively waits for the response from the worker

### Queue
The long list of urls to parse

### Worker
When one of the coroutines is available, grabs the next job from the queue, grabs the icon, pushes the icon into a queue
for the brokers to pull from

