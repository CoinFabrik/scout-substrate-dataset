# Makefile for generating findings JSON files

# Default target to create dataset files
.PHONY: dataset
dataset:
	mkdir -p dataset
	python3 scripts/aggregate_findings.py
	python3 scripts/linearize_findings.py

# Filter dataset
.PHONY: filter-dataset
filter-dataset:
	python3 scripts/filter_findings.py

# Create Precision and Recall dataset
.PHONY: precision-and-recall-dataset
precision-and-recall-dataset:
	python3 scripts/precision_and_recall.py
	
# Clean target to remove dataset folder
.PHONY: clean
clean:
	rm -rf dataset
