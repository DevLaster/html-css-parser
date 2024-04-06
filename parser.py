import requests
from bs4 import BeautifulSoup

def save_html_and_css(url, html_file='html.txt', css_file='css.txt'):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
           
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(soup.prettify())
            css_styles = '\n'.join([style.text for style in soup.find_all('style')])
            with open(css_file, 'w', encoding='utf-8') as f:
                f.write(css_styles)

            print(f"HTML Code saved to {html_file}")
            print(f"CSS styles saved to {css_file}")
        else:
            print("Error", response.status_code)
    except Exception as e:
        print("error :", e)

if __name__ == "__main__":
    url = input("Enter the URL of the website please: ")
    save_html_and_css(url)
