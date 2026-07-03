from typing import List

from pydantic import BaseModel


class ReviewSummary(BaseModel):

    summary: str

    pros: List[str]

    cons: List[str]

    sentiment: str