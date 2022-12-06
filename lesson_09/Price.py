import json
from dataclasses import dataclass
from pathlib import Path


class ExchangeRate:
    def __init__(self, currency: str, amount: float) -> None:
        self.amount: float = amount
        self.currency: str = currency

    def __str__(self) -> str:
        return f"Price({self.amount}, {self.currency})"

    def __add__(self, other: "ExchangeRate"):
        if self.currency and other.currency not in er_service.rates:
            return "currency is not supported"
        if self.currency == other.currency:
            return ExchangeRate(
                amount=self.amount + other.amount,
                currency=self.currency,
            )
        else:
            self_result = self.amount / er_service.rates[self.currency]
            other_result = other.amount / er_service.rates[other.currency]
            self.currency = "usd"
            return self_result + other_result, self.currency

    def __sub__(self, other: "ExchangeRate"):
        if self.currency and other.currency not in er_service.rates:
            return "currency is not supported"
        if self.currency == other.currency:
            return ExchangeRate(
                amount=self.amount - other.amount,
                currency=self.currency,
            )
        else:
            self_result = self.amount / er_service.rates[self.currency]
            other_result = other.amount / er_service.rates[other.currency]
            self.currency = "usd"
            return self_result - other_result, self.currency


@dataclass
class Price(ExchangeRate):
    currency: str
    amount: float


class ExchangeRatesService:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, filename: Path) -> None:
        if self._initialized:
            return

        self.filename: Path = filename
        self.rates: dict = self._get_rates()
        self._initialized = True

    def _get_rates(self):
        with open(self.filename) as file:
            print("READING FROM FILE...")
            raw_data: str = file.read()
            data: dict = json.loads(raw_data)
        return data["results"]


FILENAME = Path(__file__).parent / "exchange.json"
er_service = ExchangeRatesService(FILENAME)


def main():
    p = Price(currency="eur", amount=45)
    p1 = Price(currency="ua", amount=34)
    p2 = Price(currency="usd", amount=100)
    p3 = p + p1
    p4 = p2 - p1
    print(p3, p4)


if __name__ == "__main__":
    main()
