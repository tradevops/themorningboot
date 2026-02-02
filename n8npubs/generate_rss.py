import xml.etree.ElementTree as ET
from datetime import datetime
import sys

SOURCE_FILE = "rss.xml"
OUTPUT_FILE = "feed.rss"

def generate_rss():
    try:
        tree = ET.parse(SOURCE_FILE)
        root = tree.getroot()

        # Example: assuming XML structure like:
        # <root>
        #   <item>
        #       <title>Example</title>
        #       <link>https://example.com</link>
        #       <description>Some text</description>
        #   </item>
        # </root>

        items_xml = ""
        for item in root.findall("item"):
            title = item.findtext("title", default="No title")
            link = item.findtext("link", default="")
            description = item.findtext("description", default="")

            items_xml += f"""
            <item>
                <title>{title}</title>
                <link>{link}</link>
                <description>{description}</description>
                <pubDate>{datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}</pubDate>
            </item>
            """

        rss_feed = f"""<?xml version="1.0" encoding="UTF-8"?>
        <rss version="2.0">
            <channel>
                <title>My RSS Feed</title>
                <link>https://example.com</link>
                <description>Generated from XML</description>
                <lastBuildDate>{datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}</lastBuildDate>
                {items_xml}
            </channel>
        </rss>
        """

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(rss_feed.strip())

        print(f"✅ RSS feed generated: {OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"❌ Source file '{SOURCE_FILE}' not found.")
        sys.exit(1)
    except ET.ParseError as e:
        print(f"❌ XML parsing error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    generate_rss()
