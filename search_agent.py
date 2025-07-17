# Later this could be a vector search or LLM prompt chain
def get_recommendations(user_query):
    # Placeholder content
    if "ethical hacking" in user_query.lower():
        return {
            "Cisco U.": [
                {"title": "Ethical Hacking Basics", "url": "https://u.cisco.com/path/ethical-hacking"},
            ],
            "NetAcad": [
                {"title": "Cybersecurity Essentials", "url": "https://www.netacad.com/courses/cybersecurity"},
            ],
            "Cisco Learning Network": [
                {"title": "Ethical Hacking Discussions", "url": "https://learningnetwork.cisco.com/s/topic/0TO3i000000LZD6GAO"},
            ],
        }
    return {}

