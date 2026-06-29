import os
import streamlit as st
from PIL import Image

from pipeline import Pipeline

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="DECIMER AI",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 DECIMER AI")
st.subheader("Chemical Structure Recognition Platform")

st.divider()

# --------------------------------------------------
# Upload Section
# --------------------------------------------------

uploaded_pdf = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

local_path = st.text_input(
    "OR Enter Local PDF Path"
)

process = st.button(
    "🚀 Process PDF"
)

# --------------------------------------------------
# Processing
# --------------------------------------------------

if process:

    if uploaded_pdf is None and local_path == "":

        st.error("Please upload a PDF or enter a valid path.")
        st.stop()

    if uploaded_pdf:

        os.makedirs("temp", exist_ok=True)

        temp_path = os.path.join(
            "temp",
            uploaded_pdf.name
        )

        with open(temp_path, "wb") as f:
            f.write(uploaded_pdf.read())

        pdf_path = temp_path

    else:

        pdf_path = local_path

    pipeline = Pipeline()

    with st.spinner("Processing PDF..."):

        result = pipeline.run(pdf_path)

    metadata = result["metadata"]
    statistics = result["statistics"]
    dataframe = result["dataframe"]
    csv_path = result["csv_path"]

    # --------------------------------------------------
    # Success
    # --------------------------------------------------

    st.success("✅ Processing Completed Successfully!")

    st.divider()

    # --------------------------------------------------
    # Dashboard
    # --------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "DOC ID",
        metadata["doc_id"]
    )

    c2.metric(
        "Total Pages",
        statistics["total_pages"]
    )

    c3.metric(
        "Structures",
        statistics["total_structures"]
    )

    c4.metric(
        "Success",
        statistics["successful_predictions"]
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Failed",
        statistics["failed_predictions"]
    )

    c2.metric(
        "PDF",
        metadata["pdf_name"]
    )

    c3.metric(
        "Processed",
        "Yes"
    )

    st.divider()

    # --------------------------------------------------
    # Metadata Table
    # --------------------------------------------------

    st.subheader("📄 Metadata Table")

    st.dataframe(
        dataframe,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # --------------------------------------------------
    # Extracted Structures
    # --------------------------------------------------

    st.subheader("🧪 Extracted Chemical Structures")

    for _, row in dataframe.iterrows():

        with st.container():

            st.markdown("---")

            img1, img2 = st.columns(2)

            # -------------------------
            # Original Image
            # -------------------------

            with img1:

                st.markdown("### Original Image")

                original = Image.open(
                    row["image_path"]
                )

                st.image(
                    original,
                    use_container_width=True
                )

            # -------------------------
            # Cleaned Image
            # -------------------------

            with img2:

                st.markdown("### Cleaned Image")

                cleaned = Image.open(
                    row["clean_path"]
                )

                st.image(
                    cleaned,
                    use_container_width=True
                )

            st.markdown("### Information")

            info1, info2 = st.columns(2)

            with info1:

                st.write(
                    f"**Image ID:** {row['image_id']}"
                )

                st.write(
                    f"**Page Number:** {row['page_number']}"
                )

                st.write(
                    f"**Image Type:** {row['image_type']}"
                )

            with info2:

                st.write(
                    f"**Processed:** {'✅ Yes' if row['processed'] else '❌ No'}"
                )

                st.write(
                    f"**Formula Detected:** {'Yes' if row['is_formula'] else 'No'}"
                )

                st.write(
                    f"**Document:** {row['doc_id']}"
                )

            st.markdown("### Predicted SMILES")

            if row["smiles"]:

                st.code(
                    row["smiles"],
                    language="text"
                )

            else:

                st.warning(
                    "No SMILES Generated"
                )

    st.divider()

    # --------------------------------------------------
    # Download CSV
    # --------------------------------------------------

    st.subheader("⬇ Export Results")

    with open(csv_path, "rb") as f:

        st.download_button(

            label="Download CSV",

            data=f,

            file_name=os.path.basename(csv_path),

            mime="text/csv"

        )

    st.success("🎉 Pipeline Finished Successfully")