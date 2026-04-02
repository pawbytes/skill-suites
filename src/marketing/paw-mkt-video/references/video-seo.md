# Video SEO

## Purpose
Optimize videos for search visibility -- YouTube search, Google video results, and schema markup for embedded videos.

## Process

1. **Load Context**: Read brand positioning and target keywords
2. **Research Keywords**: YouTube autocomplete, competitor analysis, tools
3. **Optimize Video Elements**: Title, description, tags, chapters, captions
4. **Implement Schema**: VideoObject markup for embedded videos
5. **Transcribe for SEO**: Full transcripts for indexing and repurposing

---

## 1. YouTube Search Optimization

**Keyword research sources**:
- YouTube autocomplete
- TubeBuddy, vidIQ
- Google Trends (YouTube filter)
- Competitor analysis

**Title optimization**:
- Primary keyword in first 40 chars
- 50-60 total characters
- Benefit or curiosity angle
- Numbers and brackets increase CTR

**Description optimization**:
- Keyword in first 25 words
- 200+ words total
- Supporting keywords naturally
- Timestamps for chapters
- Links to related content
- 3-5 hashtags at end

**Tags**:
- 5-10 tags
- Primary keyword, variations, related topics

**Filename**:
- Rename to include keyword before upload (e.g., `how-to-start-youtube-channel.mp4`)

---

## 2. Chapters and Captions

**Chapters**:
- Timestamps starting at 0:00
- Minimum 3 chapters, 10 seconds each
- Appear in search results
- Improves navigation and retention

**Closed captions**:
- Upload corrected auto-captions
- Improves indexing, accessibility, watch time
- YouTube auto-captions often inaccurate -- review manually

---

## 3. Google Video Results

Google surfaces videos for "how to," tutorial, review, and visual queries.

**Embed strategy**:
- Embed YouTube videos on relevant blog posts
- Surrounding text context aids indexing
- Creates additional discovery path

---

## 4. VideoObject Schema

Add VideoObject schema to pages embedding video:

```json
{
  "@type": "VideoObject",
  "name": "Video title with keyword",
  "description": "Full description",
  "thumbnailUrl": "thumbnail-url.jpg",
  "uploadDate": "2026-01-15",
  "duration": "PT5M30S",
  "contentUrl": "video-file-url",
  "embedUrl": "youtube-embed-url"
}
```

**Bridge to paw-mkt-seo** for full schema implementation.

---

## 5. Transcription for SEO

Every video should have a full transcript published as text content.

**Benefits**:
- Creates indexable text
- Ranks for long-tail keywords
- Repurpose into blog posts, social, email

**Tools**:
- YouTube auto-captions (edit for accuracy)
- Descript
- Otter.ai
- Whisper

**Bridge to paw-mkt-content** for transcript repurposing.

---

## 6. Output

Deliver:
- **Keyword research** with target terms
- **Title optimization** suggestions
- **Description template** with keywords, timestamps, links
- **Tag recommendations**
- **Chapter structure** for video
- **Transcript** for SEO and repurposing
- **Schema markup** for embedded videos
- **Save to**: Transcript saved with video script or as separate file