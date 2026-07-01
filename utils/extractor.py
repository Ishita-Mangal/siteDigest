from bs4 import BeautifulSoup

def extract_content(html):

    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    title = ""
    if soup.title:
        title = soup.title.get_text(strip=True)

    meta = ""
    meta_tag = soup.find("meta", attrs={"name": "description"})
    if meta_tag:
        meta = meta_tag.get("content", "")

    og_image = ""
    og = soup.find("meta", property="og:image")
    if og:
        og_image = og.get("content", "")

    main = soup.find("main")

    if main:
        content = main.get_text(" ", strip=True)

    elif soup.find("article"):
        content = soup.find("article").get_text(" ", strip=True)

    else:
        content = soup.get_text(" ", strip=True)

    final_text = f"""
Title:
{title}

Meta Description:
{meta}

Content:
{content}
"""

    return {
        "text": final_text[:12000],
        "image": og_image,
        "characters": len(final_text)
    }
