"""Sandbox-only computational sketches. No networking, spawning, persistence, credentials, or external side effects."""
from dataclasses import dataclass
from typing import Dict
import math

def ant_path_update(weight: float, success: bool, reinforcement: float = 0.2, decay: float = 0.05) -> float:
    weight = max(0.0, weight * (1.0 - decay))
    return weight + reinforcement if success else weight

def bee_quorum(scores: Dict[str, float], threshold: float) -> str | None:
    if not scores: return None
    winner, support = max(scores.items(), key=lambda kv: kv[1])
    return winner if support >= threshold else None

def termite_recruit(active_workers: int, base_probability: float = 0.1) -> float:
    return min(1.0, base_probability + math.log1p(active_workers) / 10.0)

def locust_policy(local_density: float, high: float = 0.7, low: float = 0.3, current: str = "SOLITARY") -> str:
    if current == "SOLITARY" and local_density >= high: return "SWARM"
    if current == "SWARM" and local_density <= low: return "SOLITARY"
    return current

@dataclass
class EphemeralWorker:
    mission: str
    completed: bool = False
    def run_once(self) -> str:
        self.completed = True
        return f"artifact:{self.mission}"

def predictive_intercept(position: float, velocity: float, latency: float) -> float:
    return position + velocity * latency

def mantis_trigger(opportunity_score: float, threshold: float = 0.8) -> bool:
    return opportunity_score >= threshold

def cockroach_stay_probability(occupancy_ratio: float) -> float:
    x = max(0.0, min(1.0, occupancy_ratio))
    return x*x / (x*x + (1-x)*(1-x) + 1e-9)

def metamorphic_stage(stage: str) -> str:
    return {"ACQUIRE":"TRANSFORM","TRANSFORM":"DEPLOY","DEPLOY":"DONE"}.get(stage, "ACQUIRE")

def beetle_variant(kernel: Dict, adapter: Dict) -> Dict:
    return {"kernel": dict(kernel), "adapter": dict(adapter)}

def antlion_environment_transform(incoming_cost: float, structure_quality: float) -> float:
    q = max(0.0, min(1.0, structure_quality))
    return incoming_cost * (1.0 - 0.5*q)

def aphid_successor_mode(crowding: float, resource_quality: float) -> str:
    return "DISPERSAL" if crowding + (1.0-resource_quality) > 1.0 else "LOCAL_SPECIALIST"
