### CELERY DJANGO AND REDIS PROJECT NOTES

Celery, being a distributed task queue library for Python, offers various serialization options to serialize and deserialize task arguments and results.  The available serialization options in Celery include:

   - JSON: This is the default serialization method in Celery. It is widely used and supported across different languages and platforms.

   - Pickle: Python's native serialization format. It allows the serialization of nearly any Python object, but it's not recommended for security reasons when dealing with untrusted input.

   - YAML: YAML (YAML Ain't Markup Language) is a human-readable data serialization format. It's less common in Celery but can be configured as a serialization option.

   - Msgpack: MessagePack is an efficient binary serialization format. It's more compact than JSON or YAML and provides faster serialization and deserialization.

>To set the serialization method in Celery, you typically configure it in your Celery application's configuration or when creating the Celery instance. For example:

Python code :

    from celery import Celery

    app = Celery('myapp', broker='amqp://guest@localhost//', backend='rpc://', 
             serializer='json')


---

### COMPRESSION METHODS FOR MESSAGE BROKER IN CELERY

In Celery, zlib and bzip2 compression refer to the compression algorithms used to compress task messages before sending them to the message broker (e.g., RabbitMQ, Redis). These compression options can help reduce the size of messages being sent across the network, leading to potential improvements in performance and resource utilization.

Here's a brief overview of each compression algorithm:

   - zlib: zlib is a widely used compression library that implements the DEFLATE compression algorithm. It is fast and provides a good balance between compression ratio and speed. It's often used for general-purpose compression in various applications and protocols.

   - bzip2: bzip2 is another compression algorithm, which is slower but often provides better compression ratios compared to zlib. It's particularly useful when space-saving is a priority and the additional compression time is acceptable.

 In Celery, you can configure these compression options in your Celery application's configuration. For example

Python Code:

    from celery import Celery

    app = Celery('myapp', broker='amqp://guest@localhost//', backend='rpc://', 
                broker_transport_options={'compression': 'bzip2'})

  > In this example, 'bzip2' compression is configured for the message broker. You can replace 'bzip2' with 'zlib' or omit the option to disable compression altogether.


---

### CELERY BROKERS/RESULT STORES

Celery supports various result backends where the results of executed tasks can be stored. Result stores in Celery include:

  - AMQP (Advanced Message Queuing Protocol): Using a message broker such as RabbitMQ or Redis. This is the default result backend and it's highly recommended for most use cases.

  - Redis: Celery can store task results in a Redis database. Redis is known for its performance and versatility, making it a popular choice for Celery result storage.

  - Memcached: Celery can also use Memcached to store task results. Memcached is a distributed memory caching system that is often used for caching frequently accessed data.

  - SQL Database: Celery supports various SQL databases like MySQL, PostgreSQL, SQLite, etc., to store task results. This option is useful if you need to query or analyze task results using SQL.

  - MongoDB: Celery can store task results in a MongoDB database. MongoDB is a NoSQL database that offers flexibility and scalability.

  - Cassandra: Celery also supports using Apache Cassandra as a result backend. Cassandra is a distributed NoSQL database known for its high availability and scalability.

  - Elasticsearch: Celery can store task results in an Elasticsearch index. Elasticsearch is a distributed search and analytics engine, which can be useful for analyzing task results.

  - Amazon S3: Celery can store task results in Amazon S3 buckets, which is useful for storing large volumes of data in a scalable and cost-effective manner.

  - Django ORM: Django ORM can also be used based on django library to save data into your django database/or setup database.

These are some of the most commonly used result stores in Celery. The choice of result store depends on factors such as performance requirements, scalability, ease of use, and existing infrastructure. You can configure the result backend in your Celery application's configuration.


---

### Worker -> Pool -> Concurrenct

When you start a celery worker, you specify the pool, concurrency, autoscale etc. in the command.

  - pool : decides who will actually perform the task - thread, child process, worker itself or else.

  - concurrency: concurrency will decide the size of the pool. By default pool size == number_of_CPU_cores_of_the_system. , 

  - autoscale: to dynamically resize the pool based on load. The autoscaler adds more pool processes when there is work to do, and starts removing processes when the workload is low.

  Please refer the following python command/code:
    
        celery -A <project>.celery worker --pool=prefork --concurrency=5 --autoscale=10,3 -l info