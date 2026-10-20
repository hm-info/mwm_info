"""Render one topic tree and the corresponding language link on each page."""

from copy import copy

from mkdocs.structure.nav import Navigation, Section


PAIRS = (
    ("index.md", "home-en.md"),
    ("barcode-tr.md", "barcode-en.md"),
    ("turkish.md", "english.md"),
)


def on_page_context(context, page, config, nav, **kwargs):
    source = page.file.src_uri
    pair = next((pair for pair in PAIRS if source in pair), PAIRS[0])
    language = "en" if source == pair[1] else "tr"
    is_english = language == "en"
    labels = (
        ("Getting started", "Barcode guide", "Job files", "KD658")
        if is_english
        else ("Başlangıç", "Barkod rehberi", "İş dosyaları", "KD658")
    )
    sources = [pair[1 if is_english else 0] for pair in PAIRS]
    pages_by_source = {item.file.src_uri: item for item in nav.pages}
    localized_pages = []
    for uri, title in zip(sources, (labels[0], labels[1], labels[3])):
        item = copy(pages_by_source[uri])
        item.parent = None
        item.title = title
        item.active = uri == source
        localized_pages.append(item)

    section = Section(labels[2], [localized_pages[2]])
    localized_pages[2].parent = section
    section.active = localized_pages[2].active
    localized_nav = Navigation(
        [localized_pages[0], localized_pages[1], section], localized_pages
    )
    localized_nav.homepage = localized_pages[0]

    local_config = copy(config)
    local_config["theme"] = copy(config["theme"])
    local_config["theme"]["language"] = language
    local_config["site_name"] = "MWM User Guide" if is_english else "MWM Kullanım Rehberi"
    local_config["site_description"] = (
        "Barcode reading and job files for MWM welding machines."
        if is_english
        else config["site_description"]
    )
    local_config["extra"] = dict(config["extra"])
    local_config["extra"]["homepage"] = localized_pages[0].url
    local_config["extra"]["alternate"] = [
        {"name": "Türkçe", "lang": "tr", "link": pages_by_source[pair[0]].url},
        {"name": "English", "lang": "en", "link": pages_by_source[pair[1]].url},
    ]
    current = sources.index(source) if source in sources else 0
    local_page = localized_pages[current]
    local_page.previous_page = localized_pages[current - 1] if current else None
    local_page.next_page = localized_pages[current + 1] if current < 2 else None
    context.update(config=local_config, nav=localized_nav, page=local_page)
    return context
