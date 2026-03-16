
html = open(r'C:\Users\kcraw\camelback-golf\index.html', 'w', encoding='utf-8')

html.write("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Camelback Golf \u2014 Ambiente Course Guide</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
  :root {
    --green-dark:#0f2218; --green-mid:#1a3a28; --green-light:#2d5a3d;
    --green-fairway:#3d7a52; --green-putting:#5fb86a;
    --water:#1e6fa8; --water-light:#3a8fc4;
    --sand:#d4b483; --orange:#f4793b; --gold:#d4a843;
    --white:#f0f4f0; --gray:#8a9e8e; --card-bg:#162d20; --border:#2a4835;
  }
  *{margin:0;padding:0;box-sizing:border-box;}
  body{font-family:'Inter',sans-serif;background:var(--green-dark);color:var(--white);min-height:100vh;overflow-x:hidden;}
  #landing{display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;padding:2rem;text-align:center;}
  .logo-icon{font-size:4rem;}
  .logo-title{font-size:2.4rem;font-weight:800;letter-spacing:-0.5px;background:linear-gradient(135deg,#5fb86a,#d4a843);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
  .logo-sub{color:var(--gray);font-size:1rem;margin-top:.4rem;letter-spacing:1px;text-transform:uppercase;}
  .course-badge{background:var(--card-bg);border:1px solid var(--border);border-radius:16px;padding:1.5rem 2.5rem;margin:1.5rem 0;}
  .course-badge h2{font-size:1.5rem;font-weight:700;color:var(--gold);}
  .course-badge p{color:var(--gray);margin-top:.3rem;}
  .badge-row{display:flex;gap:2rem;justify-content:center;margin-top:1rem;}
  .badge-item .val{font-size:1.4rem;font-weight:700;}
  .badge-item .lbl{font-size:.75rem;color:var(--gray);text-transform:uppercase;letter-spacing:1px;}
  .handicap-box{background:var(--card-bg);border:1px solid var(--border);border-radius:16px;padding:1.25rem 1.5rem;margin:.75rem 0;max-width:480px;width:100%;}
  .handicap-box h3{font-size:.8rem;color:var(--gray);text-transform:uppercase;letter-spacing:1px;margin-bottom:.8rem;}
  .dist-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:.4rem;}
  .dist-item{background:#1f3d2b;border-radius:8px;padding:.45rem;text-align:center;}
  .dist-item .club{font-size:.68rem;color:var(--gray);}
  .dist-item .yds{font-size:.9rem;font-weight:600;}
  .start-section{margin-top:1.5rem;width:100%;max-width:360px;}
  .start-section label{display:block;font-size:.8rem;color:var(--gray);margin-bottom:.5rem;text-transform:uppercase;letter-spacing:1px;}
  .hole-input-row{display:flex;gap:.75rem;}
  .hole-input{flex:1;background:#1f3d2b;border:2px solid var(--border);border-radius:12px;padding:.85rem 1rem;font-size:1.5rem;font-weight:700;color:var(--white);text-align:center;outline:none;transition:.2s;}
  .hole-input:focus{border-color:var(--green-putting);}
  .start-btn{background:linear-gradient(135deg,#3d9e56,#2d7a42);border:none;border-radius:12px;padding:.85rem 1.5rem;color:white;font-size:1rem;font-weight:700;cursor:pointer;transition:.2s;}
  .start-btn:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(61,158,86,.4);}
  .quick-holes{display:flex;flex-wrap:wrap;gap:.4rem;margin-top:.75rem;justify-content:center;}
  .quick-btn{background:var(--card-bg);border:1px solid var(--border);border-radius:8px;padding:.35rem .7rem;color:var(--gray);font-size:.82rem;cursor:pointer;transition:.2s;}
  .quick-btn:hover{border-color:var(--green-putting);color:var(--white);}
  #holeView{display:none;min-height:100vh;}
  .hole-header{background:var(--green-mid);border-bottom:1px solid var(--border);padding:.9rem 1.5rem;display:flex;align-items:center;gap:1rem;position:sticky;top:0;z-index:10;flex-wrap:wrap;}
  .back-btn{background:transparent;border:1px solid var(--border);border-radius:8px;padding:.35rem .75rem;color:var(--gray);cursor:pointer;font-size:.82rem;transition:.2s;}
  .back-btn:hover{border-color:var(--green-putting);color:var(--white);}
  .hole-meta{flex:1;display:flex;align-items:center;gap:.75rem;}
  .hole-num-badge{background:var(--green-light);border-radius:10px;padding:.3rem .75rem;font-size:.95rem;font-weight:800;color:var(--gold);}
  .hole-title{font-size:1.05rem;font-weight:700;}
  .hole-par-yds{font-size:.78rem;color:var(--gray);}
  .nav-btns{display:flex;gap:.5rem;}
  .nav-btn{background:var(--green-light);border:none;border-radius:8px;padding:.4rem .9rem;color:var(--white);cursor:pointer;font-size:.82rem;font-weight:600;transition:.2s;}
  .nav-btn:hover{background:var(--green-fairway);}
  .nav-btn:disabled{opacity:.3;cursor:not-allowed;}
  .hole-content{display:grid;grid-template-columns:320px 1fr;gap:0;min-height:calc(100vh - 60px);}
  .svg-panel{background:#0d1f16;border-right:1px solid var(--border);padding:1rem;display:flex;flex-direction:column;align-items:center;gap:.75rem;}
  .svg-panel svg{width:100%;max-width:300px;border-radius:12px;}
  .svg-legend{display:flex;flex-wrap:wrap;gap:.5rem .9rem;justify-content:center;}
  .legend-item{display:flex;align-items:center;gap:.3rem;font-size:.72rem;color:var(--gray);}
  .legend-rect{width:14px;height:10px;border-radius:2px;}
  .legend-dot{width:11px;height:11px;border-radius:50%;}
  .info-panel{padding:1.25rem;display:flex;flex-direction:column;gap:1rem;overflow-y:auto;}
  .hole-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:.6rem;}
  .stat-card{background:var(--card-bg);border:1px solid var(--border);border-radius:12px;padding:.75rem;text-align:center;}
  .stat-card.par{border-color:#3d9e56;}
  .stat-card.diff{border-color:#d4a843;}
  .s-val{font-size:1.35rem;font-weight:800;}
  .s-lbl{font-size:.68rem;color:var(--gray);text-transform:uppercase;letter-spacing:.8px;margin-top:.15rem;}
  .diff-bar-bg{background:#1f3d2b;border-radius:4px;height:4px;margin-top:.4rem;}
  .diff-bar-fill{background:linear-gradient(90deg,#5fb86a,#d4a843,#e05555);border-radius:4px;height:4px;transition:.4s;}
  .section-card{background:var(--card-bg);border:1px solid var(--border);border-radius:16px;padding:1.1rem;}
  .section-title{font-size:.72rem;color:var(--gray);text-transform:uppercase;letter-spacing:1.2px;font-weight:600;margin-bottom:.75rem;}
  .shot-list{display:flex;flex-direction:column;gap:.55rem;}
  .shot-row{display:grid;grid-template-columns:28px 90px 65px 1fr;gap:.5rem;align-items:start;padding:.5rem;background:#1a3324;border-radius:8px;}
  .shot-num{background:var(--orange);border-radius:6px;width:24px;height:24px;display:flex;align-items:center;justify-content:center;font-size:.78rem;font-weight:800;flex-shrink:0;}
  .shot-club{font-size:.82rem;font-weight:600;}
  .shot-dist{font-size:.82rem;color:var(--gold);font-weight:700;}
  .shot-note{font-size:.76rem;color:#9ab8a4;line-height:1.4;}
  .strategy-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:.6rem;}
  .strat-card{background:#1a3324;border-radius:10px;padding:.75rem;}
  .strat-header{font-size:.76rem;font-weight:700;margin-bottom:.5rem;}
  .strat-card.attack .strat-header{color:#5fb86a;}
  .strat-card.avoid .strat-header{color:#e05555;}
  .strat-card.mustdo .strat-header{color:#5588e0;}
  .strat-list{list-style:none;display:flex;flex-direction:column;gap:.35rem;}
  .strat-list li{font-size:.8rem;line-height:1.5;padding-left:1rem;position:relative;}
  .strat-list li::before{content:'\\203a ';position:absolute;left:0;}
  .strat-card.attack .strat-list li{color:#a0d4a8;}
  .strat-card.avoid .strat-list li{color:#d4a0a0;}
  .strat-card.mustdo .strat-list li{color:#a0b4d4;}
  .hole-notes{background:var(--card-bg);border:1px solid var(--border);border-radius:16px;padding:1.1rem;}
  .hole-notes p{font-size:.86rem;color:#b0c8b8;line-height:1.75;}
  .hole-notes strong{color:var(--white);}

  /* ── TABLET ── */
  @media(max-width:900px){
    .strategy-grid{grid-template-columns:1fr;}
    .hole-content{grid-template-columns:280px 1fr;}
  }

  /* ── MOBILE ── */
  @media(max-width:700px){
    /* Landing */
    .logo-title{font-size:1.9rem;}
    .logo-icon{font-size:3rem;}
    .course-badge{padding:1rem 1.1rem;margin:1rem 0;}
    .course-badge h2{font-size:1.2rem;}
    .badge-row{gap:.75rem 1.25rem;flex-wrap:wrap;}
    .badge-item .val{font-size:1.1rem;}
    .handicap-box{padding:1rem;}
    .dist-grid{grid-template-columns:repeat(3,1fr);}
    .start-section{max-width:100%;}
    .quick-btn{padding:.5rem .85rem;font-size:.85rem;}

    /* Hole header */
    .hole-header{padding:.6rem .85rem;gap:.5rem;}
    .hole-num-badge{font-size:.85rem;padding:.25rem .6rem;}
    .hole-title{font-size:.9rem;}
    .hole-par-yds{font-size:.72rem;}
    .nav-btn{padding:.5rem 1rem;font-size:.82rem;min-width:64px;}
    .back-btn{padding:.45rem .75rem;}

    /* Hole layout: stack SVG on top, info below */
    .hole-content{grid-template-columns:1fr;}
    .svg-panel{border-right:none;border-bottom:1px solid var(--border);padding:.75rem;}
    .svg-panel svg{max-width:100%;height:auto;}
    .info-panel{padding:.85rem;gap:.85rem;}

    /* Stats row: 2 cols on mobile */
    .hole-stats{grid-template-columns:repeat(2,1fr);gap:.5rem;}
    .s-val{font-size:1.2rem;}

    /* Shot rows: reorganise to 2-row layout */
    .shot-row{
      grid-template-columns:28px 1fr auto;
      grid-template-rows:auto auto;
      column-gap:.45rem;
      row-gap:.2rem;
    }
    .shot-num{grid-row:1;grid-column:1;align-self:center;}
    .shot-club{grid-row:1;grid-column:2;font-size:.86rem;}
    .shot-dist{grid-row:1;grid-column:3;font-size:.86rem;white-space:nowrap;}
    .shot-note{grid-row:2;grid-column:2 / -1;font-size:.78rem;line-height:1.45;}

    /* Strategy: single column already via 900px rule */
    .strat-list li{font-size:.82rem;}
    .hole-notes p{font-size:.84rem;line-height:1.7;}
  }
</style>
</head>
<body>
<div id="landing">
  <div class="logo-icon">&#x26F3;</div>
  <div class="logo-title">Camelback Golf Guide</div>
  <div class="logo-sub">Ambiente Course &middot; Tan Tees &middot; 9 Handicap</div>
  <div class="course-badge">
    <h2>Ambiente Course &mdash; Tan Tees</h2>
    <p>Paradise Valley, AZ &middot; Hurdzan-Fry / Jason Straka Design &middot; Par 72</p>
    <div class="badge-row">
      <div class="badge-item"><div class="val">6,123</div><div class="lbl">Total Yards</div></div>
      <div class="badge-item"><div class="val">70.0</div><div class="lbl">Rating</div></div>
      <div class="badge-item"><div class="val">126</div><div class="lbl">Slope</div></div>
      <div class="badge-item"><div class="val">Par 72</div><div class="lbl">Par</div></div>
    </div>
  </div>
  <div class="handicap-box">
    <h3>Your Distances</h3>
    <div class="dist-grid">
      <div class="dist-item"><div class="club">Driver</div><div class="yds">250y</div></div>
      <div class="dist-item"><div class="club">3 Hybrid</div><div class="yds">220y</div></div>
      <div class="dist-item"><div class="club">5 Iron</div><div class="yds">180y</div></div>
      <div class="dist-item"><div class="club">6 Iron</div><div class="yds">170y</div></div>
      <div class="dist-item"><div class="club">7 Iron</div><div class="yds">160y</div></div>
      <div class="dist-item"><div class="club">8 Iron</div><div class="yds">150y</div></div>
      <div class="dist-item"><div class="club">9 Iron</div><div class="yds">140y</div></div>
      <div class="dist-item"><div class="club">PW</div><div class="yds">130y</div></div>
      <div class="dist-item"><div class="club">48&deg;</div><div class="yds">115y</div></div>
      <div class="dist-item"><div class="club">52&deg;</div><div class="yds">100y</div></div>
      <div class="dist-item"><div class="club">56&deg;</div><div class="yds">75y</div></div>
    </div>
  </div>
  <div class="start-section">
    <label>Start Round on Hole #</label>
    <div class="hole-input-row">
      <input class="hole-input" id="holeNumInput" type="number" min="1" max="18" value="1"/>
      <button class="start-btn" onclick="startHole()">&#x25B6; Start</button>
    </div>
    <div style="margin-top:.65rem;color:var(--gray);font-size:.78rem;">&mdash; or jump directly to a hole &mdash;</div>
    <div class="quick-holes" id="quickHoles"></div>
  </div>
</div>

<div id="holeView">
  <div class="hole-header">
    <button class="back-btn" onclick="showLanding()">&larr; Menu</button>
    <div class="hole-meta">
      <div class="hole-num-badge" id="hdrBadge">Hole 1</div>
      <div>
        <div class="hole-title" id="hdrTitle">Par 4 &mdash; 393 yards</div>
        <div class="hole-par-yds" id="hdrSub">Handicap 5</div>
      </div>
    </div>
    <div class="nav-btns">
      <button class="nav-btn" id="prevBtn" onclick="navigateHole(-1)">&#x25C4; Prev</button>
      <button class="nav-btn" id="nextBtn" onclick="navigateHole(1)">Next &#x25BA;</button>
    </div>
  </div>
  <div class="hole-content">
    <div class="svg-panel">
      <div id="holeSvg"></div>
      <div class="svg-legend">
        <div class="legend-item"><div class="legend-rect" style="background:#5fb86a"></div>Green</div>
        <div class="legend-item"><div class="legend-rect" style="background:#3d7a52"></div>Fairway</div>
        <div class="legend-item"><div class="legend-rect" style="background:#1e6fa8"></div>Water</div>
        <div class="legend-item"><div class="legend-rect" style="background:#d4b483"></div>Bunker</div>
        <div class="legend-item"><div class="legend-dot" style="background:#f4793b"></div>Landing Zone</div>
      </div>
    </div>
    <div class="info-panel">
      <div class="hole-stats">
        <div class="stat-card par"><div class="s-val" id="statPar">4</div><div class="s-lbl">Par</div></div>
        <div class="stat-card"><div class="s-val" id="statYards">393</div><div class="s-lbl">Yards</div></div>
        <div class="stat-card diff">
          <div class="s-val" id="statHcp">#5</div><div class="s-lbl">Difficulty</div>
          <div class="diff-bar-bg"><div class="diff-bar-fill" id="diffBar" style="width:60%"></div></div>
        </div>
        <div class="stat-card"><div class="s-val" id="statShots">2</div><div class="s-lbl">Planned Shots</div></div>
      </div>
      <div class="section-card">
        <div class="section-title">Shot Plan</div>
        <div class="shot-list" id="shotList"></div>
      </div>
      <div class="section-card">
        <div class="section-title">Strategy</div>
        <div class="strategy-grid">
          <div class="strat-card attack"><div class="strat-header">&#x2705; Plan of Attack</div><ul class="strat-list" id="stratAttack"></ul></div>
          <div class="strat-card avoid"><div class="strat-header">&#x26D4; Do NOT</div><ul class="strat-list" id="stratAvoid"></ul></div>
          <div class="strat-card mustdo"><div class="strat-header">&#x2B50; Must Do</div><ul class="strat-list" id="stratMustDo"></ul></div>
        </div>
      </div>
      <div class="hole-notes">
        <div class="section-title">Caddie Notes</div>
        <p id="holeNotes"></p>
      </div>
    </div>
  </div>
</div>
""")

html.write("""<script>
const W=320,H=500,cx=W/2;
const mkSvg=c=>`<svg viewBox="0 0 ${W} ${H}" xmlns="http://www.w3.org/2000/svg"><rect width="${W}" height="${H}" fill="#1a3320"/>${c}</svg>`;
const teeBox=(x,y)=>`<rect x="${x-14}" y="${y-8}" width="28" height="18" rx="4" fill="#8B6914" stroke="#d4a843" stroke-width="1.5"/><text x="${x}" y="${y+6}" text-anchor="middle" fill="#d4a843" font-size="9" font-weight="700">TEE</text>`;
const greenEl=(x,y,rx,ry)=>`<ellipse cx="${x}" cy="${y}" rx="${rx}" ry="${ry}" fill="#5fb86a" stroke="#7ed88a" stroke-width="1.5"/><text x="${x}" y="${y+4}" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">GREEN</text>`;
const bunker=(x,y,rx,ry)=>`<ellipse cx="${x}" cy="${y}" rx="${rx}" ry="${ry}" fill="#d4b483" stroke="#b89a60" stroke-width="1" opacity="0.9"/>`;
const waterRect=(x,y,w,h)=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="#1e6fa8" stroke="#3a8fc4" stroke-width="1" opacity="0.85"/>`;
const shotMark=(x,y,n,col)=>`<circle cx="${x}" cy="${y}" r="13" fill="${col||'#f4793b'}" stroke="white" stroke-width="1.5" opacity="0.95"/><text x="${x}" y="${y+4.5}" text-anchor="middle" fill="white" font-size="10" font-weight="800">${n}</text>`;
const dash=(x1,y1,x2,y2)=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="white" stroke-width="1.5" stroke-dasharray="6,4" opacity="0.55"/>`;
const fw=(x,y,w,h,r)=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${r||6}" fill="#3d7a52" opacity="0.9"/>`;
const yLbl=(x,y,t)=>`<text x="${x}" y="${y}" text-anchor="middle" fill="#d4a843" font-size="8" font-weight="600">${t}</text>`;
const flag=(x,y)=>`<line x1="${x}" y1="${y-24}" x2="${x}" y2="${y+8}" stroke="white" stroke-width="1.5"/><polygon points="${x},${y-24} ${x+13},${y-17} ${x},${y-10}" fill="#ff3333"/>`;
const wLabel=(x,y,t)=>`<text x="${x}" y="${y}" text-anchor="middle" fill="#7bc4e8" font-size="9" font-weight="600" opacity="0.9">${t||'WATER'}</text>`;

function buildSvg(hole){
  const s=hole.shape,hz=hole.hazards||[],sh=hole.shots;
  let p=[];

  if(s==='straight'){
    p.push(fw(cx-38,78,76,360,8));
    p.push(greenEl(cx,66,42,24)); p.push(flag(cx+12,66));
    if(hz.includes('bunkerLeft'))       p.push(bunker(cx-58,285,15,10));
    if(hz.includes('bunkerRight'))      p.push(bunker(cx+58,285,15,10));
    if(hz.includes('bunkerCenter'))     p.push(bunker(cx,275,18,11));
    if(hz.includes('bunkerLeft2'))      p.push(bunker(cx-58,215,14,9));
    if(hz.includes('bunkerRight2'))     p.push(bunker(cx+58,215,14,9));
    if(hz.includes('bunkerFront'))      p.push(bunker(cx,100,22,10));
    if(hz.includes('bunkerFrontRight')) p.push(bunker(cx+36,98,14,8));
    if(hz.includes('bunkerFrontLeft'))  p.push(bunker(cx-36,98,14,8));
    if(hz.includes('bunkerGreenLeft'))  p.push(bunker(cx-52,72,14,8));
    if(hz.includes('bunkerGreenRight')) p.push(bunker(cx+52,72,14,8));
    if(hz.includes('angledBunkerRight')) p.push(`<rect x="${cx+32}" y="205" width="16" height="75" rx="6" fill="#d4b483" stroke="#b89a60" stroke-width="1" opacity="0.9" transform="rotate(-14,${cx+40},242)"/>`);
    p.push(teeBox(cx,450));
    if(sh.length===2){
      p.push(dash(cx,442,cx,295)); p.push(shotMark(cx,295,1));
      p.push(yLbl(cx+22,310,sh[0].dist+'y'));
      p.push(dash(cx,283,cx,88)); p.push(shotMark(cx,88,2));
      p.push(yLbl(cx+22,103,sh[1].dist+'y'));
    } else if(sh.length===3){
      p.push(dash(cx,442,cx,340)); p.push(shotMark(cx,340,1));
      p.push(yLbl(cx+22,355,sh[0].dist+'y'));
      p.push(dash(cx,328,cx,210)); p.push(shotMark(cx,210,2));
      p.push(yLbl(cx+22,225,sh[1].dist+'y'));
      p.push(dash(cx,198,cx,88)); p.push(shotMark(cx,88,3));
      p.push(yLbl(cx+22,103,sh[2].dist+'y'));
    }
  }

  else if(s==='par3straight'){
    p.push(fw(cx-34,98,68,305,8));
    p.push(greenEl(cx,82,46,26)); p.push(flag(cx+12,82));
    if(hz.includes('bunkerLeft'))  p.push(bunker(cx-60,90,15,10));
    if(hz.includes('bunkerRight')) p.push(bunker(cx+60,90,15,10));
    if(hz.includes('bunkerFront')) p.push(bunker(cx,115,22,10));
    p.push(teeBox(cx,418));
    p.push(dash(cx,410,cx,110)); p.push(shotMark(cx,106,1,'#3d9e56'));
    p.push(yLbl(cx+22,118,sh[0].dist+'y'));
  }

  else if(s==='doglegLeft'){
    p.push(`<path d="M ${cx-38} 458 L ${cx-38} 222 L 58 175 L 58 88 L 114 88 L 114 175 L ${cx+38} 222 L ${cx+38} 458 Z" fill="#3d7a52" opacity="0.9"/>`);
    p.push(greenEl(86,74,38,22)); p.push(flag(98,74));
    if(hz.includes('bunkerCornerLeft'))    p.push(bunker(cx-45,210,18,12));
    if(hz.includes('bunkerCornerOutside')) p.push(bunker(cx+52,225,15,10));
    if(hz.includes('bunkerFairwayLeft'))   p.push(bunker(cx-58,340,15,10));
    if(hz.includes('bunkerGreenLeft'))     p.push(bunker(55,80,13,8));
    if(hz.includes('bunkerGreenRight'))    p.push(bunker(117,80,13,8));
    if(hz.includes('bunkerRight'))         p.push(bunker(cx+55,360,15,10));
    p.push(teeBox(cx,466));
    if(sh.length===2){
      p.push(dash(cx,458,cx-10,265)); p.push(shotMark(cx-10,265,1));
      p.push(yLbl(cx+14,278,sh[0].dist+'y'));
      p.push(dash(cx-10,253,86,96)); p.push(shotMark(86,96,2));
      p.push(yLbl(60,108,sh[1].dist+'y'));
    } else if(sh.length===3){
      p.push(dash(cx,458,cx-5,320)); p.push(shotMark(cx-5,320,1));
      p.push(yLbl(cx+18,334,sh[0].dist+'y'));
      p.push(dash(cx-5,308,cx-14,210)); p.push(shotMark(cx-14,210,2));
      p.push(yLbl(cx+10,224,sh[1].dist+'y'));
      p.push(dash(cx-14,198,86,96)); p.push(shotMark(86,96,3));
      p.push(yLbl(60,108,sh[2].dist+'y'));
    }
  }

  else if(s==='doglegRight'){
    p.push(`<path d="M ${cx-38} 458 L ${cx-38} 222 L ${W-114} 175 L ${W-114} 88 L ${W-58} 88 L ${W-58} 175 L ${cx+38} 222 L ${cx+38} 458 Z" fill="#3d7a52" opacity="0.9"/>`);
    p.push(greenEl(234,74,38,22)); p.push(flag(246,74));
    if(hz.includes('bunkerCornerRight'))   p.push(bunker(cx+45,210,18,12));
    if(hz.includes('bunkerCornerOutside')) p.push(bunker(cx-52,225,15,10));
    if(hz.includes('bunkerGreenLeft'))     p.push(bunker(203,80,13,8));
    if(hz.includes('bunkerGreenRight'))    p.push(bunker(265,80,13,8));
    if(hz.includes('bunkerLeft'))          p.push(bunker(cx-55,350,15,10));
    p.push(teeBox(cx,466));
    if(sh.length===2){
      p.push(dash(cx,458,cx+10,265)); p.push(shotMark(cx+10,265,1));
      p.push(yLbl(cx+34,278,sh[0].dist+'y'));
      p.push(dash(cx+10,253,234,96)); p.push(shotMark(234,96,2));
      p.push(yLbl(258,108,sh[1].dist+'y'));
    } else if(sh.length===3){
      p.push(dash(cx,458,cx+5,320)); p.push(shotMark(cx+5,320,1));
      p.push(yLbl(cx+28,334,sh[0].dist+'y'));
      p.push(dash(cx+5,308,cx+14,210)); p.push(shotMark(cx+14,210,2));
      p.push(yLbl(cx+38,224,sh[1].dist+'y'));
      p.push(dash(cx+14,198,234,96)); p.push(shotMark(234,96,3));
      p.push(yLbl(260,108,sh[2].dist+'y'));
    }
  }

  else if(s==='par4WaterRight'){
    p.push(waterRect(cx+22,48,W-cx-18,418));
    p.push(wLabel(W-55,285));
    p.push(`<rect x="20" y="82" width="110" height="375" rx="6" fill="#3d7a52" opacity="0.9"/>`);
    p.push(greenEl(88,70,40,24)); p.push(flag(100,70));
    if(hz.includes('bunkerGreenLeft'))  p.push(bunker(46,72,14,9));
    if(hz.includes('bunkerGreenBack'))  p.push(bunker(88,50,22,9));
    if(hz.includes('bunkerGreenRight')) p.push(bunker(130,72,13,8));
    p.push(teeBox(cx,462));
    p.push(dash(cx,454,72,295)); p.push(shotMark(72,295,1));
    p.push(yLbl(44,308,sh[0].dist+'y'));
    p.push(dash(72,283,88,94)); p.push(shotMark(88,94,2));
    p.push(yLbl(56,106,sh[1].dist+'y'));
  }

  else if(s==='par4WashCarry'){
    p.push(`<path d="M 55 268 L 55 88 L 175 88 L 175 175 L ${cx+38} 200 L ${cx+38} 268 Z" fill="#3d7a52" opacity="0.9"/>`);
    p.push(waterRect(30,268,260,42));
    p.push(wLabel(cx,296,'WASH \u2014 MUST CARRY'));
    p.push(fw(cx-38,315,76,145,6));
    p.push(greenEl(115,73,42,23)); p.push(flag(127,73));
    if(hz.includes('bunkerLeft'))  p.push(bunker(52,178,14,9));
    if(hz.includes('bunkerRight')) p.push(bunker(cx+52,190,14,9));
    p.push(teeBox(cx,464));
    p.push(dash(cx,456,cx,330)); p.push(shotMark(cx,330,1));
    p.push(yLbl(cx+22,344,sh[0].dist+'y'));
    p.push(`<text x="${cx}" y="258" text-anchor="middle" fill="#7bc4e8" font-size="8" font-weight="700">CARRY</text>`);
    p.push(dash(cx,315,115,96)); p.push(shotMark(115,96,2));
    p.push(yLbl(140,108,sh[1].dist+'y'));
  }

  else if(s==='par5DoglegLeft'){
    p.push(`<path d="M ${cx-40} 480 L ${cx-40} 228 L 55 180 L 55 86 L 115 86 L 115 180 L ${cx+40} 228 L ${cx+40} 480 Z" fill="#3d7a52" opacity="0.9"/>`);
    p.push(greenEl(85,72,40,24)); p.push(flag(97,72));
    if(hz.includes('bunkerCornerLeft'))    p.push(bunker(cx-48,215,18,12));
    if(hz.includes('bunkerCornerOutside')) p.push(bunker(cx+54,225,15,10));
    if(hz.includes('bunkerFairwayLeft'))   p.push(bunker(cx-58,375,15,10));
    if(hz.includes('bunkerFairwayLeft2'))  p.push(bunker(88,220,14,9));
    if(hz.includes('bunkerGreenLeft'))     p.push(bunker(52,76,13,8));
    if(hz.includes('bunkerGreenRight'))    p.push(bunker(118,76,13,8));
    p.push(teeBox(cx,488));
    if(sh.length===2){
      p.push(dash(cx,480,cx-10,295)); p.push(shotMark(cx-10,295,1));
      p.push(yLbl(cx+18,310,sh[0].dist+'y'));
      p.push(dash(cx-10,283,85,95)); p.push(shotMark(85,95,2));
      p.push(yLbl(58,107,sh[1].dist+'y'));
    } else {
      p.push(dash(cx,480,cx-6,355)); p.push(shotMark(cx-6,355,1));
      p.push(yLbl(cx+18,368,sh[0].dist+'y'));
      p.push(dash(cx-6,343,cx-16,212)); p.push(shotMark(cx-16,212,2));
      p.push(yLbl(cx+8,226,sh[1].dist+'y'));
      p.push(dash(cx-16,200,85,95)); p.push(shotMark(85,95,3));
      p.push(yLbl(58,107,sh[2].dist+'y'));
    }
  }

  else if(s==='par3Long'){
    p.push(fw(cx-36,96,72,320,8));
    p.push(greenEl(cx,80,46,28)); p.push(flag(cx+14,80));
    p.push(bunker(cx-64,86,18,11));
    if(hz.includes('bunkerRight')) p.push(bunker(cx+64,90,14,9));
    p.push(teeBox(cx,428));
    p.push(dash(cx,420,cx,110)); p.push(shotMark(cx,106,1,'#3d9e56'));
    p.push(yLbl(cx+22,120,sh[0].dist+'y'));
  }

  else if(s==='par4LongWaterRight'){
    p.push(waterRect(cx+26,48,W-cx-16,290));
    p.push(wLabel(W-54,205));
    p.push(`<path d="M ${cx-42} 460 L ${cx-42} 88 L ${cx+28} 88 L ${cx+26} 460 Z" fill="#3d7a52" opacity="0.9"/>`);
    p.push(bunker(cx,318,20,12));
    p.push(`<text x="${cx+28}" y="328" fill="#d4b483" font-size="8" opacity="0.9">BUNKER</text>`);
    p.push(greenEl(cx-4,74,38,22)); p.push(flag(cx+8,74));
    if(hz.includes('bunkerGreenLeft'))  p.push(bunker(cx-50,76,13,8));
    if(hz.includes('bunkerGreenRight')) p.push(bunker(cx+36,76,13,8));
    p.push(`<text x="${cx-52}" y="400" text-anchor="middle" fill="#e0c060" font-size="8" font-weight="700">GO LEFT</text>`);
    p.push(teeBox(cx-6,466));
    if(sh.length===2){
      p.push(dash(cx-6,458,cx-10,345)); p.push(shotMark(cx-10,345,1));
      p.push(yLbl(cx-38,358,sh[0].dist+'y'));
      p.push(dash(cx-10,333,cx-4,96)); p.push(shotMark(cx-4,96,2));
      p.push(yLbl(cx-32,108,sh[1].dist+'y'));
    } else {
      p.push(dash(cx-6,458,cx-10,345)); p.push(shotMark(cx-10,345,1));
      p.push(yLbl(cx-38,358,sh[0].dist+'y'));
      p.push(dash(cx-10,333,cx-14,215)); p.push(shotMark(cx-14,215,2));
      p.push(yLbl(cx-42,228,sh[1].dist+'y'));
      p.push(dash(cx-14,203,cx-4,96)); p.push(shotMark(cx-4,96,3));
      p.push(yLbl(cx-32,108,sh[2].dist+'y'));
    }
  }

  else if(s==='par5Straight'){
    p.push(fw(cx-44,76,88,388,8));
    p.push(greenEl(cx,64,46,26)); p.push(flag(cx+14,64));
    if(hz.includes('bunkerLeft'))  p.push(bunker(cx-62,330,16,11));
    if(hz.includes('bunkerLeft2')) p.push(bunker(cx-62,248,15,10));
    if(hz.includes('bunkerRight')) p.push(bunker(cx+62,295,15,10));
    if(hz.includes('bunkerRight2'))p.push(bunker(cx+62,215,14,9));
    if(hz.includes('bunkerFront')) p.push(bunker(cx,98,22,10));
    p.push(teeBox(cx,468));
    p.push(dash(cx,460,cx,360)); p.push(shotMark(cx,360,1));
    p.push(yLbl(cx+22,374,sh[0].dist+'y'));
    p.push(dash(cx,348,cx,225)); p.push(shotMark(cx,225,2));
    p.push(yLbl(cx+22,240,sh[1].dist+'y'));
    p.push(dash(cx,213,cx,86)); p.push(shotMark(cx,86,3));
    p.push(yLbl(cx+22,100,sh[2].dist+'y'));
  }

  else if(s==='par5DoglegRight'){
    p.push(`<path d="M ${cx-40} 480 L ${cx-40} 228 L ${W-115} 180 L ${W-115} 86 L ${W-58} 86 L ${W-58} 180 L ${cx+40} 228 L ${cx+40} 480 Z" fill="#3d7a52" opacity="0.9"/>`);
    p.push(greenEl(234,72,36,22)); p.push(flag(246,72));
    if(hz.includes('bunkerFairwayLeft'))  p.push(bunker(cx-54,360,15,10));
    if(hz.includes('bunkerFairwayRight')) p.push(bunker(cx+54,295,15,10));
    if(hz.includes('bunkerFairwayMid'))   p.push(bunker(cx+22,215,15,10));
    if(hz.includes('bunkerGreenLeft'))    p.push(bunker(203,78,13,8));
    if(hz.includes('bunkerGreenRight'))   p.push(bunker(265,78,13,8));
    p.push(teeBox(cx,488));
    p.push(dash(cx,480,cx+6,355)); p.push(shotMark(cx+6,355,1));
    p.push(yLbl(cx+30,368,sh[0].dist+'y'));
    p.push(dash(cx+6,343,cx+16,212)); p.push(shotMark(cx+16,212,2));
    p.push(yLbl(cx+40,226,sh[1].dist+'y'));
    p.push(dash(cx+16,200,234,94)); p.push(shotMark(234,94,3));
    p.push(yLbl(260,106,sh[2].dist+'y'));
  }

  else if(s==='par3TwoWater'){
    p.push(waterRect(18,48,95,215));
    p.push(waterRect(207,48,95,215));
    p.push(wLabel(62,170));
    p.push(wLabel(257,170));
    p.push(fw(cx-32,262,64,172,6));
    p.push(greenEl(cx,80,46,30)); p.push(flag(cx+14,80));
    p.push(bunker(cx-66,82,18,11));
    p.push(bunker(cx,118,22,10));
    p.push(`<text x="${cx}" y="46" text-anchor="middle" fill="#ff8888" font-size="9" font-weight="700">SIGNATURE HOLE</text>`);
    p.push(teeBox(cx,444));
    p.push(dash(cx,436,cx,114)); p.push(shotMark(cx,110,1,'#3d9e56'));
    p.push(yLbl(cx+22,124,sh[0].dist+'y'));
  }

  else if(s==='par4WaterLeft'){
    p.push(waterRect(0,48,cx-18,420));
    p.push(wLabel(55,290));
    p.push(`<rect x="${cx-16}" y="82" width="120" height="380" rx="6" fill="#3d7a52" opacity="0.9"/>`);
    p.push(greenEl(232,70,38,22)); p.push(flag(244,70));
    if(hz.includes('bunkerGreenLeft'))  p.push(bunker(192,72,14,9));
    if(hz.includes('bunkerGreenRight')) p.push(bunker(272,72,14,9));
    p.push(`<text x="${cx+40}" y="405" text-anchor="middle" fill="#e0c060" font-size="8" font-weight="700">STAY RIGHT</text>`);
    p.push(teeBox(cx+18,466));
    if(sh.length===2){
      p.push(dash(cx+18,458,cx+28,315)); p.push(shotMark(cx+28,315,1));
      p.push(yLbl(cx+54,328,sh[0].dist+'y'));
      p.push(dash(cx+28,303,232,94)); p.push(shotMark(232,94,2));
      p.push(yLbl(258,106,sh[1].dist+'y'));
    } else {
      p.push(dash(cx+18,458,cx+28,315)); p.push(shotMark(cx+28,315,1));
      p.push(yLbl(cx+54,328,sh[0].dist+'y'));
      p.push(dash(cx+28,303,cx+36,192)); p.push(shotMark(cx+36,192,2));
      p.push(yLbl(cx+62,205,sh[1].dist+'y'));
      p.push(dash(cx+36,180,232,94)); p.push(shotMark(232,94,3));
      p.push(yLbl(258,106,sh[2].dist+'y'));
    }
  }

  // ── NEW SHAPES ─────────────────────────────────────────────────────────────

  else if(s==='par3Island'){
    // Full water background
    p.push(waterRect(0,48,W,420));
    p.push(wLabel(cx,390));
    // Narrow fairway strip at tee end
    p.push(fw(cx-28,355,56,90,6));
    // Island: grassy surround + green
    p.push(`<ellipse cx="${cx}" cy="145" rx="56" ry="42" fill="#3d7a52" opacity="0.95"/>`);
    p.push(greenEl(cx,143,36,26)); p.push(flag(cx+14,143));
    // Thin walkway/bridge
    p.push(`<rect x="${cx-7}" y="185" width="14" height="88" fill="#4a6e40" opacity="0.75"/>`);
    if(hz.includes('bunkerGreenLeft'))  p.push(bunker(cx-62,146,14,9));
    if(hz.includes('bunkerGreenRight')) p.push(bunker(cx+62,146,14,9));
    if(hz.includes('bunkerFront'))      p.push(bunker(cx,180,18,9));
    p.push(`<text x="${cx}" y="46" text-anchor="middle" fill="#ff8888" font-size="9" font-weight="700">ISLAND GREEN</text>`);
    p.push(teeBox(cx,435));
    p.push(dash(cx,427,cx,193)); p.push(shotMark(cx,189,1,'#3d9e56'));
    p.push(yLbl(cx+22,203,sh[0].dist+'y'));
  }

  else if(s==='par5WaterRight'){
    // Water right side
    p.push(waterRect(cx+32,48,W-cx-12,430));
    p.push(wLabel(W-54,270));
    // Fairway left side
    p.push(`<rect x="18" y="76" width="116" height="392" rx="6" fill="#3d7a52" opacity="0.9"/>`);
    p.push(greenEl(76,64,40,24)); p.push(flag(88,64));
    if(hz.includes('bunkerGreenLeft'))  p.push(bunker(34,68,13,8));
    if(hz.includes('bunkerGreenRight')) p.push(bunker(118,68,13,8));
    if(hz.includes('bunkerLeft'))       p.push(bunker(20,318,14,9));
    if(hz.includes('bunkerFairwayMid')) p.push(bunker(76,238,18,11));
    if(hz.includes('bunkerFairwayLeft'))p.push(bunker(22,198,13,9));
    p.push(`<text x="76" y="430" text-anchor="middle" fill="#e0c060" font-size="8" font-weight="700">STAY LEFT</text>`);
    p.push(teeBox(76,464));
    if(sh.length===2){
      p.push(dash(76,456,70,300)); p.push(shotMark(70,300,1));
      p.push(yLbl(44,313,sh[0].dist+'y'));
      p.push(dash(70,288,76,88)); p.push(shotMark(76,88,2));
      p.push(yLbl(50,100,sh[1].dist+'y'));
    } else {
      p.push(dash(76,456,70,358)); p.push(shotMark(70,358,1));
      p.push(yLbl(44,371,sh[0].dist+'y'));
      p.push(dash(70,346,72,232)); p.push(shotMark(72,232,2));
      p.push(yLbl(46,245,sh[1].dist+'y'));
      p.push(dash(72,220,76,88)); p.push(shotMark(76,88,3));
      p.push(yLbl(50,100,sh[2].dist+'y'));
    }
  }

  else if(s==='par4SharpDoglegLeft'){
    // Near-90 degree left dogleg — fairway runs straight down then turns hard left
    p.push(`<path d="M ${cx-38} 470 L ${cx-38} 282 L 38 282 L 38 70 L 98 70 L 98 282 L ${cx+38} 282 L ${cx+38} 470 Z" fill="#3d7a52" opacity="0.9"/>`);
    p.push(greenEl(68,58,38,22)); p.push(flag(80,58));
    if(hz.includes('bunkerCornerLeft'))    p.push(bunker(cx-42,268,18,12));
    if(hz.includes('bunkerCornerOutside')) p.push(bunker(52,296,16,10));
    if(hz.includes('bunkerGreenLeft'))     p.push(bunker(28,62,13,8));
    if(hz.includes('bunkerGreenRight'))    p.push(bunker(110,62,13,8));
    if(hz.includes('bunkerRight'))         p.push(bunker(cx+56,380,15,10));
    p.push(teeBox(cx,478));
    if(sh.length===2){
      p.push(dash(cx,470,cx-6,300)); p.push(shotMark(cx-6,300,1));
      p.push(yLbl(cx+18,314,sh[0].dist+'y'));
      p.push(dash(cx-6,288,68,82)); p.push(shotMark(68,82,2));
      p.push(yLbl(42,94,sh[1].dist+'y'));
    } else {
      p.push(dash(cx,470,cx-4,355)); p.push(shotMark(cx-4,355,1));
      p.push(yLbl(cx+20,368,sh[0].dist+'y'));
      p.push(dash(cx-4,343,cx-18,294)); p.push(shotMark(cx-18,294,2));
      p.push(yLbl(cx+6,308,sh[1].dist+'y'));
      p.push(dash(cx-18,282,68,82)); p.push(shotMark(68,82,3));
      p.push(yLbl(42,94,sh[2].dist+'y'));
    }
  }

  else if(s==='par4SharpDoglegRight'){
    // Near-90 degree right dogleg
    p.push(`<path d="M ${cx-38} 470 L ${cx-38} 282 L ${W-38} 282 L ${W-38} 70 L ${W-98} 70 L ${W-98} 282 L ${cx+38} 282 L ${cx+38} 470 Z" fill="#3d7a52" opacity="0.9"/>`);
    p.push(greenEl(252,58,38,22)); p.push(flag(264,58));
    if(hz.includes('bunkerCornerRight'))   p.push(bunker(cx+42,268,18,12));
    if(hz.includes('bunkerCornerOutside')) p.push(bunker(268,296,16,10));
    if(hz.includes('bunkerGreenLeft'))     p.push(bunker(212,62,13,8));
    if(hz.includes('bunkerGreenRight'))    p.push(bunker(294,62,13,8));
    if(hz.includes('bunkerLeft'))          p.push(bunker(cx-56,380,15,10));
    p.push(teeBox(cx,478));
    if(sh.length===2){
      p.push(dash(cx,470,cx+6,300)); p.push(shotMark(cx+6,300,1));
      p.push(yLbl(cx+30,314,sh[0].dist+'y'));
      p.push(dash(cx+6,288,252,82)); p.push(shotMark(252,82,2));
      p.push(yLbl(278,94,sh[1].dist+'y'));
    } else {
      p.push(dash(cx,470,cx+4,355)); p.push(shotMark(cx+4,355,1));
      p.push(yLbl(cx+28,368,sh[0].dist+'y'));
      p.push(dash(cx+4,343,cx+18,294)); p.push(shotMark(cx+18,294,2));
      p.push(yLbl(cx+42,308,sh[1].dist+'y'));
      p.push(dash(cx+18,282,252,82)); p.push(shotMark(252,82,3));
      p.push(yLbl(278,94,sh[2].dist+'y'));
    }
  }

  return mkSvg(p.join(''));
}
""")

html.write("""
const holes=[
  {number:1,par:4,yards:363,hcp:5,shape:'doglegLeft',hazards:['bunkerCornerLeft','bunkerCornerOutside','bunkerGreenLeft','bunkerGreenRight'],
   shots:[{num:1,club:'Driver',dist:250,remaining:113,note:'Aim CENTER-RIGHT off tee — left bunker cuts into the dogleg corner, stay right of it to open the approach angle'},{num:2,club:'48\\u00b0 Wedge',dist:115,remaining:0,note:'113y to green — firm full 48-degree, thread between the greenside bunkers left and right, aim center'}],
   attack:['Drive right of the left corner bunker — opens the green perfectly for a wedge','Full 48-degree from 113y is a very comfortable scoring wedge','Par or birdie on the opener sets the tone for the entire round'],
   avoid:['The left bunker at the dogleg corner — miss left here and your approach is blocked','Cutting too hard left off the tee — driver can reach native grass beyond the corner','Chasing a tucked pin on approach — center green is the correct play'],
   mustDo:['Visualize the entire hole before you tee it up — plan the tee shot angle','Drive right-center so the corner bunker is left of your ball','Center-green approach — both sides of this green are protected by sand'],
   notes:'<strong>Hole 1 — Dogleg Left opener on a 126-slope championship course.</strong> A bunker cuts in from the left at the corner, with a second large bunker on the outside of the bend. From the tan tees at 363 yards, your <strong>Driver (250y)</strong> should aim center-right finishing right of the corner bunker, leaving just 113 yards — a perfect full <strong>48-degree wedge</strong>. The green is guarded by bunkers on both sides — aim center. <strong>This is a birdie opportunity. Take it and build momentum from hole 1.</strong>'},

  {number:2,par:3,yards:155,hcp:11,shape:'par3straight',hazards:['bunkerLeft','bunkerRight'],
   shots:[{num:1,club:'8 Iron',dist:150,remaining:5,note:'155y to an angled green — firm 8-iron, aim widest part of green, 5y short of back pins is perfectly acceptable'}],
   attack:['Firm 8-iron aimed at the widest part of the angled green','Bunkers guard both sides — center is the only smart target','Par here is easy and expected — this is a birdie opportunity at 155y'],
   avoid:['Going at a side-tucked pin guarded by bunkers left or right','Over-clubbing and flying the green into trouble behind','Any deceleration through impact — commit to the firm 8-iron swing'],
   mustDo:['Firm committed 8-iron — no steering, full smooth swing through impact','Target the CENTER of the green regardless of pin position','Two-putt for par — ideally make a confident birdie from inside 15 feet'],
   notes:'<strong>155-yard par 3 — a very manageable one-shotter from the tan tees.</strong> Bunkers guard both sides. Your <strong>8-iron (150y)</strong> is dialed in for this yardage — just a touch firm and you are pin-high. The green is angled, so read which tier the flag sits on. <strong>Center-green is the correct target</strong> — do not make this harder by hunting a tucked pin. This is one of the more birdie-able par 3s on the course. Get it close and make the putt.'},

  {number:3,par:5,yards:493,hcp:17,shape:'par5Straight',hazards:['bunkerLeft','bunkerLeft2'],
   shots:[{num:1,club:'Driver',dist:250,remaining:243,note:'Drive RIGHT of the left fairway bunkers — more room right than it looks from the tee, sets up a clean layup'},{num:2,club:'9 Iron',dist:140,remaining:103,note:'9-iron layup to 103y — stay right of the left bunkers, center of fairway'},{num:3,club:'52\\u00b0 Wedge',dist:100,remaining:3,note:'Full 52-degree from 103y — open green accepts running approaches from short, attack the flag'}],
   attack:['Drive right of the left-side bunkers — easiest hole on the course, own it','9-iron layup to 103y sets up a perfect full 52-degree approach','Green accepts running approaches — birdie is the expected result here'],
   avoid:['The left fairway bunkers — they are the only real danger on this easy par 5','Lazy 3-putt on the easiest hole on the course (HCP 17)','Over-complicating a hole that rewards simple, committed golf'],
   mustDo:['Drive RIGHT of center — the left bunkers are the sole danger on this hole','Commit to the 3-shot formula: Driver right, 9-iron, 52-degree in','Attack the flag on shot 3 — birdie here is mandatory for a 9 handicap'],
   notes:'<strong>Easiest hole on the Ambiente Course (HCP 17) — from the tan tees at 493 yards.</strong> Left-side fairway bunkers are the only real obstacle — aim right of them and the hole is wide open. The green accepts running approaches from short. <strong>Your formula:</strong> Driver (250y) right of bunkers \\u2192 9-iron (140y) layup to 103y \\u2192 52-degree (100y) in. <strong>Birdie is the expectation here for a 9 handicap. Do not give this hole away.</strong>'},

  {number:4,par:4,yards:317,hcp:13,shape:'par4WashCarry',hazards:['bunkerLeft','bunkerRight'],
   shots:[{num:1,club:'Driver',dist:250,remaining:67,note:'Carry the Indian Bend Wash — full committed driver, the carry is farther than it looks from the tee'},{num:2,club:'56\\u00b0 Wedge',dist:67,remaining:0,note:'67y to green — controlled pitch with 56-degree, aim front-center and let it release'}],
   attack:['Full committed driver to carry the wash — leaves a routine short pitch in','56-degree pitch from 67y is very comfortable — this is a birdie hole','Par or birdie expected once you clear the forced carry — take it'],
   avoid:['Any hesitation or steering on the tee shot — commit to a full driver swing','Underestimating the wash carry — it plays farther than it looks from the tee','Being cute with the pitch — front-center green is the right target, let it run'],
   mustDo:['FULL driver swing — not the place to guide or steer the ball','Relax after the carry — the pitch is very routine from 67y','Front-center green target — 56-degree pitch and let the ball release to the hole'],
   notes:'<strong>Forced carry over the Indian Bend Wash — from tan tees at 317 yards.</strong> The tee shot must carry the wash — it looks manageable but plays farther than it appears. Your <strong>Driver (250y)</strong> easily clears the wash and leaves just 67 yards. A controlled <strong>56-degree pitch</strong> is all that stands between you and a birdie. The green opens up nicely after the carry. <strong>HCP 13 — birdie is the expected outcome from the tan tees. Take it.</strong>'},

  {number:5,par:4,yards:290,hcp:15,shape:'par4WaterRight',hazards:['bunkerGreenLeft','bunkerGreenBack','bunkerGreenRight'],
   shots:[{num:1,club:'3 Hybrid',dist:220,remaining:70,note:'Stay LEFT — water runs the ENTIRE right side from tee to green, 3-hybrid left side only, no driver'},{num:2,club:'56\\u00b0 Wedge',dist:70,remaining:0,note:'70y from left side — controlled 56-degree pitch center-green, bunkers buffer right before water'}],
   attack:['3-hybrid to left side every time — this is the correct play, do not think about driver','70y from the left side is a routine pitch — birdie is very realistic here','The green bunkers right are your friends — they buffer before the water'],
   avoid:['DRIVER — water right turns any push or fade into a penalty stroke','Anything right on either shot — water runs the complete right side','Trying to drive the green — extreme high variance, water punishes every right miss'],
   mustDo:['3-hybrid to the LEFT side of the fairway — make this a deliberate decision','Approach center or left-center of green — never aim right on this hole','The green bunkers are your friends — miss in sand not in water'],
   notes:'<strong>Drivable par 4 at 290y from the tan tees — but water changes everything.</strong> Water runs the ENTIRE right side from tee to green. The green sits on a near-peninsula with bunkers left, back, and right buffering before the water. Your plan: <strong>3 Hybrid (220y)</strong> to the LEFT side, then a <strong>56-degree pitch (70y)</strong> from the safe left position. <strong>Never go right on any shot. Birdie from 70y on the left side is a very realistic outcome on this hole.</strong>'},

  {number:6,par:4,yards:369,hcp:1,shape:'par5DoglegLeft',hazards:['bunkerCornerLeft','bunkerGreenLeft','bunkerGreenRight'],
   shots:[{num:1,club:'Driver',dist:250,remaining:119,note:'Avoid the left-cutting fairway bunker at the dogleg corner — aim center-RIGHT off tee to clear it and open the approach'},{num:2,club:'48\\u00b0 Wedge',dist:115,remaining:4,note:'119y to green — firm full 48-degree, aim center of green between the bunkers on both sides'}],
   attack:['Drive right of the left bunker — opens the green for a clean wedge approach','Firm 48-degree from 119y is a standard full-swing wedge — hit your number','Par is an excellent score on the hardest hole — HCP 1 for good reason'],
   avoid:['The nasty left bunker at the dogleg corner — miss here and your approach is blocked','Over-cutting the corner with driver and ending up in the native left rough','Chasing a tucked pin on approach — bunkers left and right demand a center-green play'],
   mustDo:['Accept this is the hardest hole — stay composed and play your game plan','Driver must avoid the defining left bunker — aim right-center of the fairway','Firm 48-degree to center of green — take your par and walk away happy'],
   notes:'<strong>Stroke Index 1 — the hardest hole on the Ambiente Course.</strong> At 369 yards from the tan tees, this dogleg left still demands precision — a bunker cuts aggressively into the fairway from the left, and bunkers guard both sides of the green. Your plan: <strong>Driver (250y)</strong> right of the left bunker leaves 119 yards — a firm full <strong>48-degree wedge</strong> to center-green. From the tan tees this is now a 2-shot hole, but the bunker layout still demands accuracy. <strong>A par on the hardest hole is one of the best results of the day. Stay composed.</strong>'},

  {number:7,par:5,yards:530,hcp:7,shape:'par5DoglegLeft',hazards:['bunkerCornerLeft','bunkerFairwayLeft','bunkerFairwayLeft2'],
   shots:[{num:1,club:'Driver',dist:250,remaining:280,note:'Narrow fairway — precision off tee, aim LEFT-CENTER staying right of the left bunkers through the bend'},{num:2,club:'7 Iron',dist:160,remaining:120,note:'7-iron through the corner staying right of the bunkers — 120y remaining for the approach'},{num:3,club:'48\\u00b0 Wedge',dist:115,remaining:5,note:'Firm 48-degree from 120y — nearly exact yardage, commit to center-green, birdie opportunity'}],
   attack:['Play methodically — accuracy through the left bunkers earns a great wedge look','Driver left-center, 7-iron through the bend, 48-degree in — clean formula','Birdie here is very realistic — your 48-degree at 120y is almost a perfect number'],
   avoid:['Left-side bunkers throughout — they are constantly in play on this narrow hole','Hero shots to shorten this hole — 3 disciplined shots earn birdie','Rushing any of the three shots — every shot demands full focus'],
   mustDo:['Stay between the lines — narrow fairway demands accuracy over raw power','7-iron must clear the left corner bunkers and stay right of the fairway left bunkers','Trust the 48-degree at 120y — firm full swing, this is your number'],
   notes:'<strong>Par 5 at 530 yards from the tan tees — birdie is the target.</strong> The fairway bends left with bunkers lining the left side, making accuracy the priority. Your three-shot plan: <strong>Driver (250y)</strong> left-center, <strong>7-iron (160y)</strong> through the bend to 120 yards, then a firm <strong>48-degree wedge (115y)</strong> to the green. The green front is relatively open. <strong>From the tan tees this is a very playable birdie hole. Three fairways hit equals a great putt. Go make your score.</strong>'},

  {number:8,par:3,yards:174,hcp:9,shape:'par3Long',hazards:['bunkerRight'],
   shots:[{num:1,club:'6 Iron',dist:170,remaining:4,note:'174y to a perched green — firm 6-iron, aim DEAD CENTER, a cavernous bunker guards the entire left side'}],
   attack:['Firm 6-iron at 174y — this is very manageable from the tan tees','Dead center of the perched green is the correct target','Par here is solid — birdie is realistic from inside 10-15 feet'],
   avoid:['SHORT LEFT — a massive cavernous bunker guards the entire left side of this green','Under-clubbing — the green is perched and being short is severely punished','Any mental hesitation — this is not the 241-yard blue tee version, commit freely'],
   mustDo:['Full committed 6-iron — swing to a complete finish, no deceleration','Center of green ONLY — the left bunker makes any left miss a very difficult situation','Two-putt par at minimum — birdie from center-green is very achievable here'],
   notes:'<strong>From the tan tees, 174 yards to a perched green — very manageable.</strong> This plays nothing like the 241-yard blue tee version. Your <strong>6-iron (170y)</strong> is perfectly dialed in — just a touch firm and you are pin-high. The green is perched with a cavernous bunker guarding the left side. Aim DEAD CENTER. <strong>A par on this hole from the tan tees should be the expectation. Get it on the green and make your two-putt — or better yet, drain the birdie putt.</strong>'},

  {number:9,par:4,yards:385,hcp:3,shape:'par4LongWaterRight',hazards:['bunkerGreenLeft','bunkerGreenRight'],
   shots:[{num:1,club:'Driver',dist:250,remaining:135,note:'Drive LEFT of the center fairway bunker — water runs the full right side, stay left always'},{num:2,club:'9 Iron',dist:140,remaining:0,note:'135y from the left side — smooth 9-iron to center-green, aim left of flag, NEVER right toward water'}],
   attack:['Drive left of center bunker — leaves a smooth 9-iron approach from the safe side','9-iron to center-green from 135y is a very comfortable scoring shot','Par or birdie here — this is a 2-shot hole from the tan tees, take advantage'],
   avoid:['RIGHT of center on the tee shot — water runs the full right side to the green','Carrying or flirting with the center bunker toward the right side','Aiming right on the approach — water is only on the right, never go there'],
   mustDo:['Drive LEFT of the center bunker — this is the only correct decision off the tee','Smooth 9-iron to center-green — false front means never leave it short','Never let the water enter your mind during the swing — commit left and go'],
   notes:'<strong>HCP 3 — demanding par 4 now a 2-shot hole from the tan tees at 385 yards.</strong> A center bunker sits mid-fairway forcing a direction decision. Stay LEFT. Water runs the entire right side — the 9th and 18th holes share the same massive pond. A false front on the green means short putts feed away. <strong>Formula: Driver left of bunker (250y) \\u2192 9-iron (140y) smooth swing aimed center-left of the green.</strong> Par or birdie is the expected result from the tan tees.'},

  {number:10,par:4,yards:328,hcp:18,shape:'doglegLeft',hazards:['bunkerRight'],
   shots:[{num:1,club:'Driver',dist:250,remaining:78,note:'Cut the dogleg corner — driver aimed straight at the bend, opens a simple short pitch into the steep green'},{num:2,club:'56\\u00b0 Wedge',dist:75,remaining:3,note:'78y in — controlled 56-degree, green slopes STEEPLY BACK toward fairway, aim front and let it release'}],
   attack:['Cut the corner with driver — from the tan tees you can get very close to the green','56-degree from 78y — aim FRONT of green, the steep back-slope feeds it to the flag','Easiest hole on the course — birdie is the expectation here, go make one'],
   avoid:['Right fairway bunker if you over-cut the corner with driver — aim just left of it','Going long on the approach — the green pitches HARD back toward you, long is very bad','Lazy 2-putt on the easiest hole on the course — be aggressive with the birdie putt'],
   mustDo:['Cut the corner — straight line to the green is your driver target','The green pitches TOWARD you — aim front-center, NEVER past the flag','Read the back-slope carefully and make a confident birdie putt'],
   notes:'<strong>Easiest hole on the course (HCP 18) from the tan tees — only 328 yards.</strong> The dogleg left allows you to cut the corner and leave just 78 yards to the green. A controlled <strong>56-degree wedge</strong> is all you need. Critical note: the green is steeply pitched BACK toward the fairway — aim front-center and let the ball feed to the flag. Going past the flag is a major mistake. <strong>Birdie here is the expectation. This is where 9 handicaps build their scorecard — do not settle for par.</strong>'},

  {number:11,par:3,yards:166,hcp:12,shape:'par3straight',hazards:[],
   shots:[{num:1,club:'7 Iron',dist:160,remaining:6,note:'166y — firm 7-iron, aim center of green, no heroics needed on this very manageable par 3'}],
   attack:['Firm 7-iron — 166y target, a confident smooth swing is all you need','Center of green is the perfect target — no reason to chase a side pin','Use this hole to breathe and reset — a birdie here would be outstanding'],
   avoid:['8-iron at full swing — you risk coming up 16 yards short at 166y','Aggressively hunting a tucked pin when center-green is perfectly acceptable','Over-thinking a very manageable par 3 — just commit and swing'],
   mustDo:['Firm 7-iron — easy full swing, commit to the center of the green','Birdie putt is very realistic from center-green at 166y — read it carefully','You have 7 holes left — this is your moment to take the lead in the round'],
   notes:'<strong>Very manageable 166-yard par 3 from the tan tees.</strong> Your <strong>7-iron (160y)</strong> is almost dead-on — just a touch firm and you are pin-high. There is no reason to be aggressive from here. <strong>A center-green approach from 166y should leave you inside 15 feet. Birdie is very achievable here — make the putt and carry that momentum through the back nine.</strong>'},

  {number:12,par:4,yards:373,hcp:2,shape:'straight',hazards:['bunkerLeft','bunkerCenter','bunkerRight'],
   shots:[{num:1,club:'Driver',dist:250,remaining:123,note:'Three fairway bunkers — center, left, and right. Thread between them aiming center-left of the fairway'},{num:2,club:'48\\u00b0 Wedge',dist:115,remaining:8,note:'123y to green — firm full 48-degree, aim center of green, avoid the back-left pin position'}],
   attack:['Navigate the three bunkers off the tee — then a full 48-degree approach in','Firm 48-degree from 123y is a very standard scoring wedge distance','Par or birdie expected — from the tan tees this is a legitimate 2-shot hole'],
   avoid:['Any of the three fairway bunkers — they severely limit your approach angle','Going at the back-left pin position — it is the most punishing area of the green','Forcing a difficult angle by missing left into the left bunker off the tee'],
   mustDo:['Navigate the three fairway bunkers — center-left tee shot is the correct line','Firm 48-degree to 123y — do not steer or guide, commit to a full swing','Aim center of green — back-left is the most punishing area, never chase it'],
   notes:'<strong>Second hardest hole on the course (HCP 2) — now a 2-shot hole from tan tees at 373 yards.</strong> Three fairway bunkers — center, left, and right — make directional precision critical off the tee. A back-left pin is the hardest position to attack. <strong>Play it as 2 shots:</strong> Driver (250y) threading center-left of bunkers, then a firm <strong>48-degree wedge (115y)</strong> from 123 yards to center-green. <strong>Par here is excellent on the second hardest hole. Birdie is very realistic from 123y.</strong>'},

  {number:13,par:4,yards:335,hcp:14,shape:'straight',hazards:['angledBunkerRight','bunkerFrontLeft'],
   shots:[{num:1,club:'Driver',dist:250,remaining:85,note:'Long angled bunker on the right — aim LEFT of it for safe play, or hug it right for the best approach angle into the narrow green'},{num:2,club:'56\\u00b0 Wedge',dist:75,remaining:10,note:'85y to a narrow green — controlled pitch with 56-degree, aim center, avoid deep left greenside bunkers'}],
   attack:['Safe play: left-center tee shot leaves a comfortable 85y pitch in','Brave play: hug the right bunker off tee for the best angle into the narrow green','From 85y this is a very short approach — birdie is a very realistic target'],
   avoid:['The long angled right fairway bunker — severely limits your approach angle','Deep left greenside bunkers on the approach — do not short-side left','Under-estimating this hole just because it is HCP 14 — execute your plan'],
   mustDo:['Pick your tee shot line and commit fully — safe left or brave right','56-degree pitch must stay away from the deep left greenside bunkers','Read the green and make a confident birdie putt — this is a scoring hole'],
   notes:'<strong>Risk/reward par 4 at 335 yards from the tan tees (HCP 14).</strong> A long angled bunker runs along the right side of the fairway. The closer you drive to it, the better the approach angle into the narrow green. The safe play is left-center, leaving an 85-yard pitch. Deep bunkers guard the left of the green. <strong>For a 9 handicap: this is a birdie opportunity. Drive left-center, pitch your 56-degree to center-green from 85y, and drain the putt.</strong>'},

  {number:14,par:5,yards:497,hcp:6,shape:'par5DoglegRight',hazards:['bunkerFairwayLeft','bunkerFairwayRight','bunkerFairwayMid','bunkerGreenLeft'],
   shots:[{num:1,club:'Driver',dist:250,remaining:247,note:'Multiple fairway bunkers shape this dogleg right — drive CENTER-RIGHT through the bend avoiding the inside left bunker'},{num:2,club:'8 Iron',dist:150,remaining:97,note:'8-iron threading the bunkers — 97y remaining to the small, well-guarded green'},{num:3,club:'52\\u00b0 Wedge',dist:100,remaining:0,note:'Full 52-degree from 97y — small green requires precision, aim largest part of green, trust the club'}],
   attack:['3-shot plan is the smart play — small green and multiple bunkers make 2-on very difficult','Drive center-right through the dogleg avoiding the inside left bunker','Full 52-degree from 97y is a comfortable approach — birdie is very achievable here'],
   avoid:['Left fairway bunker on the inside of the dogleg — it catches inside tee shots','Going for the green in two — multiple bunkers and a small target make it low percentage','Firing at a tucked pin on the small green — aim for the largest area always'],
   mustDo:['3-shot plan is correct — Driver, 8-iron to 97y, full 52-degree in','Drive center-right through the bend — the left bunker is the most dangerous','Full 52-degree at 97y — commit to this club, it is your number'],
   notes:'<strong>Par 5 with dogleg right and multiple strategically placed bunkers (HCP 6) — 497 yards from tan tees.</strong> The green is relatively small, making a two-shot approach demanding. Your plan: <strong>Driver (250y)</strong> center-right through the dogleg, <strong>8-iron (150y)</strong> to 97 yards, then a full <strong>52-degree wedge (100y)</strong> aimed at the largest part of the green. <strong>From the tan tees, birdie is very much in play here. Three smart positional shots equals a birdie putt. Go make it.</strong>'},

  {number:15,par:3,yards:182,hcp:16,shape:'par3TwoWater',hazards:[],
   shots:[{num:1,club:'5 Iron',dist:180,remaining:2,note:'182y CARRY with water both sides — firm 5-iron, aim DEAD CENTER, front tier of the two-tiered green is your safest target'}],
   attack:['5-iron at 182y is almost a perfect number — this is very manageable from the tan tees','Aim dead center — water is left AND right but from 182y your 5-iron is the right tool','Front tier of the two-tiered green is the safe and correct target'],
   avoid:['SHORT — water catches short shots on BOTH sides of this green','Left cavernous bunker — a miss left is a severe penalty situation','Under-clubbing — 6-iron at 170y leaves you 12y short with water on both sides'],
   mustDo:['COMMIT — firm 5-iron, full swing to a complete finish','Dead center of the green is your ONLY target on this spectacular hole','Front tier is safe — land front tier and make a confident two-putt'],
   notes:'<strong>SIGNATURE HOLE — from the tan tees at 182 yards, this is now in your wheelhouse.</strong> At 245 yards from the blues, driver was the only option. From the tan tees your <strong>5-iron (180y)</strong> is nearly perfect for this hole. Water still flanks both sides and the cavernous left bunker is still very much in play — but this is now a very makeable par 3. <strong>Aim dead center, make a full committed 5-iron swing, and two-putt for par or better. A birdie here on the signature hole would be a highlight of your round.</strong>'},

  {number:16,par:5,yards:442,hcp:4,shape:'par5Straight',hazards:['bunkerLeft','bunkerLeft2'],
   shots:[{num:1,club:'Driver',dist:250,remaining:192,note:'Multiple left fairway bunkers — drive RIGHT of center to avoid them, the left side is lined with bunkers'},{num:2,club:'9 Iron',dist:140,remaining:52,note:'9-iron layup staying right of the left bunkers — leaves 52y for a controlled pitch'},{num:3,club:'56\\u00b0 Wedge',dist:52,remaining:0,note:'Controlled soft 56-degree pitch from 52y — aim center of green, let the ball release to the flag'}],
   attack:['Drive right of center to avoid multiple left bunkers — sets up the hole perfectly','9-iron to 52y gives you a very comfortable short pitch for the third shot','Birdie is the target — 52y pitch to center-green is a very makeable up-and-down'],
   avoid:['Left bunkers off the tee — multiple bunkers guard the entire left side','Forcing a second shot from a bad angle near the left bunkers','Short-siding yourself on the pitch — center-green is the right target'],
   mustDo:['Drive RIGHT of center — the left bunkers are the only real danger on this hole','9-iron layup to 52y — this is the correct yardage, trust the plan','Soft 56-degree from 52y — controlled swing, let it release, make your birdie putt'],
   notes:'<strong>Par 5 at 442 yards from the tan tees (HCP 4) — birdie is the expectation.</strong> The left side of this fairway is guarded by bunkers, making right-of-center the required tee shot. Your 3-shot formula: <strong>Driver (250y)</strong> right of center, <strong>9-iron (140y)</strong> layup to 52 yards, then a soft <strong>56-degree wedge pitch</strong> to center-green. <strong>Make your birdie here. This is one of the most scoreable holes on the back nine from the tan tees.</strong>'},

  {number:17,par:4,yards:370,hcp:10,shape:'straight',hazards:['bunkerCenter','bunkerRight'],
   shots:[{num:1,club:'Driver',dist:250,remaining:120,note:'Center fairway bunker is directly in play — aim LEFT of center to avoid it deliberately, opens up a clean wedge approach'},{num:2,club:'48\\u00b0 Wedge',dist:115,remaining:5,note:'120y to green — firm full 48-degree, aim center of green between the bunkers'}],
   attack:['Aim deliberately left of the center bunker — opens the hole for a clean wedge approach','Firm 48-degree from 120y is a dead-on yardage — this is a birdie hole','Par or birdie expected — from the tan tees this is a very playable 2-shot hole'],
   avoid:['Center fairway bunker off the tee — it is directly in the driver line','Right bunker far right — do not over-correct right trying to avoid the center bunker','Steering the 48-degree wedge — commit to a full swing from 120y'],
   mustDo:['Deliberately aim left of the center bunker — make this a conscious decision','Firm 48-degree at 120y — this is nearly your exact wedge distance, trust it','Stay composed — you are one hole from the stunning signature closer'],
   notes:'<strong>370-yard par 4 from the tan tees (HCP 10)</strong> — now a clean 2-shot hole. A center fairway bunker and right-side bunker are the key obstacles. Aim left of the center bunker deliberately — this opens up the approach perfectly. After your driver, a firm <strong>48-degree wedge from 120 yards</strong> is nearly your exact distance. <strong>Par or birdie here and you step onto 18 with confidence. Stay in your process — one iconic hole to go.</strong>'},

  {number:18,par:4,yards:354,hcp:8,shape:'par4WaterLeft',hazards:['bunkerGreenLeft','bunkerGreenRight'],
   shots:[{num:1,club:'Driver',dist:250,remaining:104,note:'Drive RIGHT-CENTER — water runs the ENTIRE left side from tee to green, miss right never left'},{num:2,club:'52\\u00b0 Wedge',dist:100,remaining:4,note:'104y to green — firm full 52-degree from right side, aim center of green, NEVER left toward water'}],
   attack:['Drive RIGHT of center every time — water full left makes any left miss a penalty','Firm 52-degree from 104y is a perfect full-swing wedge — great finishing birdie chance','From the right side the green opens up beautifully — commit and make your score'],
   avoid:['ANYTHING LEFT on either shot — water runs the entire left side all the way to the green','Going for a tuck left pin on the approach — water punishes every left miss severely','Letting the water affect your swing — commit right on both shots and never look left'],
   mustDo:['Aim right of center on BOTH shots — tee shot and approach stay right','Full 52-degree at 104y — this is your number, do not steer it','Finish your round strong on this iconic Arizona hole — right side and go make birdie'],
   notes:'<strong>VOTED BEST WATER HOLE IN ARIZONA — Arizona Golf Magazine.</strong> The 9th and 18th holes share the same massive pond, running the ENTIRE left side of this closing par 4. Bunkers guard both sides of the green. From the right side, your approach is clean and the green opens up clearly. Your plan from the tan tees at 354 yards: <strong>Driver (250y)</strong> right-center, then a full <strong>52-degree wedge (100y)</strong> from 104 yards — almost dead-on your yardage. <strong>Two committed right-side shots and you finish your round on this stunning signature hole. Birdie is very much in play. Go make it happen.</strong>'},
];

let currentHole=1;
function showLanding(){
  document.getElementById('landing').style.display='flex';
  document.getElementById('holeView').style.display='none';
}
function startHole(){
  const n=parseInt(document.getElementById('holeNumInput').value);
  if(n>=1&&n<=18) loadHole(n);
}
function loadHole(num){
  currentHole=num;
  const h=holes[num-1];
  document.getElementById('landing').style.display='none';
  document.getElementById('holeView').style.display='block';
  document.getElementById('hdrBadge').textContent='Hole '+h.number;
  document.getElementById('hdrTitle').textContent='Par '+h.par+' \\u2014 '+h.yards+' yards';
  document.getElementById('hdrSub').textContent='Difficulty Ranking: #'+h.hcp+' of 18 \\u00b7 '+getDiffLabel(h.hcp);
  document.getElementById('statPar').textContent=h.par;
  document.getElementById('statYards').textContent=h.yards;
  document.getElementById('statHcp').textContent='#'+h.hcp;
  document.getElementById('statShots').textContent=h.shots.length;
  const pct=Math.round(((18-h.hcp)/17)*90)+5;
  document.getElementById('diffBar').style.width=pct+'%';
  document.getElementById('holeSvg').innerHTML=buildSvg(h);
  const sl=document.getElementById('shotList');
  sl.innerHTML='';
  h.shots.forEach(s=>{
    const rem=s.remaining>0?'<span style="color:#5a7a62;font-size:.76rem;margin-left:.3rem;">('+s.remaining+'y to flag)</span>':'';
    sl.innerHTML+='<div class="shot-row"><div class="shot-num">'+s.num+'</div><div class="shot-club">'+s.club+'</div><div class="shot-dist">'+s.dist+'y'+rem+'</div><div class="shot-note">'+s.note+'</div></div>';
  });
  const fill=(id,items)=>{document.getElementById(id).innerHTML=items.map(i=>'<li>'+i+'</li>').join('');};
  fill('stratAttack',h.attack);
  fill('stratAvoid',h.avoid);
  fill('stratMustDo',h.mustDo);
  document.getElementById('holeNotes').innerHTML=h.notes;
  document.getElementById('prevBtn').disabled=num===1;
  document.getElementById('nextBtn').disabled=num===18;
  window.scrollTo(0,0);
}
function navigateHole(dir){
  const n=currentHole+dir;
  if(n>=1&&n<=18) loadHole(n);
}
function getDiffLabel(hcp){
  if(hcp<=3) return '\\ud83d\\udd34 Very Hard';
  if(hcp<=6) return '\\ud83d\\udfe0 Hard';
  if(hcp<=10) return '\\ud83d\\udfe1 Moderate';
  if(hcp<=14) return '\\ud83d\\udfe2 Manageable';
  return '\\ud83d\\udfe6 Easier Hole';
}
window.addEventListener('DOMContentLoaded',()=>{
  const qh=document.getElementById('quickHoles');
  for(let i=1;i<=18;i++){
    const b=document.createElement('button');
    b.className='quick-btn'; b.textContent='H'+i;
    b.onclick=(function(n){return function(){loadHole(n);};})(i);
    qh.appendChild(b);
  }
  document.getElementById('holeNumInput').addEventListener('keydown',function(e){if(e.key==='Enter')startHole();});
});
</script>
</body>
</html>
""")

html.close()
print("File written successfully")
