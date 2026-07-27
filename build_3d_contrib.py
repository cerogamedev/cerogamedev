import re, urllib.request, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://github.com/users/cerogamedev/contributions'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')

pattern = re.compile(r'data-date="([^"]+)"[^>]*data-level="(\d+)"')
matches = pattern.findall(html)

grid = []
current_week = []
for date_str, level_str in matches:
    current_week.append(int(level_str))
    if len(current_week) == 7:
        grid.append(current_week)
        current_week = []
if current_week:
    grid.append(current_week)

origin_x = 420
origin_y = 100
dx = 9.5
dy = 5.5

height_map = {0: 4, 1: 16, 2: 28, 3: 44, 4: 60}

colors = {
    0: ('#161b22', '#0d1117', '#11161d'),
    1: ('#00f0ff', '#00b4d8', '#0077b6'),
    2: ('#00ff88', '#00cc66', '#009944'),
    3: ('#9d4edd', '#7b2cbf', '#5a189a'),
    4: ('#ff007f', '#d0006f', '#a00055')
}

polygons_svg = []

for week_idx, week in enumerate(grid):
    for day_idx, lvl in enumerate(week):
        col = week_idx
        row = day_idx
        
        px = origin_x + (col - row) * dx
        py = origin_y + (col + row) * dy
        
        h = height_map.get(lvl, 4)
        top_color, left_color, right_color = colors.get(lvl, colors[0])
        
        p_top = f"{px},{py - h} {px + dx},{py - dy - h} {px + 2*dx},{py - h} {px + dx},{py + dy - h}"
        p_left = f"{px},{py - h} {px + dx},{py + dy - h} {px + dx},{py + dy} {px},{py}"
        p_right = f"{px + dx},{py + dy - h} {px + 2*dx},{py - h} {px + 2*dx},{py} {px + dx},{py + dy}"
        
        polygons_svg.append(f'  <polygon points="{p_left}" fill="{left_color}" stroke="#090d12" stroke-width="0.3"/>')
        polygons_svg.append(f'  <polygon points="{p_right}" fill="{right_color}" stroke="#090d12" stroke-width="0.3"/>')
        polygons_svg.append(f'  <polygon points="{p_top}" fill="{top_color}" stroke="#090d12" stroke-width="0.3"/>')

poly_str = "\n".join(polygons_svg)
count_str = str(len(matches))

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="900" height="420" viewBox="0 0 900 420" fill="none">
  <style>
    .bg { fill: #0d1117; rx: 12px; }
    .title { font-family: 'Fira Code', monospace; font-size: 16px; font-weight: bold; fill: #00f0ff; }
    .sub { font-family: 'Fira Code', monospace; font-size: 12px; fill: #8b949e; }
  </style>

  <rect width="900" height="420" class="bg"/>

  <text x="30" y="40" class="title">🏛️ 3D ISOMETRIC CONTRIBUTION EXTRUSION ENGINE</text>
  <text x="30" y="60" class="sub">cerogamedev // """ + count_str + """ Contributions in last year</text>

  <g transform="translate(0, 40)">
""" + poly_str + """
  </g>
</svg>"""

with open("profile-3d-contrib/profile-night-view.svg", "w") as f:
    f.write(svg_content)

print("Generated profile-3d-contrib/profile-night-view.svg successfully!")
