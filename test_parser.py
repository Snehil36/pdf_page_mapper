from identify_toc import find_toc


def test_parser(response):

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
            print(f"Title {title} Page {page}")
            print(toc.len()+ 1)
            toc.append({"title": title, "printed_page": page})


if __name__ == "__main__":
    test_parser(find_toc("test_pdfs/182 Textbook.pdf"))