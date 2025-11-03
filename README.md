<div align="center">
  <a href="https://pathway.com/">
    <img src="https://pathway.com/logo-light.svg"/>
  </a>
  <br /><br />
  <a href="https://trendshift.io/repositories/10388" target="_blank"><img src="https://trendshift.io/api/badge/repositories/10388" alt="pathwaycom%2Fpathway | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
  <br /><br />
</div>
<p align="center">
        <a href="https://github.com/pathwaycom/pathway/actions/workflows/ubuntu_test.yml">
        <img src="https://github.com/pathwaycom/pathway/actions/workflows/ubuntu_test.yml/badge.svg" alt="ubuntu"/>
        <br>
        <a href="https://github.com/pathwaycom/pathway/actions/workflows/release.yml">
        <img src="https://github.com/pathwaycom/pathway/actions/workflows/release.yml/badge.svg" alt="Last release"/></a>
        <a href="https://badge.fury.io/py/pathway"><img src="https://badge.fury.io/py/pathway.svg" alt="PyPI version" height="18"></a>
        <a href="https://badge.fury.io/py/pathway"><img src="https://static.pepy.tech/badge/pathway" alt="PyPI downloads" height="18"></a>
        <a href="https://github.com/pathwaycom/pathway/blob/main/LICENSE.txt">
        <img src="https://img.shields.io/badge/license-BSL-green" alt="License: BSL"/></a>
      <br>
        <a href="https://discord.gg/pathway">
        <img src="https://img.shields.io/discord/1042405378304004156?logo=discord"
            alt="chat on Discord"></a>
        <a href="https://twitter.com/intent/follow?screen_name=pathway_com">
        <img src="https://img.shields.io/twitter/follow/pathwaycom"
            alt="follow on Twitter"></a>
        <a href="https://linkedin.com/company/pathway">
        <img src="https://img.shields.io/badge/pathway-0077B5?style=social&logo=linkedin" alt="follow on LinkedIn"></a>
      <a href="https://github.com/dylanhogg/awesome-python/blob/main/README.md">
      <img src="https://awesome.re/badge.svg" alt="Awesome Python"></a>
      <a href="https://gurubase.io/g/pathway">
      <img src="https://img.shields.io/badge/Gurubase-Ask%20Pathway%20Guru-006BFF" alt="Pathway Guru"></a>
    <br>
    <a href="#getting-started">Getting Started</a> |
    <a href="#deployment">Deployment</a> |
    <a href="#resources">Documentation and Support</a> |
    <a href="https://pathway.com/blog/">Blog</a> |
    <a href="#license">License</a>

  
</p>

# Pathway<a id="pathway"> Live Data Framework</a>

[Pathway](https://pathway.com) is a Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.

Pathway comes with an **easy-to-use Python API**, allowing you to seamlessly integrate your favorite Python ML libraries.
Pathway code is versatile and robust: **you can use it in both development and production environments, handling both batch and streaming data effectively**.
The same code can be used for local development, CI/CD tests, running batch jobs, handling stream replays, and processing data streams.

Pathway is powered by a **scalable Rust engine** based on Differential Dataflow and performs incremental computation.
Your Pathway code, despite being written in Python, is run by the Rust engine, enabling multithreading, multiprocessing, and distributed computations.
All the pipeline is kept in memory and can be easily deployed with **Docker and Kubernetes**.

You can install Pathway with pip:
```
pip install -U pathway
```

For any questions, you will find the community and team behind the project [on Discord](https://discord.com/invite/pathway).

## Use-cases and templates

Ready to see what Pathway can do?

[Try one of our easy-to-run examples](https://pathway.com/developers/templates)!

Available in both notebook and docker formats, these ready-to-launch examples can be launched in just a few clicks. Pick one and start your hands-on experience with Pathway today!

### Event processing and real-time analytics pipelines
With its unified engine for batch and streaming and its full Python compatibility, Pathway makes data processing as easy as possible. It's the ideal solution for a wide range of data processing pipelines, including:

- [Showcase: Real-time ETL.](https://pathway.com/developers/templates/kafka-etl)
- [Showcase: Event-driven pipelines with alerting.](https://pathway.com/developers/templates/realtime-log-monitoring)
- [Showcase: Realtime analytics.](https://pathway.com/developers/templates/linear_regression_with_kafka)
- [Docs: Switch from batch to streaming.](https://pathway.com/developers/user-guide/connecting-to-data/switch-from-batch-to-streaming)



### AI Pipelines

Pathway provides dedicated LLM tooling to build live LLM and RAG pipelines. Wrappers for most common LLM services and utilities are included, making working with LLMs and RAGs pipelines incredibly easy. Check out our [LLM xpack documentation](https://pathway.com/developers/user-guide/llm-xpack/overview).

Don't hesitate to try one of our runnable examples featuring LLM tooling.
You can find such examples [here](https://pathway.com/developers/user-guide/llm-xpack/llm-examples).

  - [Template: Unstructured data to SQL on-the-fly.](https://pathway.com/developers/templates/unstructured-to-structured)
  - [Template: Private RAG with Ollama and Mistral AI](https://pathway.com/developers/templates/private-rag-ollama-mistral)
  - [Template: Adaptive RAG](https://pathway.com/developers/templates/adaptive-rag)
  - [Template: Multimodal RAG with gpt-4o](https://pathway.com/developers/templates/multimodal-rag)

## Features

- **A wide range of connectors**: Pathway comes with connectors that connect to external data sources such as Kafka, GDrive, PostgreSQL, or SharePoint. Its Airbyte connector allows you to connect to more than 300 different data sources. If the connector you want is not available, you can build your own custom connector using Pathway Python connector.
- **Stateless and stateful transformations**: Pathway supports stateful transformations such as joins, windowing, and sorting. It provides many transformations directly implemented in Rust. In addition to the provided transformation, you can use any Python function. You can implement your own or you can use any Python library to process your data.
- **Persistence**: Pathway provides persistence to save the state of the computation. This allows you to restart your pipeline after an update or a crash. Your pipelines are in good hands with Pathway!
- **Consistency**: Pathway handles the time for you, making sure all your computations are consistent. In particular, Pathway manages late and out-of-order points by updating its results whenever new (or late, in this case) data points come into the system. The free version of Pathway gives the "at least once" consistency while the enterprise version provides the "exactly once" consistency.
- **Scalable Rust engine**: with Pathway Rust engine, you are free from the usual limits imposed by Python. You can easily do multithreading, multiprocessing, and distributed computations.
- **LLM helpers**: Pathway provides an LLM extension with all the utilities to integrate LLMs with your data pipelines (LLM wrappers, parsers, embedders, splitters), including an in-memory real-time Vector Index, integrations with LLamaIndex and LangChain, and advanced RAG features like query transformation for improved retrieval. You can quickly build and deploy RAG applications with your live documents.