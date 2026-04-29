# Perplexity podcast transcription fallbacks

This note records the current failure cases from the curated Perplexity podcast set and the public fallback sources checked so far.

## 1) LIMITLESS: Aravind Srinivas: Perplexity CEO’s All-In Gamble to Take Down Google
- Source RSS / episode page: [Bankless RSS](https://feeds.flightcast.com/p83fuj0y0u58o82l41xei7zo.xml), [Podwise summary](https://beta.podwise.ai/dashboard/episodes/4974485)
- Enclosure URL checked: `https://episode.flightcast.com/01K30X3NA7GMNFG24NAXWRF86K.mp3`
- Current failure: `FILE_403_FORBIDDEN`
- Public note: Podwise summary confirms the episode’s core themes are Comet, AI browsing, curiosity, user agency, and the browser as an AI-native OS.

## 2) From PhD to CEO: Aravind Srinivas on Reinventing Search with Perplexity AI
- Source RSS / episode page: [Podbean episode page](https://berkeley-haas-deans-speaker-series.podbean.com/e/dss-aravind/), [Berkeley Haas article](https://newsroom.haas.berkeley.edu/deans-speaker-series-perplexity-ai-ceo-aravind-srinivas-phd-21-on-why-he-ditched-pitch-decks/)
- Enclosure URL checked: `https://mcdn.podbean.com/mf/web/juwzwfbtpsssw24n/DSS_aravind.mp3`
- Current failure: `FILE_DOWNLOAD_FAILED`
- Public note: the episode description says Aravind discusses founder journey, the AI landscape, and Perplexity’s mission to support curiosity.

## 3) AI Will Make Browsers Autonomous - Perplexity CEO Aravind Srinivas
- Source RSS / episode page: [Transistor RSS](https://feeds.transistor.fm/superhuman-ai-decoding-the-future), [Glasp transcript preview](https://glasp.co/youtube/xT_AdYfeYEc), [Lily's AI notes](https://lilys.ai/ko/notes/1134691)
- Enclosure URL checked: `https://media.transistor.fm/b0742894/32dd341b.mp3`
- Current failure: `Transcription polling timeout after 240s`
- Public note: public transcript previews emphasize the browser as a workflow layer, not just a tool, and a data flywheel between product usage and model quality.

## 4) Perplexity CEO on Chrome, AI and challenging the tech giants
- Source RSS / episode page: [Acast / Times Tech Podcast](https://shows.acast.com/dannyinthevalley/episodes/perplexity-ceo-on-chrome-ai-and-challenging-the-tech-giants), [Podfollow](https://podfollow.com/times-tech-podcast/episode/c42b8991db36876c60004b29e35147bb30f1ca4f/view), [Muck Rack](https://muckrack.com/podcast/thetimesco-danny-in-the-valley/episodes/6451343-perplexity-ceo-on-chrome-ai-and-challengin/)
- Enclosure URL checked: `https://sphinx.acast.com/p/acast/s/dannyinthevalley/e/68a85fa8718453410e39dcdc/media.mp3`
- Current failure: `FILE_DOWNLOAD_FAILED`
- Public note: the episode notes focus on the $35B Chrome bid, whether it was serious or a stunt, and how Perplexity wants to reshape the internet.

## 5) Aravind Srinivas Has All The Answers
- Source RSS / episode page: [Stanford GSB episode page](https://art19.com/shows/stanford-gsb/episodes/5779113d-5711-4c79-98b3-43f61027d6d0), [Stanford GSB article](https://www.gsb.stanford.edu/insights/perplexitys-aravind-srinivas-infinite-value-knowledge), [Apple Podcasts channel](https://podcasts.apple.com/vn/channel/stanford-gsb/id6443022350)
- Enclosure URL checked: `https://tracking.swap.fm/track/zA4xtlPBvf2K1K9zesjz/op3.dev/e/rss.art19.com/episodes/5779113d-5711-4c79-98b3-43f61027d6d0.mp3?rss_browser=BAhJIglpVE1TBjoGRVQ%3D--4577cbcc3cc5282be318e551563630a2c5c2f06f`
- Current failure: `Transcription polling timeout after 240s`
- Public note: Stanford’s article and podcast listing emphasize Perplexity as a reliable answer machine, the “infinite value of knowledge,” and the ambition to help users accomplish tasks, not just answer questions.

## Verification
- Audio URLs were reachable with `curl -I` during this run.
- The live transcription process remained active while these notes were captured, so this file should be treated as a fallback ledger, not the final success state.
