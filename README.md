# Assetique Demo
> **Make your boutique become the true asset**

## 展示網頁鏈結: 
[點此開啟 Assetique Demo 網頁]   
https://www.camtop.net/Assetique/

## 🏷️ 專案簡介
Assetique 是一個高價值動產 RWA（Real World Assets）交易與金融平台的展示網頁，專注於奢侈品資產的數位化、認證、交易與流動性管理。

![Platform Preview](https://img.shields.io/badge/Status-Demo-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## 📋 專案概述

Assetique 平台提供完整的奢侈品資產管理生態系統，包含：

- **資產認證與 NFT 化**：實體奢侈品的專業鑑定與區塊鏈數位化
- **二級市場交易**：提供安全透明的拍賣與交易機制
- **資產抵押借貸**：基於資產等級的即時流動性解決方案
- **市場數據分析**：即時趨勢追蹤與產業洞察

## ✨ 核心功能

### 1. **Home（首頁）**
- 平台趨勢儀表板
  - 熱門商品輪播
  - 最高成交價紀錄
  - 搜尋趨勢排行
- 產業新聞與市場洞察
- 全局搜尋功能

### 2. **My Assets（我的資產）**
管理個人奢侈品資產組合，支援多種狀態追蹤：

- **🔍 鑑定中（Authentication in Progress）**
  - 物流追蹤
  - 鑑定進度可視化
  - 從運送到 NFT 鑄造的完整流程

- **💎 收藏中（In Collection）**
  - 保險櫃儲存資訊
  - NFT 與鑑定報告查看
  - 一鍵上架拍賣

- **🎯 拍賣中（Listed for Auction）**
  - 即時競標狀態
  - 取消拍賣功能

- **🏦 質押中（Staked）**
  - 借貸細節追蹤
  - 還款進度管理

### 3. **Market（市場）**
- 多品類奢侈品展示（包包、手錶、珠寶、其他收藏品）
- 即時搜尋與篩選
- 資產等級標示
- 一鍵購買功能

### 4. **Lending（借貸協議）**
基於資產等級的智能借貸系統：
- **Grade A**：LTV 80%（最優質資產）
- **Grade B**：LTV 60%（優良資產）
- **Grade C**：LTV 30%（標準資產）

支援即時流動性釋放，無需出售資產。


## 📁 檔案結構

```
.
├── Assetique Demo網頁.html    # 主要展示頁面（單一檔案應用）
└── README.md                   # 專案說明文件
```

## 🚀 快速開始

### 方法 1：直接開啟
雙擊 `Assetique Demo網頁.html` 即可在瀏覽器中開啟。

### 方法 2：本地伺服器
```bash
# 使用 Python 啟動本地伺服器
python -m http.server 8000

# 或使用 Node.js
npx http-server -p 8000
```

然後在瀏覽器開啟 `http://localhost:8000`

## 📱 功能演示

### 資產認證流程
1. 用戶提交實體奢侈品
2. 物流追蹤（Shipping → Arrived）
3. 專業鑑定（AI + 人工雙重驗證）
4. 生成鑑定報告
5. 保險櫃儲存
6. 鑄造 NFT

### 搜尋功能
- **全局搜尋**：從任何頁面搜尋，自動跳轉到市場頁面
- **市場篩選**：支援品類篩選（Bags / Watches / Jewelry / Others）
- **即時搜尋**：輸入關鍵字即時過濾結果

### 借貸流程
1. 選擇可質押資產
2. 系統根據等級計算 LTV
3. 即時獲得 USDM 穩定幣
4. 追蹤還款進度
5. 完成還款後贖回資產

## 🔐 資產等級系統

| 等級 | 條件 | LTV | 顏色標示 |
|------|------|-----|----------|
| **A** | 完美狀態 + 完整文件 + 高流動性 | 80% | 🟢 綠色 |
| **B** | 良好狀態 + 部分文件 + 中流動性 | 60% | 🟡 黃色 |
| **C** | 標準狀態 + 基本驗證 + 標準流動性 | 30% | 🔴 紅色 |

## 📊 示範數據

### 市場商品（16 項）
- **包包**：Hermès Birkin, Chanel Classic Flap, Lady Dior, LV Capucines
- **手錶**：Rolex Daytona, Patek Nautilus, AP Royal Oak, Omega Speedmaster
- **珠寶**：Cartier Love, Tiffany Solitaire, VCA Alhambra, Bulgari Serpenti
- **其他**：Macallan 1926, KAWS Companion, Rothko Print, Dom Pérignon

### 用戶資產組合
- 總資產價值：$142,500 USDM
- 包含 4 項資產，涵蓋認證、收藏、拍賣、質押等不同狀態

## 🌐 外部資源連結

### 產業新聞來源
- [JP Morgan - Luxury Market Insights](https://www.jpmorgan.com/insights/global-research/retail/luxury-market)
- [Fashion Network - Luxury M&A Report](https://uk.fashionnetwork.com/)
- [Medium - Luxury Fashion Sustainability](https://medium.com/)


## 🎯 目標用戶

- **收藏家**：需要資產認證與保值管理
- **投資者**：尋求另類資產投資機會
- **奢侈品擁有者**：需要短期流動性但不想出售資產
- **交易商**：專業二級市場參與者

## 🔮 未來規劃

- [ ] 整合實際區塊鏈（Cardano）
- [ ] 實現真實的 NFT 鑄造功能
- [ ] 接入真實拍賣引擎
- [ ] 串接真實支付系統
- [ ] 多語言支援（中文/英文）
- [ ] 手機 App 開發

## 📄 授權

本專案為展示用途，版權歸 Assetique / 凱拓科技所有。

## 👥 團隊

開發團隊：凱拓科技 Camtop

## 📞 聯絡方式

email:
camtop.solutions@gmail.com

---

**Made with ❤️ for the luxury asset community**
