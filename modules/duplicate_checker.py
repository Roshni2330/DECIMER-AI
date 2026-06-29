import pandas as pd

from config import MASTER_DATABASE


class DuplicateChecker:

    def __init__(self):

        if not MASTER_DATABASE.exists():

            pd.DataFrame(

                columns=[

                    "doc_id",
                    "pdf_name",
                    "pdf_hash",
                    "processed_on"

                ]

            ).to_csv(

                MASTER_DATABASE,

                index=False

            )

    def check_duplicate(self, pdf_hash):

        df = pd.read_csv(MASTER_DATABASE)

        if len(df) == 0:
            return False

        if pdf_hash in df["pdf_hash"].values:

            old_doc = df[
                df["pdf_hash"] == pdf_hash
            ].iloc[0]

            raise Exception(
                f"PDF already processed.\n"
                f"Existing DOC_ID : {old_doc['doc_id']}"
            )

        return False

    def save_document(self, metadata):

        df = pd.read_csv(MASTER_DATABASE)

        df.loc[len(df)] = [

            metadata["doc_id"],

            metadata["pdf_name"],

            metadata["pdf_hash"],

            metadata["processed_on"]

        ]

        df.to_csv(

            MASTER_DATABASE,

            index=False

        )