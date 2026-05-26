from identify_toc import find_toc
from parse_result import parse_response

def main():
    pdf_path = "test_pdfs/182 Textbook.pdf"
    
    print("Finding TOC...")
    response_text = find_toc(pdf_path)
    
    print("Parsing response...")
    offset, toc = parse_response(response_text)
    
    print(f"\nFinal offset: {offset}")
    print("\nCorrected TOC:")
    for chapter in toc:
        print(f"{chapter['title']} -> PDF page {chapter['pdf_page']}")

if __name__ == "__main__":
    main()