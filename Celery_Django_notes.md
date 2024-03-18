### CELERY DJANGO AND REDIS PROJECT NOTES

Celery, being a distributed task queue library for Python, offers various serialization options to serialize and deserialize task arguments and results. As of my last update in January 2022, the available serialization options in Celery include:

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

 > In Celery, you can configure these compression options in your Celery application's configuration. For example:
