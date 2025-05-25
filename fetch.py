#!/usr/bin/env python3

from requests_html import HTMLSession
import os
from tqdm.auto import tqdm

s = HTMLSession()
BASE_URL = "https://merge-mansion.fandom.com/"
areas = s.get(f"{BASE_URL}/wiki/Areas")
areas = areas.html.find("table", first=True).find("tr>td:nth-child(3)>a")[1:]
for area in tqdm(areas):
    svgs = s.get(BASE_URL + area.attrs['href']).html.find("a[href$=svg]")
    for svg in svgs:
        svg_link = BASE_URL + svg.attrs["href"]
        with open(os.path.basename(svg_link), "wb") as f:
            f.write(s.get(svg_link).content)