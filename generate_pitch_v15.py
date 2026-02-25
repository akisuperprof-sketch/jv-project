import re

html_content = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MUI×WCA Joint Venture Platform</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="./assets/design-medical.css">
  <link rel="stylesheet" href="./assets/partner-section.css">
  <link rel="stylesheet" href="./assets/infographic/infographic.css">
  <link rel="stylesheet" href="./assets/competitive-section.css">
  <style>
    :root {
      --bg: #F8FAFC;
      --card: rgba(255, 255, 255, 0.7);
      --border: rgba(0, 0, 0, 0.06);
      --primary: #0284C7;
      --primary-glow: rgba(2, 132, 199, 0.1);
      --success: #059669;
      --text: #1E293B;
      --muted: #64748B;
      --radius: 24px;
      --shadow: 0 10px 40px rgba(0, 0, 0, 0.04);
      --glass: rgba(255, 255, 255, 0.4);
      --accent-blue: #E0F2FE;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Noto Sans JP', sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.6;
      background-image: radial-gradient(circle at 10% 20%, rgba(2, 132, 199, 0.03), transparent 30%), radial-gradient(circle at 90% 80%, rgba(5, 150, 105, 0.02), transparent 30%);
      background-attachment: fixed;
      padding-bottom: 80px; /* Space for the bottom script bar */
    }

    h1 { font-size: 3rem; font-weight: 900; letter-spacing: -0.03em; line-height: 1.2; margin-bottom: 1.5rem; background: linear-gradient(to bottom right, #0F172A, #334155); background-clip: text; -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    h2 { font-size: 1.8rem; font-weight: 800; border-bottom: 2px solid var(--accent-blue); padding-bottom: 0.5rem; margin-bottom: 2rem; color: #0F172A; display: flex; align-items: center; gap: 0.75rem; }
    h3 { font-size: 1.25rem; font-weight: 700; margin-bottom: 0.75rem; color: #334155; }
    p { color: var(--muted); font-size: 0.95rem; margin-bottom: 1rem; }
    
    .container { max-width: 1400px; margin: 0 auto; padding: 2rem; }
    .grid { display: grid; gap: 2rem; }
    .grid-2 { grid-template-columns: repeat(auto-fit, minmax(450px, 1fr)); }
    .grid-3 { grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); }
    .grid-4 { grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
    
    .glass { background: var(--glass); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.8); border-radius: var(--radius); box-shadow: var(--shadow); transition: transform 0.3s ease, box-shadow 0.3s ease; }
    .glass:hover { transform: translateY(-3px); box-shadow: 0 20px 50px rgba(0,0,0,0.06); }
    
    header { display: flex; justify-content: space-between; align-items: center; padding: 1rem 2rem; background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(16px); border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 100; }
    .brand { display: flex; align-items: center; gap: 1rem; font-weight: 900; font-size: 1.2rem; }
    .brand-logo { width: 32px; height: 32px; border-radius: 8px; background: linear-gradient(135deg, var(--primary), var(--success)); }
    
    .btn { font-family: inherit; font-size: 0.85rem; font-weight: 700; padding: 0.75rem 1.5rem; border-radius: 12px; cursor: pointer; transition: all 0.2s ease; border: 1px solid var(--border); background: #fff; color: var(--text); display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; text-decoration: none;}
    .btn.primary { background: var(--primary); border-color: var(--primary); color: #fff; box-shadow: 0 10px 20px var(--primary-glow); }
    .btn.primary:hover { background: #0369A1; transform: translateY(-2px); }
    
    .status-badge { display: inline-block; padding: 4px 10px; border-radius: 100px; font-size: 0.7rem; font-weight: 800; letter-spacing: 0.05em; text-transform: uppercase; }
    .status-assumed { background: #E0F2FE; color: #0284C7; border: 1px solid #BAE6FD; }
    .status-verified { background: #D1FAE5; color: #059669; border: 1px solid #A7F3D0; }
    .status-placeholder { background: #F1F5F9; color: #64748B; border: 1px solid #E2E8F0; }

    /* Number typography emphasis */
    .big-number { font-size: 3rem; font-weight: 900; color: #0F172A; line-height: 1; letter-spacing: -0.05em; display:flex; align-items:baseline; gap:0.2rem; }
    .big-number span { font-size: 1rem; font-weight: 700; color: var(--muted); }
    
    /* Modern Section Spacing */
    .section-spacing { margin-top: 5rem; margin-bottom: 5rem; }
    
    /* Floating Script Bar */
    .script-bar { position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); background: rgba(15, 23, 42, 0.9); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.1); padding: 0.75rem; border-radius: 100px; display: flex; gap: 0.5rem; z-index: 1000; box-shadow: 0 20px 40px rgba(0,0,0,0.2); align-items: center; }
    .script-btn { background: transparent; border: none; color: #fff; font-size: 0.8rem; font-weight: 700; padding: 0.5rem 1rem; border-radius: 100px; cursor: pointer; transition: all 0.2s; }
    .script-btn:hover, .script-btn.active { background: rgba(255,255,255,0.15); }
    .script-title { color: #94A3B8; font-size: 0.7rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; margin-left: 1rem; margin-right: 0.5rem; display: none; }
    @media (min-width: 768px) { .script-title { display: block; } }

    /* Talk Script Panel Overlay */
    .talk-script-panel { position: fixed; bottom: 80px; left: 50%; transform: translateX(-50%) translateY(20px); width: 90%; max-width: 600px; background: rgba(255,255,255,0.95); backdrop-filter: blur(20px); border: 1px solid rgba(0,0,0,0.1); border-radius: 24px; padding: 2rem; box-shadow: 0 30px 60px rgba(0,0,0,0.15); z-index: 999; opacity: 0; pointer-events: none; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); max-height: 70vh; overflow-y: auto; }
    .talk-script-panel.show { opacity: 1; pointer-events: auto; transform: translateX(-50%) translateY(0); }
    .script-text { font-size: 1.05rem; line-height: 1.8; color: #334155; }
    .script-text mark { background: #E0F2FE; color: #0284C7; padding: 0.1rem 0.3rem; border-radius: 4px; font-weight: 700; }
    
    /* Image Wrappers */
    .img-wrap { width: 100%; height: 100%; object-fit: cover; border-radius: calc(var(--radius) - 2px); }
  </style>
</head>
<body>

  <header>
    <div class="brand">
      <div class="brand-logo"></div>
      Air Data Infrastructure (MUI × WCA)
    </div>
    <div style="font-size: 0.8rem; font-weight: 800; color: var(--primary); background: var(--accent-blue); padding: 4px 12px; border-radius: 100px;">v1.5.0 (Investor DD Edition)</div>
  </header>

  <div class="container section-spacing">
    <!-- 1. HERO / VISION -->
    <section class="page-break" style="margin-bottom: 5rem;">
      <div class="glass" style="padding: 4rem; position: relative; overflow: hidden; background: #fff;">
        <div style="position: absolute; top: -50%; left: -50%; width: 100%; height: 100%; background: radial-gradient(circle, rgba(2, 132, 199, 0.05) 0%, transparent 70%);"></div>
        <div class="grid grid-2" style="align-items: center;">
          <div style="position: relative; z-index: 2;">
            <div style="display:inline-block; padding:0.4rem 1rem; background:var(--accent-blue); color:var(--primary); font-size:0.75rem; font-weight:800; border-radius:100px; margin-bottom:1.5rem; text-transform: uppercase;">Category Creation (Data Infrastructure)</div>
            <h1>空気をデータに変え、<br>社会インフラを定義する。</h1>
            <p style="font-size: 1.15rem; color: #475569; margin-bottom: 2rem;">
              高度センシングの「MUI」 × 医療グレード改善の「WCA」。<br>
              単なる空気清浄機メーカーではなく、「測定→改善→証明」をワンストップで提供する世界初の空間データSaaS企業を創求します。
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
              <span class="status-badge status-verified" style="font-size: 0.85rem; padding: 8px 16px;">✓ 医療グレード浄化 (Medical Purity)</span>
              <span class="status-badge status-verified" style="font-size: 0.85rem; padding: 8px 16px;">✓ ブロックチェーン級証跡 (Data Evidence)</span>
            </div>
          </div>
          <div style="position: relative; z-index: 2; height: 100%; min-height: 400px; border-radius: var(--radius); overflow: hidden; border: 1px solid var(--border);">
            <img src="./assets/img/infographic_v15_cycle.png" alt="Measure Improve Certify Cycle" class="img-wrap" style="object-fit: contain; padding: 2rem; background: #F8FAFC;">
          </div>
        </div>
      </div>
    </section>

    <!-- 2. BUSINESS MODEL / ECONOMICS (3 Min Understanding) -->
    <section class="section-spacing page-break">
      <h2>ビジネスモデルの優位性とユニットエコノミクス（Business Economics）</h2>
      <p style="margin-bottom: 2rem; font-size: 1.1rem;">ハードウェアの圧倒的優位をフックに、高収益SaaSへ繋ぐ「三段ロケット」モデル。</p>
      
      <div class="grid grid-3">
        <!-- Step 1 -->
        <div class="glass" style="padding: 2.5rem; background: #fff; position: relative;">
          <div style="position:absolute; top:-15px; left:20px; background:#0F172A; color:#fff; font-size:0.8rem; font-weight:900; padding:6px 12px; border-radius:8px;">STAGE 1</div>
          <h3 style="margin-top: 1rem;">機器販売（Hardware）</h3>
          <p>Ion Cluster × Sensing Nano Techによる高単価機器販売。</p>
          <div style="margin-top: auto; padding-top: 1.5rem; border-top: 1px dashed var(--border);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:0.85rem; font-weight:700;">想定粗利</span>
              <span style="font-size:1.5rem; font-weight:900; color:var(--primary);">30<span style="font-size:1rem">%</span></span>
            </div>
          </div>
        </div>
        
        <!-- Step 2 -->
        <div class="glass" style="padding: 2.5rem; background: #fff; position: relative;">
          <div style="position:absolute; top:-15px; left:20px; background:var(--primary); color:#fff; font-size:0.8rem; font-weight:900; padding:6px 12px; border-radius:8px;">STAGE 2 (Core)</div>
          <h3 style="margin-top: 1rem;">監視SaaS（Subscription）</h3>
          <p>ダッシュボード提供によるリアルタイム監視と月次レポート。</p>
          <div style="margin-top: auto; padding-top: 1.5rem; border-top: 1px dashed var(--border);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:0.85rem; font-weight:700;">想定粗利</span>
              <span style="font-size:1.5rem; font-weight:900; color:var(--primary);">80<span style="font-size:1rem">%+</span></span>
            </div>
          </div>
        </div>

        <!-- Step 3 -->
        <div class="glass" style="padding: 2.5rem; background: #fff; position: relative;">
          <div style="position:absolute; top:-15px; left:20px; background:var(--success); color:#fff; font-size:0.8rem; font-weight:900; padding:6px 12px; border-radius:8px;">STAGE 3</div>
          <h3 style="margin-top: 1rem;">データ資産（Data API & ESG）</h3>
          <p>蓄積した環境スコアの第三者提供、不動産価値向上（WELL認証等）支援。</p>
          <div style="margin-top: auto; padding-top: 1.5rem; border-top: 1px dashed var(--border);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:0.85rem; font-weight:700;">想定粗利</span>
              <span style="font-size:1.5rem; font-weight:900; color:var(--primary);">95<span style="font-size:1rem">%+</span></span>
            </div>
          </div>
        </div>
      </div>

      <!-- Unit Economics -->
      <div class="glass" style="margin-top: 2rem; padding: 3rem; background: linear-gradient(to right, #ffffff, #F8FAFC);">
        <h3 style="margin-bottom: 2rem;">Unit Economics <span class="status-badge status-assumed" style="margin-left: 1rem;">Assumed Data</span></h3>
        <div class="grid grid-3" style="align-items: center;">
          <div>
            <div style="font-size: 0.8rem; font-weight: 700; color: var(--muted); text-transform: uppercase;">一顧客生涯価値 (LTV)</div>
            <div class="big-number">570<span>万円</span></div>
            <p style="font-size: 0.8rem; margin-top: 0.5rem;">契約期間 10年想定 (機器+SaaS)</p>
          </div>
          <div style="text-align: center; color: var(--border);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" style="opacity:0.5;">
              <line x1="12" y1="5" x2="12" y2="19"></line>
            </svg>
          </div>
          <div>
            <div style="font-size: 0.8rem; font-weight: 700; color: var(--muted); text-transform: uppercase;">顧客獲得単価 (CAC)</div>
            <div class="big-number" style="color: var(--success);">9〜18<span>万円</span></div>
            <p style="font-size: 0.8rem; margin-top: 0.5rem;">代理店経由〜直接営業</p>
          </div>
        </div>
        <div style="margin-top: 2rem; padding-top: 2rem; border-top: 1px solid var(--border); display: flex; align-items: center; justify-content: space-between;">
          <div style="font-weight: 800; font-size: 1.1rem;">LTV / CAC Ratio (投資効率)</div>
          <div style="font-size: 2rem; font-weight: 900; color: var(--primary);">31.6<span style="font-size: 1rem;">x</span> <span style="font-size: 0.8rem; font-weight: 700; background: var(--success); color: #fff; padding: 4px 8px; border-radius: 6px; vertical-align: middle;">世界的SaaS基準(3x)を大幅超過</span></div>
        </div>
      </div>
    </section>

    <!-- 3. MARKET & BUDGET (Where to win) -->
    <section class="section-spacing page-break">
      <h2>ターゲット市場と置き換え予算（Target Market & Budget）</h2>
      <div class="grid grid-3">
        
        <!-- Medical / Dental -->
        <div class="glass" style="padding: 0; overflow: hidden; display: flex; flex-direction: column; background: #fff;">
          <div style="height: 180px; position: relative;">
            <img src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?q=80&w=800&auto=format&fit=crop" alt="Medical Clinic" class="img-wrap" style="border-radius: 0;">
            <div style="position: absolute; bottom: 1rem; left: 1rem; background: rgba(0,0,0,0.7); color: #fff; padding: 4px 12px; border-radius: 4px; font-weight: 800; font-size: 0.8rem;">Phase 1: 歯科・医院</div>
          </div>
          <div style="padding: 2rem; flex: 1; display: flex; flex-direction: column;">
            <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">院内運用＆コンプラ予算</h3>
            <p style="font-size: 0.85rem; flex: 1;">患者・スタッフの感染症対策（Pain）に対し、「見えない不安」を証明データで排除（Gain）。</p>
            <div class="status-badge status-verified">Verified (12院PoC済)</div>
          </div>
        </div>

        <!-- Factory / Lab -->
        <div class="glass" style="padding: 0; overflow: hidden; display: flex; flex-direction: column; background: #fff;">
          <div style="height: 180px; position: relative;">
            <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=800&auto=format&fit=crop" alt="High Tech Factory" class="img-wrap" style="border-radius: 0;">
            <div style="position: absolute; bottom: 1rem; left: 1rem; background: rgba(0,0,0,0.7); color: #fff; padding: 4px 12px; border-radius: 4px; font-weight: 800; font-size: 0.8rem;">Phase 2: 工業・3Dプリント</div>
          </div>
          <div style="padding: 2rem; flex: 1; display: flex; flex-direction: column;">
            <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">VOC・臭気対策予算</h3>
            <p style="font-size: 0.85rem; flex: 1;">安衛法対応の大型局所排気（数百万単位の工事）を、スマート機器分散配置で代替しコスト半減。</p>
            <div class="status-badge status-placeholder">Placeholder</div>
          </div>
        </div>

        <!-- ESG / Building -->
        <div class="glass" style="padding: 0; overflow: hidden; display: flex; flex-direction: column; background: #fff;">
          <div style="height: 180px; position: relative;">
            <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=800&auto=format&fit=crop" alt="Data Dashboard" class="img-wrap" style="border-radius: 0;">
            <div style="position: absolute; bottom: 1rem; left: 1rem; background: rgba(0,0,0,0.7); color: #fff; padding: 4px 12px; border-radius: 4px; font-weight: 800; font-size: 0.8rem;">Phase 3: 不動産・スマートビル</div>
          </div>
          <div style="padding: 2rem; flex: 1; display: flex; flex-direction: column;">
            <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">ESG認証・環境監査費用</h3>
            <p style="font-size: 0.85rem; flex: 1;">手動で行っているWELL認証等の監査プロセスを、24時間API連携で自動化。不動産価値の証拠に。</p>
            <div class="status-badge status-assumed">Assumed</div>
          </div>
        </div>

      </div>
    </section>

    <!-- 4. COMPETITIVE POSITIONING (Integration of old A+C) -->
    <section class="section-spacing page-break">
      <h2>ポジショニングと勝機（Competitive Framing & Edge）</h2>
      <div class="comp-table-wrapper" style="box-shadow: var(--shadow); background:#fff;">
        <table class="comp-table">
          <thead>
            <tr>
              <th>市場プレイヤー (Category)</th>
              <th>提供価値 (Value Proportions)</th>
              <th>当プロジェクトの優位性 (Our Edge)</th>
              <th style="width: 140px;">戦略スタンス</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>BMS (Building Management)</strong><br><span style="font-size:0.75rem; color:var(--muted); font-weight:normal;">大手空調・センサー設備</span></td>
              <td>建物全体のマクロな空冷・温度管理</td>
              <td>医療レベルの微細ウイルス・有害ガス対応データのAPI供給</td>
              <td><span class="status-badge status-placeholder" style="background:#F3F4F6;">🤝 連携 (Partner)</span></td>
            </tr>
            <tr>
              <td><strong>IAQ Dashboards</strong><br><span style="font-size:0.75rem; color:var(--muted); font-weight:normal;">空気質モニター単体</span></td>
              <td>「現状が見える化」するが解決能力なし</td>
              <td>清浄化機能(Improve)と連動した統合UI。アクション完結。</td>
              <td><span class="status-badge status-verified" style="background:#E0F2FE; color:var(--primary);">⚔️ 勝負 (Win)</span></td>
            </tr>
            <tr>
              <td><strong>High-end Purifiers</strong><br><span style="font-size:0.75rem; color:var(--muted); font-weight:normal;">高級空気清浄機</span></td>
              <td>硬件売り切り。コンプライアンス証跡に残らない</td>
              <td>常時クラウド接続。データ資産化によるLTVと継続的な監査レポート</td>
              <td><span class="status-badge status-verified" style="background:#E0F2FE; color:var(--primary);">⚔️ 勝負 (Win)</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 5. FUNDING & EXIT ROADMAP -->
    <section class="section-spacing page-break">
      <h2>調達・出口戦略（Funding & Exit Roadmap）</h2>
      <div class="grid grid-2" style="align-items: stretch;">
        <div class="glass" style="padding: 3rem; background: #fff;">
          <h3 style="display:flex; justify-content:space-between; align-items:center;">
            <span>Series A 調達目標額</span>
            <span class="status-badge status-placeholder">Placeholder</span>
          </h3>
          <div class="big-number" style="margin: 1.5rem 0;">10.0<span>億円</span></div>
          <div style="font-size: 0.85rem; margin-bottom: 1rem; color: var(--muted); font-weight: 700;">資金使途 (Use of Funds)</div>
          <div style="display:flex; align-items:center; gap:1.5rem; margin-bottom:1rem;">
            <div style="flex:1; height:16px; background:#F1F5F9; border-radius:8px; overflow:hidden;">
              <div style="width:40%; height:100%; background:var(--primary);"></div>
            </div>
            <span style="font-size:0.85rem; font-weight:700; width:80px;">R&D (40%)</span>
          </div>
          <div style="display:flex; align-items:center; gap:1.5rem; margin-bottom:1rem;">
            <div style="flex:1; height:16px; background:#F1F5F9; border-radius:8px; overflow:hidden;">
              <div style="width:30%; height:100%; background:var(--success);"></div>
            </div>
            <span style="font-size:0.85rem; font-weight:700; width:80px;">量産 (30%)</span>
          </div>
          <div style="display:flex; align-items:center; gap:1.5rem;">
            <div style="flex:1; height:16px; background:#F1F5F9; border-radius:8px; overflow:hidden;">
              <div style="width:30%; height:100%; background:#64748B;"></div>
            </div>
            <span style="font-size:0.85rem; font-weight:700; width:80px;">営業拡販 (30%)</span>
          </div>
        </div>
        
        <div class="glass" style="padding: 3rem; background: linear-gradient(135deg, #0F172A, #1E293B); color: #fff;">
          <h3 style="color: #38BDF8; font-size: 1.5rem;">Exit Strategy <span class="status-badge status-assumed" style="float:right; border-color:rgba(255,255,255,0.2); color:#fff; background:rgba(255,255,255,0.1);">Assumed</span></h3>
          <p style="color: rgba(255,255,255,0.8); margin-bottom: 2rem;">6〜8年後の事業価値の最大化（IPO または グローバルM&A）</p>
          
          <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 2rem; border-radius: 16px;">
            <div style="font-size: 0.85rem; color: #94A3B8; font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase;">推定企業価値 (Valuation Target)</div>
            <div class="big-number" style="color: #fff;">150〜250<span>億円</span></div>
            <ul style="margin-top: 1.5rem; padding-left: 1.2rem; font-size: 0.9rem; color: #E2E8F0; gap: 0.5rem; display: flex; flex-direction: column;">
              <li>世界最大級の安全空間DB構築による参入障壁</li>
              <li>SaaSマルチプル（ARRの10x〜15x）適用</li>
              <li>海外（北米/アジア）での商用利用規格化</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
    
    <!-- EVIDENCE TRAIL (SaaS Style) -->
    <section class="section-spacing page-break">
      <h2 style="font-size: 1.4rem;">☑ データ根拠プロトコル（Evidence Trail System）</h2>
      <div class="evidence-block" style="background: #111827;">
        <div>
          <span class="evidence-col-1">[Metric_Name]</span>
          <span class="evidence-col-2">[LedgerID]</span>
          <span class="evidence-col-3">[SSOT_Source_Ref]</span>
          <span class="evidence-col-4">[Status]</span>
          <span class="evidence-col-5">[Updated]</span>
        </div>
        <div>
          <span class="evidence-col-1">Medical IoT IP</span>
          <span class="evidence-col-2">LEGAL-010</span>
          <span class="evidence-col-3">./03_data/legal/patent_filing.pdf</span>
          <span class="evidence-col-4" style="color:#A7F3D0;">Verified</span>
          <span class="evidence-col-5">26-02-20</span>
        </div>
        <div>
          <span class="evidence-col-1">CAC Calculation</span>
          <span class="evidence-col-2">BUDGET-001</span>
          <span class="evidence-col-3">./03_data/assumptions/calc.xlsx</span>
          <span class="evidence-col-4" style="color:#FDE047;">Assumed</span>
          <span class="evidence-col-5">26-02-25</span>
        </div>
        <div style="margin-top:1rem; border-top: 1px dashed rgba(255,255,255,0.2); padding-top: 1rem; color: #94A3B8; font-size: 0.8rem;">
          > All parameters linked to Single Source of Truth (SSOT). Investor DD room ready.
        </div>
      </div>
    </section>

  </div> <!-- Container End -->

  <!-- ============================================== -->
  <!-- INTERNAL TALK SCRIPT SYSTEM                    -->
  <!-- ============================================== -->
  
  <div class="script-bar">
    <span class="script-title">Speaker Notes</span>
    <button class="script-btn" onclick="toggleScript('script-90s', this)">90秒 エレベーター</button>
    <button class="script-btn" onclick="toggleScript('script-5m', this)">5分 ピッチ</button>
    <button class="script-btn" onclick="toggleScript('script-15m', this)">15分 フル詳細</button>
    <button class="script-btn" onclick="closeAllScripts()" style="margin-left:auto; background:rgba(239, 68, 68, 0.2); color:#FCA5A5;">✕ 閉じる</button>
  </div>

  <div id="script-90s" class="talk-script-panel">
    <h3 style="color:var(--primary); margin-bottom:1rem; border-bottom:1px solid var(--border); padding-bottom:0.5rem;">⏱ 90秒 エレベーターピッチ</h3>
    <p class="script-text">
      「今、非常に面白いプロジェクトが動いてるんです。<strong>『センシングのMUI』と『空間改善のWCA』が組んで、世界の空気データインフラ企業を作る</strong>話です。<br><br>
      最初は、命や健康に直結するドメイン（歯科医院や精密工場）に特化して医療グレードの機器とセンサーを売ります。彼らの強みは、初期の物販で終わらず<mark>『空間の監視SaaS』</mark>と<mark>『ESG等のデータライセンス』</mark>の三段ロケットで収益化する点です。<br><br>
      一度導入されれば『空気清浄の証拠』が取れるため、解約されにくい強固なLTV（約570万）を構築できます。将来的なIPO（150~250億規模）やグローバルM&Aを狙っています。一度、具体的に話を聞いてみませんか？」
    </p>
  </div>

  <div id="script-5m" class="talk-script-panel">
    <h3 style="color:var(--success); margin-bottom:1rem; border-bottom:1px solid var(--border); padding-bottom:0.5rem;">⏱ 5分 ショートピッチ（面談導入）</h3>
    <p class="script-text">
      「我々は単なる空気清浄機を売る会社ではありません。<strong>空気を情報に変え、空間の安全性を証明する『データインフラ企業』です。</strong><br><br>
      課題は、『空気の安全性が見えない』ことです。院内感染や工場の歩留まり低下、あるいはESGの健康認証において、誰も『今の空気が安全だ』と証明できません。そこで、高精度センシングのMUIと、医療浄化力のあるWCAがJVを組みました。<br><br>
      我々のコアは<mark>Measure（測る）→ Improve（直す）→ Certify（証明する）</mark>のサイクルです。競合の多くはBMS（大規模空調）や、測るだけの安価なセンサー、もしくは証跡の残らない高級清浄機です。我々は『測って直して、クラウドで監査証跡を出す』ニッチかつ必須のポジショニングを取ります。<br><br>
      ビジネスモデルは強力です。ハード売切りで終わらず、SaaS契約での継続収益（粗利80%）と、データ資産提供（粗利95%）へ展開します。米国歯科ネットワークや工業特区を皮切りに、LTV/CAC比率 30倍以上というSaaS基準を大きく上回る効率で拡大し、6~8年でIPOを狙う計画です。」
    </p>
  </div>

  <div id="script-15m" class="talk-script-panel">
    <h3 style="color:var(--text); margin-bottom:1rem; border-bottom:1px solid var(--border); padding-bottom:0.5rem;">⏱ 15分 フルプレゼンテーション（要旨）</h3>
    <p class="script-text" style="font-size: 0.95rem;">
      <strong>1. 導入 (Why Now)</strong><br>
      ESG、健康経営、感染症リスクの観点から、室内空気質(IAQ)への投資は「コスト」から「コンプライアンス要件」に変化しています。しかし、それを「実データで証明」できるプラットフォームが存在しません。<br><br>
      
      <strong>2. ソリューション (Measure/Improve/Certify)</strong><br>
      MUIの「Electronic Nose」による空間解析と、WCAの「Ion Cluster」による99.9%空間浄化をシステム統合します。競合のBMS等の大規模工事とは異なり、後付けで「医療グレードの浄化と監査データ」を提供します。<br><br>

      <strong>3. ユニットエコノミクスと予算 (Where is the money)</strong><br>
      我々がリプレイスするのは「清浄機の買い替え予算」ではなく、歯科では「コンプラ維持費」、工場では「高額なダクト工事費」、不動産では「WELL認証等の監査外注費」です。LTV 570万円に対しCAC 18万円（代理店利用で9万）という圧倒的な資本効率を実現します。<br><br>

      <strong>4. 防御力とMoat (Why Us)</strong><br>
      大手家電メーカー参入リスクに対しては「医療特化の認証API網（ESG/ADA連携済）」で防御します。ハードは真似できても「世界中の空間の安全性を証明するデータベース」は真似できません。<br><br>

      <strong>5. 今後の展開 (Roadmap & Ask)</strong><br>
      現在Phase 1（有償PoC 12院済）から、Phase 2（量産・SaaS展開）へ移行します。そのための成長資金として10億円（R&D、量産、拡販）の調達を予定し、数年内のグローバル展開・Exitを見込んでいます。
    </p>
  </div>

  <script>
    function toggleScript(id, btnRef) {
      document.querySelectorAll('.talk-script-panel').forEach(p => p.classList.remove('show'));
      document.querySelectorAll('.script-btn').forEach(b => b.classList.remove('active'));
      const target = document.getElementById(id);
      if(target) {
        target.classList.add('show');
        btnRef.classList.add('active');
      }
    }
    function closeAllScripts() {
      document.querySelectorAll('.talk-script-panel').forEach(p => p.classList.remove('show'));
      document.querySelectorAll('.script-btn').forEach(b => b.classList.remove('active'));
    }
  </script>

</body>
</html>
