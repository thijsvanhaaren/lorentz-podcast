"""Genereert feed.xml uit episodes.json + episodes/*.mp3. Gebruik: python3 build_feed.py <BASE_URL>"""
import json, os, sys, subprocess
from email.utils import format_datetime
from datetime import datetime
from xml.sax.saxutils import escape
base = sys.argv[1].rstrip('/')
eps = json.load(open('episodes.json'))
items = []
for e in sorted(eps, key=lambda e: e['date'], reverse=True):
    f = f"episodes/{e['id']}.mp3"
    size = os.path.getsize(f)
    dur = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).decode())
    d = format_datetime(datetime.fromisoformat(e['date']))
    items.append(f"""  <item>
    <title>{escape(e['title'])}</title>
    <description>{escape(e['summary'])}</description>
    <guid isPermaLink="false">lorentz-{e['id']}</guid>
    <pubDate>{d}</pubDate>
    <enclosure url="{base}/{f}" length="{size}" type="audio/mpeg"/>
    <itunes:duration>{int(dur)}</itunes:duration>
  </item>""")
feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
<channel>
  <title>Lorentz Lyceum Nieuwsupdate</title>
  <link>{base}/</link>
  <language>nl</language>
  <description>Wekelijkse nieuwsupdate van het Lorentz Lyceum, voorgelezen. Privéfeed.</description>
  <itunes:author>Lorentz Lyceum (voorgelezen)</itunes:author>
  <itunes:image href="{base}/cover.png"/>
  <itunes:block>Yes</itunes:block>
  <itunes:explicit>false</itunes:explicit>
{chr(10).join(items)}
</channel>
</rss>
"""
open('feed.xml','w').write(feed)
print('feed.xml:', len(items), 'afleveringen')
