# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Assetique** is a luxury asset RWA (Real World Asset) trading and financial platform demo. The tagline is "Make your boutique become the true asset." The platform enables users to tokenize, trade, and leverage high-value physical assets (luxury bags, watches, jewelry) through NFTs and DeFi mechanisms on the Cardano blockchain.

## Architecture

This is a prototype demo consisting of two main components:

### 1. Frontend Demo (`Demo網頁.html` and `預備素材.html`)

Two HTML files that demonstrate the platform's UI/UX:

- **Demo網頁.html**: Main production demo with full functionality
  - Single-page application using vanilla JavaScript
  - Navigation tabs: 首頁 (Home), 我的資產 (My Assets), 商城 (Market), 質押借貸 (Lending)
  - Modals for NFT reports, auction listings, and loan details

- **預備素材.html**: Preliminary material/prototype version with simplified UI

**Key Frontend Features:**

- **Home Tab**: Platform trends dashboard with carousels showing active items and highest price transactions, industry news feed with real external links
- **My Assets Tab**: User portfolio showing assets in different states (鑑定中/identifying, 收藏中/collecting, 上架拍賣中/listing, 質押中/staking) with progress tracking timelines
- **Market Tab**: Marketplace grid with 16 items across 4 categories (bag/watch/jewelry/other), client-side search and filtering
- **Lending Tab**: Liquidity protocol interface showing available assets for staking with LTV ratios based on grade (A: 80%, B: 60%, C: 30%)

**Tech Stack:**
- Tailwind CSS via CDN for styling
- Font Awesome 6.4.0 for icons
- Google Fonts: Inter (sans-serif), Playfair Display (serif)
- Custom glass-morphism design system with brand colors:
  - Dark: #0B1121
  - Primary: #1E293B / #151E32
  - Gold: #D4AF37
  - Accent: #0EA5E9 / #3B82F6

**Data Flow:**
- All data is hardcoded in JavaScript arrays within the HTML files
- No external API calls or backend integration in the HTML demos
- Client-side state management through vanilla JS DOM manipulation

### 2. Backend API (`Test(建立一個簡易後台網頁).py`)

A minimal FastAPI backend serving as a calculator API (appears to be a placeholder/test backend):

**Endpoints:**
- `GET /` - Root welcome message
- `GET /add/{a}/{b}` - Addition
- `GET /subtract/{a}/{b}` - Subtraction
- `GET /multiply/{a}/{b}` - Multiply
- `GET /divide/{a}/{b}` - Division with zero-check

**Running the Backend:**
```bash
python Test\(建立一個簡易後台網頁\).py
```

The server runs on `127.0.0.1:8000` with Swagger UI available at `/docs`.

## Development Environment

- **Python Environment**: Conda is the default environment and package manager (see `.vscode/settings.json`)
- **Language**: Chinese (Traditional) is the primary language for UI text and comments
- **Platform Target**: Web browsers (HTML/CSS/JS frontend)

## Asset Lifecycle States

Understanding the asset states is crucial when working with the platform logic:

1. **鑑定中 (Identifying)**: Asset is being authenticated with a 6-stage progress pipeline (物流配送 → 抵達檢定商 → 鑑定中 → 查看報告 → 入庫保管 → 生成NFT)
2. **收藏中 (Collecting)**: Authenticated asset stored in vault, can view NFT/report or list for auction
3. **上架拍賣中 (Listing)**: Asset listed on marketplace, can be delisted
4. **質押中 (Staking)**: Asset used as collateral for a loan with loan details tracking

## Business Rules

### Lending/LTV Calculation
Assets are graded (A/B/C), which determines Loan-to-Value ratio:
- **Grade A**: 80% LTV
- **Grade B**: 60% LTV
- **Grade C**: 30% LTV

### Asset Grading
Higher grades (A+, A) indicate better condition and command higher prices and LTV ratios.

## File Naming Convention

File names use Chinese characters and may include parentheses. When working with these files in command-line tools, always escape or quote the paths properly:

```bash
# Correct
python "Test(建立一個簡易後台網頁).py"

# Incorrect
python Test(建立一個簡易後台網頁).py
```

## Integration Points

Currently, the HTML frontend and Python backend are **not connected**. The HTML files operate entirely client-side with hardcoded data. Future integration would require:

1. Converting the Python backend to serve relevant endpoints (asset listing, authentication, NFT minting, loan calculations)
2. Replacing hardcoded JavaScript data arrays with API calls
3. Implementing Cardano blockchain integration for NFT minting and smart contracts
4. Adding wallet connection functionality (currently shows mock wallet address `0x8A...92B1`)

## Design System

The platform uses a luxury-focused dark theme with gold accents:

- **Typography**: Serif fonts (Playfair Display) for headings/luxury feel, sans-serif (Inter) for body text
- **Glass-morphism**: Panels use backdrop-blur and semi-transparent backgrounds
- **Animations**: Fade-in transitions, carousel auto-rotation, hover scale effects
- **Responsive**: Mobile-first with breakpoints for md/lg screens

## External Resources

The frontend relies on external CDNs:
- Tailwind CSS: `https://cdn.tailwindcss.com`
- Font Awesome: `https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css`
- Google Fonts: Inter and Playfair Display
- Unsplash images: Used for product and background imagery

Industry news links point to real luxury market resources (Bloomberg Luxury, Financial Times, Vogue Business, Bain & Company).
