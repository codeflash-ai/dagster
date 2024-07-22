import os

import yaml

from dagster._core.telemetry import get_or_create_dir_from_dagster_home

NUX_FILE_STR = "nux.yaml"


# Filepath for where we store if we've seen the nux
def nux_seen_filepath():
    return os.path.join(get_or_create_dir_from_dagster_home(".nux"), "nux.yaml")


# Sets whether we've shown the Nux to any user on this instance
def set_nux_seen():
    try:  # In case we encounter an error while writing to user's file system
        with open(nux_seen_filepath(), "w", encoding="utf8") as nux_seen_file:
            # the contents of the file dont matter, we just check that it exists, but lets write seen: True here anyways.
            yaml.dump({"seen": 1}, nux_seen_file, default_flow_style=False)
    except Exception:
        return "<<unable_to_write_nux_seen>>"


def get_has_seen_nux():
    try:
        # Compute the file path once and reuse it
        path = nux_seen_filepath()
        return os.path.exists(path)
    except:
        return True
