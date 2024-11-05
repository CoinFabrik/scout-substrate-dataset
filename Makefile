# Makefile for generating findings JSON files

# Default target to create dataset files
.PHONY: dataset
dataset:
	mkdir -p dataset
	python3 scripts/aggregate_findings.py
	python3 scripts/linearize_findings.py

# Clean target to remove dataset folder
.PHONY: clean
clean:
	rm -rf dataset
