"""Load and assemble prompt text for the Pokédex agents."""

from functools import lru_cache
from pathlib import Path

import yaml

_CONFIG_PATH = Path(__file__).resolve().parents[1] / "root_agent.yaml"


@lru_cache(maxsize=1)
def load_agent_prompt_config() -> dict[str, object]:
    with _CONFIG_PATH.open(encoding="utf-8") as handle:
        config = yaml.safe_load(handle)

    if not isinstance(config, dict):
        raise ValueError("root_agent.yaml must contain a mapping at the top level.")

    return config


def _join_parts(parts: list[str]) -> str:
    return "\n\n".join(part.strip() for part in parts if part and part.strip())


def _root_spec(locale: str) -> dict[str, object]:
    roots = load_agent_prompt_config()["roots"]
    try:
        spec = roots[locale]
    except KeyError as exc:  # pragma: no cover - guarded by internal callers
        raise ValueError(f"Unknown root locale: {locale}") from exc

    if not isinstance(spec, dict):
        raise ValueError(f"root_agent.yaml roots.{locale} must be a mapping.")

    return spec


def _specialist_spec(topic: str) -> dict[str, object]:
    specialists = load_agent_prompt_config()["specialists"]
    try:
        spec = specialists[topic]
    except KeyError as exc:  # pragma: no cover - guarded by internal callers
        raise ValueError(f"Unknown specialist topic: {topic}") from exc

    if not isinstance(spec, dict):
        raise ValueError(f"root_agent.yaml specialists.{topic} must be a mapping.")

    return spec


def build_root_agent_name(locale: str) -> str:
    return _root_spec(locale)["name"]


def build_root_agent_description(locale: str) -> str:
    return _root_spec(locale)["description"]


def build_root_agent_instruction(locale: str) -> str:
    spec = _root_spec(locale)
    shared = load_agent_prompt_config()["shared"]
    routes = "\n".join(
        f"• {route['agent']}  — {route['summary']}" for route in spec["routes"]
    )
    return _join_parts(
        [
            spec["intro"],
            shared["voice"],
            spec["route_intro"],
            routes,
            spec["follow_up"],
            shared["image_instruction"],
            shared["structured_tool_output"],
            shared["factual_guardrail"],
        ]
    )


def build_specialist_agent_name(topic: str) -> str:
    return _specialist_spec(topic)["name"]


def build_specialist_agent_description(topic: str) -> str:
    return _specialist_spec(topic)["description"]


def build_specialist_agent_instruction(topic: str) -> str:
    spec = _specialist_spec(topic)
    shared = load_agent_prompt_config()["shared"]
    return _join_parts(
        [
            spec["intro"],
            shared["voice"],
            shared["specialist_language_rule"],
            shared["image_instruction"],
            shared["structured_tool_output"],
            shared["factual_guardrail"],
        ]
    )
