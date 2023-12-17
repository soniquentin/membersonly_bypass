import argparse
import requests
import os



def bypass(url, filename = "article.html"):


    s = requests.Session()


    by_pass_url = f"https://webcache.googleusercontent.com/search?q=cache:{url}"


    payload = {"q" : f'cache:{url}'}

    response = s.get(by_pass_url, params=payload).text

    # Remove scripts
    response = response.replace("<script", "<!--<script")
    response = response.replace("</script>", "</script>-->")
    
    #Put in a file
    print(f"Writing to {filename}")
    with open(filename, "w") as f:
        f.write(response)

    success_msg = f"File has been successfully written at {os.path.dirname(os.path.realpath(__file__))}/{filename}"
    print("\n\n" + "#"*len(success_msg))
    print(success_msg)
    print("#"*len(success_msg) + "\n\n")
    




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Bypass')
    parser.add_argument('-u', '--url', type=str, help='URL to bypass')
    parser.add_argument('-f', '--filename', type=str, default="article.html", help='Filename to write the bypassed article')
    args = parser.parse_args()

    bypass(args.url, args.filename)

