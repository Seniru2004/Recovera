from dataclasses import dataclass, field
from typing import Dict, List, Any


@dataclass
class AgentState:
    goal: str

    contract: Dict[str, Any] = field(default_factory=dict)
    monitoring: Dict[str, Any] = field(default_factory=dict)
    incidents: List[Dict[str, Any]] = field(default_factory=list)
    emails: List[Dict[str, Any]] = field(default_factory=list)
    finance: Dict[str, Any] = field(default_factory=dict)

    evidence: List[str] = field(default_factory=list)

    completed_tools: List[str] = field(default_factory=list)

    confidence: float = 0.0

    recommendation: str = ""