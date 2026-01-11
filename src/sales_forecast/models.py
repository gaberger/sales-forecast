"""Data models for sales pipeline."""

from dataclasses import dataclass, field
from typing import Self


@dataclass
class Deal:
    """A single deal in the sales pipeline.

    Attributes:
        name: Identifier for the deal
        value: Expected deal value in dollars
        probability: Probability of closing (0.0 to 1.0)
        days_to_close: Expected days until close (used for time-based forecasts)
    """

    name: str
    value: float
    probability: float
    days_to_close: int = 30

    def __post_init__(self) -> None:
        if not 0.0 <= self.probability <= 1.0:
            raise ValueError(f"Probability must be between 0 and 1, got {self.probability}")
        if self.value < 0:
            raise ValueError(f"Deal value must be non-negative, got {self.value}")


@dataclass
class Pipeline:
    """A collection of deals representing the sales pipeline."""

    deals: list[Deal] = field(default_factory=list)

    def add_deal(self, deal: Deal) -> None:
        """Add a deal to the pipeline."""
        self.deals.append(deal)

    def total_value(self) -> float:
        """Total value of all deals in the pipeline."""
        return sum(deal.value for deal in self.deals)

    def weighted_value(self) -> float:
        """Probability-weighted value of all deals."""
        return sum(deal.value * deal.probability for deal in self.deals)

    @classmethod
    def from_list(cls, deals_data: list[dict[str, float | str | int]]) -> Self:
        """Create a Pipeline from a list of deal dictionaries."""
        deals = [
            Deal(
                name=str(d["name"]),
                value=float(d["value"]),
                probability=float(d["probability"]),
                days_to_close=int(d.get("days_to_close", 30)),
            )
            for d in deals_data
        ]
        return cls(deals=deals)
