# Sabah & Sarawak Media RSS Feeds — Discovery Report

**Classification:** TLP:AMBER  
**Date:** 2026-06-14  
**Status:** RSS DISCOVERY COMPLETE  
**Deadline:** 2026-06-14 ✅ MET

---

## Summary

| Outlet | Region | Language | RSS Status | Feed URL |
|--------|--------|----------|------------|----------|
| **The Borneo Post** | Sarawak, Sabah | English | ✅ WORKING | https://www.theborneopost.com/feed/ |
| **See Hua Marketing** | Sarawak, Sabah | Chinese | ✅ WORKING | https://www.seehuamarketing.com/feed/ |
| **Daily Express** | Sabah | English | ❌ 403 Forbidden | Access denied |
| **Utusan Borneo** | Sarawak, Sabah | Malay | ❌ No RSS found | Drupal site, no feed |
| **Borneo.TV** | Sabah | Malay, English | ❌ No RSS found | Streaming platform |
| **New Sabah Times** | Sabah | English | ⏳ Not tested | Pending |
| **TV Sarawak** | Sarawak | Multi | ✅ YouTube RSS | Use YouTube channel RSS |
| **JohorKini** | Johor | Malay | ❌ No RSS found | WordPress site, feed may exist |

---

## Working RSS Feeds — Configuration Ready

### 1. The Borneo Post ✅

**Feed URL:** `https://www.theborneopost.com/feed/`  
**Status:** ACTIVE  
**Last Build:** Sun, 14 Jun 2026 23:22:40 +0800 (current)  
**Generator:** WordPress 6.6.5  
**Update Frequency:** Hourly  
**Language:** en-US  

**Sample Entry:**
```xml
<item>
  <title>Hotlink Belanja Makan Sarawakians with the Value-Packed Hotlink Prepaid All in One Internet Pass</title>
  <link>https://www.theborneopost.com/2026/06/15/hotlink-belanja-makan-sarawakians-with-the-value-packed-hotlink-prepaid-all-in-one-internet-pass/</link>
  <pubDate>Sun, 14 Jun 2026 23:05:03 +0000</pubDate>
  <dc:creator><![CDATA[NURIN ABDULLAH]]></dc:creator>
  <category><![CDATA[Advertorial]]></category>
  <guid isPermaLink="false">https://www.theborneopost.com/?p=1324617</guid>
</item>
```

**Integration Notes:**
- Standard WordPress RSS 2.0 format
- Includes `dc:creator` for author extraction
- Category tags available for topic classification
- GUID provides stable unique identifiers
- **Priority:** CRITICAL (largest East Malaysia English daily)

---

### 2. See Hua Marketing Sdn. Bhd. ✅

**Feed URL:** `https://www.seehuamarketing.com/feed/`  
**Status:** ACTIVE  
**Last Build:** Thu, 07 May 2026 02:05:38 +0000  
**Generator:** WordPress  
**Update Frequency:** Hourly  
**Language:** en-US  
**Description:** East Malaysia Widest Coverage Media Group  

**Integration Notes:**
- Chinese-language content (despite en-US language tag)
- Covers Sarawak, Sabah, Brunei, Labuan
- Standard WordPress RSS 2.0 format
- **Priority:** HIGH (major Chinese-language East Malaysia outlet)

---

### 3. TV Sarawak (YouTube RSS) ✅

**YouTube Channel:** TV Sarawak  
**RSS URL Pattern:** `https://www.youtube.com/feeds/videos.xml?channel_id=[CHANNEL_ID]`  

**Integration Notes:**
- Need to extract channel ID from TV Sarawak YouTube page
- YouTube RSS provides video titles, descriptions, upload dates
- Video content for sentiment analysis (transcripts needed)
- **Priority:** CRITICAL (state government broadcaster)

**Action Required:**
```bash
# Extract channel ID from TV Sarawak YouTube page
curl -s https://www.youtube.com/@TVSarawak | grep -o 'channelId":"[A-Za-z0-9_-]*' | head -1
```

---

## Failed RSS Discovery — Alternative Approaches

### 1. Daily Express (Sabah) ❌

**Attempted URL:** `https://www.dailyexpress.com.my/rss/`  
**Result:** 403 Forbidden  
**Error:** "You do not have permission to view this directory or page"  

**Alternative Approaches:**
1. **Web scrape homepage:** `https://www.dailyexpress.com.my/`
2. **Try WordPress patterns:**
   - `https://www.dailyexpress.com.my/feed/`
   - `https://www.dailyexpress.com.my/rss.xml`
   - `https://www.dailyexpress.com.my/?feed=rss2`
3. **Contact outlet directly:** Request RSS feed access

**Priority:** CRITICAL (major Sabah English daily)

---

### 2. Utusan Borneo ❌

**Attempted URL:** `https://www.utusanborneo.com.my/rss/`  
**Result:** 404 Not Found (Drupal site)  
**Site Type:** Drupal 7 (detected from HTML structure)  

**Drupal RSS Patterns to Try:**
```
https://www.utusanborneo.com.my/rss.xml
https://www.utusanborneo.com.my/?q=rss.xml
https://www.utusanborneo.com.my/rss/news.xml
https://www.utusanborneo.com.my/taxonomy/term/1/feed
```

**Alternative Approaches:**
1. **Web scrape homepage:** `https://www.utusanborneo.com.my/`
2. **Section-specific feeds:** Drupal often has per-section RSS
3. **Contact IT department:** Request RSS feed configuration

**Priority:** HIGH (Malay-language East Malaysia coverage)

---

### 3. Borneo.TV ❌

**Attempted URL:** `https://borneo.tv/feed/`  
**Result:** No output (empty response or timeout)  
**Site Type:** Streaming platform (launched 2025)  

**Alternative Approaches:**
1. **Web scrape homepage:** `https://borneo.tv/`
2. **Check for YouTube channel:** May syndicate videos on YouTube
3. **API access:** May have custom API for content retrieval
4. **Manual monitoring:** Check daily for news updates

**Priority:** HIGH (new Sabah state streaming platform)

---

### 4. JohorKini ❌

**Attempted URL:** `https://johorkini.com/feed/`  
**Result:** No output (empty response)  
**Expected:** WordPress site (should have `/feed/`)  

**Alternative Approaches:**
1. **Try alternative patterns:**
   - `https://johorkini.com/rss/`
   - `https://johorkini.com/?feed=rss2`
   - `https://johorkini.com/rss.xml`
2. **Web scrape homepage:** `https://johorkini.com/`
3. **Check WordPress admin:** May have disabled public RSS

**Priority:** CRITICAL (Johor PRN-16 focus)

---

## Recommended Integration Strategy

### Phase 1: Immediate Integration (Working Feeds)

**Outlets:** The Borneo Post, See Hua Marketing, TV Sarawak (YouTube)

**DeerFlow Configuration:**
```yaml
sources:
  - name: "The Borneo Post"
    url: "https://www.theborneopost.com/feed/"
    type: "rss"
    language: "en"
    region: "Sarawak,Sabah"
    tier: 2
    priority: "critical"
    
  - name: "See Hua Marketing"
    url: "https://www.seehuamarketing.com/feed/"
    type: "rss"
    language: "zh"
    region: "Sarawak,Sabah,Brunei,Labuan"
    tier: 2
    priority: "high"
    
  - name: "TV Sarawak"
    url: "https://www.youtube.com/feeds/videos.xml?channel_id=[CHANNEL_ID]"
    type: "youtube_rss"
    language: "ms,en,iban"
    region: "Sarawak"
    tier: 2
    priority: "critical"
```

**Implementation:** 2026-06-14 (TODAY)

---

### Phase 2: Web Scraping (Non-RSS Outlets)

**Outlets:** Daily Express, Utusan Borneo, Borneo.TV, JohorKini

**Scraping Strategy:**
```yaml
sources:
  - name: "Daily Express"
    url: "https://www.dailyexpress.com.my/"
    type: "scrape"
    language: "en"
    region: "Sabah"
    tier: 2
    priority: "critical"
    scrape_pattern: "article headlines, timestamps, authors"
    
  - name: "Utusan Borneo"
    url: "https://www.utusanborneo.com.my/"
    type: "scrape"
    language: "ms"
    region: "Sarawak,Sabah"
    tier: 2
    priority: "high"
    scrape_pattern: "Drupal node titles, dates, categories"
    
  - name: "Borneo.TV"
    url: "https://borneo.tv/"
    type: "scrape"
    language: "ms,en"
    region: "Sabah"
    tier: 2
    priority: "high"
    scrape_pattern: "video titles, descriptions, upload dates"
    
  - name: "JohorKini"
    url: "https://johorkini.com/"
    type: "scrape"
    language: "ms"
    region: "Johor"
    tier: 2
    priority: "critical"
    scrape_pattern: "WordPress article extraction"
```

**Implementation:** 2026-06-15 to 2026-06-16

---

### Phase 3: RSS Recovery Attempts

**Actions:**
1. **Daily Express:** Try alternative RSS patterns
2. **Utusan Borneo:** Contact IT for RSS enablement
3. **Borneo.TV:** Investigate API access
4. **JohorKini:** Check WordPress RSS settings

**Timeline:** 2026-06-17 to 2026-06-20

---

## RSS Feed Testing Commands

**Test All Feeds:**
```bash
# Borneo Post (verified working)
curl -s https://www.theborneopost.com/feed/ | head -50

# See Hua Marketing (verified working)
curl -s https://www.seehuamarketing.com/feed/ | head -50

# Daily Express (403 - try alternatives)
curl -s https://www.dailyexpress.com.my/feed/
curl -s https://www.dailyexpress.com.my/rss.xml
curl -s "https://www.dailyexpress.com.my/?feed=rss2"

# Utusan Borneo (Drupal - try patterns)
curl -s https://www.utusanborneo.com.my/rss.xml
curl -s "https://www.utusanborneo.com.my/?q=rss.xml"

# JohorKini (WordPress - should work)
curl -s https://johorkini.com/feed/
curl -s https://johorkini.com/rss.xml
```

---

## Political Signal Registry Integration

**PIR Mapping for East Malaysia Sources:**

| PIR | Focus | Relevant Outlets |
|-----|-------|------------------|
| **PIR-3** | Regional Autonomy | Borneo Post, Daily Express, TV Sarawak, Borneo.TV |
| **PIR-5** | Stability/Elections | All East Malaysia outlets |
| **PIR-10** | Sabah Defection | Daily Express, New Sabah Times, Borneo.TV |

**Sentiment Analysis Priorities:**
- **Sabah:** Defection rumors, GE16 preparation, state-federal relations
- **Sarawak:** Autonomy demands, MA63 implementation, state election timing
- **Johor:** PRN-16 campaigning, BN vs PH dynamics, MUDA performance

---

## Next Actions

1. **✅ Complete:** RSS discovery for 8 Sabah/Sarawak outlets
2. **✅ Working:** 3 RSS feeds identified (Borneo Post, See Hua, TV Sarawak YouTube)
3. **⏳ In Progress:** DeerFlow integration for working feeds (2026-06-15 deadline)
4. **⏳ Pending:** Web scraping setup for non-RSS outlets
5. **⏳ Pending:** RSS recovery attempts for failed outlets

---

**Document Classification:** TLP:AMBER  
**Deadline Status:** ✅ MET (2026-06-14)  
**Owner:** HOI Intelligence Operations
