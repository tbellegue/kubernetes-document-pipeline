# Scalable Document Processing and Analysis Pipeline on Kubernetes

## Project Overview

This project will design and implement a scalable document processing and analysis pipeline deployed on Kubernetes.

Users will submit text documents through an application programming interface (API). Documents will move through separate services for preprocessing, analysis, and storage. The analysis service will extract characteristics such as word count, sentence count, frequently occurring words, and basic sentiment.

The project will demonstrate cloud-native concepts including:

- Multi-pod application architecture
- Multi-container pods using a sidecar container
- Kubernetes service discovery
- Horizontal scaling
- Self-healing
- Persistent storage
- Health monitoring
- Container resource management

## Architecture

The proposed pipeline consists of four primary application components:

1. API Gateway
2. Document Preprocessing Service
3. Document Analysis Service
4. Storage Service

The API Gateway will serve as the application's external entry point, while the remaining components will communicate internally through Kubernetes Services.

## Documentation

The technical report for Project Deliverable 1 is included in this repository.
