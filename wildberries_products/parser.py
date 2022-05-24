import asyncio

import aiohttp


async def get_data_from_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as resp:
            if resp.status == 200:
                product_data = await resp.json()
                result_dict = {
                    "Article": product_data.get("nm_id"),
                    "Brand": product_data.get("selling").get("brand_name"),
                    "Title": product_data.get("imt_name"),
                }
                return result_dict


def wildberries_parser(list_of_articles):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = []
    for article in list_of_articles:
        task = get_data_from_url(
            f"https://wbx-content-v2.wbstatic.net/ru/{article}.json"
        )
        tasks.append(task)
    results = loop.run_until_complete(asyncio.gather(*tasks))
    return [product for product in results if product is not None]
