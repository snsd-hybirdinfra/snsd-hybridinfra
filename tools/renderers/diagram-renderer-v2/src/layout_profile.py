from src.layout_profiles.visibility_layout import (
    resolve_layout as visibility_layout
)

from src.layout_profiles.correlation_layout import (
    resolve_layout as correlation_layout
)

from src.layout_profiles.recovery_layout import (
    resolve_layout as recovery_layout
)

from src.layout_profiles.resilience_layout import (
    resolve_layout as resilience_layout
)

from src.layout_profiles.continuity_layout import (
    resolve_layout as continuity_layout
)


LAYOUT_PROFILE_RESOLVERS = {
    "level-1-visibility": visibility_layout,
    "level-2-correlation": correlation_layout,
    "level-3-recovery": recovery_layout,
    "level-4-resilience": resilience_layout,
    "level-5-continuity": continuity_layout
}


def resolve_layout_profile(
    lifecycle: str
):

    resolver = LAYOUT_PROFILE_RESOLVERS.get(
        lifecycle
    )

    if not resolver:

        raise ValueError(
            f"Unsupported lifecycle: {lifecycle}"
        )

    return resolver()
