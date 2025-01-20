from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import aiohttp


class BaseParser(ABC):
    @abstractmethod
    def parse_time() -> int:
        pass

class MPCParser(BaseParser):
    def __init__(self, url: str):
        super().__init__()
        self.url = url
    async def parse_time(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                text = await response.text()
        soup = BeautifulSoup(text, 'html.parser')
        time_str = soup.find(id='position').text
        total_seconds = float(time_str) / 1_000
        return total_seconds