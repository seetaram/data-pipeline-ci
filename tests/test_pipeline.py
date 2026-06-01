import pytest
from etl.pipeline import extract, transform, load
import json
import os
import tempfile


# --- transform() tests ---

def test_transform_filters_inactive():
    data = [
        {"id": 1, "name": "alice", "status": "active"},
        {"id": 2, "name": "bob", "status": "inactive"},
    ]
    result = transform(data)
    assert len(result) == 1
    assert result[0]["id"] == 1


def test_transform_normalizes_name():
    data = [{"id": 1, "name": "  john doe  ", "status": "active"}]
    result = transform(data)
    assert result[0]["name"] == "John Doe"


def test_transform_empty_input():
    assert transform([]) == []


def test_transform_all_inactive():
    data = [{"id": 1, "name": "alice", "status": "inactive"}]
    assert transform(data) == []


# --- extract() tests ---

def test_extract_reads_json():
    sample = [{"id": 1, "name": "alice", "status": "active"}]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(sample, f)
        tmp_path = f.name
    result = extract(tmp_path)
    os.unlink(tmp_path)
    assert result == sample


# --- load() tests ---

def test_load_writes_json():
    data = [{"id": 1, "name": "Alice", "status": "active"}]
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = os.path.join(tmpdir, "out", "output.json")
        load(data, output_path)
        with open(output_path) as f:
            result = json.load(f)
        assert result == data
