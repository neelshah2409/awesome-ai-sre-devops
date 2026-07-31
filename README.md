# Awesome AI SRE & DevOps [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Lint](https://github.com/neelshah2409/awesome-ai-sre-devops/actions/workflows/lint.yml/badge.svg)](https://github.com/neelshah2409/awesome-ai-sre-devops/actions/workflows/lint.yml)
[![Link Check](https://github.com/neelshah2409/awesome-ai-sre-devops/actions/workflows/link-check.yml/badge.svg)](https://github.com/neelshah2409/awesome-ai-sre-devops/actions/workflows/link-check.yml)
[![Discover New Tools](https://github.com/neelshah2409/awesome-ai-sre-devops/actions/workflows/discover-tools.yml/badge.svg)](https://github.com/neelshah2409/awesome-ai-sre-devops/actions/workflows/discover-tools.yml)
[![Site](https://img.shields.io/badge/site-live-blue)](https://neelshah2409.github.io/awesome-ai-sre-devops/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> A living, filterable directory of AI tools for DevOps, Site Reliability Engineering, and Platform Engineering — with a browsable site, weekly automated discovery, and detailed, decision-useful descriptions (not just a link dump).

**🔍 [Browse the searchable site →](https://neelshah2409.github.io/awesome-ai-sre-devops/)**

**407 tools** across **20 tool categories** — updated continuously via automated weekly discovery (see [How This Stays Updated](#how-this-stays-updated)). If this saved you time, a star helps more engineers find it. 🌟

---

## Contents

- [Tool of the Month](#tool-of-the-month)
- [Quick Picks by Use Case](#quick-picks-by-use-case)
- [AI Coding Agents for Infrastructure](#ai-coding-agents-for-infrastructure)
- [AI-Powered Kubernetes](#ai-powered-kubernetes)
- [AI-Powered Terraform and IaC](#ai-powered-terraform-and-iac)
- [AI Incident Response and AI SRE Agents](#ai-incident-response-and-ai-sre-agents)
- [AI Monitoring and Observability](#ai-monitoring-and-observability)
- [AI Security Scanning and AI SOC](#ai-security-scanning-and-ai-soc)
- [AI Cost Optimization and FinOps](#ai-cost-optimization-and-finops)
- [MCP Servers for DevOps and SRE](#mcp-servers-for-devops-and-sre)
- [AI-Powered CI/CD](#ai-powered-cicd)
- [AI Log Analysis and Debugging](#ai-log-analysis-and-debugging)
- [AI Agent Frameworks](#ai-agent-frameworks)
- [AI for Platform Engineering](#ai-for-platform-engineering)
- [AI for Database Operations](#ai-for-database-operations)
- [AI for Networking and Service Mesh](#ai-for-networking-and-service-mesh)
- [AI for Container Security and Supply Chain](#ai-for-container-security-and-supply-chain)
- [AI for Chaos Engineering and Reliability](#ai-for-chaos-engineering-and-reliability)
- [AI for Cloud Migration and Modernization](#ai-for-cloud-migration-and-modernization)
- [AI for GitOps](#ai-for-gitops)
- [System Prompt and Config Templates](#system-prompt-and-config-templates)
- [Learning Resources](#learning-resources)
- [Community and Newsletters](#community-and-newsletters)
- [How This Stays Updated](#how-this-stays-updated)
- [Contributing](#contributing)
- [About](#about)

---

## Tool of the Month

**[K8sGPT](https://github.com/k8sgpt-ai/k8sgpt)** — a CNCF Sandbox project that scans a live Kubernetes cluster, finds misconfigurations and failing resources, and explains them in plain English instead of raw kubectl errors. Free, open-source, installs in minutes — the best first stop if you're evaluating whether AI-assisted troubleshooting is worth adopting.

---

## Quick Picks by Use Case

| If you need to... | Start with |
|---|---|
| Get paged less and resolve faster | HolmesGPT, Keep, Cleric |
| Understand why a k8s pod is broken | K8sGPT, Robusta |
| Let AI write/refactor Terraform | Claude Code, Pulumi AI |
| Cut idle cloud spend automatically | Kubecost, Antimetal |
| Connect an LLM to your infra tools | MCP Servers section below |
| Triage a flood of noisy alerts | Keep, BigPanda, Moogsoft |
| Ship an internal developer platform | Backstage, Port, Score |

---

## AI Coding Agents for Infrastructure

AI-powered coding agents that write, review, and maintain infrastructure code — Terraform, Kubernetes manifests, Dockerfiles, CI/CD pipelines.

- **[Aider](https://github.com/aider-ai/aider)** — *Open-source.* Terminal-based AI pair programming that works with any LLM and commits each change to git automatically, well suited to infrastructure repos where you want an auditable diff per change.
- **[Amazon Q Developer](https://aws.amazon.com/q/developer/)** — *Commercial (AWS).* AWS-native assistant with deep CloudFormation and CDK awareness, best if your infrastructure is already AWS-centric.
- **[Augment Code](https://www.augmentcode.com/)** — *Commercial.* Enterprise coding platform built for deep multi-repo context, useful when infra code is spread across many services rather than one monorepo.
- **[Bolt](https://bolt.new/)** — *Commercial (StackBlitz).* Browser-based AI app builder that generates and deploys full-stack apps in-browser, more useful for prototyping dashboards than core infra work.
- **[Clanker](https://github.com/bgdnvk/clanker)** — *Open-source.* Autonomous CLI agent for systems engineering across AWS, GCP, and Cloudflare without needing a full IDE.
- **[Claude Code](https://docs.claude.com/en/docs/claude-code)** — *Commercial (Anthropic).* Agentic terminal coding tool strong at large multi-file Terraform refactors and debugging across an entire infrastructure repo at once.
- **[Cline](https://github.com/cline/cline)** — *Open-source.* Autonomous VS Code agent that can run terminal commands and edit files directly, good for teams wanting an open, extensible agent inside their existing editor.
- **[Continue](https://github.com/continuedev/continue)** — *Open-source.* Editor-agnostic AI assistant for VS Code and JetBrains that supports local models, a good fit for air-gapped or compliance-sensitive infra work.
- **[Cursor](https://cursor.com)** — *Commercial.* AI-first IDE with inline multi-file editing, popular for fast iterative Terraform/YAML work.
- **[Devin](https://devin.ai/)** — *Commercial (Cognition).* Fully autonomous software engineer that can take an infra task from planning through deployment with minimal supervision.
- **[Gemini Code Assist](https://cloud.google.com/gemini/docs/codeassist/overview)** — *Commercial (Google).* Google Cloud's coding assistant with native GCP awareness, the natural pick for GCP-heavy shops.
- **[GitHub Copilot](https://github.com/features/copilot)** — *Commercial.* The most widely deployed AI pair programmer, with Copilot Workspace extending it to multi-file infra changes.
- **[JetBrains AI](https://www.jetbrains.com/ai/)** — *Commercial.* Built into IntelliJ-based IDEs, context-aware completions for teams already standardized on JetBrains tooling.
- **[Lovable](https://lovable.dev/)** — *Commercial.* Full-stack app builder with one-click deploy, useful for spinning up internal tools and dashboards quickly.
- **[Crush](https://github.com/charmbracelet/crush)** — *Open-source (Charm).* Terminal coding agent supporting many model providers without losing session context between them.
- **[Factory AI](https://factory.ai/)** — *Commercial.* Enterprise agent platform built for large codebases with local execution, web search, and MCP access baked in.
- **[OpenCode](https://github.com/opencode-ai/opencode)** — *Open-source.* Go-based terminal agent with 140k+ stars supporting 75+ models across Claude, OpenAI, Gemini, and local providers.
- **[OpenHands](https://github.com/OpenHands/OpenHands)** — *Open-source (MIT).* Fully open autonomous software engineering platform with a 77.6% SWEBench score, a solid pick if you need to self-host rather than depend on a vendor.
- **[Qwen Code](https://github.com/QwenLM/Qwen3-Coder)** — *Open-source (Alibaba).* CLI agent built around the Qwen3-Coder models, a strong free option for teams comfortable outside the OpenAI/Anthropic ecosystem.
- **[Replit Agent](https://replit.com/ai)** — *Commercial.* Builds and deploys full-stack apps from natural language, most useful for quickly standing up infra dashboards or internal tools.
- **[Roo Code](https://github.com/RooCodeInc/Roo-Code)** — *Open-source.* VS Code agent forked from Cline with SOC 2 compliance features, aimed at regulated enterprise teams.
- **[Trae](https://www.trae.ai/)** — *Commercial (ByteDance), free tier.* AI-first IDE with built-in MCP support and generous free usage.
- **[Sourcegraph Cody](https://sourcegraph.com/cody)** — *Commercial.* Full-codebase-context assistant, particularly strong for navigating large monorepos with shared infra modules.
- **[Tabnine](https://www.tabnine.com/)** — *Commercial.* Code completion that can run fully locally, aimed at teams with strict data-privacy requirements around infra code.
- **[Windsurf](https://codeium.com/windsurf)** — *Commercial (Codeium).* AI IDE with an agentic "Cascade" mode for multi-step infra tasks.
- **[Void](https://voideditor.com/)** — *Open-source.* VS Code fork supporting local and remote LLMs for teams wanting a privacy-first, fully open editor.
- **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** — *Open-source, free tier.* Google's terminal agent with a 1,000 requests/day free allowance and native MCP support.
- **[Goose](https://github.com/block/goose)** — *Open-source (Block), Apache 2.0.* Rust-based autonomous agent that installs, edits, and tests using any LLM via MCP.
- **[Kiro](https://kiro.dev/)** — *Commercial (AWS).* Spec-driven agentic IDE that produces reproducible infra code from structured requirements and design docs rather than freeform prompts.
- **[Zed AI](https://zed.dev/)** — *Commercial.* High-performance editor with built-in assistant and terminal integration.
- **[aiac](https://github.com/gofireflyio/aiac)** — *Open-source (Firefly).* CLI generator for Terraform, Pulumi, Helm, CloudFormation, and Dockerfiles from natural language, supports OpenAI, Bedrock, and Ollama.
- **[JetBrains Junie](https://www.jetbrains.com/junie/)** — *Commercial.* Standalone, LLM-agnostic coding agent usable from terminal, IDE, or CI/CD.
- **[Kilo Code](https://github.com/Kilo-Org/kilocode)** — *Open-source (MIT).* Agentic platform across VS Code/JetBrains/CLI with 500+ models at zero markup and a persistent memory bank for long-running projects.
- **[Plandex](https://github.com/plandex-ai/plandex)** — *Open-source.* Plan-first terminal agent with a 2M-token context and cumulative-diff sandbox, built for large multi-file IaC changes.
- **[Mistral Vibe](https://github.com/mistralai/mistral-vibe)** — *Open-source (Apache 2.0).* CLI agent with explicit on-prem/VPC deployment support, aimed at regulated DevOps teams.

## AI-Powered Kubernetes

AI tools purpose-built for cluster management, troubleshooting, and operations.

- **[Glasskube](https://github.com/glasskube/glasskube)** — *Open-source.* Kubernetes package manager with AI-assisted package discovery and dependency resolution.
- **[Headlamp](https://github.com/headlamp-k8s/headlamp)** — *Open-source.* Extensible Kubernetes web UI with a plugin architecture supporting AI-powered visualization.
- **[K8sGPT](https://github.com/k8sgpt-ai/k8sgpt)** — *Open-source (CNCF Sandbox).* See Tool of the Month above.
- **[Kagent](https://github.com/kagent-dev/kagent)** — *Open-source (CNCF Sandbox).* Framework for running AI agents natively inside a Kubernetes cluster.
- **[KAITO](https://github.com/kaito-project/kaito)** — *Open-source (CNCF Sandbox).* Kubernetes AI Toolchain Operator that simplifies LLM inference and fine-tuning on clusters.
- **[Karpenter](https://github.com/kubernetes-sigs/karpenter)** — *Open-source.* Node autoscaler using intelligent bin-packing and just-in-time provisioning to cut cluster cost.
- **[KServe](https://github.com/kserve/kserve)** — *Open-source.* Standardized distributed inference platform for multi-framework model serving with autoscaling and canary rollouts.
- **[KubeStellar Console](https://github.com/kubestellar/console)** — *Open-source (CNCF Sandbox).* Multi-cluster dashboard with an AI natural-language layer for edge and cloud cluster management.
- **[Komodor](https://komodor.com/)** — *Commercial.* Troubleshooting platform focused on change-tracking — "what changed right before this broke" — with AI root cause analysis.
- **[kubectl-ai](https://github.com/GoogleCloudPlatform/kubectl-ai)** — *Open-source (Google Cloud).* kubectl plugin generating and applying manifests from natural language.
- **[Kubernetes ChatGPT Bot](https://github.com/robusta-dev/kubernetes-chatgpt-bot)** — *Open-source.* Slack-integrated ChatGPT bot for cluster troubleshooting notifications.
- **[Kubeflow](https://github.com/kubeflow/kubeflow)** — *Open-source (CNCF incubating).* Full ML platform for Kubernetes: training, serving, pipelines, notebooks.
- **[Kubescape](https://github.com/kubescape/kubescape)** — *Open-source (CNCF incubating).* Security platform with runtime threat detection, SBOMs, and eBPF monitoring.
- **[Kubeshark](https://github.com/kubeshark/kubeshark)** — *Open-source.* API traffic analyzer giving real-time cluster network visibility, useful as a data source for AI anomaly detection.
- **[Robusta](https://github.com/robusta-dev/robusta)** — *Open-source core / Commercial.* Monitoring and troubleshooting with automated playbooks that react to cluster events, not just alert on them.
- **[ValidKube](https://github.com/komodorio/validkube)** — *Open-source.* One-stop tool to validate, clean, and secure Kubernetes manifests.
- **[k8m](https://github.com/weibaohui/k8m)** — *Open-source.* Lightweight single-binary AI dashboard with multi-cluster support.
- **[KubeAI](https://github.com/kubeai-project/kubeai)** — *Open-source.* Inference operator for serving LLMs, embeddings, and speech models with zero external dependencies.
- **[Kubewall](https://github.com/kubewall/kubewall)** — *Open-source.* Single-binary dashboard with multi-cluster support and pluggable AI model backends.
- **[vCluster](https://github.com/loft-sh/vcluster)** — *Open-source.* Virtual Kubernetes clusters for isolated dev/test, including AI workload experimentation.
- **[KAI Scheduler](https://github.com/NVIDIA/KAI-Scheduler)** — *Open-source (CNCF Sandbox, NVIDIA).* GPU-native scheduler with topology-aware and gang scheduling for AI workloads.
- **[llm-d](https://github.com/llm-d/llm-d)** — *Open-source (CNCF Sandbox).* Distributed LLM inference framework for Kubernetes from Red Hat, IBM, and Google with disaggregated serving.
- **[NVIDIA AI Cluster Runtime](https://github.com/NVIDIA/aicr)** — *Open-source (alpha, NVIDIA).* Cluster runtime with a dedicated CLI and validated recipes for training/inference on H100/Blackwell hardware.
- **[Sedai](https://sedai.io/)** — *Commercial.* Reinforcement-learning-driven autonomous optimization for scaling and remediation, offered in copilot or full-autopilot mode.
- **[Velero](https://github.com/vmware-tanzu/velero)** — *Open-source (CNCF Sandbox).* Backup, disaster recovery, and migration for Kubernetes with AI-assisted scheduling.
- **[Causely](https://www.causely.ai/)** — *Commercial.* Causal-AI diagnosis platform with an MCP server, claims a 60% cut in agent token use versus general coding agents on the same diagnostic task.
- **[Parity](https://www.tryparity.com/)** — *Commercial (YC).* AI SRE for on-call Kubernetes engineers that investigates and runs runbooks before a human is paged.
- **[Azure SRE Agent](https://azure.microsoft.com/en-us/products/sre-agent)** — *Commercial (Microsoft).* GA AI ops teammate for AKS that investigates and, with approval, executes remediation.
- **[NVIDIA Grove](https://github.com/ai-dynamo/grove)** — *Open-source (NVIDIA).* Kubernetes API for orchestrating multi-node AI inference with hierarchical gang scheduling.
- **[Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox)** — *Open-source (K8s SIG Apps).* Sandbox CRD for isolated stateful AI-agent workloads via gVisor/Kata.
- **[Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit)** — *Open-source.* Sidecar policy engine enforcing OWASP agentic-AI risk controls on AKS.
- **[KubeCopilot Core](https://github.com/kubecopilot/kubecopilot-core)** — *Open-source.* Operator deploying an in-cluster AI agent controlled via CRDs, engine-agnostic across model providers.
- **[kube-agent](https://github.com/feiskyer/kube-agent)** — *Open-source.* Autonomous agent that plans and executes multi-step cluster operations, not just chat-based diagnostics.
- **[LLMKube](https://github.com/defilantech/llmkube)** — *Open-source.* Operator for local LLM inference on Kubernetes via llama.cpp/vLLM/TGI, aimed at air-gapped deployments.
- **[OpenSRE](https://github.com/Tracer-Cloud/opensre)** — *Open-source.* Toolkit and eval environment for building AI SRE agents across Kubernetes, EC2, Lambda, ECS, and Flink.

## AI-Powered Terraform and IaC

- **[Atmos](https://github.com/cloudposse/atmos)** — *Open-source.* Framework for managing Terraform at scale with AI-assisted component discovery.
- **[Brainboard](https://www.brainboard.co/)** — *Commercial.* Visual Terraform designer that generates architecture from diagrams.
- **[Env0](https://www.env0.com/)** — *Commercial.* Self-service IaC platform with AI-assisted policy enforcement and drift detection.
- **[Firefly](https://www.firefly.ai/)** — *Commercial.* Detects drift and auto-generates Terraform from existing unmanaged cloud resources.
- **[Infracost](https://github.com/infracost/infracost)** — *Open-source.* Adds cloud cost estimates directly to Terraform pull requests, covering 1,100+ resource types.
- **[OpenTofu](https://github.com/opentofu/opentofu)** — *Open-source (Linux Foundation).* Community-governed Terraform fork, the foundation many AI IaC tools now build on.
- **[Pulumi AI](https://www.pulumi.com/ai/)** — *Commercial.* Generates Pulumi programs across AWS/Azure/GCP/Kubernetes from natural language.
- **[Spacelift AI](https://spacelift.io/)** — *Commercial.* AI-enhanced IaC management with drift detection and automated remediation.
- **[Terrascan](https://github.com/tenable/terrascan)** — *Open-source.* Static analyzer detecting compliance and security violations across Terraform, Kubernetes, and Helm.
- **[Terramate](https://github.com/terramate-io/terramate)** — *Open-source.* Orchestration and code generation for complex multi-stack Terraform.
- **[tfswitch](https://github.com/warrensbox/terraform-switcher)** — *Open-source.* CLI for switching between Terraform versions across multi-version pipelines.
- **[ControlMonkey](https://controlmonkey.io/)** — *Commercial.* Governance platform with AI-powered drift remediation and auto-generated IaC from existing resources.
- **[Terracotta AI](https://tryterracotta.com/)** — *Commercial (YC).* AI PR reviewer for Terraform/OpenTofu/CDK-TF covering plan analysis, IAM security, and cost impact.
- **[Resourcely](https://www.resourcely.io/)** — *Commercial.* Guardrails platform with reusable blueprints and a policy language enforced at PR time.
- **[Terrateam](https://github.com/terrateamio/terrateam)** — *Open-source (MPL-2.0).* GitOps IaC orchestration across Terraform/OpenTofu/CDKTF/Pulumi with an OPA policy engine.
- **[Pulumi Neo](https://www.pulumi.com/product/neo/)** — *Commercial.* Agentic platform-engineer product that provisions and governs multi-cloud IaC end to end.
- **[HashiCorp Project Infragraph](https://developer.hashicorp.com/hcp/docs/infragraph)** — *Commercial (HashiCorp).* Real-time infra knowledge graph powering agentic reasoning over Terraform state and cloud APIs.
- **[HashiCorp Agent Skills](https://www.hashicorp.com/en/blog/introducing-hashicorp-agent-skills)** — *Open-source.* Official Claude Code Skills for generating and refactoring Terraform/Packer using HashiCorp best practices.
- **[Overmind](https://github.com/overmindtech)** — *Open-source core / Commercial.* Blast-radius risk analysis that discovers unmanaged AWS resources and converts them to Terraform.
- **[Saturnhead AI](https://spacelift.io/blog/introducing-saturnhead-ai)** — *Commercial (Spacelift).* Auto-explains failed Terraform run logs across init/plan/apply in plain language.
- **[Quali Torque](https://www.quali.com/agentic-ai/)** — *Commercial.* Agentic control plane with modular agents for blueprints, cost modeling, and drift remediation.

## AI Incident Response and AI SRE Agents

- **[Aiden for SRE](https://stackgen.com/product/aiden-for-sre)** — *Commercial.* Aiden that acts autonomously on recurring incidents and works complex ones alongside your team through to resolution — policy-bound and fully auditable.
- **[BigPanda](https://www.bigpanda.io/)** — *Commercial.* AIOps event correlation and automated root cause analysis across hybrid environments.
- **[Blameless](https://www.blameless.com/)** — *Commercial.* SRE platform with AI-powered incident management and automated retrospectives.
- **[FireHydrant](https://firehydrant.com/)** — *Commercial.* Incident management with AI-generated retrospectives and automated status pages.
- **[GitHub Agentic Workflows](https://github.github.io/gh-aw/)** — *Open-source.* Run AI agents inside GitHub Actions for issue triage and CI failure analysis.
- **[HolmesGPT](https://github.com/HolmesGPT/holmesgpt)** — *Open-source (CNCF Sandbox).* Combines observability telemetry with LLM reasoning for agentic troubleshooting, self-hostable so data doesn't leave your environment.
- **[incident.io](https://incident.io/)** — *Commercial.* End-to-end incident management with AI summaries and native Slack workflows.
- **[IncidentFox](https://github.com/incidentfox/incidentfox)** — *Open-source.* Automated investigation and hypothesis formation with Slack/PagerDuty integration.
- **[Moogsoft](https://www.moogsoft.com/)** — *Commercial.* AIOps correlation platform focused on reducing alert fatigue via noise reduction.
- **[Opsgenie](https://www.atlassian.com/software/opsgenie)** — *Commercial (Atlassian).* AI-assisted alert routing and on-call scheduling.
- **[PagerDuty AIOps](https://www.pagerduty.com/platform/aiops/)** — *Commercial.* ML-based event correlation and noise reduction before alerts reach a human.
- **[Keep](https://github.com/keephq/keep)** — *Open-source.* Correlates and deduplicates alerts from any monitoring tool with AI-powered noise reduction — a good hub if you already run several disconnected monitoring tools.
- **[Rootly](https://rootly.com/)** — *Commercial.* Automated incident timelines and AI-generated postmortems in Slack-native workflows.
- **[Shoreline](https://shoreline.io/)** — *Commercial.* Converts runbooks into automated remediation that executes across entire fleets.
- **[Tracecat](https://github.com/TracecatHQ/tracecat)** — *Open-source.* Security/reliability automation with 100+ integrations and sandboxed execution.
- **[Cleric](https://cleric.ai/)** — *Commercial.* Autonomous AI SRE that maps architecture and delivers root-cause diagnoses with confidence scores in Slack; a 2025 Gartner Cool Vendor.
- **[Resolve AI](https://resolve.ai/)** — *Commercial.* Agentic production engineer for Kubernetes/AWS/GitHub targeting 80% autonomous alert resolution.
- **[NeuBird Hawkeye](https://neubird.ai/)** — *Commercial.* Hybrid/multi-cloud incident resolution with Datadog/Splunk/PagerDuty/ServiceNow integrations; available SOC-2 VPC deployment.
- **[Edge Delta](https://edgedelta.com/)** — *Commercial.* Telemetry pipelines plus role-aware "AI Teammates" that autonomously investigate anomalies across SRE, DevOps, and security.
- **[Traversal](https://www.traversal.com/)** — *Commercial.* Causal-ML root cause analysis using reinforcement learning over a "Production World Model."
- **[Datafruit](https://datafruit.dev/)** — *Commercial (YC).* Agentic DevOps engineer that learns your deploy standards and handles ops requests via Slack.
- **[SRE.ai](https://www.sre.ai/)** — *Commercial (YC).* Autonomous agents for CI, test, and incident workflow automation.
- **[AWS Security Incident Response Agent](https://aws.amazon.com/blogs/security/aws-launches-ai-enhanced-security-innovations-at-reinvent-2025/)** — *Commercial (AWS).* Native agentic AI for autonomous on-call security incident response.

## AI Monitoring and Observability

- **[Arize Phoenix](https://github.com/Arize-ai/phoenix)** — *Open-source.* AI observability with OpenTelemetry tracing, drift detection, and RAG debugging for production AI systems.
- **[Chronosphere](https://chronosphere.io/)** — *Commercial.* Cloud-native observability with AI-driven telemetry cost optimization.
- **[Coralogix](https://coralogix.com/)** — *Commercial.* Full-stack observability with AI-powered log analysis and cost-effective retention.
- **[Datadog Bits AI](https://www.datadoghq.com/product/platform/bits-ai/)** — *Commercial.* Natural-language metric queries and automated root cause investigation across the Datadog platform.
- **[Dynatrace Davis AI](https://docs.dynatrace.com/docs/platform/davis-ai)** — *Commercial.* Causal AI engine for automated RCA and predictive problem detection.
- **[Grafana](https://github.com/grafana/grafana)** — *Open-source.* The foundational dashboarding layer most AI observability workflows are built on top of.
- **[Grafana AI](https://grafana.com/products/cloud/ai-tools-for-observability/)** — *Commercial.* Built-in SRE agent, adaptive telemetry cost reduction, and AI-assisted query generation on top of the OSS stack.
- **[Groundcover](https://www.groundcover.com/)** — *Commercial.* eBPF-based observability requiring zero manual instrumentation, with AI root cause analysis.
- **[Honeycomb](https://www.honeycomb.io/)** — *Commercial.* Translates natural language into complex queries for debugging distributed systems.
- **[Metoro Guardian](https://metoro.io/)** — *Commercial.* Combines telemetry and code analysis to auto-generate fix PRs from observed incidents.
- **[New Relic AI](https://newrelic.com/platform/new-relic-ai)** — *Commercial.* Natural-language querying and anomaly explanation across the New Relic platform.
- **[Prometheus Operator](https://github.com/prometheus-operator/prometheus-operator)** — *Open-source.* Foundation for cloud-native monitoring pipelines feeding most AI alerting tools.
- **[Splunk AI](https://www.splunk.com/en_us/products.html)** — *Commercial.* Natural-language search and predictive insights across IT infrastructure data.
- **[Sumo Logic](https://www.sumologic.com/)** — *Commercial.* Cloud-native machine data analytics with AI-driven threat detection.
- **[Thanos](https://github.com/thanos-io/thanos)** — *Open-source (CNCF incubating).* Long-term storage and global query view for large-scale Prometheus deployments.
- **[OpenObserve](https://github.com/openobserve/openobserve)** — *Open-source (Rust).* Unified logs/metrics/traces platform claiming 140x lower storage cost than typical stacks.
- **[Opswald](https://www.opswald.com/ai-agent-debugging/)** — *Commercial.* Debugging platform specifically for AI agents — captures prompts, tool calls, and side effects so you can replay a failed run.
- **[VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics)** — *Open-source.* Fast, cost-effective, Prometheus/Grafana-compatible time series database.
- **[Coroot](https://github.com/coroot/coroot)** — *Open-source.* eBPF-based zero-instrumentation APM with AI root cause analysis and SLO-based alerting.
- **[Apache SkyWalking](https://github.com/apache/skywalking)** — *Open-source.* Full-stack APM with distributed tracing and eBPF-powered Kubernetes monitoring.
- **[Dash0](https://dash0.com/)** — *Commercial.* OpenTelemetry-native platform with specialized "Agent0" agents for SRE, cost, migration, and security.
- **[SigNoz](https://github.com/SigNoz/signoz)** — *Open-source.* OpenTelemetry-native APM unifying logs/metrics/traces with native LLM-app observability.
- **[Flip AI](https://www.flip.ai/)** — *Commercial.* DevOps-specific LLM predicting incidents and generating RCAs across Datadog/Splunk/AppDynamics.
- **[Coralogix Olly](https://ollyhq.com/)** — *Commercial.* Autonomous agent correlating logs/metrics/traces with code-aware root cause analysis.
- **[LogicMonitor Edwin AI](https://www.logicmonitor.com/edwin-ai)** — *Commercial.* Connects 3,000+ tools for correlation, RCA, and autonomous remediation.
- **[New Relic SRE Agent](https://newrelic.com/platform/sre-agent)** — *Commercial.* AI-powered autonomous incident diagnosis across app and infra layers.
- **[AgentSight](https://github.com/eunomia-bpf/agentsight)** — *Open-source.* eBPF boundary tracing for monitoring AI *agents themselves* (Claude Code, Cursor, Gemini CLI) with under 3% overhead.

## AI Security Scanning and AI SOC

- **[Aqua Security](https://www.aquasec.com/)** — *Commercial.* Cloud-native platform with AI-powered runtime protection and image scanning.
- **[Checkov](https://github.com/bridgecrewio/checkov)** — *Open-source.* Static IaC security analysis across Terraform, CloudFormation, Kubernetes, and Dockerfile.
- **[Falco](https://github.com/falcosecurity/falco)** — *Open-source (CNCF graduated).* Runtime threat detection for containers and Kubernetes.
- **[GitGuardian](https://www.gitguardian.com/)** — *Commercial.* AI-powered secrets detection across Git repos, CI/CD, and Docker images.
- **[Endor Labs](https://www.endorlabs.com/)** — *Commercial.* Identifies *reachable* vulnerabilities to cut false positives in supply-chain scanning.
- **[Lacework](https://www.lacework.com/)** — *Commercial.* Behavioral AI detecting cloud-workload anomalies without hand-written rules.
- **[MCP-Scan](https://labs.snyk.io/)** — *Open-source.* Audits Model Context Protocol servers for security issues before you connect an LLM to them.
- **[Orca Security](https://orca.security/)** — *Commercial.* Agentless cloud security with AI-prioritized risk across workloads and identities.
- **[Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud)** — *Commercial.* CNAPP with AI-driven vulnerability prioritization and compliance checks.
- **[Semgrep](https://github.com/semgrep/semgrep)** — *Open-source.* Fast static analysis across 30+ languages, including HCL and YAML.
- **[Snyk](https://snyk.io/product/)** — *Commercial.* DeepCode AI engine scanning code, containers, IaC, and AI-generated code in real time.
- **[Socket](https://socket.dev/)** — *Commercial.* Detects malicious/compromised open-source packages before they reach production.
- **[SonarQube](https://www.sonarsource.com/products/sonarqube/)** — *Open-source core / Commercial.* Code quality and security analysis with AI-assisted vulnerability detection.
- **[Terraform Sentinel](https://www.hashicorp.com/sentinel)** — *Commercial (HashiCorp).* Policy-as-code enforcement for Terraform changes.
- **[tfsec](https://github.com/aquasecurity/tfsec)** — *Open-source.* Security scanner for Terraform misconfigurations.
- **[Trivy](https://github.com/aquasecurity/trivy)** — *Open-source.* Widely adopted vulnerability scanner for containers, IaC, Kubernetes, and code.
- **[Wiz](https://www.wiz.io/)** — *Commercial.* Unifies vulnerability findings with cloud context to prioritize exploitable risk.
- **[Kyverno](https://github.com/kyverno/kyverno)** — *Open-source (CNCF incubating).* Kubernetes-native policy engine for validating and mutating configs.
- **[OPA Gatekeeper](https://github.com/open-policy-agent/gatekeeper)** — *Open-source.* Policy controller for Kubernetes admission control based on Open Policy Agent.
- **[Sysdig](https://www.sysdig.com/)** — *Commercial.* Runtime protection with "Sysdig Sage" AI analyst for automated threat investigation.
- **[AccuKnox](https://accuknox.com/)** — *Commercial.* Zero-trust cloud-native security with eBPF runtime visibility and GenAI policy generation.
- **[Checkmarx One](https://checkmarx.com/)** — *Commercial.* Unified SAST/SCA/DAST/IaC/API/container platform with AI-powered autonomous remediation.
- **[Credo AI](https://www.credo.ai/)** — *Commercial.* AI governance/compliance platform for EU AI Act and NIST AI RMF enforcement.
- **[Holistic AI](https://www.holisticai.com/)** — *Commercial.* Continuous audit, bias detection, and compliance tracking for AI systems in production.
- **[Microsoft Purview](https://www.microsoft.com/en-us/security/business/microsoft-purview)** — *Commercial.* Unified data governance and AI security across Microsoft 365/Azure.
- **[Aikido Security](https://www.aikido.dev/)** — *Commercial.* Unified AppSec (SAST/DAST/SCA/IaC/secrets/runtime) with AI AutoTriage cutting noise ~95%.
- **[ZeroPath](https://zeropath.com/)** — *Commercial.* AI-native SAST combining LLMs with AST analysis; found 170 verified bugs in curl.
- **[Pixee](https://www.pixee.ai/)** — *Commercial.* Agentic AppSec that writes context-aware fix PRs with a 76% merge rate across 100,000+ PRs.
- **[Corgea](https://corgea.com/)** — *Commercial (YC).* Finds and fixes insecure code/IaC/containers with over 90% claimed fix accuracy.
- **[Backslash Security](https://www.backslash.security/)** — *Commercial.* Digital-twin approach to securing AI-native development across IDEs, agents, and MCPs.
- **[Ghost Security](https://ghostsecurity.ai/)** — *Commercial.* Agent-native AppSec with an autonomous engine and a Claude Code plugin for in-IDE vulnerability fixing.
- **[Cyera](https://www.cyera.com/)** — *Commercial.* AI-native data security posture management, agentlessly classifying data at scale.
- **[Prophet Security](https://www.prophetsecurity.ai/)** — *Commercial.* Agentic SOC platform automating Tier 1-3 alert triage and threat hunting.
- **[Dropzone AI](https://www.dropzone.ai/)** — *Commercial.* Pre-trained agents acting as Tier-1 SOC analysts, investigating alerts end to end.
- **[7AI](https://7ai.com/)** — *Commercial.* Agentic security platform from the Cybereason founders, processed 2.5M+ alerts.
- **[Conifers CognitiveSOC](https://www.conifers.ai/)** — *Commercial.* Multi-tier AI SOC agents for enterprise-scale autonomous triage.
- **[Hex Security](https://www.ycombinator.com/companies/hex-security)** — *Commercial (YC).* Continuous autonomous 24/7 penetration testing agents.
- **[Upwind](https://www.upwind.io/)** — *Commercial.* Runtime-first CNAPP with eBPF-based threat detection.
- **[HexStrike AI](https://github.com/0x4m4/hexstrike-ai)** — *Open-source.* MCP server bridging LLMs to 150+ offensive security tools for AI-driven red-teaming.
- **[Databricks Lakewatch](https://www.databricks.com/product/lakewatch)** — *Commercial.* Agentic SIEM on the lakehouse for automated triage and natural-language-to-SQL queries.
- **[Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/agents-overview)** — *Commercial.* Agentic SOC platform extending Defender with autonomous investigation agents.

## AI Cost Optimization and FinOps

- **[Anodot](https://www.anodot.com/)** — *Commercial.* Autonomous anomaly detection and commitment management for cloud cost.
- **[CAST AI](https://cast.ai/)** — *Commercial.* Kubernetes cost optimization with automated rightsizing and spot management.
- **[CloudZero](https://www.cloudzero.com/)** — *Commercial.* Cost intelligence with AI-driven allocation and unit economics tracking.
- **[Finout](https://www.finout.io/)** — *Commercial.* FinOps cost allocation across cloud, Kubernetes, and SaaS combined with observability data.
- **[Kubecost](https://github.com/kubecost/kubecost)** — *Open-source core / Commercial.* Real-time Kubernetes cost monitoring by service, deployment, and namespace.
- **[nOps](https://www.nops.io/)** — *Commercial.* AWS-focused rightsizing and automated savings execution.
- **[OpenCost](https://github.com/opencost/opencost)** — *Open-source (CNCF Sandbox).* Vendor-neutral real-time Kubernetes cost monitoring.
- **[Spot by NetApp](https://spot.io/)** — *Commercial.* AI-driven spot-instance and autoscaling optimization.
- **[Turbonomic](https://www.ibm.com/products/turbonomic)** — *Commercial (IBM).* Continuously optimizes compute, storage, and network allocation.
- **[Vantage](https://www.vantage.sh/)** — *Commercial.* Cost transparency and AI recommendations across AWS/Azure/GCP/Kubernetes.
- **[Komiser](https://github.com/tailwarden/komiser)** — *Open-source.* Multi-cloud cost dashboard.
- **[Antimetal](https://www.antimetal.com/)** — *Commercial.* Autonomously purchases Reserved Instances/Savings Plans based on real-time usage.
- **[PointFive](https://www.pointfive.co/)** — *Commercial.* DeepWaste detection (400+ checks) with a Claude-powered assistant for savings actions.
- **[ProsperOps](https://www.prosperops.com/)** — *Commercial.* No-touch discount management across AWS/Azure/GCP, manages $6B+ in annual spend.
- **[Costimizer](https://costimizer.ai/)** — *Commercial.* Agentic FinOps autopilot that rightsizes and enforces budgets automatically.

## MCP Servers for DevOps and SRE

Model Context Protocol servers give AI assistants (Claude, ChatGPT, Cursor) direct, structured access to real infra tools instead of copy-pasted context.

- **[Atlassian MCP Server](https://www.atlassian.com/blog/announcements/remote-mcp-server)** — Jira/Confluence: query issues, create tickets, search docs.
- **[AWS MCP Servers](https://awslabs.github.io/mcp/)** — Official AWS suite covering Terraform, CDK, CloudFormation, Lambda, S3, CloudWatch, ECS.
- **[Cloudflare MCP Server](https://github.com/cloudflare/mcp-server-cloudflare)** — Manage Workers, KV, R2, and DNS.
- **[Datadog MCP Server](https://github.com/datadog-labs/mcp-server)** — Query metrics, monitors, dashboards, logs.
- **[Docker MCP Gateway](https://github.com/docker/mcp-gateway)** — Container management and Compose workflows.
- **[GitHub MCP Server](https://github.com/github/github-mcp-server)** — Repos, issues, PRs, Actions, code search.
- **[Grafana MCP Server](https://github.com/grafana/mcp-grafana)** — Query dashboards, datasources, alerts.
- **[Kubernetes MCP Server](https://github.com/Flux159/mcp-server-kubernetes)** — kubectl operations and cluster introspection.
- **[KubeStellar Console MCP](https://github.com/kubestellar/console/tree/main/cmd/kc-agent)** — Bridges kubeconfig contexts to LLMs for multi-cluster ops.
- **[Linear MCP Server](https://github.com/jerhadf/linear-mcp-server)** — Manage issues, projects, cycles.
- **[MCP Reference Servers](https://github.com/modelcontextprotocol/servers)** — Official reference implementations: filesystem, Git, GitHub, PostgreSQL, Puppeteer.
- **[PagerDuty MCP Server](https://github.com/PagerDuty/pagerduty-mcp-server)** — Incident management, on-call schedules, alert routing.
- **[Sentry MCP Server](https://github.com/getsentry/sentry-mcp)** — Error tracking, issue search, event analysis.
- **[Terraform MCP Server](https://github.com/hashicorp/terraform-mcp-server)** — Official: module search, provider docs, policy enforcement.
- **[Argo CD MCP Server](https://github.com/argoproj-labs/mcp-for-argocd)** — List, inspect, sync, manage Argo CD applications.
- **[Azure DevOps MCP Server](https://github.com/microsoft/azure-devops-mcp)** — Work items, PRs, pipelines, repos, wikis.
- **[GitLab MCP Server](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server/)** — Projects, issues, MRs, CI/CD pipelines with OAuth 2.0.
- **[Jenkins MCP Server](https://github.com/jenkinsci/mcp-server-plugin)** — Jobs, builds, pipelines via SSE/streamable HTTP.
- **[JFrog MCP Server](https://github.com/jfrog/jfrog-mcp-server)** — Artifactory repo management, artifact search, security scanning.
- **[Notion MCP Server](https://developers.notion.com/docs/mcp)** — Semantic search across workspaces plus page creation.
- **[Prometheus MCP Server](https://github.com/pab1it0/prometheus-mcp-server)** — PromQL queries from AI agents.
- **[Slack MCP Server](https://docs.slack.dev/ai/slack-mcp-server/)** — Search messages, read history, send messages.
- **[Pulumi MCP Server](https://www.pulumi.com/docs/ai/mcp-server/)** — Infra previews, resource lookups, delegates to Pulumi Neo.
- **[Vercel MCP Server](https://github.com/vercel/mcp-adapter)** — Serverless deployment and edge function management.
- **[Lens MCP Server](https://lenshq.io/)** — Built into Lens Kubernetes IDE, native EKS/AKS integration.
- **[StackGen MCP Server](https://docs.stackgen.com/docs/stackgen-mcp)** — Generates policy-compliant Terraform/K8s/Helm from natural language.
- **[GCP gcloud MCP Server](https://github.com/googleapis/gcloud-mcp)** — Interact with GCP resources via gcloud CLI in natural language.
- **[Google Cloud Run MCP Server](https://github.com/GoogleCloudPlatform/cloud-run-mcp)** — Deploy and manage Cloud Run apps.
- **[DigitalOcean MCP Server](https://github.com/digitalocean/digitalocean-mcp)** — Droplets, App Platform, databases, DOKS, networking.
- **[Oracle Cloud MCP Server](https://github.com/oracle/mcp)** — Reference implementations for OCI products.
- **[New Relic MCP Server](https://github.com/newrelic/mcp-server)** — Telemetry queries and alert investigation.
- **[Splunk MCP Server](https://github.com/CiscoDevNet/Splunk-MCP-Server-official)** — Run searches, query data for agentic workflows.
- **[Elasticsearch MCP Server](https://github.com/elastic/mcp-server-elasticsearch)** — Natural-language querying and data retrieval.
- **[Dynatrace MCP Server](https://github.com/dynatrace-oss/dynatrace-mcp)** — Metrics, traces, logs into AI dev workflows.
- **[CircleCI MCP Server](https://github.com/CircleCI-Public/mcp-server-circleci)** — Pipelines, builds, workflows via natural language.
- **[Buildkite MCP Server](https://github.com/buildkite/buildkite-mcp-server)** — Pipelines, builds, jobs, test data.
- **[MongoDB MCP Server](https://github.com/mongodb-js/mongodb-mcp-server)** — Atlas/Community/Enterprise natural-language DB management.
- **[Redis MCP Server](https://github.com/redis/mcp-redis)** — Natural-language interface for managing/searching Redis data.
- **[Neon MCP Server](https://github.com/neondatabase/mcp-server-neon)** — Manage serverless Postgres projects, branches, run SQL.
- **[Supabase MCP Server](https://github.com/supabase-community/supabase-mcp)** — Tables, queries, config, database ops.
- **[HashiCorp Vault MCP Server](https://github.com/hashicorp/vault-mcp-server)** — Manage secrets and mounts.
- **[Snyk MCP Server](https://github.com/snyk/studio-mcp)** — Security scanning for code, dependencies, configs.
- **[Trivy MCP Server](https://github.com/aquasecurity/trivy-mcp)** — Vulnerability scanning, misconfiguration and secret detection.
- **[Rootly MCP Server](https://docs.rootly.com/integrations/mcp-server)** — Resolve incidents without leaving the IDE.
- **[FireHydrant MCP Server](https://github.com/firehydrant/firehydrant-mcp)** — Interact with the incident management API.
- **[Incident.io MCP Server](https://github.com/incident-io/incidentio-mcp-golang)** — Incident management and response.
- **[Ansible MCP Server](https://github.com/sibilleb/AAP-Enterprise-MCP-Server)** — AI-driven playbook execution and automation.
- **[Bitbucket MCP Server](https://github.com/MatanYemini/bitbucket-mcp)** — Repos, PRs, code reviews.
- **[Cloudflare Code Mode MCP Server](https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/)** — Search/execute tools over a type-aware SDK across 2,500+ endpoints.
- **[Render MCP Server](https://github.com/render-oss/render-mcp-server)** — Manage services, deploys, environments.
- **[Fly.io MCP Server](https://github.com/superfly/flymcp)** — Wraps flyctl to provision Fly machines/apps.
- **[SigNoz MCP Server](https://github.com/SigNoz/signoz-mcp-server)** — Metrics, traces, logs, alerts, dashboards, ClickHouse SQL.
- **[Coralogix MCP Server](https://coralogix.com/docs/user-guides/mcp-server/overview/)** — Logs, metrics, traces, RUM data.
- **[Logz.io MCP Server](https://docs.logz.io/docs/open360/logzio-mcp/)** — Logs, metrics, dashboards, alerts.
- **[ClickHouse MCP Server](https://github.com/ClickHouse/mcp-clickhouse)** — SQL queries, schema exploration, read-only defaults.
- **[Turso MCP Server](https://turso.tech/blog/introducing-the-turso-database-mcp-server)** — Query/manage Turso and LibSQL databases.
- **[Databricks MCP Servers](https://docs.databricks.com/aws/en/generative-ai/mcp/)** — Genie Space, Vector Search, Unity Catalog Functions.
- **[Harness MCP Server](https://github.com/harness/mcp-server)** — CI/CD, GitOps, feature flags, FinOps, security testing, chaos.
- **[Twilio MCP Server](https://github.com/twilio-labs/mcp)** — All Twilio public APIs plus an OpenAPI-to-MCP generator.
- **[Stripe MCP Server](https://github.com/stripe/agent-toolkit)** — Payments, customers, invoices, products.
- **[CrowdStrike Falcon MCP Server](https://github.com/CrowdStrike/falcon-mcp)** — Detections, incidents, behaviors for automated threat hunting.
- **[Wiz MCP Server](https://www.wiz.io/blog/introducing-mcp-server-for-wiz)** — Natural-language queries over cloud inventory and risk posture.
- **[Bitwarden MCP Server](https://github.com/bitwarden/mcp-server)** — Local-only CLI-backed vault access.
- **[Doppler MCP Server](https://github.com/DopplerHQ/mcp-server)** — Secrets and configuration management.
- **[Hetzner Cloud MCP Server](https://github.com/dkruyt/mcp-hetzner)** — Servers, networks, volumes via natural language.
- **[Snowflake MCP Server](https://github.com/Snowflake-Labs/mcp)** — Cortex AI integration, object management, SQL orchestration.
- **[MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox)** — BigQuery, Spanner, AlloyDB, Cloud SQL, and 15+ databases.
- **[LaunchDarkly MCP Server](https://github.com/launchdarkly/mcp-server)** — Feature flags, targeting rules, segments, AI configs.
- **[Unleash MCP Server](https://github.com/cuongtl1992/unleash-mcp)** — Read and toggle open-source feature flags.
- **[Temporal MCP Server](https://github.com/alisaitteke/temporal-mcp)** — Run, query, signal Temporal workflows.
- **[Istio MCP Server](https://github.com/krutsko/istio-mcp-server)** — Read-only access to VirtualServices, DestinationRules, Gateways.

## AI-Powered CI/CD

- **[ArgoCD](https://github.com/argoproj/argo-cd)** — *Open-source (CNCF graduated).* GitOps continuous delivery for Kubernetes, foundation for AI-driven deployment workflows.
- **[Buildkite](https://buildkite.com/)** — *Commercial.* CI/CD with AI-powered test analytics and flaky test detection.
- **[CircleCI](https://circleci.com/)** — *Commercial.* Cloud CI/CD with AI-powered test splitting and pipeline optimization.
- **[Codefresh](https://codefresh.io/)** — *Commercial.* GitOps CI/CD built on Argo with AI-assisted pipeline creation.
- **[Dagger](https://github.com/dagger/dagger)** — *Open-source.* Programmable CI/CD engine running pipelines in containers, composable by AI agents.
- **[Depot](https://depot.dev/)** — *Commercial.* Managed build infra with up to 40x faster Docker builds via layer caching.
- **[GitLab Duo](https://about.gitlab.com/gitlab-duo/)** — *Commercial.* AI across the GitLab DevSecOps lifecycle including CI/CD pipeline generation.
- **[Harness AIDA](https://www.harness.io/products/aida)** — *Commercial.* AI assistant for pipeline creation and failure analysis.
- **[Mergify](https://mergify.com/)** — *Commercial.* AI-powered merge queue with intelligent batch merging.
- **[PR-Agent](https://github.com/qodo-ai/pr-agent)** — *Open-source.* Auto-describes, reviews, and generates tests for PRs across GitHub/GitLab/Bitbucket.
- **[Tekton](https://github.com/tektoncd/pipeline)** — *Open-source.* Cloud-native CI/CD building blocks for Kubernetes.
- **[Trunk](https://trunk.io/)** — *Commercial.* AI-powered code quality checks, merge queues, flaky test management.
- **[Devtron](https://github.com/devtron-labs/devtron)** — *Open-source.* Kubernetes-native DevOps platform with AI-driven cost optimization and canary deployments.
- **[Woodpecker CI](https://github.com/woodpecker-ci/woodpecker)** — *Open-source.* Community fork of Drone CI, container-native pipeline engine.
- **[Claude Code Review](https://github.com/anthropics/claude-code-security-review)** — *Open-source (Anthropic).* Multi-agent GitHub Action analyzing PRs for logic errors and security vulnerabilities in parallel.
- **[Cursor BugBot](https://cursor.com/bugbot)** — *Commercial.* Reviews 2M+ PRs monthly with 8 parallel review passes.
- **[Mendral](https://www.mendral.com/)** — *Commercial (YC).* Always-on AI DevOps engineer that diagnoses CI failures and opens fix PRs at a 75% acceptance rate.
- **[Momentic](https://momentic.ai/)** — *Commercial (YC).* Writes and self-heals end-to-end tests for CI/CD.
- **[Stably AI](https://www.stably.ai/)** — *Commercial (YC).* Diff-aware end-to-end tests written directly into CI with automatic selector healing.
- **[testRigor](https://testrigor.com/)** — *Commercial.* Codeless natural-language test creation for CI/CD pipelines.
- **[Testsigma](https://github.com/testsigmahq/testsigma)** — *Open-source.* Agentic test automation with self-healing tests.

## AI Log Analysis and Debugging

- **[agenttrace](https://github.com/luoyuctl/agenttrace)** — *Open-source.* Local TUI for inspecting AI coding-agent logs — cost, tokens, latency, failures.
- **[Axiom](https://axiom.co/)** — *Commercial.* AI-powered query generation with unlimited data retention.
- **[Elasticsearch](https://github.com/elastic/elasticsearch)** — *Open-source.* Foundation for AI log analysis via ES|QL, vector search, and ML anomaly detection.
- **[Grafana Loki](https://github.com/grafana/loki)** — *Open-source.* Log aggregation designed for cloud-native environments, pairs with Grafana AI.
- **[LogAI](https://www.salesforce.com/blog/logai/)** — *Open-source (Salesforce).* Toolkit for AI-powered log anomaly detection, clustering, and summarization.
- **[OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector)** — *Open-source.* Vendor-agnostic telemetry pipeline feeding most AI analysis tools.
- **[Parseable](https://github.com/parseablehq/parseable)** — *Open-source (Rust).* Cloud-native log storage with AI-powered analysis and alerting.
- **[Vector](https://github.com/vectordotdev/vector)** — *Open-source.* High-performance pipeline for routing logs/metrics/traces to AI analysis backends.
- **[Zebrium](https://www.zebrium.com/)** — *Commercial.* ML-powered root cause analysis directly from logs, no manual queries.
- **[Fluentd](https://github.com/fluent/fluentd)** — *Open-source (CNCF graduated).* Unified logging layer for routing logs from any source to any destination.
- **[Fluent Bit](https://github.com/fluent/fluent-bit)** — *Open-source.* Fast, lightweight log processor for cloud-native environments.
- **[Langfuse](https://github.com/langfuse/langfuse)** — *Open-source.* LLM observability with tracing, prompt management, and evals for monitoring agents in DevOps pipelines.
- **[OpenLLMetry](https://github.com/traceloop/openllmetry)** — *Open-source.* OpenTelemetry-compatible instrumentation for OpenAI/Anthropic/other LLM providers.
- **[Braintrust](https://braintrust.dev/)** — *Commercial.* AI observability/eval platform with trace capture and automated scoring.

## AI Agent Frameworks

- **[AutoGen](https://github.com/microsoft/autogen)** — *Open-source (Microsoft).* Multi-agent framework with tool use and human-in-the-loop approvals.
- **[Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview)** — *Commercial (Anthropic).* Framework for agentic apps with tool orchestration and guardrails.
- **[CrewAI](https://github.com/crewAIInc/crewAI)** — *Open-source.* Multi-agent orchestration for teams of agents handling complex tasks like migration planning.
- **[Dify](https://github.com/langgenius/dify)** — *Open-source.* LLM app platform with agent workflows and RAG for custom DevOps chatbots.
- **[Haystack](https://github.com/deepset-ai/haystack)** — *Open-source (deepset).* RAG pipeline and agent framework for infra knowledge bases.
- **[LangChain](https://github.com/langchain-ai/langchain)** — *Open-source.* The most widely used framework for building custom DevOps agents with tool integrations.
- **[LangChain Deep Agents](https://github.com/langchain-ai/deepagents)** — *Open-source.* Reference agent harness with planning tools and subagent spawning for complex tasks.
- **[LangGraph](https://github.com/langchain-ai/langgraph)** — *Open-source.* Stateful multi-actor apps with LLMs, ideal for complex orchestration workflows.
- **[Llama Stack](https://github.com/meta-llama/llama-stack)** — *Open-source (Meta).* Unified deployment stack: inference, agents, safety, evaluation.
- **[LlamaIndex](https://github.com/run-llama/llama_index)** — *Open-source.* Indexing/retrieval/agent framework for infra documentation.
- **[Mastra](https://github.com/mastra-ai/mastra)** — *Open-source.* TypeScript agent framework with built-in tools, workflows, RAG.
- **[Microsoft Agent Framework](https://github.com/microsoft/agent-framework)** — *Open-source.* Unified .NET/Python SDK merging Semantic Kernel and AutoGen with MCP/A2A support.
- **[n8n](https://github.com/n8n-io/n8n)** — *Open-source.* 400+ integrations with AI agent capabilities for low-code automation.
- **[Google ADK](https://github.com/google/adk-python)** — *Open-source.* Code-first multi-agent framework with MCP tool integration and Cloud Run deployment.
- **[OpenAI Agents SDK](https://github.com/openai/openai-agents-python)** — *Open-source.* Multi-agent systems with handoffs, guardrails, and tracing.
- **[Pydantic AI](https://github.com/pydantic/pydantic-ai)** — *Open-source.* Type-safe agent framework with native MCP support and 25+ model providers.
- **[smolagents](https://github.com/huggingface/smolagents)** — *Open-source (Hugging Face).* Minimalist agents that write and execute Python code with sandboxing.
- **[Semantic Kernel](https://github.com/microsoft/semantic-kernel)** — *Open-source.* Plugin-architecture SDK for integrating LLMs into applications.
- **[Temporal](https://github.com/temporalio/temporal)** — *Open-source.* Durable execution platform for long-running infra workflows.
- **[DSPy](https://github.com/stanfordnlp/dspy)** — *Open-source (Stanford).* Programming framework for LMs with automatic prompt optimization.
- **[OpenClaw](https://github.com/openclaw/openclaw)** — *Open-source.* Personal AI assistant with 50+ integrations and fully local execution.
- **[Wren AI](https://github.com/Canner/WrenAI)** — *Open-source.* Text-to-SQL agent for infra analytics and reporting.
- **[MetaGPT](https://github.com/geekan/MetaGPT)** — *Open-source.* Simulates an AI software company — PM, architect, engineer, QA agents collaborating.
- **[Letta](https://github.com/letta-ai/letta)** — *Open-source.* Stateful agents with self-editing memory, evolved from MemGPT.
- **[Strands Agents](https://github.com/strands-agents)** — *Open-source (AWS).* Model-driven SDK with Graph/Swarm/Workflow patterns and native MCP/A2A.
- **[BeeAI Framework](https://github.com/i-am-bee/beeai-framework)** — *Open-source (IBM/Linux Foundation).* Multi-agent toolkit with Agent Communication Protocol for cross-framework interop.
- **[Agno](https://github.com/agno-agi/agno)** — *Open-source.* Lightweight multi-modal agent framework with built-in FastAPI runtime.
- **[Mirascope](https://github.com/Mirascope/mirascope)** — *Open-source.* Pythonic LLM toolkit with a unified provider interface and structured outputs.
- **[Kubiya](https://www.kubiya.ai/)** — *Commercial.* Agentic engineering platform with deterministic execution and Slack/Teams interface for Terraform/CI automation.
- **[agentgateway](https://github.com/agentgateway/agentgateway)** — *Open-source (Solo.io).* Rust proxy with deep MCP/A2A protocol awareness and unified LLM routing.
- **[open-multi-agent](https://github.com/JackChen-me/open-multi-agent)** — *Open-source.* TypeScript orchestrator decomposing goals into a task DAG with live tracing.
- **[Composio Agent Orchestrator](https://github.com/ComposioHQ/agent-orchestrator)** — *Open-source.* Parallel coding-agent fleet manager with per-agent git worktrees.

## AI for Platform Engineering

- **[Backstage](https://github.com/backstage/backstage)** — *Open-source (CNCF incubating, Spotify).* Developer portal foundation with service catalogs and plugins.
- **[Cortex](https://www.cortex.io/)** — *Commercial.* AI-driven service maturity scorecards and ownership tracking.
- **[Cycloid](https://www.cycloid.io/)** — *Commercial.* AI-powered infra self-service with cost governance.
- **[Humanitec](https://humanitec.com/)** — *Commercial.* Platform orchestrator powering enterprise internal developer platforms.
- **[Kratix](https://github.com/syntasso/kratix)** — *Open-source.* Framework for platforms-as-a-product on Kubernetes.
- **[Mia-Platform](https://mia-platform.eu/)** — *Commercial.* AI-powered microservice orchestration and developer self-service.
- **[OpsLevel](https://www.opslevel.com/)** — *Commercial.* Service ownership platform with AI-powered maturity tracking.
- **[Port](https://www.getport.io/)** — *Commercial (open core).* AI-powered software catalog and self-service actions.
- **[Qovery](https://www.qovery.com/)** — *Commercial.* Production-like developer environments with AI-assisted deployment.
- **[Roadie](https://roadie.io/)** — *Commercial.* Managed Backstage with AI-powered scaffolding and TechDocs hosting.
- **[Upbound](https://www.upbound.io/)** — *Commercial.* Universal cloud platform built on Crossplane for declarative infra APIs.
- **[Score](https://github.com/score-spec/spec)** — *Open-source.* Workload spec eliminating config drift between local and remote environments.
- **[StackGen](https://stackgen.com/)** — *Commercial.* Autonomous infra platform generating validated, policy-compliant Terraform from natural language.
- **[OpenChoreo](https://github.com/openchoreo/openchoreo)** — *Open-source (CNCF Sandbox).* IDP exposing MCP servers so agents can deploy components and reason about platform state.

## AI for Database Operations

- **[Aiven AI](https://aiven.io/)** — *Commercial.* Managed databases with AI-powered query optimization and anomaly detection.
- **[Bytebase](https://github.com/bytebase/bytebase)** — *Open-source.* Database DevOps/CI-CD with AI-assisted schema review and migration management.
- **[CloudNativePG](https://github.com/cloudnative-pg/cloudnative-pg)** — *Open-source.* Kubernetes operator managing full PostgreSQL cluster lifecycle with automated failover.
- **[Drizzle](https://github.com/drizzle-team/drizzle-orm)** — *Open-source.* TypeScript ORM with declarative, AI-friendly type-safe migrations.
- **[Metabase](https://github.com/metabase/metabase)** — *Open-source.* BI platform with natural-language querying for non-technical users.
- **[Neon](https://github.com/neondatabase/neon)** — *Open-source core / Commercial.* Serverless Postgres with branching and AI-powered query optimization.
- **[OtterTune](https://github.com/ottertune/)** — *Commercial.* Automatically tunes Postgres/MySQL/MariaDB configuration for performance.
- **[pganalyze](https://pganalyze.com/)** — *Commercial.* Postgres monitoring with AI-powered query recommendations and index advisor.
- **[PlanetScale](https://planetscale.com/)** — *Commercial.* Serverless MySQL with AI-powered schema change management and non-blocking deploys.
- **[SchemaHero](https://github.com/schemahero/schemahero)** — *Open-source.* Kubernetes-native declarative schema migrations.
- **[Tembo](https://tembo.io/)** — *Open-source.* Serverless Postgres with AI-driven optimization and error resolution.
- **[Vitess](https://github.com/vitessio/vitess)** — *Open-source (CNCF graduated).* Horizontal scaling clustering system for MySQL.
- **[Xata](https://xata.io/)** — *Commercial.* Serverless database combining Postgres with OpenSearch for full-text/vector search.

## AI for Networking and Service Mesh

- **[Calico](https://github.com/projectcalico/calico)** — *Open-source.* Cloud-native networking/security with AI-enhanced policy management.
- **[Cilium](https://github.com/cilium/cilium)** — *Open-source.* eBPF-based networking/observability for Kubernetes with the Hubble flow-analysis UI.
- **[Consul](https://github.com/hashicorp/consul)** — *Open-source core / Commercial (HashiCorp).* Service mesh and discovery with intentions-based security.
- **[Istio](https://github.com/istio/istio)** — *Open-source (CNCF graduated).* Traffic management, security, and observability for microservices.
- **[Linkerd](https://github.com/linkerd/linkerd2)** — *Open-source (CNCF graduated).* Ultralight service mesh with automated mTLS and golden metrics.
- **[Ngrok](https://ngrok.com/)** — *Commercial.* Unified ingress with AI-powered traffic inspection and policy enforcement.
- **[Traefik](https://github.com/traefik/traefik)** — *Open-source.* Cloud-native proxy with automatic service discovery.
- **[Envoy](https://github.com/envoyproxy/envoy)** — *Open-source (CNCF graduated).* High-performance proxy powering Istio's data plane.

## AI for Container Security and Supply Chain

- **[Chainguard](https://www.chainguard.dev/)** — *Commercial.* Secure container images with zero known CVEs.
- **[Cosign](https://github.com/sigstore/cosign)** — *Open-source (Sigstore).* Container signing and verification.
- **[Docker Scout](https://docs.docker.com/scout/)** — *Commercial.* AI-powered supply-chain analysis and CVE remediation guidance.
- **[Grype](https://github.com/anchore/grype)** — *Open-source.* Fast vulnerability scanner with SBOM-based analysis.
- **[Harbor](https://github.com/goharbor/harbor)** — *Open-source (CNCF graduated).* Registry with vulnerability scanning and image signing.
- **[Slim.AI](https://www.slim.ai/)** — *Commercial.* AI-powered image minification and vulnerability reduction.
- **[Copa](https://github.com/project-copacetic/copacetic)** — *Open-source.* Directly patches image vulnerabilities without a full rebuild.
- **[Syft](https://github.com/anchore/syft)** — *Open-source.* SBOM generator for images and filesystems.
- **[Wolfi](https://github.com/wolfi-dev/os)** — *Open-source.* Community Linux distro for minimal container images with automated CVE patching.

## AI for Chaos Engineering and Reliability

- **[Chaos Mesh](https://github.com/chaos-mesh/chaos-mesh)** — *Open-source (CNCF incubating).* Cloud-native chaos platform with fault injection and workflow orchestration.
- **[Gremlin](https://www.gremlin.com/)** — *Commercial.* Enterprise chaos engineering with AI-powered reliability recommendations.
- **[k6](https://github.com/grafana/k6)** — *Open-source (Grafana).* Scriptable load testing with AI-assisted test generation.
- **[Litmus](https://github.com/litmuschaos/litmus)** — *Open-source (CNCF incubating).* Chaos framework with a hub of prebuilt experiments and GitOps integration.
- **[Steadybit](https://www.steadybit.com/)** — *Commercial.* AI-assisted experiment design and reliability validation.
- **[Testkube](https://github.com/kubeshop/testkube)** — *Open-source.* Kubernetes-native test orchestration for any testing tool.
- **[Toxiproxy](https://github.com/Shopify/toxiproxy)** — *Open-source (Shopify).* TCP proxy simulating network conditions for resilience testing.
- **[ChaosEater](https://github.com/ntt-dkiku/chaos-eater)** — *Open-source (NTT).* LLM-based system automating the whole chaos-engineering cycle across GPT/Claude/Gemini/Ollama.

## AI for Cloud Migration and Modernization

- **[AWS Application Discovery Service](https://aws.amazon.com/application-discovery/)** — *Commercial.* Automated discovery and dependency mapping for migration planning.
- **[AWS Migration Hub](https://aws.amazon.com/migration-hub/)** — *Commercial.* Central migration tracking with AI-powered progress tracking.
- **[Azure Migrate](https://azure.microsoft.com/en-us/products/azure-migrate/)** — *Commercial.* Unified migration with AI-powered assessment and modernization tools.
- **[Google Cloud Migrate](https://cloud.google.com/solutions/migration-center)** — *Commercial.* AI-driven workload discovery and TCO analysis.
- **[Konveyor](https://github.com/konveyor/tackle2-hub)** — *Open-source.* Migration toolkit for modernizing apps to Kubernetes with AI-assisted code transformation.
- **[Zerto](https://www.zerto.com/)** — *Commercial.* Disaster recovery and workload migration with continuous data protection.

## AI for GitOps

- **[Argo Rollouts](https://github.com/argoproj/argo-rollouts)** — *Open-source.* Progressive delivery controller with canary/blue-green releases and automated rollback analysis.
- **[Flux](https://github.com/fluxcd/flux2)** — *Open-source (CNCF graduated).* GitOps toolkit with automated image updates and Helm/Kustomize reconciliation.
- **[Helm](https://github.com/helm/helm)** — *Open-source (CNCF graduated).* Kubernetes package manager for templating AI workloads and infra components.
- **[Kargo](https://github.com/akuity/kargo)** — *Open-source.* Continuous promotion orchestrator across environments with GitOps principles.
- **[Kustomize](https://github.com/kubernetes-sigs/kustomize)** — *Open-source.* Declarative manifest customization without template engines.
- **[Weave GitOps](https://github.com/weaveworks/weave-gitops)** — *Commercial (open core).* Enterprise GitOps with progressive delivery and policy enforcement.
- **[Crossplane](https://github.com/crossplane/crossplane)** — *Open-source (CNCF incubating).* Cloud-native control planes with declarative infra APIs.

## System Prompt and Config Templates

- **[AGENTS.md](https://agents.md/)** — *Open standard (OpenAI).* Universal format for project-specific AI agent guidance, supported across Cursor, Claude Code, Codex, Gemini CLI.
- **[Awesome CursorRules](https://github.com/PatrickJS/awesome-cursorrules)** — *Open-source.* Community `.cursorrules` files for various project types.
- **[Claude Skills](https://github.com/anthropics/skills)** — *Open-source (Anthropic).* Official repository of agent skills for specialized DevOps workflows.
- **[GitHub Copilot Custom Instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)** — *Official docs.* Guide for `copilot-instructions.md` per-repo customization.

## Learning Resources

### Books
- **[Site Reliability Engineering](https://sre.google/books/)** — Google's foundational SRE book; the practices today's AI SRE tools automate.
- **[Platform Engineering on Kubernetes](https://www.manning.com/books/platform-engineering-on-kubernetes)** — Building internal platforms with Kubernetes, GitOps, and developer self-service.

### Certifications
- **[AWS Certified DevOps Engineer Professional](https://aws.amazon.com/certification/certified-devops-engineer-professional/)** — CI/CD automation, monitoring, and operations at scale on AWS.
- **[Azure DevOps Engineer Expert](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-400/)** — DevOps process design including IaC and compliance on Azure.
- **[AWS Certified Machine Learning Engineer Associate](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/)** — Getting ML models into production with SageMaker.

## Community and Newsletters

- **[CNCF Slack](https://slack.cncf.io/)** — The default hub for CNCF project discussion, including most AI-adjacent Sandbox/incubating projects on this list.
- **[SRE Weekly](https://sreweekly.com/)** — Curated weekly SRE news and incident write-ups.
- **[DevOps Weekly](https://www.devopsweekly.com/)** — Long-running weekly DevOps roundup.

---

## How This Stays Updated

This repo runs a scheduled GitHub Action (`.github/workflows/discover-tools.yml`) that:
1. Queries the GitHub API weekly for repos matching topics like `ai-sre`, `llmops`, `ai-devops`, `kubernetes-ai` sorted by recent star growth.
2. Filters out anything already listed here.
3. Opens a pull request with candidate entries drafted for review — nothing is auto-merged, so the list stays curated, not spammy.

See [`scripts/discover_tools.py`](scripts/discover_tools.py). New tools get folded into the categories above roughly weekly; the total count in the badge at the top is accurate as of the last merge, not aspirational.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). PRs for new tools, corrections, or dead-link fixes are welcome — please follow the `- **[Name](url)** — *Type.* Description.` format used above.

## About

Maintained by [Neel Shah](https://github.com/neelshah2409) — add a line here about why you built this and a link to your blog/socials.

## License

[CC0](LICENSE) — this list is dedicated to the public domain, per [awesome list conventions](https://github.com/sindresorhus/awesome/blob/main/awesome.md).
