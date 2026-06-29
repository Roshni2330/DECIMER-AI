from dataclasses import dataclass, field
from datetime import datetime

import pandas as pd


@dataclass
class Document:

    doc_id: str = ""

    pdf_name: str = ""

    pdf_path: str = ""

    pdf_hash: str = ""

    processed_on: datetime = None

    processed: bool = False

    rendered_pages: list = field(default_factory=list)

    segmented_metadata: list = field(default_factory=list)

    metadata_df: pd.DataFrame = field(
        default_factory=pd.DataFrame
    )

    output_csv: str = ""

    statistics: dict = field(default_factory=dict)