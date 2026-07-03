from pydantic import BaseModel


class RecommendationResult(BaseModel):

    recommended_product: str

    reason: str

    best_for: str

    runner_up: str

    confidence: int