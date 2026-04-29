#!/usr/bin/env python3
"""Build αLike Investment Presentation v4"""
import json

with open('/tmp/companies_compact.json', 'r') as f:
    companies_json = f.read()

html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>αLike Investment</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked@15.0.4/marked.min.js"></script>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#f5f3ee;--card:#ffffff;--border:#e5e2db;
  --text-primary:#1a1a1a;--text-secondary:#6b6b6b;--text-tertiary:#999;
  --green:#16a34a;--green-bg:#dcfce7;--green-border:#bbf7d0;
  --amber:#d97706;--amber-bg:#fef3c7;--amber-border:#fde68a;
  --gray-pill:#6b7280;--gray-bg:#f3f4f6;--gray-border:#e5e7eb;
  --radius:12px;--radius-sm:8px;--radius-xs:6px;
  --shadow-sm:0 1px 2px rgba(0,0,0,0.04);
  --shadow-md:0 4px 12px rgba(0,0,0,0.06);
  --shadow-lg:0 8px 30px rgba(0,0,0,0.08);
  --font:-apple-system,BlinkMacSystemFont,"SF Pro Text","SF Pro Display","Helvetica Neue","PingFang SC","Noto Sans CJK SC",sans-serif;
  --max-w:1200px;
  --dark:#1a1a1a;--dark-card:#222;--dark-border:#333;--accent:#d4a574;--accent-dim:rgba(212,165,116,0.15);
}
html{scroll-behavior:smooth;-webkit-font-smoothing:antialiased}
body{font-family:var(--font);background:var(--bg);color:var(--text-primary);line-height:1.6;font-size:15px}

/* Utility */
.container{max-width:var(--max-w);margin:0 auto;padding:0 40px}
.section{padding:80px 0}
.section-title{font-size:28px;font-weight:700;letter-spacing:-0.02em;margin-bottom:8px}
.section-subtitle{font-size:15px;color:var(--text-secondary);margin-bottom:48px}

/* ===== NAV ===== */
.nav{position:fixed;top:0;left:0;right:0;z-index:100;padding:16px 40px;display:flex;justify-content:flex-end;gap:24px;background:rgba(245,243,238,0.85);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid rgba(229,226,219,0.5)}
.nav a{font-size:13px;font-weight:500;color:var(--text-secondary);text-decoration:none;transition:color 0.2s;letter-spacing:0.01em}
.nav a:hover,.nav a.active{color:var(--text-primary)}

/* ===== HERO ===== */
.hero{min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;position:relative;overflow:hidden;padding:80px 20px 60px}
.hero-content{position:relative;z-index:1;max-width:800px}
.hero-logo{display:flex;align-items:center;justify-content:center;gap:12px;margin-bottom:56px}
.hero-logo img{height:56px}
.hero h1{font-size:clamp(32px,4.5vw,48px);font-weight:800;letter-spacing:-0.03em;line-height:1.2;margin-bottom:40px;color:var(--text-primary)}
.hero-subtitle{max-width:640px;margin:0 auto 56px;text-align:left}
.hero-subtitle p{font-size:16px;color:var(--text-secondary);line-height:1.9;margin-bottom:4px;letter-spacing:0.01em}

/* Causal chain */
.chain-wrapper{position:relative;margin:0 auto;max-width:700px}
.causal-chain{display:flex;align-items:center;justify-content:center;gap:0;flex-wrap:wrap}
.chain-node{background:var(--card);border:1px solid var(--border);border-radius:var(--radius-sm);padding:10px 20px;font-size:14px;font-weight:600;color:var(--text-primary);white-space:nowrap;opacity:0;transform:translateY(8px);animation:chainFadeIn 0.5s ease forwards}
.chain-arrow{color:var(--text-tertiary);font-size:18px;margin:0 4px;opacity:0;animation:chainFadeIn 0.3s ease forwards}
.chain-node:nth-child(1){animation-delay:0.3s}
.chain-arrow:nth-child(2){animation-delay:0.5s}
.chain-node:nth-child(3){animation-delay:0.7s}
.chain-arrow:nth-child(4){animation-delay:0.9s}
.chain-node:nth-child(5){animation-delay:1.1s}
.chain-arrow:nth-child(6){animation-delay:1.3s}
.chain-node:nth-child(7){animation-delay:1.5s}
@keyframes chainFadeIn{to{opacity:1;transform:translateY(0)}}

.chain-bracket{position:relative;margin-top:16px;display:flex;align-items:center;justify-content:center}
.bracket-line{height:1px;flex:1;background:var(--accent);max-width:520px;position:relative;opacity:0;animation:chainFadeIn 0.5s ease 2.2s forwards}
.bracket-line::before,.bracket-line::after{content:'';position:absolute;top:-4px;width:1px;height:9px;background:var(--accent)}
.bracket-line::before{left:0}
.bracket-line::after{right:0}
.bracket-label{position:absolute;top:-28px;left:50%;transform:translateX(-50%);font-size:13px;color:var(--accent);font-weight:600;white-space:nowrap;opacity:0;animation:chainFadeIn 0.5s ease 2.5s forwards;letter-spacing:0.02em}

/* ===== PHILOSOPHY SECTION (Dark theme cards) ===== */
.belief-section{background:var(--bg);padding:80px 0}
.belief-nav{display:flex;gap:8px;margin-bottom:40px;flex-wrap:wrap}
.belief-nav-btn{padding:10px 24px;border-radius:var(--radius-xs);border:1px solid var(--border);background:var(--card);font-size:14px;font-weight:600;cursor:pointer;color:var(--text-secondary);transition:all 0.15s;font-family:var(--font);letter-spacing:-0.01em}
.belief-nav-btn:hover{border-color:#ccc;color:var(--text-primary)}
.belief-nav-btn.active{background:var(--dark);color:#fff;border-color:var(--dark)}
.belief-page{display:none}
.belief-page.active{display:block}

/* Dark card containers for belief content */
.dark-section{background:var(--dark);border-radius:var(--radius);padding:48px;color:#e5e5e5;margin-bottom:24px}
.dark-section .section-intro{font-size:15px;line-height:1.85;color:#aaa;margin-bottom:36px;max-width:760px}
.dark-section h2{font-size:22px;font-weight:700;color:#fff;margin-bottom:6px;letter-spacing:-0.02em}
.dark-section h2 span{color:var(--accent)}
.dark-section .sub-title{font-size:14px;color:#888;margin-bottom:28px;font-style:italic}

/* D1-D7 grid */
.d-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px;margin-bottom:32px}
.d-card{background:var(--dark-card);border:1px solid var(--dark-border);border-radius:var(--radius-sm);padding:24px;transition:border-color 0.2s}
.d-card:hover{border-color:#444}
.d-card-header{display:flex;align-items:baseline;gap:8px;margin-bottom:10px}
.d-card-id{font-size:13px;font-weight:700;color:var(--accent);letter-spacing:0.02em}
.d-card-name{font-size:15px;font-weight:600;color:#fff}
.d-card-weight{margin-left:auto;font-size:12px;color:#666;font-weight:600}
.d-card-question{font-size:13px;color:#999;line-height:1.6;margin-bottom:12px;font-style:italic}
.d-card-example{font-size:13px;color:#777;line-height:1.6}
.d-card-example strong{color:var(--accent);font-weight:600}
.d-closing{font-size:14px;color:#999;line-height:1.8;border-top:1px solid var(--dark-border);padding-top:24px;margin-top:8px}

/* Case study cards */
.case-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px}
.case-card{background:var(--dark-card);border:1px solid var(--dark-border);border-radius:var(--radius-sm);padding:24px}
.case-card h4{font-size:15px;font-weight:600;color:var(--accent);margin-bottom:12px}
.case-card p{font-size:13px;color:#aaa;line-height:1.75}
.case-card .case-highlight{font-size:14px;color:#ccc;font-weight:500;margin-bottom:8px}

/* ABCD framework */
.abcd-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}
.abcd-card{background:var(--dark-card);border:1px solid var(--dark-border);border-radius:var(--radius-sm);padding:24px}
.abcd-card .abcd-letter{font-size:24px;font-weight:800;color:var(--accent);margin-bottom:4px;letter-spacing:-0.02em}
.abcd-card .abcd-name{font-size:14px;font-weight:600;color:#fff;margin-bottom:10px}
.abcd-card .abcd-question{font-size:13px;color:#999;font-style:italic;margin-bottom:12px;line-height:1.6}
.abcd-card .abcd-example{font-size:13px;color:#777;line-height:1.6}

/* ===== ENGINE SECTION ===== */
.engine-section{padding:80px 0;background:rgba(255,255,255,0.3)}
.engine-layers{max-width:800px;margin:0 auto 48px;position:relative}
.engine-layer{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:32px;margin-bottom:0;position:relative;box-shadow:var(--shadow-sm)}
.engine-layer:not(:last-child){margin-bottom:24px}
.engine-layer:not(:last-child)::after{content:'↓';position:absolute;bottom:-20px;left:50%;transform:translateX(-50%);font-size:16px;color:var(--text-tertiary);z-index:1;background:transparent;width:24px;text-align:center}
.layer-header{display:flex;align-items:center;gap:12px;margin-bottom:12px}
.layer-number{width:32px;height:32px;border-radius:50%;background:var(--dark);color:#fff;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;flex-shrink:0}
.layer-title{font-size:16px;font-weight:700;letter-spacing:-0.01em}
.layer-subtitle{font-size:14px;color:var(--accent);font-weight:600;margin-left:8px}
.layer-desc{font-size:14px;color:var(--text-secondary);line-height:1.7;margin-bottom:8px}
.layer-detail{display:flex;gap:16px;flex-wrap:wrap;margin-top:12px}
.layer-tag{font-size:12px;color:var(--text-tertiary);background:rgba(0,0,0,0.03);padding:4px 12px;border-radius:20px;border:1px solid var(--border)}
.layer-output{font-size:13px;font-weight:600;color:var(--text-primary);margin-top:8px}

/* Decision matrix */
.decision-matrix{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow-sm);max-width:800px;margin:0 auto}
.matrix-row{display:grid;grid-template-columns:1fr auto;align-items:center;padding:14px 24px;border-bottom:1px solid var(--border);font-size:14px;gap:16px}
.matrix-row:last-child{border-bottom:none}
.matrix-row:first-child{background:rgba(0,0,0,0.02);font-weight:600;font-size:12px;text-transform:uppercase;letter-spacing:0.05em;color:var(--text-secondary)}
.matrix-condition{color:var(--text-secondary);line-height:1.5}

/* Stats bar */
.stats-bar{display:flex;justify-content:center;gap:16px;margin-top:32px;flex-wrap:wrap}
.stat-pill{display:flex;align-items:center;gap:6px;font-size:14px;font-weight:600}

/* ===== LEAGUE TABLE ===== */
.table-filters{display:flex;gap:8px;margin-bottom:20px;flex-wrap:wrap}
.filter-btn{padding:8px 20px;border-radius:var(--radius-xs);border:1px solid var(--border);background:var(--card);font-size:13px;font-weight:600;cursor:pointer;color:var(--text-secondary);transition:all 0.15s;font-family:var(--font)}
.filter-btn:hover{border-color:#ccc;color:var(--text-primary)}
.filter-btn.active{background:var(--text-primary);color:#fff;border-color:var(--text-primary)}

.league-table{width:100%;background:var(--card);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow-sm)}
.league-table thead{background:rgba(0,0,0,0.02)}
.league-table th{padding:12px 16px;font-size:12px;font-weight:600;color:var(--text-secondary);text-transform:uppercase;letter-spacing:0.05em;text-align:left;border-bottom:1px solid var(--border);white-space:nowrap}
.league-table th:first-child{width:40px;text-align:center}
.league-table td{padding:12px 16px;font-size:14px;border-bottom:1px solid var(--border);vertical-align:middle}
.league-table td:first-child{text-align:center;color:var(--text-tertiary);font-size:13px;font-weight:500}
.league-table .company-name{font-weight:600}
.league-table .thesis-preview{font-size:12px;color:var(--text-tertiary);max-width:240px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}

.league-table tr.clickable{cursor:pointer;transition:background 0.15s}
.league-table tr.clickable:hover{background:rgba(0,0,0,0.02)}
.league-table tr.no-memo{color:var(--text-secondary)}
.league-table tr.no-memo .company-name{font-weight:500;color:var(--text-secondary)}
.league-table tr.no-memo td:first-child{color:#ccc}

/* Score pills */
.score-pill{display:inline-flex;align-items:center;padding:2px 10px;border-radius:20px;font-size:13px;font-weight:700;min-width:44px;justify-content:center}
.score-green{background:var(--green-bg);color:var(--green)}
.score-amber{background:var(--amber-bg);color:var(--amber)}
.score-gray{background:var(--gray-bg);color:var(--gray-pill)}

/* Signal pills */
.pill{display:inline-flex;align-items:center;padding:3px 10px;border-radius:20px;font-size:12px;font-weight:600;letter-spacing:0.02em;white-space:nowrap}
.pill-auto{background:var(--green-bg);color:var(--green);border:1px solid var(--green-border)}
.pill-proposal{background:var(--amber-bg);color:var(--amber);border:1px solid var(--amber-border)}
.pill-watch{background:var(--gray-bg);color:var(--gray-pill);border:1px solid var(--gray-border)}

/* Expanded row */
.expanded-content{display:none;background:rgba(0,0,0,0.01)}
.expanded-content.show{display:table-row}
.expanded-inner{padding:32px;display:grid;grid-template-columns:240px 1fr;gap:32px;align-items:start}
.radar-wrap{background:var(--card);border:1px solid var(--border);border-radius:var(--radius-sm);padding:20px;display:flex;align-items:center;justify-content:center}
.radar-wrap canvas{max-width:200px;max-height:200px}
.exec-summary-content{font-size:14px;line-height:1.8;color:var(--text-secondary);text-align:left}
.exec-summary-content h2{font-size:17px;font-weight:700;color:var(--text-primary);margin:16px 0 8px}
.exec-summary-content h3{font-size:15px;font-weight:600;color:var(--text-primary);margin:12px 0 6px}
.exec-summary-content strong{color:var(--text-primary)}
.exec-summary-content blockquote{border-left:3px solid var(--border);padding-left:16px;margin:12px 0;font-style:italic;color:var(--text-secondary)}
.exec-summary-content table{border-collapse:collapse;margin:12px 0;font-size:13px;width:100%}
.exec-summary-content th,.exec-summary-content td{border:1px solid var(--border);padding:6px 10px;text-align:left}
.exec-summary-content th{background:rgba(0,0,0,0.02);font-weight:600}
.exec-summary-content code{background:rgba(0,0,0,0.04);padding:1px 5px;border-radius:3px;font-size:13px}
.exec-summary-content pre{background:rgba(0,0,0,0.03);padding:12px 16px;border-radius:var(--radius-xs);overflow-x:auto;font-size:13px;line-height:1.6;margin:12px 0}
.exec-summary-content pre code{background:none;padding:0}

.view-memo-btn{display:inline-flex;align-items:center;gap:6px;padding:10px 24px;background:var(--text-primary);color:#fff;border:none;border-radius:var(--radius-xs);font-size:14px;font-weight:600;cursor:pointer;margin-top:20px;transition:opacity 0.15s;font-family:var(--font);float:right}
.view-memo-btn:hover{opacity:0.85}

/* ===== MEMO VIEWER ===== */
#memo-viewer{display:none;position:fixed;top:0;left:0;right:0;bottom:0;z-index:1000;background:var(--bg);overflow-y:auto}
#memo-viewer.show{display:block}
.memo-header{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--border);z-index:10;padding:16px 0}
.memo-header-inner{max-width:860px;margin:0 auto;padding:0 40px;display:flex;align-items:center;justify-content:space-between}
.back-btn{display:inline-flex;align-items:center;gap:6px;padding:8px 16px;background:var(--card);border:1px solid var(--border);border-radius:var(--radius-xs);font-size:14px;font-weight:500;cursor:pointer;color:var(--text-primary);transition:all 0.15s;font-family:var(--font)}
.back-btn:hover{background:var(--border)}
.memo-company-name{font-size:16px;font-weight:600;color:var(--text-primary)}
.memo-body{max-width:860px;margin:0 auto;padding:48px 40px 80px}
.memo-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:48px 56px;box-shadow:var(--shadow-md)}
.memo-card h1{font-size:24px;font-weight:800;letter-spacing:-0.02em;margin-bottom:8px;line-height:1.3}
.memo-card h2{font-size:19px;font-weight:700;margin:32px 0 12px;letter-spacing:-0.01em;color:var(--text-primary)}
.memo-card h3{font-size:16px;font-weight:600;margin:24px 0 8px;color:var(--text-primary)}
.memo-card h4{font-size:15px;font-weight:600;margin:20px 0 6px;color:var(--text-primary)}
.memo-card p{margin:8px 0;font-size:15px;line-height:1.8;color:var(--text-secondary)}
.memo-card strong{color:var(--text-primary)}
.memo-card blockquote{border-left:3px solid var(--border);padding:8px 20px;margin:16px 0;background:rgba(0,0,0,0.015);border-radius:0 var(--radius-xs) var(--radius-xs) 0}
.memo-card blockquote p{font-style:italic;font-size:14px;line-height:1.8}
.memo-card ul,.memo-card ol{margin:8px 0;padding-left:24px}
.memo-card li{margin:4px 0;font-size:15px;line-height:1.7;color:var(--text-secondary)}
.memo-card table{border-collapse:collapse;margin:16px 0;font-size:14px;width:100%}
.memo-card th,.memo-card td{border:1px solid var(--border);padding:8px 12px;text-align:left}
.memo-card th{background:rgba(0,0,0,0.02);font-weight:600;font-size:13px}
.memo-card code{background:rgba(0,0,0,0.04);padding:1px 5px;border-radius:3px;font-size:14px}
.memo-card pre{background:rgba(0,0,0,0.03);padding:16px 20px;border-radius:var(--radius-xs);overflow-x:auto;margin:12px 0}
.memo-card pre code{background:none;padding:0;font-size:13px;line-height:1.6}
.memo-card hr{border:none;border-top:1px solid var(--border);margin:32px 0}
.memo-card img{max-width:100%;border-radius:var(--radius-xs)}

/* ===== FOOTER ===== */
.footer{text-align:center;padding:48px 0;color:var(--text-tertiary);font-size:13px;border-top:1px solid var(--border)}

/* ===== ANIMATIONS ===== */
.fade-in{opacity:0;transform:translateY(16px);transition:opacity 0.6s ease,transform 0.6s ease}
.fade-in.visible{opacity:1;transform:translateY(0)}

/* Table sort indicator */
.league-table th.sortable{cursor:pointer;user-select:none}
.league-table th.sortable:hover{color:var(--text-primary)}
.sort-arrow{font-size:10px;margin-left:4px;opacity:0.4}
.league-table th.sort-active .sort-arrow{opacity:1}

/* ===== RESPONSIVE ===== */
@media(max-width:900px){
  .d-grid{grid-template-columns:1fr}
  .case-grid{grid-template-columns:1fr}
  .abcd-grid{grid-template-columns:1fr}
  .engine-layers{max-width:100%}
  .expanded-inner{grid-template-columns:1fr}
  .radar-wrap{max-width:240px;margin:0 auto}
  .container{padding:0 20px}
  .dark-section{padding:32px 20px}
  .memo-card{padding:24px 20px}
  .nav{padding:16px 20px;gap:16px}
  .hero{padding:80px 16px 40px}
  .causal-chain{gap:4px}
  .chain-node{padding:8px 12px;font-size:12px}
  .belief-nav{gap:4px}
  .belief-nav-btn{padding:8px 14px;font-size:13px}
  .matrix-row{grid-template-columns:1fr;gap:8px}
  .league-table .thesis-preview{max-width:120px}
}
@media(max-width:600px){
  .causal-chain{flex-direction:column;gap:0}
  .chain-arrow{transform:rotate(90deg);margin:2px 0}
  .bracket-line{display:none}
  .bracket-label{display:none}
}
</style>
</head>
<body>

<nav class="nav">
  <a href="#belief" onclick="showBeliefPage(0)">投资信念</a>
  <a href="#engine">投资逻辑</a>
  <a href="#league-table">投资榜单</a>
</nav>

<!-- ===== SECTION 1: HERO ===== -->
<section class="hero" id="hero">
  <div class="hero-content">
    <div class="hero-logo">
      <img src="logo.png" alt="αLike Investment">
    </div>
    <h1>好组织 + 好Timing = 好投资</h1>
    <div class="hero-subtitle">
      <p>我们相信，长期回报来自组织，而超额回报来自拐点。</p>
      <p>组织决定战略上限，战略决定业务结果，市场通常最后才看见。</p>
      <p>我们的工作，是在结果显现之前，识别组织生成力与关键拐点。</p>
    </div>
    <div class="chain-wrapper">
      <div class="causal-chain">
        <div class="chain-node">组织变化</div>
        <div class="chain-arrow">→</div>
        <div class="chain-node">战略变化</div>
        <div class="chain-arrow">→</div>
        <div class="chain-node">业务结果</div>
        <div class="chain-arrow">→</div>
        <div class="chain-node">市场定价</div>
      </div>
      <div class="chain-bracket">
        <div class="bracket-line">
          <div class="bracket-label">时间差 = 投资窗口</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ===== SECTION 2: 投资信念 (3 sub-pages) ===== -->
<section class="belief-section" id="belief">
  <div class="container">
    <div class="section-title fade-in">投资信念</div>
    <div class="section-subtitle fade-in">从组织质量到投资机会的三层递进框架</div>

    <div class="belief-nav fade-in">
      <button class="belief-nav-btn active" onclick="showBeliefPage(0)">Winner Pattern</button>
      <button class="belief-nav-btn" onclick="showBeliefPage(1)">Org Inflection</button>
      <button class="belief-nav-btn" onclick="showBeliefPage(2)">Biz Inflection</button>
    </div>

    <!-- Page 2a: Winner Pattern -->
    <div class="belief-page active" id="belief-0">
      <div class="dark-section fade-in">
        <h2><span>Winner Pattern</span>：识别组织生成力</h2>
        <div class="sub-title">这家公司是否具备持续生成正确选择的组织机制？</div>
        <div class="section-intro">
          核心原则只有一条：组织形态应该由"你在造什么东西"倒推出来。如果一家公司的组织和其他公司长得一模一样，这本身就是负面信号。我们不看"有没有做到最佳实践"，而是看"有没有发明别处没见过的组织设计"。
        </div>

        <div class="d-grid">
          <div class="d-card">
            <div class="d-card-header">
              <span class="d-card-id">D1</span>
              <span class="d-card-name">创始人认知</span>
              <span class="d-card-weight">20%</span>
            </div>
            <div class="d-card-question">组织思考是否有"原生性"——在别处没见过的组织设计？</div>
            <div class="d-card-example"><strong>NVIDIA 黄仁勋</strong> T5T + One Architecture + 不看numbers + 60个直接汇报</div>
          </div>
          <div class="d-card">
            <div class="d-card-header">
              <span class="d-card-id">D2</span>
              <span class="d-card-name">Key Leader配置</span>
              <span class="d-card-weight">15%</span>
            </div>
            <div class="d-card-question">联创的互补性可能是预测组织质量最有效的单一指标</div>
            <div class="d-card-example"><strong>Anthropic</strong> 7位联创覆盖全栈——Hausman(DeepMind+Stanford)做基础理论、Finn(Stanford)做桥梁</div>
          </div>
          <div class="d-card">
            <div class="d-card-header">
              <span class="d-card-id">D3</span>
              <span class="d-card-name">考核与激励</span>
              <span class="d-card-weight">15%</span>
            </div>
            <div class="d-card-question">不看公司说什么价值观，看它怎么考核——考核什么，员工就做什么</div>
            <div class="d-card-example"><strong>ElevenLabs</strong> "Kill deal + pay commission"——CEO亲手毙掉可能削弱模型IP壁垒的大deal，但仍然给sales团队发commission</div>
          </div>
          <div class="d-card">
            <div class="d-card-header">
              <span class="d-card-id">D4</span>
              <span class="d-card-name">信息架构</span>
              <span class="d-card-weight">10%</span>
            </div>
            <div class="d-card-question">CEO的判断和一线观察是否在同一通道双向流动？</div>
            <div class="d-card-example"><strong>Anduril</strong> Mission Command——从军事教义借鉴，设定意图不设定指令</div>
          </div>
          <div class="d-card">
            <div class="d-card-header">
              <span class="d-card-id">D5</span>
              <span class="d-card-name">组织熵减</span>
              <span class="d-card-weight">10%</span>
            </div>
            <div class="d-card-question">员工增速是否低于业务增速？好的熵减是结构性的，不是靠周期性大裁员</div>
            <div class="d-card-example"><strong>Cursor</strong> 300人→$2B ARR——人效比SaaS史上最高</div>
          </div>
          <div class="d-card">
            <div class="d-card-header">
              <span class="d-card-id">D6</span>
              <span class="d-card-name">Talent Density</span>
              <span class="d-card-weight">15%</span>
            </div>
            <div class="d-card-question">"最好的人"的定义必须从业务本质出发——没有通用定义</div>
            <div class="d-card-example"><strong>DeepSeek</strong> 招"好奇心强的年轻人"而非"功成名就的大佬"</div>
          </div>
          <div class="d-card">
            <div class="d-card-header">
              <span class="d-card-id">D7</span>
              <span class="d-card-name">Key Bet战略取舍</span>
              <span class="d-card-weight">15%</span>
            </div>
            <div class="d-card-question">战略上有没有极致的取舍？是否all-in在最重要的事上？</div>
            <div class="d-card-example"><strong>Anthropic</strong> 只聚焦coding = 极致取舍。<strong>Perplexity</strong> 同时做8条产品线 = 撒胡椒面</div>
          </div>
        </div>

        <div class="d-closing">
          七维度之上，还有三个核心判断：CEO的组织认知有没有"原生性"？机制有没有被"战役级结果"验证？组织形态和业务本质是否匹配？
        </div>
      </div>
    </div>

    <!-- Page 2b: Org Inflection -->
    <div class="belief-page" id="belief-1">
      <div class="dark-section fade-in">
        <h2><span>Org Inflection</span>：识别组织跃迁</h2>
        <div class="sub-title">组织机制是否正在发生关键跃迁——而市场还没看见？</div>
        <div class="section-intro">
          好组织是必要条件，但不是充分条件。我们还需要看到变化——组织正在变成新的自己。Org Inflection 是 timing 的前因：组织效率提升领先利润率改善6-12个月，CEO认知迭代领先新战略落地12-24个月，人才换血领先产品质变12-18个月。
        </div>

        <div class="case-grid">
          <div class="case-card">
            <h4>Meta：Year of Efficiency</h4>
            <div class="case-highlight">从 87,000人→67,000人 + 关闭 Reality Labs 非核心项目</div>
            <p>组织拐点：2023.Q1。利润率拐点：2023.Q3。股价从$88→$600。市场后知后觉了两个季度。</p>
          </div>
          <div class="case-card">
            <h4>Duolingo：AI-first 静默革命</h4>
            <div class="case-highlight">von Ahn 内部备忘录替代合同工→900人产出$1B营收</div>
            <p>组织拐点：2024.Q1。P/E从120x跌至11x，但人效创历史新高。市场在用增速下滑定价，我们在看组织效率跃迁。</p>
          </div>
          <div class="case-card">
            <h4>TransDigm：三代CEO交接</h4>
            <div class="case-highlight">Howley→Stein→Lisman 30年制度化传承</div>
            <p>AOP期权机制让CEO交接不影响执行纪律。组织拐点：2025.Q4。Lisman首季度完美复刻Howley模式。市场还在用"换CEO=风险"定价。</p>
          </div>
          <div class="case-card">
            <h4>Veeva：PBC制度化 + Hard Working文化重置</h4>
            <div class="case-highlight">Gassner将CEO股权锁定至2030，PBC从治理标签变为招募杠杆</div>
            <p>Vault CRM迁移加速（125+客户上线）。Forward P/E 17.6x = 历史底部。</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Page 2c: Biz Inflection -->
    <div class="belief-page" id="belief-2">
      <div class="dark-section fade-in">
        <h2><span>Biz Inflection</span>：从组织变化到投资机会</h2>
        <div class="sub-title">组织变化是否开始转化为业务拐点与估值重估？</div>
        <div class="section-intro">
          Biz Inflection 不是看增长加速。我们用 ABCD 框架判断业务是否真的发生了结构性变化：
        </div>

        <div class="abcd-grid">
          <div class="abcd-card">
            <div class="abcd-letter">A</div>
            <div class="abcd-name">Asset Quality</div>
            <div class="abcd-question">核心资产是否达到自给自足/规模效应临界点？</div>
            <div class="abcd-example">Netflix原创内容库达到授权独立点 / NVIDIA CUDA生态lock-in</div>
          </div>
          <div class="abcd-card">
            <div class="abcd-letter">B</div>
            <div class="abcd-name">Engine Switch</div>
            <div class="abcd-question">增长引擎是否正在切换——而非只是加速？</div>
            <div class="abcd-example">Netflix DVD→流媒体→广告 / AMD CPU→AI GPU / Broadcom 芯片→芯片+软件</div>
          </div>
          <div class="abcd-card">
            <div class="abcd-letter">C</div>
            <div class="abcd-name">Valuation Safety</div>
            <div class="abcd-question">市场定价是否存在认知差——而非只是便宜？</div>
            <div class="abcd-example">Duolingo P/E 11x（市场定价增速放缓，我们定价效率跃迁）/ Veeva PEG 0.80</div>
          </div>
          <div class="abcd-card">
            <div class="abcd-letter">D</div>
            <div class="abcd-name">Catalyst</div>
            <div class="abcd-question">未来6-12个月有哪些可能改变市场叙事的催化剂？</div>
            <div class="abcd-example">TransDigm aftermarket复苏 + Lisman首个完整财年 / AMD MI450量产</div>
          </div>
        </div>

        <div class="d-closing" style="margin-top:32px">
          最终，αLike 投资的是：组织拐点先于业务拐点，而市场尚未充分定价的公司。
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ===== SECTION 3: 投资逻辑 (Engine) ===== -->
<section class="engine-section section" id="engine">
  <div class="container">
    <div class="section-title fade-in">投资判断引擎</div>
    <div class="section-subtitle fade-in">从300+家公司到最终投资决策</div>

    <div class="engine-layers fade-in">
      <div class="engine-layer">
        <div class="layer-header">
          <div class="layer-number">1</div>
          <div>
            <span class="layer-title">Winner Pattern</span>
            <span class="layer-subtitle">值不值得长期看？</span>
          </div>
        </div>
        <div class="layer-desc">D1-D7 评分 + Fit Score → 从 300+ 家公司中筛选出具备组织生成力的标的</div>
        <div class="layer-detail">
          <span class="layer-tag">D1 创始人认知</span>
          <span class="layer-tag">D2 Leader配置</span>
          <span class="layer-tag">D3 考核激励</span>
          <span class="layer-tag">D4 信息架构</span>
          <span class="layer-tag">D5 组织熵减</span>
          <span class="layer-tag">D6 人才密度</span>
          <span class="layer-tag">D7 战略取舍</span>
        </div>
        <div class="layer-output">→ Alike League Table · 88家已评分</div>
      </div>

      <div class="engine-layer">
        <div class="layer-header">
          <div class="layer-number">2</div>
          <div>
            <span class="layer-title">Org Inflection</span>
            <span class="layer-subtitle">组织有没有开始变化？</span>
          </div>
        </div>
        <div class="layer-desc">识别正在发生组织跃迁的公司——变化尚未被市场定价</div>
        <div class="layer-detail">
          <span class="layer-tag">CEO变化</span>
          <span class="layer-tag">管理层重组</span>
          <span class="layer-tag">文化重置</span>
          <span class="layer-tag">权力迁移</span>
          <span class="layer-tag">激励切换</span>
        </div>
        <div class="layer-output">→ Inflection Candidates</div>
      </div>

      <div class="engine-layer">
        <div class="layer-header">
          <div class="layer-number">3</div>
          <div>
            <span class="layer-title">Biz Inflection</span>
            <span class="layer-subtitle">变化有没有开始传导？</span>
          </div>
        </div>
        <div class="layer-desc">ABCD 框架验证组织变化是否已传导至业务层面</div>
        <div class="layer-detail">
          <span class="layer-tag">A · Asset Quality</span>
          <span class="layer-tag">B · Engine Switch</span>
          <span class="layer-tag">C · Valuation Safety</span>
          <span class="layer-tag">D · Catalyst</span>
        </div>
        <div class="layer-output">→ Signal Engine → 投资决策</div>
      </div>
    </div>

    <!-- Decision Matrix -->
    <div class="decision-matrix fade-in">
      <div class="matrix-row" style="background:rgba(0,0,0,0.02)">
        <div>判断条件</div>
        <div>评级</div>
      </div>
      <div class="matrix-row">
        <div class="matrix-condition">高组织质量 + 强组织拐点 + 初显业务拐点</div>
        <div><span class="pill pill-auto">AUTO-APPLY</span></div>
      </div>
      <div class="matrix-row">
        <div class="matrix-condition">高组织质量 + 拐点证据积累中</div>
        <div><span class="pill pill-proposal">PROPOSAL</span></div>
      </div>
      <div class="matrix-row">
        <div class="matrix-condition">高组织质量 + 无拐点</div>
        <div><span class="pill pill-watch">WATCH</span></div>
      </div>
      <div class="matrix-row">
        <div class="matrix-condition">组织不达标</div>
        <div><span style="font-size:13px;color:var(--text-tertiary);font-weight:500">DISCARD</span></div>
      </div>
    </div>

    <div class="stats-bar fade-in">
      <div class="stat-pill"><span class="pill pill-auto">2 AUTO-APPLY</span></div>
      <div class="stat-pill"><span class="pill pill-proposal">7 PROPOSAL</span></div>
      <div class="stat-pill"><span class="pill pill-watch">3 WATCH</span></div>
    </div>
  </div>
</section>

<!-- ===== SECTION 4: LEAGUE TABLE ===== -->
<section class="section" id="league-table">
  <div class="container">
    <div class="section-title fade-in">投资榜单</div>
    <div class="section-subtitle fade-in">组织质量 × 拐点强度 × 投资吸引力</div>

    <div class="table-filters fade-in" id="table-filters">
      <button class="filter-btn active" data-filter="all">全部 <span style="opacity:0.5;margin-left:2px">88</span></button>
      <button class="filter-btn" data-filter="AUTO-APPLY">Auto-Apply <span style="opacity:0.5;margin-left:2px">2</span></button>
      <button class="filter-btn" data-filter="PROPOSAL">Proposal <span style="opacity:0.5;margin-left:2px">7</span></button>
      <button class="filter-btn" data-filter="WATCH">Watch <span style="opacity:0.5;margin-left:2px">3</span></button>
    </div>

    <div class="fade-in" style="overflow-x:auto">
      <table class="league-table" id="league-tbody-wrap">
        <thead>
          <tr>
            <th>Rk</th>
            <th>Company</th>
            <th class="sortable" data-sort="score">Alike Score <span class="sort-arrow">▼</span></th>
            <th>Fit</th>
            <th>Most Resonant</th>
            <th>Signal</th>
            <th>Memos</th>
          </tr>
        </thead>
        <tbody id="league-tbody">
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- ===== MEMO VIEWER ===== -->
<div id="memo-viewer">
  <div class="memo-header">
    <div class="memo-header-inner">
      <button class="back-btn" onclick="closeMemo()">← 返回榜单</button>
      <div class="memo-company-name" id="memo-title"></div>
    </div>
  </div>
  <div class="memo-body">
    <div class="memo-card" id="memo-content"></div>
  </div>
</div>

<!-- ===== FOOTER ===== -->
<footer class="footer">
  αLike Investment · April 2026
</footer>

<script>
// ===== DATA =====
const DATA = ''' + companies_json + ''';

let currentFilter = 'all';
const chartInstances = {};

function getScoreClass(score) {
  if (score >= 80) return 'score-green';
  if (score >= 60) return 'score-amber';
  return 'score-gray';
}

function getSignalPill(signal) {
  if (signal === 'AUTO-APPLY') return '<span class="pill pill-auto">AUTO-APPLY</span>';
  if (signal === 'PROPOSAL') return '<span class="pill pill-proposal">PROPOSAL</span>';
  if (signal === 'WATCH') return '<span class="pill pill-watch">WATCH</span>';
  return '<span style="color:var(--text-tertiary)">—</span>';
}

function capitalizeResonant(r) {
  if (!r) return '—';
  const map = {
    'nvidia': 'NVIDIA', 'shopify': 'Shopify', 'netflix': 'Netflix',
    'meta': 'Meta', 'anthropic': 'Anthropic', 'pdd': 'PDD',
    'applovin': 'AppLovin'
  };
  return map[r.toLowerCase()] || r.charAt(0).toUpperCase() + r.slice(1);
}

function extractThesis(execSummary) {
  if (!execSummary) return '—';
  const lines = execSummary.split('\\n');
  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed.startsWith('> ')) {
      let thesis = trimmed.substring(2).trim();
      if (thesis.length > 60) thesis = thesis.substring(0, 60) + '...';
      return thesis;
    }
  }
  return '—';
}

function renderTable() {
  const tbody = document.getElementById('league-tbody');
  tbody.innerHTML = '';

  let filtered = DATA;
  if (currentFilter !== 'all') {
    filtered = DATA.filter(c => c.signal === currentFilter);
  }

  filtered.forEach((c, i) => {
    const rank = DATA.indexOf(c) + 1;
    const isClickable = c.has_memos;
    const rowClass = isClickable ? 'clickable' : 'no-memo';
    const thesis = isClickable ? extractThesis(c.exec_summary) : '—';

    const tr = document.createElement('tr');
    tr.className = rowClass;
    tr.dataset.slug = c.slug;
    tr.innerHTML = `
      <td>${rank}</td>
      <td class="company-name">${c.name}</td>
      <td><span class="score-pill ${getScoreClass(c.score)}">${c.score}</span></td>
      <td>${c.fit || '—'}</td>
      <td style="font-size:13px">${capitalizeResonant(c.resonant)}</td>
      <td>${getSignalPill(c.signal)}</td>
      <td class="thesis-preview">${thesis}</td>
    `;

    if (isClickable) {
      tr.addEventListener('click', () => toggleExpand(c.slug));
    }

    tbody.appendChild(tr);

    // Expanded row
    if (isClickable) {
      const expTr = document.createElement('tr');
      expTr.className = 'expanded-content';
      expTr.id = `expand-${c.slug}`;
      expTr.innerHTML = `<td colspan="7"><div class="expanded-inner">
        <div class="radar-wrap"><canvas id="radar-${c.slug}" width="200" height="200"></canvas></div>
        <div>
          <div class="exec-summary-content" id="exec-${c.slug}"></div>
          <button class="view-memo-btn" onclick="event.stopPropagation();openMemo('${c.slug}')">查看全文 →</button>
        </div>
      </div></td>`;
      tbody.appendChild(expTr);
    }
  });
}

function toggleExpand(slug) {
  const row = document.getElementById(`expand-${slug}`);
  if (!row) return;

  const wasVisible = row.classList.contains('show');

  // Close all expanded
  document.querySelectorAll('.expanded-content.show').forEach(el => {
    el.classList.remove('show');
    const s = el.id.replace('expand-', '');
    if (chartInstances[s]) {
      chartInstances[s].destroy();
      delete chartInstances[s];
    }
  });

  if (!wasVisible) {
    row.classList.add('show');
    const company = DATA.find(c => c.slug === slug);
    if (!company) return;

    // Render exec summary
    const execEl = document.getElementById(`exec-${slug}`);
    if (company.exec_summary && execEl.innerHTML === '') {
      execEl.innerHTML = marked.parse(stripFrontmatter(company.exec_summary));
    }

    // Render radar chart
    renderRadar(slug, company.d_scores);
  }
}

function renderRadar(slug, dScores) {
  if (!dScores || Object.keys(dScores).length === 0) return;

  const canvas = document.getElementById(`radar-${slug}`);
  if (!canvas) return;

  const labels = ['D1 CEO认知', 'D2 Leader', 'D3 激励', 'D4 信息', 'D5 熵减', 'D6 人才', 'D7 Key Bet'];
  const values = [dScores.d1||0, dScores.d2||0, dScores.d3||0, dScores.d4||0, dScores.d5||0, dScores.d6||0, dScores.d7||0];

  chartInstances[slug] = new Chart(canvas.getContext('2d'), {
    type: 'radar',
    data: {
      labels: labels,
      datasets: [{
        label: 'D Score',
        data: values,
        backgroundColor: 'rgba(22,163,74,0.08)',
        borderColor: 'rgba(22,163,74,0.6)',
        borderWidth: 2,
        pointBackgroundColor: 'rgba(22,163,74,0.8)',
        pointBorderColor: '#fff',
        pointBorderWidth: 1,
        pointRadius: 3
      }]
    },
    options: {
      responsive: false,
      plugins: { legend: { display: false } },
      scales: {
        r: {
          min: 0, max: 5,
          ticks: { stepSize: 1, font: { size: 10 }, backdropColor: 'transparent', color: '#999' },
          grid: { color: 'rgba(0,0,0,0.06)' },
          angleLines: { color: 'rgba(0,0,0,0.06)' },
          pointLabels: { font: { size: 11, family: '-apple-system,sans-serif' }, color: '#6b6b6b' }
        }
      }
    }
  });
}

// ===== MEMO VIEWER =====
function stripFrontmatter(md) {
  return md.replace(/^---[\\s\\S]*?---\\s*/, '');
}

function openMemo(slug) {
  const company = DATA.find(c => c.slug === slug);
  if (!company || !company.full_memo) return;

  document.getElementById('memo-title').textContent = company.name;
  document.getElementById('memo-content').innerHTML = marked.parse(stripFrontmatter(company.full_memo));
  document.getElementById('memo-viewer').classList.add('show');
  document.body.style.overflow = 'hidden';
  document.getElementById('memo-viewer').scrollTop = 0;
}

function closeMemo() {
  document.getElementById('memo-viewer').classList.remove('show');
  document.body.style.overflow = '';
}

// ===== BELIEF PAGE NAVIGATION =====
function showBeliefPage(idx) {
  document.querySelectorAll('.belief-page').forEach((p, i) => {
    p.classList.toggle('active', i === idx);
  });
  document.querySelectorAll('.belief-nav-btn').forEach((b, i) => {
    b.classList.toggle('active', i === idx);
  });
  // Re-observe fade-in elements in newly visible pages
  document.querySelectorAll('.belief-page.active .fade-in').forEach(el => observer.observe(el));
}

// ===== FILTERS =====
document.getElementById('table-filters').addEventListener('click', e => {
  const btn = e.target.closest('.filter-btn');
  if (!btn) return;
  currentFilter = btn.dataset.filter;
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderTable();
});

// ===== SCROLL ANIMATIONS =====
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

// ===== NAV HIGHLIGHT =====
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav a');
window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(s => {
    const top = s.offsetTop - 100;
    if (window.scrollY >= top) current = s.id;
  });
  navLinks.forEach(a => {
    a.classList.remove('active');
    if (a.getAttribute('href') === '#' + current) a.classList.add('active');
  });
});

// ===== KEYBOARD =====
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeMemo();
});

// ===== INIT =====
renderTable();
</script>
</body>
</html>'''

with open('/home/user/workspace/alike-presentation/index.html', 'w') as f:
    f.write(html)

print(f"Written {len(html)} chars to index.html")
