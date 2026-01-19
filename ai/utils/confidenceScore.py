def getConfidenceScore(result: dict) -> float:
    fake_count = result.get("fake", {}).get("count", 0)
    real_count = result.get("real", {}).get("count", 0)

    total = fake_count + real_count

    # No evidence at all
    if total == 0:
        return 0.0

    # Decide winner
    if fake_count >= real_count:
        winner = "fake"
        winner_count = fake_count
    else:
        winner = "real"
        winner_count = real_count

    dominance_ratio = winner_count / total  # 1.0 means 100% one-sided

    items = result.get(winner, {}).get("items", [])
    if not items:
        avg_similarity = 0.5
    else:
        avg_similarity = sum(item.get("score", 0) for item in items) / len(items)

    raw_confidence = (0.7 * dominance_ratio) + (0.3 * avg_similarity)

    # Scale to 0–100
    confidence_percent = raw_confidence * 100

    # Clamp
    confidence_percent = max(0, min(100, confidence_percent))

    return round(confidence_percent, 2)


# print(getConfidenceScore({
#   "final_verdict": "fake",
#   "fake": {
#     "count": 5,
#     "items": [
#       {
#         "label": "fake",
#         "title": "Miley Cyrus and Liam Hemsworth split for a second time: Reports",
#         "text": "Miley Cyrus and Liam Hemsworth split for a second time: Reports. Source: meaww.com",
#         "url": "meaww.com/miley-cyrus-and-liam-hemsworth-split-up-second-time",
#         "image_url": "",
#         "video_url": "",
#         "score": 0.9425694
#       },
#       {
#         "label": "fake",
#         "title": "Did Miley Cyrus and Liam Hemsworth secretly get married?",
#         "text": "Did Miley Cyrus and Liam Hemsworth secretly get married?. Source: www.dailymail.co.uk",
#         "url": "www.dailymail.co.uk/tvshowbiz/article-5874213/Did-Miley-Cyrus-Liam-Hemsworth-secretly-married.html",
#         "image_url": "",
#         "video_url": "",
#         "score": 0.92701393
#       },
#       {
#         "label": "fake",
#         "title": "Miley Cyrus & Liam Hemsworth’s Secret Wedding: The Vows, Her Dress & More — Report",
#         "text": "Miley Cyrus & Liam Hemsworth’s Secret Wedding: The Vows, Her Dress & More — Report. Source: hollywoodlife.com",
#         "url": "hollywoodlife.com/2017/01/04/miley-cyrus-liam-hemsworth-secret-wedding-christmas-holiday/",
#         "image_url": "",
#         "video_url": "",
#         "score": 0.92352617
#       },
#       {
#         "label": "fake",
#         "title": "Miley Cyrus and Liam Hemsworth Are Going to Be More Private After Breakup Rumors",
#         "text": "Miley Cyrus and Liam Hemsworth Are Going to Be More Private After Breakup Rumors. Source: www.wmagazine.com",
#         "url": "www.wmagazine.com/story/miley-cyrus-liam-hemsworth-more-private-breakup",
#         "image_url": "",
#         "video_url": "",
#         "score": 0.918419
#       },
#       {
#         "label": "fake",
#         "title": "Are Miley Cyrus and Liam Hemsworth married, when did they get engaged and what are their wedding plans?",
#         "text": "Are Miley Cyrus and Liam Hemsworth married, when did they get engaged and what are their wedding plans?. Source: www.thesun.co.uk",
#         "url": "www.thesun.co.uk/tvandshowbiz/5735247/miley-cyrus-liam-hemsworth-married-engaged-split/",
#         "image_url": "",
#         "video_url": "",
#         "score": 0.9102393
#       }
#     ]
#   },
#   "real": {
#     "count": 0,
#     "items": []
#   }
# }))