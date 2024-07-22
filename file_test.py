import pytest
import os
from collections import defaultdict
from main import categorize_files_by_type


@pytest.fixture
def create_temp_env(tmp_path):
    (tmp_path / "1.txt").write_text("sun")
    (tmp_path / "2.jpg").write_text("sun")
    sub_dir = tmp_path / "subfol"
    sub_dir.mkdir()
    (sub_dir / "3.txt").write_text("sun")
    (sub_dir / "4.pdf").write_text("sun")
    return tmp_path


@pytest.fixture
def create_temp_env_non_extensions(tmp_path):
    (tmp_path / "1").write_text("sun")
    (tmp_path / "2").write_text("sun")
    sub_dir = tmp_path / "subfol"
    sub_dir.mkdir()
    (sub_dir / "3").write_text("sun")
    (sub_dir / "4").write_text("sun")
    return tmp_path


def test_existing_path(create_temp_env):
    result = categorize_files_by_type(str(create_temp_env))
    exp_result = {
        '.txt': [str(create_temp_env / "1.txt"), str(create_temp_env / "subfol" / "3.txt")],
        '.jpg': [str(create_temp_env / "2.jpg")],
        '.pdf': [str(create_temp_env / "subfol" / "4.pdf")],
    }
    assert result == exp_result


def test_empty_folder(tmp_path):
    result = categorize_files_by_type(str(tmp_path))
    exp_result = defaultdict(list)
    assert result == exp_result


def test_files_non_extension(create_temp_env_non_extensions):
    result = categorize_files_by_type(str(create_temp_env_non_extensions))
    expected = {
        '': [str(create_temp_env_non_extensions / "1"), str(create_temp_env_non_extensions / "2"),
             str(create_temp_env_non_extensions / "subfol" / "3"), str(create_temp_env_non_extensions / "subfol" / "4")],
    }
    print(dict(result))
    print(dict(expected))
    assert sorted(result['']) == sorted(expected[''])
