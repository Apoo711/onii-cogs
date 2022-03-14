import glob
import json
import logging
import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Mapping, Optional

import click
import tabulate
from babel.lists import format_list as babel_list

DEFAULT_INFO = {
    "author": [],
    "install_msg": "",
    "name": "",
    "disabled": False,
    "short": "",
    "description": "",
    "tags": [],
    "requirements": [],
    "hidden": False,
}

logging.basicConfig(filename="scripts.log", level=logging.INFO)
log = logging.getLogger(__file__)

ROOT = Path(__file__).parent.resolve().parents[1]

VER_REG = re.compile(r"\_\_version\_\_ = \"(\d+\.\d+\.\d+)", flags=re.I)

DEFAULT_AUTHOR = ["Onii-chan"]


HEADER = """# Onii-cogs V3
[![Red-DiscordBot](https://img.shields.io/badge/Red--DiscordBot-V3-red.svg)](https://github.com/Cog-Creators/Red-DiscordBot)
[![Discord.py](https://img.shields.io/badge/Discord.py-rewrite-blue.svg)](https://github.com/Rapptz/discord.py/tree/rewrite)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![CodeFactor](https://www.codefactor.io/repository/github/onii-chan-discord/onii-cogs/badge)](https://www.codefactor.io/repository/github/onii-chan-discord/onii-cogs)


Onii-chan's Cogs for  [Red-DiscordBot](https://github.com/Cog-Creators/Red-DiscordBot/tree/V3/develop).
To add the cogs to your instance please do: `[p]repo add Onii-cogs https://github.com/Onii-Chan-Discord/onii-cogs`

## About Cogs

{body}

Any questions you can find [Izumi](https://dcg.gg/izumi) and myself over on the [Redbot Cog Support server](https://discord.gg/GET4DVk).

## Credits

- Everyone who contributed to make this better.
- Thank you Red community, you guys are awesome.
- Thank you TrustyJAID#0001 for making the tool that has generated this README.
You can find his tool [here](https://github.com/TrustyJAID/Trusty-cogs/tree/master/.utils)
"""


@dataclass
class InfoJson:
    author: List[str]
    description: Optional[str] = ""
    install_msg: Optional[str] = "Thanks for installing"
    short: Optional[str] = ""
    name: Optional[str] = ""
    min_bot_version: Optional[str] = "3.3.0"
    max_bot_version: Optional[str] = "0.0.0"
    hidden: Optional[bool] = False
    disabled: Optional[bool] = False
    required_cogs: Mapping = field(default_factory=dict)
    requirements: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    type: Optional[str] = "COG"
    permissions: List[str] = field(default_factory=list)
    min_python_version: Optional[List[int]] = field(
        default_factory=lambda: [3, 8, 0]
    )
    end_user_data_statement: str = (
        "This cog does not persistently store data or metadata about users."
    )

    @classmethod
    def from_json(cls, data: dict):
        author = []
        description = ""
        install_msg = "Thanks for installing"
        short = "Thanks for installing"
        min_bot_version = "3.1.8"
        max_bot_version = "0.0.0"
        name = ""
        required_cogs: Mapping = {}
        requirements = []
        tags = []
        hidden = False
        disabled = False
        type = "COG"
        permissions = []
        min_python_version = []
        end_user_data_statement = "This cog does not persistently store data or metadata about users."
        if "author" in data:
            author = data["author"]
        if "description" in data:
            description = data["description"]
        if "install_msg" in data:
            install_msg = data["install_msg"]
        if "short" in data:
            short = data["short"]
        if "bot_version" in data:
            min_bot_version = data["bot_version"]
            if isinstance(min_bot_version, list):
                min_bot_version = ".".join(str(i) for i in data["bot_version"])
        if "min_bot_version" in data:
            min_bot_version = data["min_bot_version"]
            # min_bot_version = "3.3.0"
        if "max_bot_version" in data:
            max_bot_version = data["max_bot_version"]
            # max_bot_version = "0.0.0"
        if "name" in data:
            name = data["name"]
        if "required_cogs" in data:
            if isinstance(data["required_cogs"], list):
                required_cogs = {}
            else:
                required_cogs = data["required_cogs"]
        if "requirements" in data:
            requirements = data["requirements"]
        if "tags" in data:
            tags = data["tags"]
        if "hidden" in data:
            hidden = data["hidden"]
        if "disabled" in data:
            disabled = data["disabled"]
        if "type" in data:
            type = data["type"]
        if "permissions" in data:
            permissions = data["permissions"]
        if "min_python_version" in data:
            min_python_version = data["min_python_version"]
            # min_python_version = [3, 8, 0]
        if "end_user_data_statement" in data:
            end_user_data_statement = data["end_user_data_statement"]

        return cls(
            author,
            description,
            install_msg,
            short,
            name,
            min_bot_version,
            max_bot_version,
            hidden,
            disabled,
            required_cogs,
            requirements,
            tags,
            type,
            permissions,
            min_python_version,
            end_user_data_statement,
        )


def save_json(folder, data):
    with open(folder, "w") as newfile:
        json.dump(
            data, newfile, indent=4, sort_keys=True, separators=(",", " : ")
        )


@click.group()
def cli():
    """Utilities for Cog creation!"""
    pass


@cli.command()
def mass_fix():
    """Ensure all info.json files are up-to-date with current standards"""
    for folder in os.listdir(f"{ROOT}/"):
        if folder.startswith("."):
            continue
        try:
            with open(f"{ROOT}/{folder}/info.json", "r") as infile:
                info = InfoJson.from_json(json.load(infile))
            save_json(f"{ROOT}/{folder}/info.json", info.__dict__)
        except Exception:
            log.exception(f"Error reading info.json in {folder}")
            continue


@cli.command()
@click.option(
    "--author", default=DEFAULT_AUTHOR, help="Author of the cog", prompt=True
)
@click.option(
    "--name",
    prompt="Enter the name of the cog",
    help="Name of the cog being added",
)
@click.option(
    "--description",
    prompt="Enter a longer description for the cog.",
    help="Description about what the cog can do.",
)
@click.option(
    "--install-msg",
    prompt=True,
    default="Thanks for installing!",
    help="Enter the install message you would like. Default is `Thanks for installing!`",
)
@click.option(
    "--short",
    prompt="Enter a short description about the cog.",
    help="Enter a short description about the cog.",
)
@click.option(
    "--min-bot-version",
    default="3.3.0",
    help="This cogs minimum python version requirements.",
    prompt=True,
)
@click.option(
    "--max-bot-version",
    default="0.0.0",
    help="This cogs minimum python version requirements.",
    prompt=True,
)
@click.option(
    "--hidden",
    default=False,
    help="Whether or not the cog is hidden from downloader.",
    prompt=True,
    type=bool,
)
@click.option(
    "--disabled",
    default=False,
    help="Whether or not the cog is disabled in downloader.",
    prompt=True,
    type=bool,
)
@click.option(
    "--required-cogs",
    default={},
    help="Required cogs for this cog to function.",
)
@click.option(
    "--requirements", prompt=True, default=[], help="Requirements for the cog."
)
@click.option(
    "--tags",
    default=[],
    prompt=True,
    help="Any tags to help people find the cog better.",
)
@click.option(
    "--permissions",
    prompt=True,
    default=[],
    help="Any permissions the cog requires.",
)
@click.option(
    "--min-python-version",
    default=[3, 8, 0],
    help="This cogs minimum python version requirements.",
)
@click.option(
    "--end-user-data-statement",
    prompt=True,
    default="This cog does not persistently store data or metadata about users.",
    help="The end user data statement for this cog.",
)
def make(
    author: list,
    name: str,
    description: str = "",
    install_msg: str = "",
    short: str = "",
    min_bot_version: str = "3.3.0",
    max_bot_version: str = "0.0.0",
    hidden: bool = False,
    disabled: bool = False,
    required_cogs: Mapping[str, str] = {},
    requirements: List[str] = [],
    tags: list = [],
    permissions: list = [],
    min_python_version: list = [3, 8, 0],
    end_user_data_statement: str = "This cog does not persistently store data or metadata about users.",
):
    """Generate a new info.json file for your new cog!"""
    if isinstance(author, str):
        author = [author]
        if ", " in author:
            author = author.split(", ")
    if isinstance(requirements, str):
        requirements = requirements.split(" ")
    if isinstance(permissions, str):
        permissions = permissions.split(" ")
    if isinstance(tags, str):
        tags = tags.split(" ")
    if isinstance(min_python_version, str):
        min_python_version = [int(i) for i in min_python_version.split(".")]
    type = "COG"
    data_obj = InfoJson(
        author,
        description,
        install_msg,
        short,
        name,
        min_bot_version,
        max_bot_version,
        hidden,
        disabled,
        required_cogs,
        requirements,
        tags,
        type,
        permissions,
        min_python_version,
        end_user_data_statement,
    )
    print(data_obj)
    save_json(f"{ROOT}/{name}/info.json", data_obj.__dict__)


"""
author: List[str]
description: Optional[str] = ""
install_msg: Optional[str] = "Thanks for installing"
short: Optional[str] = ""
name: Optional[str] = ""
min_bot_version: Optional[str] = "3.3.0"
max_bot_version: Optional[str] = "0.0.0"
hidden: Optional[bool] = False
disabled: Optional[bool] = False
required_cogs: Mapping = field(default_factory=dict)
requirements: List[str] = field(default_factory=list)
tags: List[str] = field(default_factory=list)
type: Optional[str] = "COG"
permissions: List[str] = field(default_factory=list)
min_python_version: Optional[List[int]] = field(default_factory=lambda: [3, 8, 0])
end_user_data_statement: str = "This cog does not persistently store data or metadata about users."
"""


@cli.command()
@click.option("--include-hidden", default=False)
@click.option("--include-disabled", default=False)
def countlines(include_hidden: bool = False, include_disabled: bool = False):
    """Count the number of lines of .py files in all folders"""
    total = 0
    totals = []
    log.info(f"{ROOT}")
    for folder in os.listdir(f"{ROOT}/"):
        cog = 0
        if folder.startswith("."):
            continue
        try:
            with open(f"{ROOT}/{folder}/info.json", "r") as infile:
                info = InfoJson.from_json(json.load(infile))
        except Exception:
            continue
        if info.hidden and not include_hidden:
            continue
        if info.disabled and not include_disabled:
            continue
        try:
            for file in glob.glob(f"{ROOT}/{folder}/*.py"):
                try:
                    with open(file, "r") as infile:
                        lines = len(infile.readlines())
                    cog += lines
                    total += lines
                except Exception:
                    pass
            totals.append((folder, cog))
        except Exception:
            pass
    totals = sorted(totals, key=lambda x: x[1], reverse=True)
    totals.insert(0, ("Total", total))
    print(
        tabulate.tabulate(
            totals, headers=["Cog", "# ofLines"], tablefmt="pretty"
        )
    )
    return totals


@cli.command()
@click.option("--include-hidden", default=False)
@click.option("--include-disabled", default=False)
def countchars(include_hidden: bool = False, include_disabled: bool = False):
    """Count the number of lines of .py files in all folders"""
    total = 0
    totals = []
    log.info(f"{ROOT}")
    for folder in os.listdir(f"{ROOT}/"):
        cog = 0
        if folder.startswith("."):
            continue
        try:
            with open(f"{ROOT}/{folder}/info.json", "r") as infile:
                info = InfoJson.from_json(json.load(infile))
        except Exception:
            continue
        if info.hidden and not include_hidden:
            continue
        if info.disabled and not include_disabled:
            continue
        try:
            for file in glob.glob(f"{ROOT}/{folder}/*.py"):
                try:
                    with open(file, "r") as infile:
                        lines = len(infile.read())
                    cog += lines
                    total += lines
                except Exception:
                    pass
            totals.append((folder, cog))
        except Exception:
            pass
    totals = sorted(totals, key=lambda x: x[1], reverse=True)
    totals.insert(0, ("Total", total))
    print(
        tabulate.tabulate(
            totals, headers=["Cog", "# ofchars"], tablefmt="pretty"
        )
    )
    return totals


@cli.command()
def makereadme():
    """Generate README.md from info about all cogs"""
    table_data = []
    for folder in os.listdir(ROOT):
        if folder.startswith(".") or folder.startswith("_"):
            continue
        _version = ""
        info = None
        for file in glob.glob(f"{ROOT}/{folder}/*"):
            if not file.endswith(".py") and not file.endswith("json"):
                continue
            if file.endswith("info.json"):
                try:
                    with open(file) as infile:
                        data = json.loads(infile.read())
                    info = InfoJson.from_json(data)
                except Exception:
                    log.exception(f"Error reading info.json {file}")
            if _version == "":
                with open(file) as infile:
                    data = infile.read()
                    maybe_version = VER_REG.search(data)
                    if maybe_version:
                        _version = maybe_version.group(1)
        if info and not (info.disabled or info.hidden):
            to_append = [info.name, _version]
            description = f"<details><summary>{info.short}</summary>{info.description}</details>"
            to_append.append(description)
            to_append.append(babel_list(info.author, style="standard"))
            table_data.append(to_append)

    body = tabulate.tabulate(
        table_data,
        headers=[
            "Name",
            "Status/Version",
            "Description (Click to see full status)",
            "Authors",
        ],
        tablefmt="github",
    )
    with open(f"{ROOT}/README.md", "w") as outfile:
        outfile.write(HEADER.format(body=body))


@cli.command()
def makerequirements():
    """Generate a requirements.txt for all cogs.
    Useful when setting up the bot in a new venv and requirements are missing.
    """
    requirements = set()
    for folder in os.listdir(ROOT):
        if folder.startswith(".") or folder.startswith("_"):
            continue
        info = None
        for file in glob.glob(f"{ROOT}/{folder}/*"):
            if not file.endswith(".py") and not file.endswith("json"):
                continue
            if file.endswith("info.json"):
                try:
                    with open(file) as infile:
                        data = json.loads(infile.read())
                    info = InfoJson.from_json(data)
                    if info.disabled:
                        continue
                    for req in info.requirements:
                        requirements.add(req)
                except Exception:
                    log.exception(f"Error reading info.json {file}")
    with open(ROOT / "requirements.txt", "w") as outfile:
        outfile.write("\n".join(r for r in requirements))


def run_cli():
    try:
        cli()
    except KeyboardInterrupt:
        print("Exiting.")
    else:
        print("Exiting.")


if __name__ == "__main__":
    run_cli()
