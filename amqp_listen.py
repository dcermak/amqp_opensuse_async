#!/usr/bin/env python3

import aio_pika


async def main() -> None:
    connection = await aio_pika.connect(
        "amqps://opensuse:opensuse@rabbit.opensuse.org",
    )

    channel = await connection.channel()
    queue = await channel.declare_queue(exclusive=True, auto_delete=True)

    exchange = await channel.declare_exchange(
        "pubsub", type=aio_pika.ExchangeType.TOPIC, passive=True, durable=True
    )
    await queue.bind(exchange, routing_key="#")

    # Maximum message count which will be processing at the same time.
    await channel.set_qos(prefetch_count=10)

    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                print(f" [x] {message.routing_key}:{message.body.decode()}")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
