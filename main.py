import streamlit as st
import pandas as pd
from scrape import scrape_website
import concurrent.futures
import time

st.title("AI Web Scraper")

uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])
keywords_input = st.text_input("Enter keywords to extract (comma-separated):")

def read_excel_urls(excel_file_path):
    df = pd.read_excel(excel_file_path)
    return df['URL'].tolist()

if st.button("Scrape"):
    if uploaded_file and keywords_input:
        try:
            urls_to_scrape = read_excel_urls(uploaded_file)
            keywords_to_extract = [kw.strip() for kw in keywords_input.split(',')]
            all_product_data = []

            # Create a Streamlit progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()
            data_placeholder = st.empty()

            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                # Use executor.map for parallel processing
                results = executor.map(scrape_website, urls_to_scrape, [keywords_to_extract]*len(urls_to_scrape))
                
                for i, result in enumerate(results):
                    progress_bar.progress((i + 1) / len(urls_to_scrape))
                    status_text.text(f"Scraping {i+1} of {len(urls_to_scrape)} URLs...")
                    
                    product_data = result 
                    product_data['URL'] = urls_to_scrape[i] # Add URL to scraped data
                    all_product_data.append(product_data)
                    
                    df_results = pd.DataFrame(all_product_data)
                    data_placeholder.dataframe(df_results)

                    # Rate limiting (adjust delay as needed)
                    time.sleep(1)  

            status_text.text("Scraping complete!")

            st.download_button(
                label="Download data as CSV",
                data=df_results.to_csv(index=False),
                file_name='extracted_data.csv',
                mime='text/csv',
            )

        except Exception as e:
            st.error(f"An error occurred: {e}")