import re

BOOK_MAP = {
    # --- Old Testament ---
    "Genesis": 1, "Gen.": 1, "Gen": 1,
    "Exodus": 2, "Exo.": 2, "Exo": 2, 
    "Leviticus": 3, "Lev.": 3, "Lev": 3,
    "Numbers": 4, "Num.": 4, "Num": 4,
    "Deuteronomy": 5, "Deut.": 5, "Deut": 5,

    "Joshua": 6, "Josh.": 6, # "Josh": 6,
    "Judges": 7, "Judg.": 7, "Judg": 7,
    "Ruth": 8,

    "1 Samuel": 9, "1 Sam.": 9, "1 Sam": 9,
    "2 Samuel": 10, "2 Sam.": 10, "2 Sam": 10,
    "1 Kings": 11, # "1 Kgs.": 11, "1 Kgs": 11,
    "2 Kings": 12, # "2 Kgs.": 12, "2 Kgs": 12,
    "1 Chronicles": 13, "1 Chron.": 13, "1 Chron": 13,
    "2 Chronicles": 14, "2 Chron.": 14, "2 Chron": 14,

    "Ezra": 15,
    "Nehemiah": 16, "Neh.": 16, "Neh": 16,
    "Esther": 17, "Esth.": 17, "Esth": 17,

    "Job": 18,
    "Psalms": 19, "Psalm": 19, "Psa.": 19, "Psa": 19, 
    "Proverbs": 20, "Prov.": 20, "Prov": 20,
    "Ecclesiastes": 21, "Eccl.": 21, "Eccl": 21,
    "Song of Songs": 22, "S. S.": 22, "SoS": 22, "S.s.": 22,

    "Isaiah": 23, "Isa.": 23, "Isa": 23,
    "Jeremiah": 24, "Jer.": 24, "Jer": 24,
    "Lamentations": 25, "Lam.": 25, # "Lam": 25,
    "Ezekiel": 26, "Ezek.": 26, "Ezek": 26,
    "Daniel": 27, "Dan.": 27, # "Dan": 27,

    "Hosea": 28, "Hos.": 28, "Hos": 28,
    "Joel": 29,
    "Amos": 30,
    "Obadiah": 31, "Obad.": 31, "Obad": 31,
    "Jonah": 32,
    "Micah": 33, 
    "Nahum": 34,
    "Habakkuk": 35, "Hab.": 35, "Hab": 35,
    "Zephaniah": 36, "Zeph.": 36, # "Zeph": 36,
    "Haggai": 37, "Hag.": 37, "Hag": 37,
    "Zechariah": 38, "Zech.": 38, # "Zech": 38,
    "Malachi": 39, "Mal.": 39, # "Mal": 39,

    # --- New Testament ---
    "Matthew": 40, "Matt.": 40, 
    "Mark": 41, 
    "Luke": 42,
    "John": 43,

    "Acts": 44,

    "Romans": 45, "Rom.": 45, "Rom": 45,
    "1 Corinthians": 46, "1 Cor.": 46, "1 Cor": 46,
    "2 Corinthians": 47, "2 Cor.": 47, "2 Cor": 47,
    "Galatians": 48, "Gal.": 48, "Gal": 48,
    "Ephesians": 49, "Eph.": 49, "Eph": 49,
    "Philippians": 50, "Phil.": 50, "Phil": 50,
    "Colossians": 51, "Col.": 51, "Col": 51,
    "1 Thessalonians": 52, "1 Thes.": 52, "1 Thes": 52,
    "2 Thessalonians": 53, "2 Thes.": 53, "2 Thes": 53,
    "1 Timothy": 54, "1 Tim.": 54, "1 Tim": 54,
    "2 Timothy": 55, "2 Tim.": 55, "2 Tim": 55,
    "Titus": 56, 
    "Philemon": 57, "Philem.": 57, "Philem": 57,

    "Hebrews": 58, "Heb.": 58, "Heb": 58,
    "James": 59,
    "1 Peter": 60, "1 Pet.": 60, "1 Pet": 60,
    "2 Peter": 61, "2 Pet.": 61, "2 Pet": 61,
    "1 John": 62, 
    "2 John": 63, 
    "3 John": 64, 
    "Jude": 65, 
    "Revelation": 66, "Rev.": 66,
}

PLAINTEXT_BIBLE_REF = re.compile(
    r"""
    \b
    (?P<book>
        (?:[1-3]\s)?          # Optional numeric prefix (1–3)
        [A-Z][a-z]+           # Book name root
        (?:\sof\s[A-Z][a-z]+)?# "Song of Solomon"
        \.?                   # Optional trailing period
    )
    \s+
    (?P<chapter>\d+)
    :
    (?P<verse_start>\d+)
    (?:[-–](?P<verse_end>\d+))?
    \b
    """,
    re.VERBOSE,
)

def tag_plaintext_bible_refs(text: str) -> str:
    def replacer(match):
        book_raw = match.group("book").strip()
        chapter = int(match.group("chapter"))
        verse_start = int(match.group("verse_start"))
        verse_end = match.group("verse_end")

        book_num = BOOK_MAP.get(book_raw)
        if not book_num:
            return match.group(0)  # unknown book → leave unchanged

        verse_end = int(verse_end) if verse_end else verse_start

        label = (
            f"{book_raw} {chapter}:{verse_start}"
            if verse_start == verse_end
            else f"{book_raw} {chapter}:{verse_start}–{verse_end}"
        )

        return (
            f'<BIBLE_REF '
            f'book="{book_num}" '
            f'chapter="{chapter}" '
            f'verse_start="{verse_start}" '
            f'verse_end="{verse_end}">'
            f'{label}'
            f'</BIBLE_REF>'
        )

    return PLAINTEXT_BIBLE_REF.sub(replacer, text)
