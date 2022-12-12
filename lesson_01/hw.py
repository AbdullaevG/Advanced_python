import time
import logging

logger = logging.getLogger("custom")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(levelname)s\t%(message)s")
handler.setFormatter(formatter)
 
logger.addHandler(handler)

class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.order = 0
        self.t = time.time()


class LRUCache:

    def __init__(self, limit=42):
        self.items = []
        self.count = 0
        self.limit = limit
        logger.info(f"Create new instance with {limit=}")

    def get(self, key):
        logger.info(f"Seek the value for {key=} ...")
        for item in self.items:
            if item.key == key:
                item.order += 1
                item.t = time.time()
                time.sleep(0.0001)
                logger.info(f"Value is finded!!!")
                return item.value
        logger.error(f"Ups! This key isn't in the cache")
        return None

    def get_min_value_idx(self, field, idx_array):
        min_value = float("inf")
        idx = 0

        for temp_idx in idx_array:
            item = self.items[temp_idx]

            if field == "order":
                temp_value = item.order
            else:
                temp_value = item.t

            if temp_value < min_value:
                min_value = temp_value
                idx = temp_idx

        return idx

    def get_idx_list(self, min_value):
        idx_array = []
        for idx, item in enumerate(self.items):
            if item.order == min_value:
                idx_array.append(idx)
        return idx_array

    def set(self, key, value):
        item = Item(key, value)
        logger.info(f"Try to set for key: {key} the value: {value} ...")
        if self.count == self.limit:
            logger.info("The cache is full, trying to free up space...")
            # get idx of item with minimal order
            min_value_idx = self.get_min_value_idx(field="order", idx_array=range(len(self.items)))

            # minimal order value
            min_value_order = self.items[min_value_idx].order

            # get the indexes of items with order == minimal_order_value
            idx_array = self.get_idx_list(min_value_order)

            # remove from elements with minimal order the item which has minimal time attribute
            remove_idx = self.get_min_value_idx(field="time", idx_array=idx_array)

            # add new element
            logger.info(f"Remove the key {self.items[remove_idx].key} from cache")
            self.items[remove_idx] = item
            logger.info(f"New key was added!!!")
        else:
            logger.info(f"There is an empty space in cache")
            self.items.append(item)
            self.count += 1
            logger.info(f"New key was added!!!")
    def info(self):
        for item in self.items:
            print(item.key, item.order, item.t)
