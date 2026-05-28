def infer_topology(
    scenario_name: str,
    lifecycle_level: str
):

    name = scenario_name.lower()

    if "vpn" in name:

        nodes, edges = vpn_topology(
            scenario_name,
            lifecycle_level
        )

    elif "database" in name or "replication" in name or "query" in name:

        nodes, edges = database_topology(
            scenario_name,
            lifecycle_level
        )

    elif "kubernetes" in name or "pod" in name or "cluster" in name:

        nodes, edges = kubernetes_topology(
            scenario_name,
            lifecycle_level
        )

    elif "security" in name or "identity" in name or "privilege" in name:

        nodes, edges = security_topology(
            scenario_name,
            lifecycle_level
        )

    elif "load-balancer" in name or "traffic" in name or "api" in name:

        nodes, edges = service_topology(
            scenario_name,
            lifecycle_level
        )

    else:

        nodes, edges = default_topology(
            scenario_name,
            lifecycle_level
        )

    nodes = apply_node_groups(
        nodes
    )

    return nodes, edges


def base_nodes(
    scenario_name: str,
    lifecycle_level: str
):

    return [
        {
            "id": "telemetry-source",
            "label": "Telemetry Source",
            "type": "source"
        },
        {
            "id": "observability-pipeline",
            "label": "Observability Pipeline",
            "type": "pipeline"
        },
        {
            "id": "analysis-engine",
            "label": "Analysis Engine",
            "type": "analysis"
        },
        {
            "id": "operations-dashboard",
            "label": "Operations Dashboard",
            "type": "dashboard"
        }
    ]


def base_edges():

    return [
        {
            "from": "telemetry-source",
            "to": "observability-pipeline",
            "label": "emit telemetry"
        },
        {
            "from": "observability-pipeline",
            "to": "analysis-engine",
            "label": "normalize signals"
        },
        {
            "from": "analysis-engine",
            "to": "operations-dashboard",
            "label": "publish findings"
        }
    ]


def vpn_topology(
    scenario_name: str,
    lifecycle_level: str
):

    nodes = [
        {
            "id": "branch-site",
            "label": "Branch Site",
            "type": "site"
        },
        {
            "id": "vpn-gateway",
            "label": "VPN Gateway",
            "type": "network"
        },
        {
            "id": "vpn-tunnel",
            "label": "VPN Tunnel",
            "type": "connectivity"
        },
        {
            "id": "telemetry-collector",
            "label": "Telemetry Collector",
            "type": "telemetry"
        },
        {
            "id": "operations-dashboard",
            "label": "Operations Dashboard",
            "type": "dashboard"
        }
    ]

    edges = [
        {
            "from": "branch-site",
            "to": "vpn-gateway",
            "label": "connects through"
        },
        {
            "from": "vpn-gateway",
            "to": "vpn-tunnel",
            "label": "establishes tunnel"
        },
        {
            "from": "vpn-tunnel",
            "to": "telemetry-collector",
            "label": "exports tunnel metrics"
        },
        {
            "from": "telemetry-collector",
            "to": "operations-dashboard",
            "label": "publishes visibility"
        }
    ]

    return apply_lifecycle_mutation(
        nodes,
        edges,
        lifecycle_level
    )


def database_topology(
    scenario_name: str,
    lifecycle_level: str
):

    nodes = [
        {
            "id": "application-service",
            "label": "Application Service",
            "type": "service"
        },
        {
            "id": "database-primary",
            "label": "Primary Database",
            "type": "database"
        },
        {
            "id": "database-replica",
            "label": "Database Replica",
            "type": "database"
        },
        {
            "id": "database-telemetry",
            "label": "Database Telemetry",
            "type": "telemetry"
        },
        {
            "id": "analysis-engine",
            "label": "Analysis Engine",
            "type": "analysis"
        }
    ]

    edges = [
        {
            "from": "application-service",
            "to": "database-primary",
            "label": "queries"
        },
        {
            "from": "database-primary",
            "to": "database-replica",
            "label": "replicates"
        },
        {
            "from": "database-primary",
            "to": "database-telemetry",
            "label": "emits metrics"
        },
        {
            "from": "database-telemetry",
            "to": "analysis-engine",
            "label": "correlates health"
        }
    ]

    return apply_lifecycle_mutation(
        nodes,
        edges,
        lifecycle_level
    )


def kubernetes_topology(
    scenario_name: str,
    lifecycle_level: str
):

    nodes = [
        {
            "id": "kubernetes-cluster",
            "label": "Kubernetes Cluster",
            "type": "cluster"
        },
        {
            "id": "worker-node",
            "label": "Worker Node",
            "type": "compute"
        },
        {
            "id": "pod-workload",
            "label": "Pod Workload",
            "type": "workload"
        },
        {
            "id": "cluster-telemetry",
            "label": "Cluster Telemetry",
            "type": "telemetry"
        },
        {
            "id": "operations-dashboard",
            "label": "Operations Dashboard",
            "type": "dashboard"
        }
    ]

    edges = [
        {
            "from": "kubernetes-cluster",
            "to": "worker-node",
            "label": "schedules workloads"
        },
        {
            "from": "worker-node",
            "to": "pod-workload",
            "label": "runs pods"
        },
        {
            "from": "pod-workload",
            "to": "cluster-telemetry",
            "label": "emits runtime signals"
        },
        {
            "from": "cluster-telemetry",
            "to": "operations-dashboard",
            "label": "publishes visibility"
        }
    ]

    return apply_lifecycle_mutation(
        nodes,
        edges,
        lifecycle_level
    )


def security_topology(
    scenario_name: str,
    lifecycle_level: str
):

    nodes = [
        {
            "id": "identity-provider",
            "label": "Identity Provider",
            "type": "identity"
        },
        {
            "id": "access-policy",
            "label": "Access Policy",
            "type": "policy"
        },
        {
            "id": "security-telemetry",
            "label": "Security Telemetry",
            "type": "telemetry"
        },
        {
            "id": "risk-analysis-engine",
            "label": "Risk Analysis Engine",
            "type": "analysis"
        }
    ]

    edges = [
        {
            "from": "identity-provider",
            "to": "access-policy",
            "label": "enforces access"
        },
        {
            "from": "access-policy",
            "to": "security-telemetry",
            "label": "emits policy events"
        },
        {
            "from": "security-telemetry",
            "to": "risk-analysis-engine",
            "label": "correlates risk"
        }
    ]

    return apply_lifecycle_mutation(
        nodes,
        edges,
        lifecycle_level
    )


def service_topology(
    scenario_name: str,
    lifecycle_level: str
):

    nodes = [
        {
            "id": "client-traffic",
            "label": "Client Traffic",
            "type": "traffic"
        },
        {
            "id": "load-balancer",
            "label": "Load Balancer",
            "type": "network"
        },
        {
            "id": "application-service",
            "label": "Application Service",
            "type": "service"
        },
        {
            "id": "service-telemetry",
            "label": "Service Telemetry",
            "type": "telemetry"
        }
    ]

    edges = [
        {
            "from": "client-traffic",
            "to": "load-balancer",
            "label": "routes through"
        },
        {
            "from": "load-balancer",
            "to": "application-service",
            "label": "distributes requests"
        },
        {
            "from": "application-service",
            "to": "service-telemetry",
            "label": "emits service signals"
        }
    ]

    return apply_lifecycle_mutation(
        nodes,
        edges,
        lifecycle_level
    )


def default_topology(
    scenario_name: str,
    lifecycle_level: str
):

    return base_nodes(
        scenario_name,
        lifecycle_level
    ), base_edges()
def apply_lifecycle_mutation(
    nodes: list,
    edges: list,
    lifecycle_level: str
):

    if lifecycle_level == "level-1-visibility":

        return nodes, edges

    last_node = nodes[-1]["id"]

    if lifecycle_level == "level-2-correlation":

        nodes.append(
            {
                "id": "correlation-engine",
                "label": "Correlation Engine",
                "type": "analysis"
            }
        )

        edges.append(
            {
                "from": last_node,
                "to": "correlation-engine",
                "label": "correlates operational signals"
            }
        )

    elif lifecycle_level == "level-3-recovery":

        nodes.append(
            {
                "id": "recovery-orchestrator",
                "label": "Recovery Orchestrator",
                "type": "automation"
            }
        )

        edges.append(
            {
                "from": last_node,
                "to": "recovery-orchestrator",
                "label": "triggers recovery workflow"
            }
        )

    elif lifecycle_level == "level-4-resilience":

        nodes.append(
            {
                "id": "resilience-coordinator",
                "label": "Resilience Coordinator",
                "type": "coordination"
            }
        )

        edges.append(
            {
                "from": last_node,
                "to": "resilience-coordinator",
                "label": "coordinates survivability"
            }
        )

    elif lifecycle_level == "level-5-continuity":

        nodes.append(
            {
                "id": "continuity-governance",
                "label": "Continuity Governance",
                "type": "governance"
            }
        )

        edges.append(
            {
                "from": last_node,
                "to": "continuity-governance",
                "label": "reports continuity posture"
            }
        )

    return nodes, edges
def apply_node_groups(
    nodes: list
):

    group_by_type = {
        "site": "connectivity",
        "network": "connectivity",
        "connectivity": "connectivity",

        "telemetry": "observability",
        "dashboard": "observability",

        "analysis": "analysis",
        "automation": "recovery",
        "coordination": "resilience",
        "governance": "governance",

        "database": "data",
        "service": "service",
        "cluster": "platform",
        "compute": "platform",
        "workload": "platform",
        "identity": "security",
        "policy": "security",
        "traffic": "service"
    }

    for node in nodes:

        node.setdefault(
            "group",
            group_by_type.get(
                node.get(
                    "type",
                    "unknown"
                ),
                "operational"
            )
        )

    return nodes


