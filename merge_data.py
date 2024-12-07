import requests
import pandas as pd


try:
   tenants_api = requests.get("http://localhost:8000/api/v1/tenants/")
   tenants_api.raise_for_status()
   tenants_api_data = tenants_api.json()
   properties_api = requests.get("http://localhost:8000/api/v1/properties/")
   properties_api.raise_for_status()
   properties_api_data = properties_api.json()


   tdf = pd.DataFrame(tenants_api_data)
   pdf = pd.DataFrame(properties_api_data)

   tdf.to_csv("tenants_data.csv",index=False)
   pdf.to_csv("properties_data.csv", index=False)
   print(tdf.shape, pdf.shape)

   inner_merged_df = pd.merge(tdf, pdf, on="id" , how="inner")
   inner_merged_df.to_csv("merged_data.csv", index=False)
   print(inner_merged_df.shape)

except requests.exceptions.RequestException as e:
    print(f"Error while fetching data: {e}")

