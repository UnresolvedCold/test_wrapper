import os
import tempfile
import requests

def download_file(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        temp_dir = tempfile.gettempdir()
        file_name = os.path.basename(url)
        file_path = os.path.join(temp_dir, file_name)
        
        with open(file_path, 'wb') as file:
            file.write(response.content)
        
        print("Transit time model is initiallized"  + file_path)
        return file_path
    else:
        print(f"Error in downloading Transit time model: {response.status_code}")
        return None

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("Cannot find the transit time model file")

# if __name__ == "__main__":
#     file_url = "https://example.com/sample.pdf"  # Replace with your desired file URL
    
#     downloaded_file_path = download_file(file_url)
#     if downloaded_file_path:
#         input("Press Enter to delete the downloaded file...")
#         delete_file(downloaded_file_path)
