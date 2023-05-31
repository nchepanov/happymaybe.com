#!/usr/bin/env python3
import argparse
import json
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass
class Episode:
    title: str
    episode_audio_url: str
    subtitle: str
    duration: str
    description: str
    published: datetime


TEMPLATE = """\
---
title: {title}
number: {number}
duration: {duration}
date: {published}
description: {subtitle}
episode_audio_url: {episode_audio_url}
tags: []
---

{description}
"""


def format_datetime(dt: datetime) -> str:
    # Format the datetime object as a string
    return dt.strftime("%Y-%m-%d")


def render_episodes(episodes: List[Episode]) -> None:
    for number, episode in enumerate(episodes):
        with open(f"content/posts/episode-{number + 1:03d}.md", "w") as episode_file:
            episode_file.write(
                TEMPLATE.format(
                    title=json.dumps(episode.title).replace("#", ""),
                    episode_audio_url=episode.episode_audio_url,
                    number=number + 1,
                    duration=episode.duration.strftime("%M min"),
                    published=format_datetime(episode.published),
                    subtitle=json.dumps(episode.subtitle),
                    description=episode.description
                )
            )


# Function to parse the item and return an Episode
def parse_item(item: ET.Element) -> Episode:
    title = item.find("title").text
    subtitle = item.find("{http://www.itunes.com/dtds/podcast-1.0.dtd}subtitle").text
    duration_string = item.find("{http://www.itunes.com/dtds/podcast-1.0.dtd}duration").text
    duration = datetime.strptime(duration_string, "%M:%S")
    description = item.find("description").text
    pub_date = item.find("pubDate").text
    episode_audio_url = item.find("enclosure").attrib["url"]
    
    #published = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z") # the format for wakingup-rss.xml
    published = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M %Z") # the format for happiness-not-guaranteed.xml
    return Episode(
        title=title,
        episode_audio_url=episode_audio_url,
        subtitle=subtitle,
        duration=duration,
        description=description,
        published=published,
    )


def parse_xml(filename: str) -> List[Episode]:
    output: List[Episode] = []
    # Parse the XML
    root = ET.fromstring(open(filename).read())

    # Iterate over items and parse them
    channel = root.find("channel")
    for item in reversed(channel.findall("item")):
        try:
            episode = parse_item(item)
            output.append(episode)
        except Exception as exc:
            print("Failed parsing an item", exc)

    return output


def main():
    parser = argparse.ArgumentParser(description="Process a file.")
    parser.add_argument("file", type=str, help="Path to the file to process")

    args = parser.parse_args()

    episodes: List[Episode] = parse_xml(args.file)
    render_episodes(episodes)


if __name__ == "__main__":
    main()
