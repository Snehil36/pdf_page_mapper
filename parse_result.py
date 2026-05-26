def parse_response(response):
    
    lines = response.strip().split("\n")

    first_printed = None
    first_pdf = None
    toc = []
    
    for line in lines:
        if line.startswith("FIRST_CHAPTER_PRINTED_PAGE:"):
            first_printed = int(line.split(":")[1].strip())
        elif line.startswith("FIRST_CHAPTER_PDF_PAGE:"):
            first_pdf = int(line.split(":")[1].strip())
        elif line.startswith("TOC:"):
            continue
        elif ":" in line:
            parts = line.split(":")
            title = parts[0].strip()
            page = int(parts[1].strip())
            toc.append({"title": title, "printed_page": page})
    
    offset = first_pdf - first_printed

    print(f"Offset: {offset}")
    for chapter in toc:
        chapter["pdf_page"] = chapter["printed_page"] + offset
        print(f"{chapter['title']} -> PDF page {chapter['pdf_page']}")
    
    return offset, toc


